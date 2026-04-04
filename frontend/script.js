/*
Name: script.js
Type: Frontend Logic (Placeholder)
Location: /ui/script.js
Summary:
    Handles UI events only. No AI or backend logic implemented.
*/

const chatWindow = document.getElementById("chat-window");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

sendBtn.addEventListener("click", handleSend);

// Allow Enter key to send
input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        handleSend();
    }
});

function handleSend() {
    const message = input.value.trim();

    if (!message) return;

    addMessage("user", message);

    // TODO: Replace this with actual AI/backend call
    addMessage("bot", "[Bot response goes here]");

    input.value = "";
}

function addMessage(sender, text) {
    const msg = document.createElement("div");
    msg.classList.add("message", sender);
    msg.textContent = text;

    chatWindow.appendChild(msg);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}