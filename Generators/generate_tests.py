from groq import Groq
import os

# Step 1: Log in to Groq using the saved key
client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Step 2: This is your input - the requirement you want tested
requirement = "User should be able to log in with a valid email and password."

# Step 3: Build a prompt that asks for CODE, not plain text
prompt = f"""
Write a Python test file using pytest for this requirement:
{requirement}

Rules:
- Only output valid Python code, nothing else
- Do not include any explanation, notes, or markdown formatting
- Use simple pytest functions (def test_...)
- Since there is no real application to test yet, write the test logic
  using placeholder functions like login(email, password) that we will
  replace later
- Include at least 3 test cases: valid login, wrong password, empty email
"""

# Step 4: Send it to the AI and get the answer back
response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

# Step 5: Get just the code text from the response
generated_code = response.choices[0].message.content

# Step 6: Sometimes AI wraps code in ```python blocks - remove those if present
generated_code = generated_code.replace("```python", "").replace("```", "")

# Step 7: Save the code into a new file called test_login.py
with open("test_login.py", "w") as f:
    f.write(generated_code)

print("Test file saved as test_login.py")