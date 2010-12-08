$(document).ready(function() {
    function drawPoly(ctx, parray, color){
        ctx.fillStyle = getColor(color);
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
    function drawCircle(ctx, posx, posy, radius, color) {
        //ctx.fillStyle = getColor(color);
        ctx.beginPath();
        ctx.arc(posx, posy, radius, degToRad(0), degToRad(360));
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
            for (var i=0;i<data["circle"].length;i++) {
                var posx = data["circle"][i][0];
                var posy = data["circle"][i][1];
                var radius = data["circle"][i][2];
                var color = data["circle"][i][3];
                drawCircle(ctx, posx, posy, radius, color);
            }
        });
    }

    function getColor(color){
        return 'rgba(' + color[0] + ', ' + color[1] + ', ' + color[2] + ', 0.5)';
    }

    function degToRad(deg) {
        return (Math.PI/180)*deg;
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
    $('#add_block').click(function() {
        var block = [300, 250, 50, 50];
        $.post('/canvas/physics/add_block', {poly: JSON.stringify(block)})
    })
    $('#add_circle').click(function() {
        var circle = [300, 250, 25];
        $.post('/canvas/physics/add_circle', {circle: JSON.stringify(circle)})
    })
    $('#reset').click(function() {
        $.post('/canvas/physics/reset');
    })

    init();
});
