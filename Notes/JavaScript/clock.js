// DIGITAL CLOCK
function digital() {
  const time = new Date();
  const canvas = document.getElementById("digital");
  const ctx = canvas.getContext("2d");
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.font = "40px serif";
  ctx.fillText(time.toLocaleTimeString(), 25, 35);
  window.requestAnimationFrame(digital);
}
window.requestAnimationFrame(digital);

// ANALOG CLOCK
function analog() {
  const time = new Date();
  const canvas = document.getElementById("analog");
  const ctx = canvas.getContext("2d");
  const w = canvas.width;
  const wHalf = Math.floor(w / 2);
  const h = canvas.height;
  const hHalf = Math.floor(h / 2);
  ctx.clearRect(0, 0, w, h);

  //   OUTER CIRCLE
  ctx.save();
  ctx.lineWidth = 5;
  const margin = Math.min(Math.floor(w / 20), 15);
  const radius = Math.min(wHalf, hHalf) - margin;
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  ctx.fillStyle = "#f2c7ba";
  ctx.arc(0, 0, radius, 0, 2 * Math.PI);
  ctx.stroke();
  ctx.fill();
  ctx.restore();

  //   HOURS MARKS
  ctx.save();
  ctx.lineWidth = w > 200 ? 3 : 2;
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  var l = Math.min(Math.floor(w / 10), 15);
  // var l = 15;
  for (let i = 0; i < 12; i++) {
    ctx.beginPath();
    ctx.rotate(Math.PI / 6);
    ctx.moveTo(radius, 0);
    ctx.lineTo(radius - l, 0);

    if ((i + 4) % 12) {
      text = (i + 4) % 12;
    } else {
      text = 12;
    }
    ctx.stroke();
    ctx.save();
    ctx.textBaseline = "middle";
    ctx.fillStyle = "#2a13a0";
    ctx.font = "16px serif";
    ctx.textAlign = "end";
    ctx.fillText(text, radius - 1.4 * l, 0);
    ctx.restore();
  }
  ctx.restore();

  //   MINUTES MARKS
  ctx.save();
  ctx.lineWidth = w > 200 ? 2 : 1;
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  var l = Math.min(Math.floor(w / 6.6), 10);
  for (let i = 0; i < 60; i++) {
    ctx.beginPath();
    ctx.rotate(Math.PI / 30);
    ctx.moveTo(radius, 0);
    ctx.lineTo(radius - l, 0);
    ctx.stroke();
  }
  ctx.restore();

  //   CENTRAL CIRCLE
  ctx.save();
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  const cCircle = Math.min(Math.floor(w / 50), 7);
  ctx.arc(0, 0, cCircle, 0, 2 * Math.PI);
  ctx.fillStyle = "red";
  ctx.fill();
  ctx.restore();

  const lengthTriangle = Math.min(Math.floor(w / 50), 5);

  function drawHands(n) {
    ctx.lineWidth = w > 200 ? 4 : 3;
    ctx.beginPath();
    var maxLen = radius - n * lengthTriangle;
    ctx.moveTo(0, 0);
    ctx.lineTo(0, -maxLen);
    ctx.lineTo(lengthTriangle, -maxLen);
    ctx.lineTo(0, -maxLen - 2 * lengthTriangle);
    ctx.lineTo(-lengthTriangle, -maxLen);
    ctx.lineTo(0, -maxLen);
    ctx.lineTo(0, 0);
  }

  //   HOUR HAND
  ctx.save();
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  ctx.rotate(
    (Math.PI / 30) * (time.getHours() % 12) * 5 +
      (Math.PI / 30) * (time.getMinutes() / 60) * 5
  );
  drawHands(15);
  ctx.stroke();
  ctx.restore();

  //   MINUTE HAND
  ctx.save();
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  ctx.rotate(
    (Math.PI / 30) * time.getMinutes() +
      (Math.PI / 30) * (time.getSeconds() / 60)
  );
  drawHands(10);
  ctx.stroke();
  ctx.restore();

  //   SECOND HAND
  ctx.save();
  ctx.translate(Math.floor(w / 2), Math.floor(h / 2));
  ctx.rotate(
    (Math.PI / 30) * time.getSeconds() +
      (Math.PI / 30) * (time.getMilliseconds() / 1000)
  );
  drawHands(11);
  ctx.fill();
  ctx.stroke();
  ctx.restore();
  window.requestAnimationFrame(analog);
}
window.requestAnimationFrame(analog);
