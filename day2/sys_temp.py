import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq  

load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API key not found.")

client = Groq(api_key=my_api_key)

model ="openai/gpt-oss-120b"    
role="user"
prompt="suggest only one name for my food company"
#SYSTEM 
message_system={
    "role": "system",
    "content": "You are a brand manager who suggests name for my food company. Name should be in one word"
}

message={
    "role": role,
    "content": prompt
}

messages = [message_system, message]
#Iemperature by default is 0 meaning safe. Range is [0,2]
response = client.chat.completions.create(model=model, messages=messages,temperature=2)
# print(response)

print("#############################")

answer = response.choices[0].message.content
print(answer)