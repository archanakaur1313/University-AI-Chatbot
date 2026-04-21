from flask import Flask, request, jsonify, send_from_directory
from chatbot import get_ai_response

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('message', '')
    
    if not user_query:
        return jsonify({"response": "I didn't catch that."})

    try:
        # Call the logic from your chatbot.py snippet
        response = get_ai_response(user_query)
    except Exception as e:
        # Since 'antigravity.geospatial_query' is a mock method, this will catch the 
        # missing attribute error and return a fallback message so the UI still works!
        response = f"Simulated AI Response to: '{user_query}' \n(Note: antigravity engine not found - {str(e)})"
        
    return jsonify({"response": response})

if __name__ == '__main__':
    # Run the server on http://127.0.0.1:5000
    app.run(debug=True, port=5000)
