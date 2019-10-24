document.getElementById('create_journal').addEventListener('click', function(){
    document.getElementById('dimmer').style.display = 'block';
    document.getElementById('create_journal_parent').style.cssText = "display: block; z-index: 11; transition: 0.8s;";
})


document.getElementById('cancel_button').addEventListener('click', function(){
    document.getElementById('dimmer').style.display = 'none';
    document.getElementById('create_journal_parent').style.cssText = "display: none;";
})

$('#journal_form').on('submit', function newJournal(el) {
    el.preventDefault();
    var form = $('#journal_form').serialize();
    var url = window.location.href;
    var csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url: url,
        headers: {"X-CSRFToken": csrftoken},
        type: 'post',
        datatype: 'json',
        async: true,
        data: form,
        success: function(data) {
            if (data['error']) {
                $('#error').text(data['error']);
            }
            else if (data['success']) {
                location.reload();
            }
        }
    })
})