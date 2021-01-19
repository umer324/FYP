import React, { Component } from "react";
import img from "../Images/00.png";
import axios from "axios";
import { Link } from "react-router-dom";
import UserNav from "./UserNav";

class AddControls extends Component {
  state = {
    users: [],
    lines: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/logs/packaging_line/").then((res) => {
      const pro = res.data;
      this.setState({ lines: pro });
      console.log(this.state.lines);
    });

    axios.get("http://127.0.0.1:8000/logs/profile").then((res) => {
      const pro = res.data;
      this.setState({ users: pro });
      console.log(this.state.users);
    });
  }
  handleSubmit = (e) => {
    e.preventDefault();
    var u_id = document.getElementById("users").value;
    var l_id = document.getElementById("lines").value;
    var fe = {
      user_id: u_id,
      line_id: l_id,
    };
    axios.post("http://127.0.0.1:8000/logs/batch/", fe).then((res) => {
      alert("batch added");
    });
  };

  render() {
    return (
      <div className="c1">
        <UserNav />
        <div className="simpleDiv">
          <div className="col-md-4 col-sm-4 col-lg-4">
            <h2>Add New inspector Controls</h2>
            <form className="form-container" onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label for="sel1">Select User:</label>
                <select className="form-control" id="users">
                  {this.state.users.map((stu) => (
                    <option value={stu.id}>
                      id: {stu.id} name:{stu.name}
                    </option>
                  ))}
                </select>
                <br />

                <label for="sel1">Select Packaging line:</label>
                <select className="form-control" id="lines">
                  {this.state.lines.map((stu) => (
                    <option value={stu.line_id}>
                      id: {stu.line_id} desc:{stu.description}
                    </option>
                  ))}
                </select>

                <br />
                <input
                  type="submit"
                  value="Add Control"
                  className="btn btn-success"
                ></input>
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default AddControls;
