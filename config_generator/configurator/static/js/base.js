// Form ajax script
$(function() {
    function ajax_send($form){
        let formURL = $form.attr("action");
        let data = new FormData();
        let form_array = $form.serializeArray();
        for (let i = 0; i < form_array.length; i++){
            data.append(form_array[i].name, form_array[i].value);
        }
        $form.find('input[type=file]').each(function(index, elem){
            let file = elem.files[0];
            if (file){
                data.append($(elem).attr('name'), file);
            }
        });
        $.ajax({
            url: formURL,
            data:  data,
            processData: false,
            contentType: false,
            method: 'POST',
            success: function(data) {
                $form.replaceWith(data).show();
                if (data.match(/success-modal/)){
                    $('#success-modal').modal('show');
                }
            },
        });
        return false;
    }

    $( document ).on('submit', '.ajax_form', function(e){
        e.preventDefault();
        ajax_send($(this));
    });
});