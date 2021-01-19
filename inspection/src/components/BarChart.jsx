import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import CanvasJSReact from "../assets/canvasjs.react";
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
class BarChart extends Component {
  render() {
    const options = {
      title: {
        text: "Valid and Invalid packaging In All Batches ",
      },
      toolTip: {
        shared: true,
      },
      legend: {
        verticalAlign: "top",
      },
      axisY: {
        suffix: "%",
      },
      data: [
        {
          type: "stackedBar100",
          color: "#9bbb59",
          name: "valid",
          showInLegend: true,
          indexLabel: "{y}",
          indexLabelFontColor: "white",
          yValueFormatString: "#,###'%'",
          dataPoints: [
            { label: "12/10/2020", y: 85 },
            { label: "13/10/2020", y: 79 },
            { label: "14/10/2020", y: 77 },
            { label: "15/10/2020", y: 68 },
            { label: "16/10/2020", y: 85 },
            { label: "17/10/2020", y: 79 },
            { label: "18/10/2020", y: 77 },
          ],
        },
        {
          type: "stackedBar100",
          color: "#7f7f7f",
          name: "InValid",
          showInLegend: true,
          indexLabel: "{y}%",
          indexLabelFontColor: "white",
          yValueFormatString: "#,###'%'",
          dataPoints: [
            { label: "12/10/2020", y: 15 },
            { label: "13/10/2020", y: 21 },
            { label: "14/10/2020", y: 23 },
            { label: "15/10/2020", y: 32 },
            { label: "16/10/2020", y: 15 },
            { label: "17/10/2020", y: 21 },
            { label: "18/10/2020", y: 23 },
          ],
        },
      ],
    };
    return (
      <div>
        <CanvasJSChart
          options={options}
          /* onRef={ref => this.chart = ref} */
        />
        {/*You can get reference to the chart instance as shown above using onRef. This allows you to access all chart properties and methods*/}
      </div>
    );
  }
}

export default BarChart;
