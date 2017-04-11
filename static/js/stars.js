/*
	Random Stars
	Author: Alexandre Dees
	https://codepen.io/alexandredees/pen/wseEi
*/
(function($){
  
  function generateStar(canvas, ctx, starRadius){
			ctx.beginPath();
			ctx.arc(starRadius + (Math.random() * canvas.width), starRadius + (Math.random() * canvas.height), starRadius*Math.random(), 0, Math.PI*2, false);
      //ctx.arc(100, 30, starRadius, 0, Math.PI*2, false);
    
      var rand = Math.random();
      if(rand <= 0.5){
				  ctx.fillStyle = "rgba(255, 255, 255, 1)";
				  ctx.shadowColor = "rgba(255, 255, 255, 0.5)";
				  ctx.shadowBlur = 3;
			}
			else if(rand > 0.75){
				  ctx.fillStyle = "rgba(255, 254, 196, 1)";
				  ctx.shadowColor = "rgba(255, 254, 196, 0.5)";
				  ctx.shadowBlur = 4; 
			}
			else{
				  ctx.fillStyle = "rgba(192, 247, 255, 1)";
				  ctx.shadowColor = "rgba(192, 247, 255, 0.5)";
				  ctx.shadowBlur = 7;
			}
			ctx.fill();
	}

	function drawButton(canvas, ctx, x, y) {
		// Draw circle
		ctx.beginPath();
		ctx.arc(x, y,50,0,2*Math.PI);
		ctx.stroke();
		ctx.fillStyle = "rgba(255, 254, 196, 1)";
		ctx.shadowColor = "rgba(255, 254, 196, 0.5)";
		ctx.shadowBlur = 7;
		ctx.fill();

		// Draw text
		ctx.font = '32pt Just Another Hand';
        ctx.fillStyle = 'black';
        ctx.textAlign = 'center';
        ctx.fillText('Enter', x, y+3);
        
        
        
	}
  
  $(function(){
    
	var canvas = document.getElementById("space");
	var context = canvas.getContext("2d");
    
    onresize = function(){
      canvas.width = canvas.clientWidth;
      canvas.height = canvas.clientHeight;
    }
    onresize();
		
    interval = setInterval(
      function(interval){
        generateStar(canvas, context, 3);
      }
      , 24);

    drawButton(canvas, context, canvas.width/2 - 30, canvas.height - 100);

    setTimeout( // Stop sreating stars after 10s
      function(){ clearInterval(interval); }
      ,10000
    );
    
	});
})(jQuery);