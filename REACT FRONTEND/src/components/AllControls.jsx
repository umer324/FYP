import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import UserNav from "./UserNav";
class AllControls extends Component {
  state = {
    controls: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/logs/batch/").then((res) => {
      var id = JSON.parse(localStorage.getItem("userT")).user.id;
      var pro = res.data;
      //pro = pro.filter((m) => m.user_id == id);
      console.log(pro);
      this.setState({ controls: pro });
    });
  }
  handleDel = (stu) => {
    const ne = this.state.controls.filter((m) => m.id != stu.id);
    const me = this.state.controls.filter((m) => m.id === stu.id);
    this.setState({ controls: ne });
    axios
      .delete("http://127.0.0.1:8000/logs/batch/" + me[0].test_id + "/")
      .then((res) => alert("line deleted successfully"));
  };

  render() {
    return (
      <div>
        <UserNav />
        <br />
        <br />

        <p>There are {this.state.controls.length} batch available</p>

        <table className="table table-dark">
          <thead>
            <tr>
              <th> Test no</th>
              <th>line id</th>
              <th>user id</th>
              <th>Start date</th>

              <th>delete</th>
            </tr>
          </thead>
          <tbody>
            {this.state.controls.map((stu) => (
              <tr key={stu.test_id}>
                <td>{stu.test_id}</td>
                <td>{stu.line_id}</td>
                <td>{stu.user_id}</td>
                <td>{stu.start_dateTime}</td>

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

export default AllControls;
