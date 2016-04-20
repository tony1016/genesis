$(function() {
    var ws = new WebSocket("ws://genesis.tonylee.name/ws/story");
    ws.onopen = function() {
        $('.tlt').on('inAnimationEnd.tlt', function() {
            $('.tlt').textillate('out');
        });
        $('.tlt').on('outAnimationEnd.tlt', function() {
            ws.send("fetchOne");
        });

        ws.send("fetchOne");
    };
    ws.onmessage = function(evt) {
        $('#story').find('.texts li:first').text(evt.data);
        $('.tlt').textillate('in');
    };



})
