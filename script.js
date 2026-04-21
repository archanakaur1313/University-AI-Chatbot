const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

// Handle enter key press
function handleKeyPress(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
}

// Ensure the scrolling makes the newest messages visible
function scrollToBottom() {
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Bot logic initialization
setTimeout(() => {
    addBotMessage("Welcome to the garage! I am AutoMechanic AI. Got a question about your engine, brakes, or oil?");
}, 600);

function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    // Show user message
    addUserMessage(text);
    
    // Clear the input
    userInput.value = '';

    // Simulate bot thinking with typing indicator
    const typingElement = addTypingIndicator();

    fetch('/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text })
    })
    .then(res => res.json())
    .then(data => {
        typingElement.remove();
        addBotMessage(data.response);
    })
    .catch(err => {
        typingElement.remove();
        addBotMessage("Sorry, there was an error connecting to the garage's computer.");
        console.error(err);
    });
}

function addUserMessage(text) {
    const div = document.createElement('div');
    div.className = 'message user-message';
    div.textContent = text;
    chatBox.appendChild(div);
    scrollToBottom();
}

function addBotMessage(text) {
    const div = document.createElement('div');
    div.className = 'message bot-message';
    div.textContent = text;
    chatBox.appendChild(div);
    scrollToBottom();
}

function addTypingIndicator() {
    const div = document.createElement('div');
    div.className = 'typing-indicator bot-message message';
    
    for(let i=0; i<3; i++) {
        const dot = document.createElement('div');
        dot.className = 'typing-dot';
        div.appendChild(dot);
    }
    
    chatBox.appendChild(div);
    scrollToBottom();
    return div;
}
