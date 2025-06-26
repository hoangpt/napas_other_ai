from google_adk import ADKApp
from agents.leader_agent import LeaderAgent
from agents.sdk_agent import SDKAgent

# Khởi tạo ứng dụng ADK
app = ADKApp()

# Đăng ký các agent
# TODO: only mock data, replace with real data in production
leader_agent = LeaderAgent('data/leaders.txt')

# TODO: only mock data, replace with real data in production
sdk_agent = SDKAgent('data/sdk_docs.txt')

app.register_agent('leader', leader_agent)
app.register_agent('sdk', sdk_agent)

if __name__ == '__main__':
    # Chạy app theo chuẩn Google ADK (có thể là HTTP server hoặc socket, tùy cấu hình adk-ui)
    app.run()
