import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import UserNav from "./UserNav";
class AllLines extends Component {
  state = {
    lines: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/logs/packaging_line/").then((res) => {
      const pro = res.data;
      this.setState({ lines: pro });
      console.log(this.state.lines);
    });
  }
  handleDel = (stu) => {
    const ne = this.state.lines.filter((m) => m.line_id != stu.line_id);
    const me = this.state.lines.filter((m) => m.line_id === stu.line_id);
    this.setState({ lines: ne });
    axios
      .delete(
        "http://127.0.0.1:8000/logs/packaging_line/" + me[0].line_id + "/"
      )
      .then((res) => alert("line deleted successfully"));
  };

  render() {
    return (
      <div>
        <UserNav />
        <br />
        <br />

        <p>there are {this.state.lines.length} lines</p>
        <table className="table table-dark">
          <thead>
            <tr>
              <th>Id</th>
              <th>Description</th>
              <th>delete</th>
            </tr>
          </thead>
          <tbody>
            {this.state.lines.map((stu) => (
              <tr key={stu.line_id}>
                <td>{stu.line_id}</td>
                <td>{stu.description}</td>

                <td>
                  <button
                    onClick={() => this.handleDel(stu)}
                    className="btn btn-danger btn-sm"
                  >
                    DELETE
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default AllLines;
