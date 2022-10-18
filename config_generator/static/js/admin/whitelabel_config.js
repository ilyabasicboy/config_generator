$(function(){
    // Disable keys of unselected languages
    let translations = $('.field-language select');
    translations.each(function() {
        if(!$(this).val()) {
            $(this).parents('.form-row').find('.field-key select').prop('disabled', true);
        }
    });

    // Dynamic key choices ajax
    $('.field-language select').on('change', function(){
        let key_field = $(this).parents('.form-row').find('.field-key select')
        let value = $(this).val();
        if (value) {
            let data = {
                'language': $(this).val(),
            };
            $.get('/keys_list/', data, function(data){
                key_field.html(data);
                key_field.prop('disabled', false);
            });
        }
        else {
            key_field.val('');
            key_field.prop('disabled', true);
        }
    });

});

