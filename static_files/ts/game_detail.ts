import $ from 'jquery';



$(function() {
    $('#game').height(function() {
        return $(this).width()! * 9 / 16;
    });

    if (typeof getGamePoints !== 'undefined') {
        setInterval(() => {
            $('#game-result').text(getGamePoints());
        }, 50);

    } else {
        console.error('The function for extracting the result of the game has not been announced.');
    }
});