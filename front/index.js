$(function() {
    $('.tlt').on('inAnimationEnd.tlt', function() {
        $('.tlt').textillate('out');
    });
    $('.tlt').textillate();

})
