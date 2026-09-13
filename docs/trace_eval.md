# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** Nguyễn Thị Minh Khánh  
> **Mã Sinh Viên / Mã Học viên:** 2A202602546  
> **Chủ đề Lựa chọn:** Gợi ý 1.2 — Trợ lý Quản lý Thư viện & Tài liệu (Tra cứu vị trí sách, tình trạng mượn/trả và gia hạn tài liệu)  

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm |
| :--- | :---: | :--- |
| **1. Multi-step Reasoning** | 4 / 5 | Bài toán cần sử dụng nhiều bước suy luận liên tiếp nối tiếp nhau: (1) Nhận yêu cầu từ người dùng → (2) Xác định loại thao tác (tra cứu sách hay gia hạn tài liệu) → (3) Trích xuất tham số phù hợp (mã sách, mã thẻ thư viện) → (4) Gọi Tool tương ứng → (5) Tổng hợp kết quả trả lời. Với trường hợp gia hạn, cần tra cứu tình trạng mượn trước rồi mới thực hiện gia hạn. Chưa đạt 5 vì một số truy vấn đơn giản chỉ cần 1-2 bước. |
| **2. Tool Interaction** | 5 / 5 | Đây là điểm mạnh nhất của bài toán vì hệ thống cần tương tác cơ sở dữ liệu của thư viện để lấy thông tin về người mượn, loại sách mượn, quyển sách đã mượn, số lượng còn lại, hạn trả...|
| **3. Dynamic Decision** | 4 / 5 | Quyết định bước tiếp theo phụ thuộc mạnh vào bước trước: Nếu tra cứu sách ở trạng thái "Đang được mượn" thì cần thông báo thời gian cần phải trả, thời gian được gia hạn. Nếu tra cứu sách ở trạng thái "đang còn" thì trả vị trí |
| **4. Long Horizon Goal** | 4 / 5 | Agent phải duy trì ngữ cảnh xuyên suốt nhiều lượt hội thoại: người dùng có thể hỏi tra cứu sách → hỏi thêm về tình trạng mượn → yêu cầu gia hạn, tất cả trong cùng một phiên. Agent cần nhớ mã sách, mã thẻ thư viện đã đề cập trước đó để không yêu cầu nhập lại. Chưa đạt 5 vì mục tiêu cuối cùng không quá phức tạp so với các hệ thống quản lý đa miền. |
| **TỔNG ĐIỂM AGENTIC FIT** | **17 / 20** | *Tổng điểm 17/20 > 12/20: Bài toán Trợ lý Thư viện rất phù hợp triển khai Agentic System. Hệ thống đòi hỏi kết hợp tra cứu dữ liệu thời gian thực và hành động cập nhật (gia hạn), suy luận đa bước có điều kiện, phù hợp kiến trúc ReAct Agent + MCP.* |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
[
  {
    "step": 1,
    "action_type": "TOOL_EXECUTION",
    "tool_name": "academic_query",
    "arguments": {
      "student_id": "SV2026001"
    },
    "observation": {
      "status": "SUCCESS",
      "student_id": "SV2026001",
      "data": {
        "full_name": "Nguyễn Văn An",
        "gpa": 3.85
      }
    },
    "latency_ms": 120.5
  }
]
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [ ] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini/OpenAI).
- **Tổng số Test Cases đã chạy thành công:** ___ / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** ___ lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.

---

> ✅ **HOÀN TẤT NỘP BÀI:** Sao chép đường link GitHub Repository cá nhân của bạn và dán vào ô nộp bài trên hệ thống LMS VLearn để hoàn tất Bài Lab 3!
