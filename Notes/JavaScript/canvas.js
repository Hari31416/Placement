// function draw() {
// const canvas = document.getElementById("canvas");
// if (canvas.getContext) {
//   const ctx = canvas.getContext("2d");

//   ctx.fillRect(25, 25, 100, 100);
//   ctx.clearRect(45, 45, 60, 60);
//   ctx.strokeRect(50, 50, 50, 50);
// }

// const canvas = document.getElementById("canvas2");
// if (canvas.getContext) {
//   const ctx = canvas.getContext("2d");

//   ctx.beginPath();
//   ctx.moveTo(75, 50);
//   ctx.lineTo(100, 75);
//   ctx.lineTo(100, 25);
//   ctx.fill();
// }
// const canvas = document.getElementById("canvas3");
// if (canvas.getContext) {
//   const ctx = canvas.getContext("2d");

// ctx.beginPath();
// ctx.arc(75, 75, 50, 0, Math.PI * 2, true); // Outer circle
// ctx.moveTo(110, 75);
// ctx.arc(75, 75, 35, 0, Math.PI, false); // Mouth (clockwise)
// ctx.moveTo(65, 65);
// ctx.arc(60, 65, 5, 0, Math.PI * 2, true); // Left eye
// ctx.moveTo(95, 65);
// ctx.arc(90, 65, 5, 0, Math.PI * 2, true); // Right eye
// ctx.stroke();

// Filled triangle
// ctx.beginPath();
// ctx.moveTo(25, 25);
// ctx.lineTo(105, 25);
// ctx.lineTo(25, 105);
// ctx.fill();

// // Stroked triangle
// ctx.beginPath();
// ctx.moveTo(125, 125);
// ctx.lineTo(125, 45);
// ctx.lineTo(45, 125);
// ctx.closePath();
// ctx.stroke();

//     for (let i = 0; i < 4; i++) {
//       for (let j = 0; j < 3; j++) {
//         ctx.beginPath();
//         const x = 75 + j * 50; // x coordinate
//         const y = 55 + i * 50; // y coordinate
//         const radius = 20; // Arc radius
//         const startAngle = 0; // Starting point on circle
//         const endAngle = Math.PI + (Math.PI * j) / 2; // End point on circle
//         const counterclockwise = i % 2 !== 0; // clockwise or counterclockwise

//         ctx.arc(x, y, radius, startAngle, endAngle, counterclockwise);

//         if (i > 1) {
//           ctx.fill();
//         } else {
//           ctx.stroke();
//         }
//       }
//     }
//   }
// }

// function draw() {
//   const canvas = document.getElementById("canvas3");
//   if (canvas.getContext) {
//     const ctx = canvas.getContext("2d");

//     // roundedRect(ctx, 12, 12, 150, 150, 15);
//     roundedRect(ctx, 19, 19, 175, 155, 9);
//     roundedRect(ctx, 53, 53, 49, 33, 10);
//     roundedRect(ctx, 53, 119, 49, 16, 6);
//     roundedRect(ctx, 135, 53, 49, 33, 10);
//     roundedRect(ctx, 135, 119, 25, 49, 10);

//     ctx.beginPath();
//     ctx.arc(37, 37, 13, Math.PI / 7, -Math.PI / 7, false);
//     ctx.lineTo(31, 37);
//     ctx.fill();

//     for (let i = 0; i < 8; i++) {
//       ctx.fillRect(51 + i * 16, 35, 4, 4);
//     }

//     for (i = 0; i < 6; i++) {
//       ctx.fillRect(115, 51 + i * 16, 4, 4);
//     }

//     for (i = 0; i < 8; i++) {
//       ctx.fillRect(51 + i * 16, 99, 4, 4);
//     }

//     ctx.beginPath();
//     ctx.moveTo(83, 116);
//     ctx.lineTo(83, 102);
//     ctx.bezierCurveTo(83, 94, 89, 88, 97, 88);
//     ctx.bezierCurveTo(105, 88, 111, 94, 111, 102);
//     ctx.lineTo(111, 116);
//     ctx.lineTo(106.333, 111.333);
//     ctx.lineTo(101.666, 116);
//     ctx.lineTo(97, 111.333);
//     ctx.lineTo(92.333, 116);
//     ctx.lineTo(87.666, 111.333);
//     ctx.lineTo(83, 116);
//     ctx.fill();

//     ctx.fillStyle = "white";
//     ctx.beginPath();
//     ctx.moveTo(91, 96);
//     ctx.bezierCurveTo(88, 96, 87, 99, 87, 101);
//     ctx.bezierCurveTo(87, 103, 88, 106, 91, 106);
//     ctx.bezierCurveTo(94, 106, 95, 103, 95, 101);
//     ctx.bezierCurveTo(95, 99, 94, 96, 91, 96);
//     ctx.moveTo(103, 96);
//     ctx.bezierCurveTo(100, 96, 99, 99, 99, 101);
//     ctx.bezierCurveTo(99, 103, 100, 106, 103, 106);
//     ctx.bezierCurveTo(106, 106, 107, 103, 107, 101);
//     ctx.bezierCurveTo(107, 99, 106, 96, 103, 96);
//     ctx.fill();

//     ctx.fillStyle = "black";
//     ctx.beginPath();
//     ctx.arc(101, 102, 2, 0, Math.PI * 2, true);
//     ctx.fill();

//     ctx.beginPath();
//     ctx.arc(89, 102, 2, 0, Math.PI * 2, true);
//     ctx.fill();
//   }
// }

// // A utility function to draw a rectangle with rounded corners.

// function roundedRect(ctx, x, y, width, height, radius) {
//   ctx.beginPath();
//   ctx.moveTo(x, y + radius);
//   ctx.arcTo(x, y + height, x + radius, y + height, radius);
//   ctx.arcTo(x + width, y + height, x + width, y + height - radius, radius);
//   ctx.arcTo(x + width, y, x + width - radius, y, radius);
//   ctx.arcTo(x, y, x, y + radius, radius);
//   ctx.stroke();
// }

function draw() {
  var ctx = document.getElementById("canvas").getContext("2d");
  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
      ctx.fillStyle = `rgb(${Math.floor(255 - 42.5 * i)}, ${Math.floor(
        255 - 42.5 * j
      )}, 0)`;
      ctx.fillRect(j * 25, i * 25, 25, 25);
    }
  }
  for (let i = 0; i < 6; i++) {
    for (let j = 0; j < 6; j++) {
      ctx.strokeStyle = `rgb(0, ${Math.floor(255 - 42.5 * i)}, ${Math.floor(
        255 - 42.5 * j
      )})`;
      ctx.beginPath();
      ctx.arc(12.5 + j * 25, 12.5 + i * 25, 10, 0, 2 * Math.PI, true);
      ctx.stroke();
    }
  }
  var ctx = document.getElementById("canvas2").getContext("2d");
  // draw background
  ctx.fillStyle = "#FD0";
  ctx.fillRect(0, 0, 75, 75);
  ctx.fillStyle = "#6C0";
  ctx.fillRect(75, 0, 75, 75);
  ctx.fillStyle = "#09F";
  ctx.fillRect(0, 75, 75, 75);
  ctx.fillStyle = "#F30";
  ctx.fillRect(75, 75, 75, 75);
  ctx.fillStyle = "#FFF";

  // set transparency value
  ctx.globalAlpha = 0.2;

  // Draw semi transparent circles
  for (let i = 0; i < 7; i++) {
    ctx.beginPath();
    ctx.arc(75, 75, 10 + 10 * i, 0, Math.PI * 2, true);
    ctx.fill();
  }

  for (let i = 0; i < 10; i++) {
    ctx.lineWidth = 1 + i;
    ctx.beginPath();
    ctx.moveTo(5 + i * 14, 5);
    ctx.lineTo(5 + i * 14, 140);
    ctx.stroke();
  }

  // Draw guides
  var ctx = document.getElementById("canvas3").getContext("2d");
  ctx.strokeStyle = "#199f";
  ctx.beginPath();
  ctx.moveTo(10, 10);
  ctx.lineTo(140, 10);
  ctx.moveTo(10, 140);
  ctx.lineTo(140, 140);
  ctx.stroke();

  // Draw lines
  ctx.strokeStyle = "black";
  ["butt", "round", "square"].forEach((lineCap, i) => {
    ctx.lineWidth = 15;
    ctx.lineCap = lineCap;
    ctx.beginPath();
    ctx.moveTo(25 + i * 50, 10);
    ctx.lineTo(25 + i * 50, 140);
    ctx.stroke();
  });

  var ctx = document.getElementById("canvas4").getContext("2d");
  // ctx.font = "22px serif";
  // ctx.textBaseline = "alphabetic";
  // ctx.fillText("Hello World", 10, 50);
  // ctx.strokeText("Hello World", 10, 50);
  // ctx.fillRect(0, 0, 150, 150); // Draw a rectangle with default settings
  // ctx.save(); // Save the default state

  // ctx.fillStyle = "#09F"; // Make changes to the settings
  // ctx.fillRect(15, 15, 120, 120); // Draw a rectangle with new settings

  // ctx.save(); // Save the current state
  // ctx.fillStyle = "#FFF"; // Make changes to the settings
  // ctx.globalAlpha = 0.5;
  // ctx.fillRect(30, 30, 90, 90); // Draw a rectangle with new settings

  // ctx.restore(); // Restore previous state
  // ctx.fillRect(45, 45, 60, 60); // Draw a rectangle with restored settings

  // ctx.restore(); // Restore original state
  // ctx.fillRect(60, 60, 30, 30); // Draw a rectangle with restored settings

  // for (let i = 0; i < 3; i++) {
  //   for (let j = 0; j < 3; j++) {
  //     ctx.save();
  //     ctx.fillStyle = `rgb(${51 * i}, ${255 - 51 * i}, 255)`;
  //     ctx.translate(10 + j * 50, 10 + i * 50);
  //     ctx.fillRect(0, 0, 30, 30);
  //     ctx.fillStyle = "white";
  //     ctx.arc(15, 15, 10, 0, Math.PI * 2, true);
  //     ctx.fill();
  //     ctx.moveTo(0, 0);
  //     ctx.restore();
  //   }
  // }

  // // left rectangles, rotate from canvas origin
  // ctx.save();
  // // blue rect
  // ctx.fillStyle = "#0095DD";
  // ctx.fillRect(30, 30, 100, 100);
  // ctx.rotate((Math.PI / 180) * 25);
  // // grey rect
  // ctx.fillStyle = "#4D4E53";
  // ctx.fillRect(30, 30, 100, 100);
  // ctx.restore();

  // // right rectangles, rotate from rectangle center
  // // draw blue rect
  // ctx.save();
  // ctx.fillStyle = "#0095DD";
  // ctx.fillRect(150, 30, 100, 100);

  // ctx.translate(200, 80); // translate to rectangle center
  // // x = x + 0.5 * width
  // // y = y + 0.5 * height
  // ctx.rotate((Math.PI / 180) * 25); // rotate
  // ctx.translate(-200, -80); // translate back

  // // draw grey rect
  // ctx.fillStyle = "#4D4E53";
  // ctx.fillRect(150, 30, 100, 100);
  // ctx.restore();
  // // draw a simple rectangle, but scale it.
  // ctx.save();
  // ctx.scale(10, 3);
  // ctx.fillRect(1, 10, 10, 10);
  // ctx.restore();

  // // mirror horizontally
  // ctx.scale(-1, 1);
  // ctx.font = "48px serif";
  // ctx.fillText("MDN", -135, 120);

  const sin = Math.sin(Math.PI / 6);
  const cos = Math.cos(Math.PI / 6);
  ctx.translate(100, 100);
  let c = 0;
  for (let i = 0; i <= 12; i++) {
    c = Math.floor((255 / 12) * i);
    ctx.fillStyle = `rgb(${c}, ${c}, ${c})`;
    ctx.fillRect(0, 0, 100, 10);
    ctx.transform(cos, sin, -sin, cos, 0, 0);
  }

  ctx.setTransform(-1, 0, 0, 1, 100, 100);
  ctx.fillStyle = "rgba(255, 128, 255, 0.5)";
  ctx.fillRect(0, 50, 100, 100);

  var ctx = document.getElementById("canvas5").getContext("2d");
  ctx.fillRect(0, 0, 150, 150);
  ctx.translate(75, 75);

  // Create a circular clipping path
  ctx.beginPath();
  ctx.arc(0, 0, 60, 0, Math.PI * 2, true);
  ctx.clip();

  // draw background
  const lingrad = ctx.createLinearGradient(0, -75, 0, 75);
  lingrad.addColorStop(0, "#232256");
  lingrad.addColorStop(1, "#143778");

  ctx.fillStyle = lingrad;
  ctx.fillRect(-75, -75, 150, 150);

  // draw stars
  for (let j = 1; j < 50; j++) {
    ctx.save();
    ctx.fillStyle = "#fff";
    ctx.translate(
      75 - Math.floor(Math.random() * 150),
      75 - Math.floor(Math.random() * 150)
    );
    drawStar(ctx, Math.floor(Math.random() * 4) + 2);
    ctx.restore();
  }

  var canvas = document.getElementById("canvas6");
  var ctx = canvas.getContext("2d");
  let raf;

  const ball = {
    x: 100,
    y: 100,
    vx: 5,
    vy: 2,
    radius: 25,
    color: "blue",
    draw() {
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2, true);
      ctx.closePath();
      ctx.fillStyle = this.color;
      ctx.fill();
    },
  };

  function draw() {
    ctx.fillStyle = "rgba(255, 255, 255, 0.3)";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ball.draw();
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.vy *= 0.95;
    ball.vy += 0.25;

    if (ball.y + ball.vy > canvas.height || ball.y + ball.vy < 0) {
      ball.vy = -ball.vy;
    }
    if (ball.x + ball.vx > canvas.width || ball.x + ball.vx < 0) {
      ball.vx = -ball.vx;
    }

    raf = window.requestAnimationFrame(draw);
  }

  canvas.addEventListener("mouseover", (e) => {
    raf = window.requestAnimationFrame(draw);
  });

  canvas.addEventListener("mouseout", (e) => {
    window.cancelAnimationFrame(raf);
  });

  ball.draw();
}

function drawStar(ctx, r) {
  ctx.save();
  ctx.beginPath();
  ctx.moveTo(r, 0);
  for (let i = 0; i < 9; i++) {
    ctx.rotate(Math.PI / 5);
    if (i % 2 === 0) {
      ctx.lineTo((r / 0.525731) * 0.200811, 0);
    } else {
      ctx.lineTo(r, 0);
    }
  }
  ctx.closePath();
  ctx.fill();
  ctx.restore();
}

function clock() {
  const now = new Date();
  var ctx = document.getElementById("canvas").getContext("2d");
  ctx.save();
  ctx.clearRect(0, 0, 150, 150);
  ctx.translate(75, 75);
  ctx.scale(0.4, 0.4);
  ctx.rotate(-Math.PI / 2);
  ctx.strokeStyle = "black";
  ctx.fillStyle = "white";
  ctx.lineWidth = 8;
  ctx.lineCap = "round";

  // Hour marks
  ctx.save();
  for (let i = 0; i < 12; i++) {
    ctx.beginPath();
    ctx.rotate(Math.PI / 6);
    ctx.moveTo(100, 0);
    ctx.lineTo(120, 0);
    ctx.stroke();
  }
  // ctx.restore();

  // // Minute marks
  // ctx.save();
  ctx.lineWidth = 5;
  for (i = 0; i < 60; i++) {
    if (i % 5 !== 0) {
      ctx.beginPath();
      ctx.moveTo(117, 0);
      ctx.lineTo(120, 0);
      ctx.stroke();
    }
    ctx.rotate(Math.PI / 30);
  }
  ctx.restore();

  const sec = now.getSeconds();
  const min = now.getMinutes();
  const hr = now.getHours() % 12;

  ctx.fillStyle = "black";

  // Write Hours
  ctx.save();
  ctx.rotate(
    (Math.PI / 6) * hr + (Math.PI / 360) * min + (Math.PI / 21600) * sec
  );
  ctx.lineWidth = 14;
  ctx.beginPath();
  ctx.moveTo(-20, 0);
  ctx.lineTo(80, 0);
  ctx.stroke();
  ctx.restore();

  // Write Minutes
  ctx.save();
  ctx.rotate((Math.PI / 30) * min + (Math.PI / 1800) * sec);
  ctx.lineWidth = 10;
  ctx.beginPath();
  ctx.moveTo(-28, 0);
  ctx.lineTo(112, 0);
  ctx.stroke();
  ctx.restore();

  // Write seconds
  ctx.save();
  ctx.rotate((sec * Math.PI) / 30);
  ctx.strokeStyle = "#D40000";
  ctx.fillStyle = "#D40000";
  ctx.lineWidth = 6;
  ctx.beginPath();
  ctx.moveTo(-30, 0);
  ctx.lineTo(83, 0);
  ctx.stroke();
  ctx.beginPath();
  ctx.arc(0, 0, 10, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.beginPath();
  ctx.arc(95, 0, 10, 0, Math.PI * 2, true);
  ctx.stroke();
  ctx.fillStyle = "rgba(0, 0, 0, 0)";
  ctx.arc(0, 0, 3, 0, Math.PI * 2, true);
  ctx.fill();
  ctx.restore();

  ctx.beginPath();
  ctx.lineWidth = 14;
  ctx.strokeStyle = "#325FA2";
  ctx.arc(0, 0, 142, 0, Math.PI * 2, true);
  ctx.stroke();

  ctx.restore();

  window.requestAnimationFrame(clock);
}

window.requestAnimationFrame(clock);
