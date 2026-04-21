import os
import google.generativeai as genai

# Setup Gemini AI
# Ideally, you should set this as an environment variable for security:
# export GEMINI_API_KEY="your_key_here"
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDpTp1EwPsMIFvN9HtytX30wfEDLXQkSmo")

genai.configure(api_key=API_KEY)

# Initializing the model with the "Expert Automotive Mechanic" persona
model = genai.GenerativeModel(
    model_name="gemini-flash-latest",
    system_instruction=(
        "You are 'AutoMechanic AI', a world-class automotive mechanic with 30 years of experience. "
        "Your personality is helpful, professional, and mechanical-minded. "
        "Provide expert technical advice on car repairs, diagnostics, and vehicle maintenance. "
        "Always prioritize safety and suggest professional inspections for critical issues like brakes or engine trouble. "
        "Keep your tone consistent with being in a high-tech garage."
    )
)

def get_ai_response(user_query):
    try:
        # Generate the response using Gemini
        response = model.generate_content(user_query)
        return response.text
    except Exception as e:
        # Fallback to a helpful error message if the API fails
        return f"Sorry, I'm having trouble connecting to the shop's computer. Error: {str(e)}"

# Directions:
# Previously we had manual rules here. Now, Gemini handles everything dynamically
# while following the 'AutoMechanic AI' persona set in the system_instruction.
