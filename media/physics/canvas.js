$(document).ready(function() {
    function drawPoly(ctx, parray, color){
        ctx.fillStyle = 'rgba(' + color[0] + ', ' + color[1] + ', ' + color[2] + ', 0.5)';
        ctx.beginPath();
        for (var i=0;i<parray.length;i++) {
            var p = parray[i];
            if (i == 0) {
                ctx.moveTo(p[0], p[1]);
            }
            else {
                ctx.lineTo(p[0], p[1]);
            }
        }
        ctx.fill();
    }
    function draw(ctx) {
        $.getJSON('/canvas/physics/scene_data', function(data) {
            ctx.clearRect(0, 0, 640, 480);
            for (var i=0;i<data["poly"].length;i++) {
                var parray = data["poly"][i].slice(0,4);
                var color = data["poly"][i].slice(4)[0];
                drawPoly(ctx, parray, color);
            }
        });
    }

    function randRange(lowVal,highVal) {
         return Math.floor(Math.random()*(highVal-lowVal+1))+lowVal;
    }

    function init() {
        var ctx = $("#surface").get(0).getContext('2d');
        if (ctx) {
            setInterval(function() {draw(ctx)}, 100);
        }
        else {
            alert('Canvas not supported!');
        }
    }
    init();


    $('#add_block').click(function() {
        var block = [300, 250, 50, 50];
        $.post('/canvas/physics/add_block', {poly: JSON.stringify(block)})
    })
    $('#reset').click(function() {
        $.post('/canvas/physics/reset');
    })



});
