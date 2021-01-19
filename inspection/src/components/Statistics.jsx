import React, { Component } from "react";
import Nav from "./Nav";
import Graphs from "./Graphs";
import BarChart from "./BarChart";
class Statistics extends Component {
  state = {};
  render() {
    return (
      <div>
        <Nav />
        <hr />
        <div className="container">
          
          <Graphs />
          <hr />
          <BarChart />
        </div>
      </div>
    );
  }
}

export default Statistics;
