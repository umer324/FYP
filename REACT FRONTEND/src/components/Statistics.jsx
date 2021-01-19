import React, { Component } from "react";
import InspectorNav from "./InspectorNav";
import Graphs from "./Graphs";
import BatchStates from "./BatchStates";
class Statistics extends Component {
  state = {};
  render() {
    return (
      <div>
        <InspectorNav />
        <hr />
        <div className="container">
          <Graphs />
          <hr />
        </div>

        <h1>All Batches details :</h1>
        <BatchStates />
      </div>
    );
  }
}

export default Statistics;
