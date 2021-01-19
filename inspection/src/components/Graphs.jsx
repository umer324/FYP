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
    axios.get("http://127.0.0.1:8000/logs/states").then((res) => {
      this.setState({ valid_packets: (res.data.valid / res.data.total) * 100 });
      this.setState({
        Invalid_packets: (res.data.invalid / res.data.total) * 100,
      });
    });
  }
  render() {
    const options = {
      animationEnabled: true,
      exportEnabled: true,
      theme: "dark2", // "light1", "dark1", "dark2"
      title: {
        text: "valid/invlid packets",
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
