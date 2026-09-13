# -*- coding: utf-8 -*-
"""Script test nhanh tools.py"""
import sys
sys.stdout.reconfigure(encoding='utf-8')

from src.tools import dispatch_tool_call

print("=" * 60)
print("TEST 1: Tra cuu sach BK001 (co ton tai)")
print("=" * 60)
result = dispatch_tool_call("library_query", {"book_id": "BK001"})
print(result)
assert '"status": "SUCCESS"' in result
print(">>> PASSED\n")

print("=" * 60)
print("TEST 2: Tra cuu sach BK9999999 (khong ton tai)")
print("=" * 60)
result = dispatch_tool_call("library_query", {"book_id": "BK9999999"})
print(result)
assert '"status": "NOT_FOUND"' in result
print(">>> PASSED\n")

print("=" * 60)
print("TEST 3: Gia han sach BK002 cho the TV2026001")
print("=" * 60)
result = dispatch_tool_call("renew_book", {
    "book_id": "BK002",
    "library_card_id": "TV2026001",
    "extend_days": 14
})
print(result)
assert '"status": "SUCCESS"' in result
print(">>> PASSED\n")

print("=" * 60)
print("TEST 4: Goi tool khong ton tai")
print("=" * 60)
result = dispatch_tool_call("fake_tool", {"x": 1})
print(result)
assert '"UNKNOWN_TOOL"' in result
print(">>> PASSED\n")

print("=" * 60)
print("TAT CA 4 TEST PASSED! Tools.py hoat dong chinh xac.")
print("=" * 60)
