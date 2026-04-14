import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
# Ensure the API key is available
if not api_key:
    raise ValueError("No API key found. Please check your .env file.")
client = OpenAI(api_key=api_key, base_url="http://localhost:1234/v1")
#client = OpenAI(api_key=api_key)


# Example function to query ChatGPT
def ask_chatgpt(user_message):
    response = client.chat.completions.create(
        model="gpt-5.1",  # gpt-4 turbo or a model of your preference
        messages=[{"role": "system", "content": "You are a helpful assistant specialized in history of Poland."},
                  {"role": "user", "content": user_message}],
        temperature=0.7
        )
    return response.choices[0].message.content


# Example usage
user = "What is winning Polish uprising? Step 1 is listing most important uprising in last 1000 years. Step 2 is to list in bullets with item: uprising name, dates, result."
response = ask_chatgpt(user)
print(response)

'''
   print(prompt_llm(prompt, 
                                     model="local-model", 
                                     base_url="http://localhost:1234/v1",
                                     api_key="not used"))


OpenAI
    
local from LM Studio 
    total time =   87929.63 ms /   664 tokens
'''