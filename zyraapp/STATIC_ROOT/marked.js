$.ajax({
    type: 'POST',
    url: '',
    data: {
        'question': question,
        csrfmiddlewaretoken: '{{ csrf_token }}'
    },
    success: function(response) {
        $('.waiting').remove();
        // Parse Markdown response to HTML using marked.js
        var htmlResponse = marked(response);
        $('#chat-history').append('<p><strong>Bot:</strong> ' + htmlResponse + '</p>');
    }
});
