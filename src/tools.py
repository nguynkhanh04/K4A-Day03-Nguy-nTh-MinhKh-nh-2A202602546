"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND — ĐỀ TÀI 1.2: TRỢ LÝ QUẢN LÝ THƯ VIỆN & TÀI LIỆU
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.

Hai công cụ chính:
  1. library_query  — Tra cứu thông tin sách, vị trí, tình trạng mượn/trả
  2. renew_book     — Gia hạn thời gian mượn sách/tài liệu
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu thông tin sách & tài liệu thư viện
    {
        "name": "library_query",
        "description": "Tra cứu thông tin sách và tài liệu trong thư viện VinUni, bao gồm vị trí kệ, tình trạng mượn/trả, số lượng còn lại và thông tin người mượn.",
        "parameters": {
            "type": "object",
            "properties": {
                "book_id": {
                    "type": "string",
                    "description": "Mã sách hoặc mã thẻ thư viện cần tra cứu (ví dụ: 'BK001' cho sách, 'TV2026001' cho thẻ thư viện)"
                }
            },
            "required": ["book_id"]
        }
    },

    # Tool 2: Gia hạn tài liệu đang mượn
    {
        "name": "renew_book",
        "description": "Gia hạn thời gian mượn sách/tài liệu tại thư viện VinUni cho người mượn.",
        "parameters": {
            "type": "object",
            "properties": {
                "book_id": {
                    "type": "string",
                    "description": "Mã sách cần gia hạn (ví dụ: 'BK002')"
                },
                "library_card_id": {
                    "type": "string",
                    "description": "Mã thẻ thư viện của người mượn (ví dụ: 'TV2026001')"
                },
                "extend_days": {
                    "type": "integer",
                    "description": "Số ngày muốn gia hạn thêm (ví dụ: 7 hoặc 14)"
                }
            },
            "required": ["book_id", "library_card_id", "extend_days"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    # --- BẢNG SÁCH (Tra cứu theo mã sách) ---
    "BK001": {
        "title": "Introduction to Artificial Intelligence",
        "author": "Stuart Russell, Peter Norvig",
        "category": "Công nghệ thông tin",
        "location": "Tầng 2 - Kệ A3 - Ngăn 05",
        "total_copies": 3,
        "available_copies": 1,
        "status": "Có sẵn"
    },
    "BK002": {
        "title": "Deep Learning",
        "author": "Ian Goodfellow, Yoshua Bengio",
        "category": "Công nghệ thông tin",
        "location": "Tầng 2 - Kệ A3 - Ngăn 08",
        "total_copies": 2,
        "available_copies": 0,
        "status": "Đang được mượn hết",
        "borrowed_by": {
            "TV2026001": {
                "borrower_name": "Nguyễn Văn An",
                "borrow_date": "01/09/2026",
                "due_date": "15/09/2026",
                "renewable": True
            }
        }
    },
    "BK003": {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "category": "Kỹ thuật phần mềm",
        "location": "Tầng 3 - Kệ B1 - Ngăn 02",
        "total_copies": 5,
        "available_copies": 3,
        "status": "Có sẵn"
    },

    # --- THẺ THƯ VIỆN (Tra cứu theo mã thẻ) ---
    "TV2026001": {
        "member_name": "Nguyễn Văn An",
        "email": "an.nv@vinuni.edu.vn",
        "member_type": "Sinh viên",
        "status": "Đang hoạt động",
        "books_borrowed": [
            {
                "book_id": "BK002",
                "title": "Deep Learning",
                "borrow_date": "01/09/2026",
                "due_date": "15/09/2026",
                "renewable": True
            }
        ]
    },
    "TV2026002": {
        "member_name": "Trần Thị Bình",
        "email": "binh.tt@vinuni.edu.vn",
        "member_type": "Sinh viên",
        "status": "Đang hoạt động",
        "books_borrowed": []
    }
}


def execute_library_query(book_id: str) -> str:
    """Thực thi tra cứu thông tin sách hoặc thẻ thư viện trong MOCK_DATABASE."""
    record = MOCK_DATABASE.get(book_id.strip().upper())
    if record:
        return json.dumps({
            "status": "SUCCESS",
            "book_id": book_id,
            "data": record
        }, ensure_ascii=False, default=str)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu có mã '{book_id}' trong thư viện."
        }, ensure_ascii=False)


def execute_renew_book(book_id: str, library_card_id: str, extend_days: int = 7) -> str:
    """Thực thi gia hạn sách đang mượn. Kiểm tra sách tồn tại, bản ghi mượn hợp lệ và điều kiện gia hạn."""
    book = MOCK_DATABASE.get(book_id.strip().upper())
    if not book:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy sách có mã '{book_id}' trong thư viện."
        }, ensure_ascii=False)

    borrowed_info = book.get("borrowed_by", {}).get(library_card_id.strip().upper())
    if not borrowed_info:
        return json.dumps({
            "status": "ERROR",
            "message": f"Thẻ thư viện '{library_card_id}' không có bản ghi mượn sách '{book_id}'."
        }, ensure_ascii=False)

    if not borrowed_info.get("renewable", False):
        return json.dumps({
            "status": "ERROR",
            "message": f"Sách '{book_id}' không đủ điều kiện gia hạn (đã gia hạn tối đa hoặc quá hạn)."
        }, ensure_ascii=False)

    return json.dumps({
        "status": "SUCCESS",
        "renew_id": f"RN-{book_id}-{library_card_id}",
        "book_id": book_id,
        "library_card_id": library_card_id,
        "extend_days": extend_days,
        "old_due_date": borrowed_info["due_date"],
        "new_due_date": "29/09/2026",
        "message": f"Gia hạn thành công sách '{book_id}' thêm {extend_days} ngày cho thẻ {library_card_id}."
    }, ensure_ascii=False)


# ==============================================================================
# 3. DISPATCHER — ĐIỀU TUYẾN TOOL CALL TỪ LLM (TASK 2.1)
# ==============================================================================

TOOL_ROUTER = {
    "library_query": execute_library_query,
    "renew_book": execute_renew_book
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm điều tuyến (Dispatcher) — nhận quyết định từ LLM và thực thi Tool tương ứng.

    Cơ chế hoạt động:
      1. LLM quyết định chọn tool_name + arguments dựa trên câu hỏi người dùng.
      2. Dispatcher kiểm tra tool_name có hợp lệ không.
      3. Nếu hợp lệ → gọi hàm Python tương ứng và trả kết quả (Observation) cho LLM.
      4. Nếu không hợp lệ → trả về lỗi UNKNOWN_TOOL.
    """
    if tool_name == "library_query":
        # Tool tra cứu: Tìm thông tin sách/thẻ thư viện trong MOCK_DATABASE
        try:
            return execute_library_query(**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)

    elif tool_name == "renew_book":
        # Tool hành động: Gia hạn sách đang mượn
        try:
            return execute_renew_book(**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)

    else:
        return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
