# MMChatbot Monorepo

## Kiến trúc hệ thống

Hệ thống gồm 4 agent, mỗi agent chạy trong một Docker container riêng biệt:

- **Agent QA**: Điều phối, trả lời câu hỏi chung, chuyển tiếp tới các agent chuyên biệt.
- **Agent Frequent QA**: Trả lời về chính sách bảo hành, đổi trả.
- **Agent Tư vấn Sản phẩm**: Tư vấn, hỏi đáp sản phẩm, lưu đơn hàng, filter sản phẩm.
- **Agent Đơn hàng**: Hỏi đáp về đơn hàng, tra cứu trạng thái đơn theo order code.

## Cấu trúc thư mục

```
agents/
  qa/
  frequent_qa/
  product_advisor/
  order_agent/
db/
```

## Chạy hệ thống

```bash
docker-compose up --build
```

## Mỗi agent có thể truy cập qua các port riêng biệt (xem docker-compose.yml) 