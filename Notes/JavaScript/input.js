"use strict";
const missingNumber = (array, n) => {
  var arrSet = new Set();
  array.forEach((a) => {
    arrSet.add(a);
  });
  for (let i = 1; i < n + 2; i++) {
    if (!arrSet.has(i)) {
      return i;
    }
  }
};

const isBeneficiary = (n, start, end, quant) => {
  var diffPrice = [];
  for (let i = 0; i < n; i++) {
    const diff = (end[i] - start[i]) * quant[i];
    diffPrice.push(diff);
  }
  return diffPrice.reduce((a, b) => a + b, 0);
};

function takeInput() {
  let input = document.getElementById("input").value.trim();
  const lines = input.split("\n").map((line) => line.trim());
  const n = parseInt(lines[0]);
  var array = lines[1].split(" ").map((num) => parseInt(num));
  console.log(n, array);
  var result = missingNumber(array, n);
  document.getElementById("result").innerHTML = result;
}

function takeInput() {
  let input = document.getElementById("input").value.trim();
  const lines = input.split("\n").map((line) => line.trim());
  const n = parseInt(lines[0]);
  const start = lines[1].split(" ").map((num) => parseFloat(num));
  const end = lines[2].split(" ").map((num) => parseFloat(num));
  const quant = lines[3].split(" ").map((num) => parseFloat(num));

  const output = isBeneficiary(n, start, end, quant);
  var resultText = output > 0 ? "Success" : "Failure";
  var result = `${output} So it is a ${resultText}`;
  document.getElementById("result").innerHTML = result;
}
