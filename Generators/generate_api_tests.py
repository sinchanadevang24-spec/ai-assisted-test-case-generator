from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Step 1: Describe the real API endpoint we're testing
api_description = """
Endpoint: GET https://jsonplaceholder.typicode.com/users/2
Description: Returns details of a single user as JSON.
Expected successful response: status code 200, and JSON containing "id", "name", "username", "email".
If user does not exist (e.g. /users/999), it returns status code 404 with an empty JSON object.
"""

# Step 2: Ask the AI to write real pytest tests using the requests library
prompt = f"""
Write a Python pytest test file for this API:
{api_description}

Rules:
- Only output valid Python code, nothing else
- No explanations, no markdown formatting
- Use the "requests" library to make real HTTP calls
- Include at least 2 test cases: a successful request, and a 404 case
- Use assert statements to check status code and JSON fields
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

generated_code = response.choices[0].message.content
generated_code = generated_code.replace("```python", "").replace("```", "")

with open("test_api.py", "w") as f:
    f.write(generated_code)

print("Test file saved as test_api.py")