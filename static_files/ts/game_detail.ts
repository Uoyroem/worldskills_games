import $ from 'jquery';
import './game_detail.d.ts';


$(function() {
    const game: JQuery<HTMLIFrameElement> = $('#game');
    game.height(function() {
        return $(this).width()! * 9 / 16;
    });

    if (typeof getGamePoints !== 'undefined') {
        const iframeWindow = game[0].contentWindow;
        setInterval(() => {
            const points = getGamePoints(iframeWindow);
            $('#game-result').text(points);
            $('#id_points').val(points)
        }, 50);
    } else {
        console.error('The function for extracting the result of the game has not been announced.');
    }
});