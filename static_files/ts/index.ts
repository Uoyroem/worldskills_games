import '../scss/main.scss';
import $ from 'jquery';


$(function() {
    $('button[data-check]').on('click', function() {
        $('#' + $(this).data('check')).prop('checked', true);
    });
    $('form[data-override-method]').on('submit', function(event) {
        event.preventDefault();
        const data = $(this).serialize();
        const method = $(this).data('overrideMethod');
        const url = $(this).attr('action');
        if (url != null) {
            $.ajax(url, {
               method, data
            }).done(function() {
                location.reload();
            });
        }
    });
});

