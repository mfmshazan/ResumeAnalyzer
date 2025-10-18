import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("Error: GEMINI_API_KEY not found in .env file")
    exit(1)

print(f"API Key found: {GEMINI_API_KEY[:20]}...")

genai.configure(api_key=GEMINI_API_KEY)

print("\nListing available models:")
print("-" * 50)

try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"✓ {model.name}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Description: {model.description[:100]}...")
            print()
except Exception as e:
    print(f"Error listing models: {e}")
    print("\nTrying direct model access...")
    
    # Try common model names
    test_models = [
        'models/gemini-pro',
        'models/gemini-1.5-pro',
        'models/gemini-1.5-flash',
        'gemini-pro',
        'gemini-1.5-pro',
        'gemini-1.5-flash'
    ]
    
    for model_name in test_models:
        try:
            model = genai.GenerativeModel(model_name)
            response = model.generate_content("Say 'Hello'")
            print(f"✓ {model_name} - WORKS!")
            print(f"  Response: {response.text}")
            break
        except Exception as e:
            print(f"✗ {model_name} - {str(e)[:80]}")
