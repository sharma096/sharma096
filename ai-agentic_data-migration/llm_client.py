from groq import Groq
import os
# client = Groq()

client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))
print(os.environ.get("GROQ_API_KEY", ""))
def call_llm(prompt: str) -> str:
   response = client.chat.completions.create(
       model="llama3-8b-8192",
       messages=[{"role": "user", "content": prompt}],
       temperature=0
   )
   return response.choices[0].message.content