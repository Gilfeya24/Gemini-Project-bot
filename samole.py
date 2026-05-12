import os
import google.generativeai as genai

genai.configure(api_key=os.environ["AIzaSyDmXE1t0ezu9cR6cMxUEeQC3wLEX5__KdE"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Hello")
print(response.text)