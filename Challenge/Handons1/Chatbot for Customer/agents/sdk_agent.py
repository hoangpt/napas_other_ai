from google_adk import ADKAgent

class SDKAgent(ADKAgent):
    def __init__(self, data_path):
        super().__init__()
        with open(data_path, encoding='utf-8') as f:
            self.data = f.read()

    def answer(self, question):
        return self.generate_answer(question, context=self.data)
