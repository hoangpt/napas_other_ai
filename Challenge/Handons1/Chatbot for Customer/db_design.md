# Thiết kế bảng lưu cache câu trả lời từ LLM

## Bảng: `llm_response_cache`

| Tên trường      | Kiểu dữ liệu    | Mô tả                                  |
|-----------------|----------------|----------------------------------------|
| id              | INT, PK, AI    | Khóa chính, tự tăng                   |
| user_id         | VARCHAR(64)    | ID người dùng đặt câu hỏi             |
| question_hash   | VARCHAR(64)    | Hash của câu hỏi (để so khớp nhanh)    |
| question_text   | TEXT           | Nội dung câu hỏi gốc                   |
| response_text   | TEXT           | Câu trả lời từ LLM                     |
| created_at      | DATETIME       | Thời điểm lưu vào cache                |
| updated_at      | DATETIME       | Thời điểm cập nhật gần nhất            |
| hit_count       | INT            | Số lần truy xuất cache                 |

**Ghi chú:**
- `user_id` là định danh người dùng, có thể là email, username hoặc mã hệ thống.
- `question_hash` nên dùng SHA256 hoặc MD5 của câu hỏi để so khớp nhanh.
- Có thể tạo chỉ mục (index) trên trường `question_hash` để tăng tốc truy vấn.
```

---

**SQL Statement:**

```sql
CREATE TABLE llm_response_cache (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id VARCHAR(64) NOT NULL,
    question_hash VARCHAR(64) NOT NULL,
    question_text TEXT NOT NULL,
    response_text TEXT NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    hit_count INT DEFAULT 0,
    INDEX idx_question_hash (question_hash)
);
```

---

**dbdiagram (dbml):**

```dbml
Table llm_response_cache {
    id            int       [pk, increment, note: 'Khóa chính, tự tăng']
    user_id       varchar(64) [note: 'ID người dùng đặt câu hỏi']
    question_hash varchar(64) [index, note: 'Hash của câu hỏi (SHA256 hoặc MD5) để so khớp nhanh']
    question_text text        [note: 'Nội dung câu hỏi gốc']
    response_text text        [note: 'Câu trả lời từ LLM']
    created_at    datetime    [note: 'Thời điểm lưu vào cache']
    updated_at    datetime    [note: 'Thời điểm cập nhật gần nhất']
    hit_count     int         [note: 'Số lần truy xuất cache']
}
```

