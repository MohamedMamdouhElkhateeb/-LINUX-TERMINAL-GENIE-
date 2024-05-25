import requests
import json
import sys


# Replace 'YOUR_API_KEY' with your actual Google Cloud API key

API_KEY = 'Your API Key'
text=""

if len(sys.argv) > 1:

    text = sys.argv[1]
else:
    exit()

def is_bash_related(text):
  """Checks if a question is likely related to Linux Bash."""
  keywords = ["bash", "shell script", "command line", "linux terminal", "sh"]
  for keyword in keywords:
    if keyword.lower() in text.lower():
      return True
  return False

if is_bash_related(text):

    # Define the URL of the Google AI Platform Generative Language API endpoint
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

    # Prepare the request body with the prompt and content structure
    data = {
    "contents": [
        {
        "parts": [
            {
            "text":text
            }
        ]
        }
    ]
    }

    # Set the headers specifying the content type as JSON
    headers = {'Content-Type': 'application/json'}

    # Send the POST request using the requests library
    response = requests.post(url, headers=headers, json=data)

    # Handle response
    if response.status_code == 200:
        # Parse the JSON response
        response_data = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')
        # Access the generated text from the response (assuming the structure remains consistent)
        print(response_data )
    else:
        print(f"Error: API request failed with status code: {response.status_code}")

else:
    print("This question does not appear to be related to Bash.")
