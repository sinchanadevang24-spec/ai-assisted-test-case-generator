# AI-Assisted Test Case Generator

## Overview

This project is an AI-assisted QA automation tool that uses an Large Language Model (LLM) to generate software test cases and automated test scripts from plain-English requirements, API descriptions, and web application requirements.

The project demonstrates how AI can assist QA engineers by generating test cases and automation code using Python, pytest, and Playwright.

## Features

- Generate test cases from plain-English requirements
- Generate pytest automation code
- Generate API test scripts
- Generate Playwright browser automation tests
- Execute generated tests automatically
- Validate AI-generated test code
- Review and debug AI-generated test scripts

## Technologies Used

- Python
- Groq API
- Llama Large Language Model
- pytest
- Requests
- Playwright
- GitHub

## Project Structure

```text
ai-test-case-generator/
│
├── generators/
│   ├── generate_tests.py
│   ├── generate_api_tests.py
│   └── generate_playwright_tests.py
│
├── tests/
│   ├── test_login.py
│   ├── test_api.py
│   └── test_website.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── conftest.py
