from dotenv import load_dotenv
from google import genai
from google.genai.types import GenerateContentConfig

load_dotenv()


client = genai.Client()


print("\n------------ CHATBOT (ENTER 'quit' to close) -----------------\n")
while True:
    prompt = input("You : ")

    if prompt == "":
        print("Enter a valid prompt to continue")
        continue
    elif prompt.lower() == 'quit':
        print(f"Agent : Bye Bye")
        exit(0)

    response = client.models.generate_content(
        model='gemini-3.5-flash-lite',
        contents=prompt,
        config=GenerateContentConfig(
            temperature=0
        )
    )


    print(f"Agent : {response.text}")

    
    assert response.usage_metadata is not None
    tokens_used = response.usage_metadata.total_token_count
    print(f"Tokens Used : {tokens_used}")