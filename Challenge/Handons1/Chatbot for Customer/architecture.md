Dưới đây là kiến trúc tổng thể đề xuất để sử dụng mô hình Google Agent Development Kit (ADK) với nhiều agent trên một hệ thống chatbot hiện đại, phù hợp cho website napas.com.vn:

---

## 1. Tổng quan kiến trúc

```
+----------------------+
|      Website UI      |  <-- Nhúng widget chat (JS SDK)
+----------+-----------+
           |
           v
+----------------------+
|   Chatbot Gateway    |  <-- Xử lý nhận/gửi message, bảo mật, logging
+----------+-----------+
           |
           v
+---------------------------------------------------+
|            Orchestrator / Router (ADK)            |
|  (Điều phối, phân luồng hội thoại giữa các agent) |
+----------+-----------+-----------+----------------+
           |           |           |
           v           v           v
+----------+   +-------+-----+   +-----------------+
|  FAQ     |   | Lãnh đạo   |   | Product         |
|  Agent   |   | Agent      |   | Agent           |
+----------+   +------------+   +-----------------+
           |           |           |
           +-----------+-----------+
                       |
                       v
          +---------------------------+
          |   Nguồn dữ liệu/Knowledge |
          |   (FAQ, DB, API, CMS,...) |
          +---------------------------+
```

---

## 2. Giải thích từng thành phần

### 2.1 Website UI
- Giao diện chat tích hợp lên website (JS widget hoặc iframe).
- Gửi/nhận message với Chatbot Gateway qua WebSocket hoặc REST API.

### 2.2 Chatbot Gateway
- Là entrypoint nhận request chat từ web, kiểm tra bảo mật, xác thực người dùng (nếu cần).
- Có thể ghi log, thống kê, chống spam, kiểm soát truy cập.
- Forward message vào Orchestrator (ADK).

### 2.3 Orchestrator / Router (ADK)
- Thành phần trung tâm, dùng Google ADK để:
    - Tách nghĩa, xác định intent, route hội thoại đến agent phù hợp (FAQ, Lãnh đạo, Product).
    - Có thể phối hợp nhiều agent khi câu hỏi phức tạp.
    - Có thể duy trì context, lịch sử hội thoại.
- Có thể ứng dụng Gemini, Dialogflow, hoặc custom NLP cho việc phân luồng.

### 2.4 Các Agent chuyên biệt
- **FAQ Agent**: Trả lời các câu hỏi thường gặp, có thể dùng knowledge base (file, DB, API).
- **Lãnh đạo Agent**: Trả lời thông tin về đội ngũ lãnh đạo (profile, chức vụ, kinh nghiệm).
- **Product Agent**: Tư vấn, giải đáp về các sản phẩm/dịch vụ của Napas.
- Các agent này có thể dùng mô hình LLM (Gemini, GPT, hoặc mô hình nhỏ hơn) và truy cập dữ liệu chuyên biệt riêng.

### 2.5 Nguồn dữ liệu / Knowledge Base
- Các agent sẽ truy vấn vào các nguồn dữ liệu nội bộ (FAQ text, database lãnh đạo, API product…).

---

## 3. Luồng hoạt động

1. User chat trên website → gửi message lên Chatbot Gateway.
2. Gateway chuyển message cho Orchestrator (ADK).
3. Orchestrator phân tích câu hỏi, quyết định agent nào phù hợp (có thể dùng intent classification, entity extraction).
4. Orchestrator chuyển message cho agent tương ứng.
5. Agent truy vấn dữ liệu, trả lời → Orchestrator → Gateway → trả về UI.

---

## 4. Công nghệ gợi ý

- **Orchestrator/Router**: Google ADK (Agent Development Kit).
- **NLP phân tích ý định**: Dialogflow, Gemini hoặc tích hợp NLP riêng nếu cần.
- **Agent chuyên biệt**: Có thể code Python (nếu dùng ADK), hoặc tích hợp với Google Cloud Functions, Vertex AI, hoặc API nội bộ.
- **Knowledge base**: Google Cloud Datastore, Firestore, SQL, hoặc connect CMS/API tùy yêu cầu.

---

## 5. Lưu ý mở rộng

- Có thể bổ sung thêm agent mới mà không ảnh hưởng hệ thống tổng thể.
- Orchestrator có thể kết hợp nhiều agent nếu một câu hỏi liên quan nhiều lĩnh vực.
- Có thể mở rộng tích hợp đăng nhập, lưu lịch sử chat, gửi email/ticket nếu cần.

---

## 6. Mẫu sơ đồ kiến trúc

````markdown name=architecture.md
```mermaid
flowchart TD
  A[Website UI] --> B[Chatbot Gateway]
  B --> C[Orchestrator (ADK)]
  C --> D1[FAQ Agent]
  C --> D2[Lãnh đạo Agent]
  C --> D3[Product Agent]
  D1 --> E[FAQ Data/KB]
  D2 --> F[Lãnh đạo DB/API]
  D3 --> G[Product DB/API]
```
````
