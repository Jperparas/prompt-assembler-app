from groq import Groq
class GroqService:

    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
    
    def generate(self, prompt):
        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content



