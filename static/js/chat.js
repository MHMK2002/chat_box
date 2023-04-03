function sendMessage(token, conversationId){
    var message = document.getElementById("chat-input").value;

    var data = {
        "message": message,
        "csrfmiddlewaretoken": token
    }

    // TODO: Send message to server with conversation id and then clear the input field and add the message to the chat window
    $.ajax({

    }).then();

}