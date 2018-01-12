$(function () {
    var $from = $('.from');
    var $to = $('.to');
    var $fun = $('.fun');
    var $button = $("button");
    clear_background();
    cell();
    $button.click(function(e) {
        e.preventDefault();
        var from = parseFloat($from.val());
        var to = parseFloat($to.val());
        var fun = $fun.val();
        const points = [];
        var miny = 0, maxy = 0;
        for (var x = from; x <= to; x = x+0.01) {
            var y = parseFloat(eval(fun));
            if (miny > y) miny = y;
            if (maxy < y) maxy = y;
            points.push([x.toFixed(2),y.toFixed(2)]);
        }
        var max = maxy;
        if (Math.abs(maxy) < Math.abs(miny)) max = Math.abs(miny);
        axes(max, from, to);
        plot(points, max);
        legend(fun);
    })
});

function plot(points, max) {
    clear_background();
    cell();
    var context = $("#canvas")[0].getContext("2d");
    var kx = context.canvas.width/(points.length-1);
    var ky = context.canvas.height/2/max;
    context.strokeStyle="#FF0000";
    context.lineWidth = 1;
    context.beginPath();
    context.moveTo(0, (context.canvas.width/2-ky*points[0][1]));

    // var i = 0, x = 0, y = 0;
    // var interval = setInterval(function() {
    //     x = i*kx;
    //     y = points[i][1];
    //     context.lineTo(x, (canvas.width/2-ky*y));
    //     context.stroke();
    //     if(i >= points.length-1) {
    //         clearInterval(interval);
    //     }
    //     i++;
    // }, 1);

    for (var i = 0; i < points.length; i++) {
        var x = i*kx;
        var y = points[i][1];
        context.lineTo(x, (context.canvas.width/2-ky*y));
    }
    context.stroke();
}

function cell()
{
    var context1 = $("#canvas")[0].getContext("2d");
    context1.strokeStyle="#000000";
    context1.lineWidth = 0.3;
    context1.beginPath();
    for (var i = 100; i <= 400; i = i + 100)
    {
        context1.moveTo(i,0);
        context1.lineTo(i,400);
    }
    for (var j = 100; j <=400; j = j + 100)
    {
        context1.moveTo(0,j);
        context1.lineTo(400,j);
    }
    context1.stroke();
}

function clear_background() {
    var context = $("#canvas")[0].getContext("2d");
    var my_gradient = context.createLinearGradient(0,0,0,400);
    my_gradient.addColorStop(0,"gainsboro");
    my_gradient.addColorStop(1,"white");
    context.fillStyle = my_gradient;
    context.fillRect(0, 0, context.canvas.width, context.canvas.height);
    //context.clearRect(0, 0, canvas.width, canvas.height);
}

function legend(fun_name)
{
    var context = $("#canvas")[0].getContext("2d");
    context.fillStyle = "black";
    context.font = "15pt Cambria Math";
    context.textAlign = "right";
    context.fillText(fun_name.replace(/Math./gi, ''), 400, 20);
}

function axes(max, from, to) {
    $('.py1').html(parseFloat(max).toFixed(1));
    $('.py2').html(parseFloat(max/2).toFixed(1));
    $('.py3').html(0);
    $('.py4').html(parseFloat(-max/2).toFixed(1));
    $('.py5').html(parseFloat(-max).toFixed(1));

    if (Math.abs(from) == Math.abs(to))
    {
        $('.px1').html(from.toFixed(1));
        $('.px2').html((from/2).toFixed(1));
        $('.px3').html(0);
        $('.px4').html((to/2).toFixed(1));
        $('.px5').html(to.toFixed(1));
    }
    else
    {
        $('.px1').html(from.toFixed(1));
        $('.px2').html((from+Math.abs(Math.abs(to)-Math.abs(from))/4).toFixed(1));
        $('.px3').html((from+Math.abs(Math.abs(to)-Math.abs(from))/2).toFixed(1));
        $('.px4').html((from+Math.abs(Math.abs(to)-Math.abs(from))/4*3).toFixed(1));
        $('.px5').html(to.toFixed(1));
    }
}