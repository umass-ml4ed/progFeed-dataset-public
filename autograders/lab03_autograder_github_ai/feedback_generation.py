import csv
import json
from openai import OpenAI
import os

def get_student_email(metadata_file="../submission_metadata.json"):
    try:
        with open(metadata_file) as f:
            metadata = json.load(f)
            return metadata["users"][0].get("email", "").strip().lower()
    except Exception as e:
        print(f"⚠️ Could not read {metadata_file}: {e}")
        return None

def student_consented(email, consent_file="consent.csv"):
    try:
        with open(consent_file, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("Email", "").strip().lower() == email:
                    return row.get("AI", "").strip().lower() == "yes"
        # No match → still generate feedback
        return True
    except FileNotFoundError:
        print("⚠️ consent.csv not found, defaulting to generate AI feedback.")
        return True

def generate_ai_feedback(problem_description_file, file_name, function_name, openaiprompt):
    api_key = os.getenv("OPENAI_API_KEY")  # Fetch from environment variable
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set.")

    # Initialize the OpenAI client with the API key
    client = OpenAI(api_key=api_key)

 
    prompt = ""
    # Append the problem description to the prompt
    with open(problem_description_file, "r") as file:
        problem_description = file.read()
    prompt += f"\n\nproblem:\n{problem_description}\n\n" 
    
    # Append the student's code to the prompt
    with open(file_name, "r") as file:
        code = file.read()
    prompt += f"\n\nHere is the student's code for {function_name}:\n{code}\n\n"

   # Read the file openaiprompt and put in a string
    with open(openaiprompt, "r") as file:
        prompt += file.read()

    prompt += "\n\nOnly give hints for the given function: " + function_name + "\n"

    # print("Final prompt sent to OpenAI:", prompt)  # Debugging line
    # Create the chat completion
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a teacher trying to give hints to your students to help them solve their programming assignments."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return completion.choices[0].message.content
