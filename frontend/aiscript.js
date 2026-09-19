// =========================
// GET HTML ELEMENTS
// =========================

const chatInput = document.getElementById("chatInput");
const sendButton = document.getElementById("sendButton");
const messagesContainer = document.querySelector(".messages-container");


// =========================
// SEND MESSAGE
// =========================

function sendMessage() {

    // Get the user's message and remove extra spaces
    const message = chatInput.value.trim();

    // Don't send empty messages
    if (message === "") {
        return;
    }


    // =========================
    // CREATE USER MESSAGE
    // =========================

    const userMessage = document.createElement("div");

    userMessage.classList.add("message", "user-message");

    userMessage.innerHTML = `
        <div class="message-content">

            <div class="message-header">
                <strong>You</strong>
            </div>

            <div class="message-bubble">
                ${message}
            </div>

        </div>

        <div class="avatar user-avatar">
            You
        </div>
    `;


    // Add the user's message to the chat
    messagesContainer.appendChild(userMessage);


    // Clear the input box
    chatInput.value = "";


    // Scroll to the newest message
    messagesContainer.scrollTop = messagesContainer.scrollHeight;


    // =========================
    // CREATE AI RESPONSE
    // =========================

    setTimeout(() => {

        const aiMessage = document.createElement("div");

        aiMessage.classList.add("message", "ai-message");

        aiMessage.innerHTML = `
            <div class="avatar ai-avatar">
                AI
            </div>

            <div class="message-content">

                <div class="message-header">
                    <strong>Health AI</strong>
                </div>

                <div class="message-bubble">
                    Message received
                </div>

            </div>
        `;


        // Add AI message
        messagesContainer.appendChild(aiMessage);


        // Scroll to newest message
        messagesContainer.scrollTop = messagesContainer.scrollHeight;

    }, 500);

}


// =========================
// SEND BUTTON
// =========================

sendButton.addEventListener("click", sendMessage);


// =========================
// ENTER KEY
// =========================

chatInput.addEventListener("keydown", function(event) {

    // Enter sends the message
    // Shift + Enter creates a new line

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        sendMessage();

    }

});