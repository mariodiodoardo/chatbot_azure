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

    // Simula il messaggio del bot
    const botMessage = document.createElement('div');
    botMessage.classList.add('message', 'bot');
    botMessage.textContent = 'Sto elaborando la tua richiesta...';
    chatBox.appendChild(botMessage);

    // Pulisci il campo di input
    document.getElementById('user-input').value = '';

    // Scorri automaticamente verso il basso
    chatBox.scrollTop = chatBox.scrollHeight;

    // Simula una risposta del bot dopo 1 secondo
    setTimeout(() => {
        botMessage.textContent = 'Ciao! Come posso aiutarti oggi?';
        chatBox.scrollTop = chatBox.scrollHeight;
    }, 1000);
}
