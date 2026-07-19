
import pytest

@pytest.mark.parametrize("username, password, expected_url, expected_text", [
    ("tomsmith", "SuperSecretPassword!", "/secure", "You logged into a secure area!"),
    ("tomsmith", "wrongpassword", None, "Your password is invalid!")
])
def test_login(page, username, password, expected_url, expected_text):
    page.goto("https://the-internet.herokuapp.com/login")
    page.fill("input[id='username']", username)
    page.fill("input[id='password']", password)
    page.click("button[type='submit']")

    if expected_url:
        assert page.url.endswith(expected_url)
        assert "Secure Area" in page.text_content("h2")
    else:
        assert page.url == "https://the-internet.herokuapp.com/login"
        assert page.query_text("#flash") == expected_text
