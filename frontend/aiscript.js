// =========================
// GET HTML ELEMENTS
// =========================

const chatInput = document.getElementById("chatInput");
const sendButton = document.getElementById("sendButton");
const messagesContainer =
    document.querySelector(".messages-container");


// =========================
// SEND MESSAGE
// =========================

async function sendMessage() {

    // Get the user's message
    const message = chatInput.value.trim();


    // Don't send empty messages
    if (message === "") {
        return;
    }


    // =========================
    // DISPLAY USER MESSAGE
    // =========================

    const userMessage =
        document.createElement("div");

    userMessage.classList.add(
        "message",
        "user-message"
    );


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


    messagesContainer.appendChild(userMessage);


    // Clear input
    chatInput.value = "";


    // Scroll to newest message
    messagesContainer.scrollTop =
        messagesContainer.scrollHeight;


    // =========================
    // SEND MESSAGE TO BACKEND
    // =========================

    try {

        const response = await fetch(
            "http://localhost:8000/ai",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    message: message
                })
            }
        );


        // Check whether backend returned an error
        if (!response.ok) {

            throw new Error(
                "Server returned an error."
            );
        }


        // Get JSON response
        const resultData =
            await response.json();


        console.log(
            "AI response:",
            resultData
        );


        // =========================
        // DISPLAY AI RESPONSE
        // =========================

        const aiMessage =
            document.createElement("div");

        aiMessage.classList.add(
            "message",
            "ai-message"
        );


        aiMessage.innerHTML = `

            <div class="avatar ai-avatar">
                AI
            </div>

            <div class="message-content">

                <div class="message-header">
                    <strong>Health AI</strong>
                </div>

                <div class="message-bubble">
                    ${resultData.response}
                </div>

            </div>

        `;


        messagesContainer.appendChild(aiMessage);


        // Scroll to newest message
        messagesContainer.scrollTop =
            messagesContainer.scrollHeight;


    } catch (error) {

        console.error(error);


        // Display error in chat
        const errorMessage =
            document.createElement("div");

        errorMessage.classList.add(
            "message",
            "ai-message"
        );


        errorMessage.innerHTML = `

            <div class="avatar ai-avatar">
                AI
            </div>

            <div class="message-content">

                <div class="message-header">
                    <strong>Health AI</strong>
                </div>

                <div class="message-bubble">
                    Sorry, I couldn't connect to the server.
                </div>

            </div>

        `;


        messagesContainer.appendChild(
            errorMessage
        );


        messagesContainer.scrollTop =
            messagesContainer.scrollHeight;
    }
}


// =========================
// SEND BUTTON
// =========================

sendButton.addEventListener(
    "click",
    sendMessage
);


// =========================
// ENTER KEY
// =========================

chatInput.addEventListener(
    "keydown",
    function(event) {

        // Enter = send
        // Shift + Enter = new line

        if (
            event.key === "Enter" &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendMessage();
        }
    }
);