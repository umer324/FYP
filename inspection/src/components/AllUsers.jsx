import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import Nav from "./Nav";
class AllUsers extends Component {
  state = {
    users: [],
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/logs/profile").then((res) => {
      const pro = res.data;
      this.setState({ users: pro });
      console.log(this.state.users);
    });
  }
  handleDel = (stu) => {
    const ne = this.state.users.filter((m) => m.id != stu.id);
    const me = this.state.users.filter((m) => m.id === stu.id);
    this.setState({ users: ne });
    axios
      .delete("http://127.0.0.1:8000/logs/profile/" + me[0].id + "/")
      .then((res) => alert("customer deleted successfully"));
  };

  handleUpdate = (stu) => {
    const me = this.state.users.filter((m) => m.id === stu.id);
    sessionStorage.setItem("toUpate", JSON.stringify(me[0]));
    window.location.href = "/update";
  };

  render() {
    return (
      <div>
        <Nav />
        <br />
        <br />

        <p>there are {this.state.users.length} users</p>
        <table className="table table-dark">
          <thead>
            <tr>
              <th>NAME</th>
              <th>EMAIL</th>
              <th>Role</th>
              <th>delete</th>
              <th>update</th>
            </tr>
          </thead>
          <tbody>
            {this.state.users.map((stu) => (
              <tr key={stu.id}>
                <td>{stu.name}</td>
                <td>{stu.email}</td>

                <td>{stu.role}</td>

                <td>
                  <button
                    onClick={() => this.handleDel(stu)}
                    className="btn btn-danger btn-sm"
                  >
                    DELETE
                  </button>
                </td>
                <td>
                  <button
                    className="btn btn-info btn-sm"
                    onClick={() => this.handleUpdate(stu)}
                  >
                    Update
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

export default AllUsers;
