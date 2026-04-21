import datetime

def get_ai_response(user_query):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Simulate an Automotive AI response engine
    query = user_query.lower()
    
    response = ""
    if "oil" in query:
        response = "For an oil change, you should typically check your manufacturer's manual. Most modern cars recommend synthetic oil every 7,500 to 10,000 miles. Don't forget the filter!"
    elif "brake" in query or "brakes" in query:
        response = "If your brakes are squeaking, it's usually the wear indicator telling you your brake pads are getting thin. I'd recommend a visual inspection of your rotors and pads immediately."
    elif "engine" in query or "light" in query:
        response = "A check engine light can mean a loose gas cap, or something more serious like a failing oxygen sensor or catalytic converter. Try plugging in an OBD-II scanner to get the exact code!"
    elif "tire" in query or "tires" in query or "pressure" in query:
        response = "Always check the sticker on the driver's side door jamb for the correct tire pressure (PSI) for your vehicle. Don't use the max pressure listed on the tire itself!"
    elif "hello" in query or "hi" in query or "hey" in query:
        response = "Hey there! I'm AutoMechanic AI. What's going on under the hood today?"
    elif "time" in query:
        response = f"My clock says it's {current_time}. Perfect time to hit the garage!"
    else:
        response = "I'm mostly tuned to talk about cars right now. Ask me about your engine, oil, tires, or brakes!"
        
    return response

# Example direction:
# If user asks "Should I go for a run?", the AI sees it's 11 PM 
# and suggests an indoor stretch instead.
