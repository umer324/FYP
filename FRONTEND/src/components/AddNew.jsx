import React, { Component } from "react";
import img from "../Images/00.png";
import axios from "axios";
import { Link } from "react-router-dom";
import Nav from "./Nav";
class AddNew extends Component {
  state = {
    name: "",
    email: "",
    password: "",
    confirm: "",
    role: "inspector",
  };

  onName = (e) => {
    this.setState({ name: e.target.value });
  };
  onEmail = (e) => {
    this.setState({ email: e.target.value });
  };

  onPassword = (e) => {
    this.setState({ password: e.target.value });
  };
  onConfirm = (e) => {
    this.setState({ confirm: e.target.value });
  };

  onC1 = (e) => {
    this.setState({ role: "admin" });
  };
  onC2 = (e) => {
    this.setState({ role: "supervisor" });
  };
  onC3 = (e) => {
    this.setState({ role: "inspector" });
  };

  handleSubmit = (e) => {
    e.preventDefault();
    if (
      this.state.name == "" ||
      this.state.email == "" ||
      this.state.password == "" ||
      this.state.confirm == ""
    ) {
      alert("Please fill out the complete form");
    } else if (this.state.password != this.state.confirm) {
      alert("Password and Confirm Password fields are not matching");
    } else {
      const fe = {
        name: this.state.name,
        email: this.state.email,
        password: this.state.password,
        role: this.state.role,
      };
      axios.post("http://127.0.0.1:8000/logs/profile/", fe).then((res) => {
        alert("NEW USER ADDED");
        window.location.href = "/all";
      });
    }
  };

  render() {
    return (
      <div className="c1">
        <Nav />
        <div className="bts">
          <button
            type="button"
            class="btn btn-danger btn-lg"
            onClick={this.onC1}
          >
            ADD ADMIN
          </button>
          <br />
          <button
            type="button"
            class="btn btn-danger btn-lg"
            onClick={this.onC2}
          >
            ADD SUPERVISOR
          </button>
          <br />
          <button
            type="button"
            class="btn btn-danger btn-lg"
            onClick={this.onC3}
          >
            ADD INSPECTOR
          </button>
          <br />
        </div>

        <div className="simpleDiv">
          <div className="col-md-4 col-sm-4 col-lg-4">
            <h2>Add New {this.state.role}</h2>
            <form className="form-container" onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label>Name </label>
                <input
                  type="text"
                  name="name"
                  onChange={this.onName}
                  className="form-control"
                  placeholder="Enter Name"
                  aria-describedby="helpId"
                />
                <br />
                <label>Email :</label>
                <input
                  onChange={this.onEmail}
                  type="text"
                  name="Password"
                  className="form-control"
                  placeholder="Enter Email"
                  aria-describedby="helpId"
                />
                <br />
                <label>Password :</label>
                <input
                  onChange={this.onPassword}
                  type="text"
                  name="Password"
                  className="form-control"
                  placeholder="Password"
                  aria-describedby="helpId"
                />
                <br />
                <label>Confirm password :</label>
                <input
                  onChange={this.onConfirm}
                  type="text"
                  name="Password"
                  className="form-control"
                  placeholder="Confirm Oassword"
                  aria-describedby="helpId"
                />
                <br />

                <br />
                <input
                  type="submit"
                  value="submit"
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

export default AddNew;
