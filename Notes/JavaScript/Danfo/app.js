"use strict";

console.log("App.js is running!");

// d3.select("#header").style("color", "red");
// var test = document.querySelector(".test");
// Plotly.newPlot(
//   test,
//   [
//     {
//       x: [1, 2, 3, 4, 5],
//       y: [1, 2, 4, 8, 16],
//     },
//   ]
//     {
//       margin: { t: 0 },
//     }
// );
// const myForm = document.getElementById("myForm");
// const csvFile = document.getElementById("csvFile");
// var data_final;

// myForm.addEventListener("submit", function (e) {
//   e.preventDefault();
//   const input = csvFile.files[0];
//   const reader = new FileReader();

//   reader.onload = function (e) {
//     const text = e.target.result;
//     const data = d3.csvParse(text);
//     // document.write(JSON.stringify(data));
//     data_final = JSON.stringify(data);
//   };

//   reader.readAsText(input);
// });
// console.log(data_final);

// const myForm = document.getElementById("myForm");
// const csvFile = document.getElementById("csvFile");
// // var text;
// // console.log();

// myForm.addEventListener("submit", function (e) {
//   e.preventDefault();
//   const input = csvFile.files[0];
//   console.log(input);
//   const reader = new FileReader();

//   reader.onload = function (e) {
//     var text = e.target.result;
//     // document.write(text);
//     const data = d3.csvParse(text);
//     console.log(data);
//   };

//   reader.readAsText(input);
// });

const url = "Data/AAPL.csv";

// d3.csv(url).then(function (data) {
//   console.log(data);
//   console.log(data.columns);
// });
const plotBTN = document.getElementById("plot_btn");
plotBTN.addEventListener("click", function (e) {
  e.preventDefault();
  dfd.readCSV(url).then((df) => {
    const layout = {
      title: {
        text: "Time series plot of AAPL Open",
        x: 0,
      },
      // legend: {
      //   bgcolor: "#fcba03",
      //   bordercolor: "#444",
      //   borderwidth: 1,
      //   font: { family: "Arial", size: 10, color: "#fff" },
      // },
      width: 1000,
      yaxis: {
        title: "Open",
      },
      xaxis: {
        title: "Date",
      },
    };

    const config = {
      columns: ["Open"], //columns to plot
      displayModeBar: true,
      displaylogo: false,
    };
    const new_df = df.setIndex({ column: "Date" });
    var trace = {
      x: new_df.index,
      y: new_df["Open"].values,
      type: "line",
    };
    // new_df.plot("plot_div").line({ layout, config });
    Plotly.newPlot("plot_div", [trace]);
  });
});
