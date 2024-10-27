document.getElementById('send-button').addEventListener('click', function() {
    sendMessage();
});

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === "") return;

    // Aggiungi il messaggio dell'utente
    const chatBox = document.getElementById('chat-box');
    const userMessage = document.createElement('div');
    userMessage.classList.add('message', 'user');
    userMessage.textContent = userInput;
    chatBox.appendChild(userMessage);

    // Messaggio di attesa del bot
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot');
    botMessage.textContent = 'Sto elaborando la tua richiesta...';
    chatBox.appendChild(botMessage);

    // Pulisci il campo di input
    document.getElementById('user-input').value = '';

    // Scorri automaticamente verso il basso
    chatBox.scrollTop = chatBox.scrollHeight;

    // Invio della richiesta all'API Flask
    fetch("https://hidden-phantasm-9qxjwrj49552q4v-3000.app.github.dev/getPromptContent", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ content: userInput })
    })
    .then(response => response.json())
    .then(data => {
        // Modifica il testo del bot con la risposta dell'API
        botMessage.textContent = data.message || "Risposta non disponibile";
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => {
        // Mostra un messaggio di errore se la richiesta fallisce
        botMessage.textContent = "Si è verificato un errore, riprova.";
        console.error("Errore:", error);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
