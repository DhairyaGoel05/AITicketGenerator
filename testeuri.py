# Using requests library
import requests

def generate_completion():
    url = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIwNWY3N2NiYy00NWEyLTQ5NjctYWFjNS1kYjBjYjYxYjFkMGYiLCJwaG9uZSI6Iis5MTkzMTA3NzEwMDgiLCJpYXQiOjE3NDQyMTYwNDYsImV4cCI6MTc3NTc1MjA0Nn0.JxLQHqKG5RJKeVJGdYu8YR91Dj3iUS5sXeGwIG89dU0"
    }
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Write a poem about artificial intelligence"
            }
        ],
        "model": "gpt-4.1-nano",
        "max_tokens": 1000,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    print(data)

generate_completion()