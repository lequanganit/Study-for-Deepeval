import os
import requests
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import (
    FaithfulnessMetric,
    AnswerRelevancyMetric,
    ContextualRelevancyMetric
)
from deepeval.models import GeminiModel

# 1. Khởi tạo Gemini Judge với model tên chuẩn
gemini_judge = GeminiModel(
    model="gemini-3.6-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# 2. Hàm giả lập gọi API Chatbot RAG thật của dự án
def call_rag_chatbot_api(user_query: str):
    return {
        "actual_output": "Sản phẩm được bảo hành 12 tháng. Điều kiện là tem bảo hành phải còn nguyên vẹn.",
        "retrieval_context": [
            "Chính sách bảo hành: Sản phẩm được bảo hành 12 tháng kể từ ngày mua.",
            "Điều kiện bảo hành: Sản phẩm còn nguyên tem, không rơi vỡ hoặc vào nước."
        ]
    }

# 3. Hàm Automation Test
def test_rag_chatbot_pipeline():
    user_input = "Sản phẩm bảo hành bao lâu và điều kiện là gì?"

    # Gọi API nhận dữ liệu động tại runtime
    api_result = call_rag_chatbot_api(user_input)

    # Đưa toàn bộ vào LLMTestCase
    test_case = LLMTestCase(
        input=user_input,
        actual_output=api_result["actual_output"],
        retrieval_context=api_result["retrieval_context"]
    )

    # Khai báo FaithfulnessMetric (Tạm thời test 1 metric để tránh Rate Limit 429)
    faithfulness = FaithfulnessMetric(threshold=0.8, model=gemini_judge)

    # Thực hiện test
    assert_test(test_case, [faithfulness])