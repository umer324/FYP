import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import CanvasJSReact from "../assets/canvasjs.react";
import BarChart from "./BarChart";
//var CanvasJSReact = require('./canvasjs.react');
var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;
class Graphs extends Component {
  state = {
    valid_packets: 0,
    Invalid_packets: 0,
  };
  componentDidMount() {
    const stats = JSON.parse(sessionStorage.getItem("statistics"));
    this.setState({
      valid_packets: (stats.valid / stats.all) * 100,
      Invalid_packets: (stats.invalid / stats.all) * 100,
    });
  }
  render() {
    const options = {
      animationEnabled: true,
      exportEnabled: true,
      theme: "dark2", // "light1", "dark1", "dark2"
      title: {
        text: "Overall Statistics",
      },
      data: [
        {
          type: "pie",
          indexLabel: "{label}: {y}%",
          startAngle: -90,
          dataPoints: [
            { y: this.state.valid_packets, label: "Valid Sachets" },
            { y: this.state.Invalid_packets, label: "Invalid Sachets" },
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
        <br />
        <br />

        <br />
        <br />
      </div>
    );
  }
}

export default Graphs;
