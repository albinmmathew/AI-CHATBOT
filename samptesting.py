from dotenv import load_dotenv
from amm_geminiassist import get_response, summarize_text, format_response

load_dotenv(override=True)  # This will now work

# Test 1: Basic AI response
print("=== Test 1: Basic Response ===")
response = get_response("Name 3 programming languages.")
print(response)

# Test 2: Summarization
print("\n=== Test 2: Summarization ===")
long_text = """
Python is a high-level programming language widely used for web development,
data science, machine learning, automation, and more.
"""
summary = summarize_text(long_text)
print(summary)

# Test 3: Formatting
print("\n=== Test 3: Formatted Output ===")
formatted = format_response(response, width=40)
print(formatted)
