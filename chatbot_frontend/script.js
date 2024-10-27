document.getElementById('send-button').addEventListener('click', function() {
    sendMessage();
});

document.getElementById('user-input').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});

async function callPrompt(contentStr) {
    const payload = { content: contentStr }; // Crea l'oggetto payload

    const response = await fetch('https://hidden-phantasm-9qxjwrj49552q4v-3000.app.github.dev/getPromptContent', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Imposta il Content-Type come application/json
        },
        body: JSON.stringify(payload) // Invia l'oggetto come JSON
    });

    const result = await response.json();
    return result;
}

function formatReport(text) {
    // Replace ** with <strong> tags for bold text
    let formattedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

    // Replace numbered items with an ordered list
    formattedText = formattedText.replace(/(\d\.)/g, '<br><ol><li>');
    formattedText = formattedText.replace(/\[doc\d+\]/g, (match) => `${match}</li>`);

    // Replace bullet points with an unordered list
    formattedText = formattedText.replace(/-\s/g, '<ul><li>');
    formattedText = formattedText.replace(/\s(?=Damage|Severity|Size)/g, '</li><li>');
    formattedText += '</li></ul></ol>';

    // Add a newline at the end if required
    formattedText = formattedText.replace(/\n/g, '<br>');

    return formattedText;
}

async function sendMessage() {
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
    botMessage.textContent = 'Thinking...';
    chatBox.appendChild(botMessage);

    // Pulisci il campo di input
    document.getElementById('user-input').value = '';

    // Scorri automaticamente verso il basso
    chatBox.scrollTop = chatBox.scrollHeight;

    // Ottieni la risposta dal bot e aggiorna il messaggio
    try {
        let responseMessage = await callPrompt(userInput);
        responseMessage = JSON.parse(responseMessage).choices[0].message.content;
        const formatResponse = formatReport(responseMessage);
        botMessage.innerHTML = formatResponse;
    } catch (error) {
        botMessage.textContent = "Sorry, try again later.";
        console.error("Error:", error);
    }

    chatBox.scrollTop = chatBox.scrollHeight;
}
