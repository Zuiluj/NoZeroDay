// receive ajax url from anchor link in template then perform ajax
$('header').on('click', 'a.entry_select', function getEntry(el) {
        el.preventDefault();
        var url = $(this).attr('href');
        $.ajax({
            url: url,
            type: 'get',
            datatype: 'json',
            async: true,
            success: function(data) {
                // replace the three entries of the journal with the received json
                $('#entry_title').val(data['title']);
                $("#plan_today").val(data['plan_today']);
                $("#did_today").val(data['did_today']);
                $("#plan_tom").val(data['plan_tom']);
                $("#date_created").val(data['date_created']);
            }
        })
});


// save entry 
$('#entry_data').on('submit', function saveEntry(el) {
    el.preventDefault();
    var form = $('#entry_data').serialize();
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
            var result = $(data).find('#entries').html();
            $('#entries').html(result);   
        }
    })
})

// remove current entries
$('#new_entry').on('click', function clearEntry(el) {
    $('#entry_title').val('Title');
    $("#plan_today").val('');
    $("#did_today").val('');
    $("#plan_tom").val('');
})

document.getElementById('delete_journal').addEventListener('click', function () {
    document.getElementById('dimmer').style.display = 'block';
    document.getElementById('delete_confirm').style.cssText = 'display: block; z-index: 11';
})

document.getElementById('delete_cancel').addEventListener('click', function () {
    document.getElementById('dimmer').style.display = 'none';
    document.getElementById('delete_confirm').style.display = 'none';
})

$('#delete_journal_cnfrm').on('click', function deleteJournal(el) {
    var url = window.location.href;
    var csrftoken = Cookies.get('csrftoken');
    $.ajax({
        url: url,
        headers: {"X-CSRFToken": csrftoken},
        type: 'delete',
        async: true,
        success: function(data) {
            link = 'http://' + document.location.host.toString() + '/journals/'
            window.location.replace(link);
        }
    })
})