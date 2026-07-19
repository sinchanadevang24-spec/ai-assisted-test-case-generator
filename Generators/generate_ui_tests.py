from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

# Step 1: Describe the webpage we're testing
page_description = """
Website: https://the-internet.herokuapp.com/login
Description: A login page for practicing test automation.
Valid username: tomsmith
Valid password: SuperSecretPassword!
On successful login, the page redirects to a URL containing "/secure" 
and shows the text "You logged into a secure area!"
On failed login, it shows the text "Your username is invalid!" 
or "Your password is invalid!" without navigating away.
"""

# Step 2: Ask the AI to write Playwright test code
prompt = f"""
Write a Python pytest test file using Playwright (pytest-playwright) for this webpage:
{page_description}

Rules:
- Only output valid Python code, nothing else
- No explanations, no markdown formatting
- Use the "page" fixture provided by pytest-playwright
- Include 2 test cases: successful login, and failed login with wrong password
- Use page.goto(), page.fill(), page.click(), and assertions on page content or URL
"""

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

generated_code = response.choices[0].message.content
generated_code = generated_code.replace("```python", "").replace("```", "")

with open("test_login_ui.py", "w") as f:
    f.write(generated_code)

print("Test file saved as test_login_ui.py")