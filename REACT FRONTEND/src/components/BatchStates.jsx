import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import InspectorNav from "./InspectorNav";

class BatchStates extends Component {
  state = {
    Results: [],
  };

  componentDidMount() {
    var batch = JSON.parse(sessionStorage.getItem("batches"));
    var result = JSON.parse(sessionStorage.getItem("all"));
    var final = [];
    var r2 = [];
    var ele;
    for (let index = 0; index < batch.length; index++) {
      r2 = result.filter((r) => r.test_id == batch[index].test_id);
      ele = {
        batch_id: batch[index].test_id,
        line_id: batch[index].line_id,

        total: r2.length,
        valid: r2.filter((r) => r.result_status === "valid").length,
        invalid: r2.filter((r) => r.result_status === "invalid").length,
      };
      final.push(ele);
    }
    this.setState({ Results: final });
    console.log(final);
  }

  render() {
    return (
      <div>
        <br />

        <p>There are {this.state.Results.length} batch available</p>

        <table className="table table-dark">
          <thead>
            <tr>
              <th> Test no</th>
              <th>line id</th>
              <th>Total tested</th>
              <th>Valid </th>

              <th>invalid</th>
            </tr>
          </thead>
          <tbody>
            {this.state.Results.map((stu) => (
              <tr key={stu.batch_id}>
                <td>{stu.batch_id}</td>
                <td>{stu.line_id}</td>
                <td>{stu.total}</td>
                <td>{stu.valid}</td>

                <td>{stu.invalid}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default BatchStates;
