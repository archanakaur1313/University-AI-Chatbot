import datetime

def get_ai_response(user_query):
    # Training with Time: Fetching real-time context
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    hour = datetime.datetime.now().hour
    
    query = user_query.lower()
    
    # Mechanic Logic
    if "oil" in query:
        response = "For an oil change, check your manual. Most modern cars need synthetic oil every 7,500 miles. Don't forget the filter!"
    elif "brake" in query:
        response = "Squeaking pads usually mean they are getting thin. Check your rotors and pads immediately!"
    elif "engine" in query or "light" in query:
        response = "A check engine light could be a loose gas cap or a sensor issue. Use an OBD-II scanner to find the code."
    elif "hello" in query or "hi" in query:
        response = "Hey there! I'm AutoMechanic AI. What's going on under the hood today?"
    else:
        response = "I'm tuned for cars! Ask me about your engine, oil, or brakes. Or ask me the time!"

    # The "Time Awareness" Twist
    if hour >= 18: # After 6 PM
        response += f" \n\n(Note: It's {current_time}. The physical garage is closed, but I'm here to help digitally!)"
    
    return response
