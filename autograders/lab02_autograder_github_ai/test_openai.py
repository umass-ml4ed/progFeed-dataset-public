import os
from openai import OpenAI

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")  # Fetch from environment variable
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

    # Read the file openaiprompt and put in a string
    with open("openaiprompt_with_desc", "r") as file:
        prompt = file.read()

    # Create the chat completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a teacher trying to give hints to your students to help them solve their programming assignments."},
            {"role": "user", "content": prompt}
        ]
    )
    # Print the result
    print(completion.choices[0].message.content)