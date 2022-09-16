draw = function () {
  var ctx = document.getElementById("canvas").getContext("2d");
  const ball = {
    x: 100,
    y: 100,
    vx: 5,
    vy: 2,
    radius: 25,
    color: "blue",
    fill() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
      ctx.closePath();
      ctx.fillStyle = this.color;
      ctx.fill();
    },
  };
  for (var i = 0; i < 200; i++) {
    ball.x = Math.floor(Math.random() * 500);
    ball.y = Math.floor(Math.random() * 500);
    ball.radius = Math.floor(Math.random() * 15);
    ball.color = `rgb(${Math.floor(Math.random() * 255)},${Math.floor(
      Math.random() * 255
    )},${Math.floor(Math.random() * 255)})`;
    ball.fill();
  }
};
