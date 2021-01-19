import React, { Component } from "react";
import img from "../Images/00.png";
import axios from "axios";
import { Link } from "react-router-dom";
import Nav from "./Nav";
class Update extends Component {
  state = {
    name: "",
    email: "",
    password: "",
    confirm: "",
    role: "inspector",
    pFlag: 0,
  };

  componentDidMount() {
    const value = JSON.parse(sessionStorage.getItem("toUpate"));
    this.setState({
      name: value.name,
      email: value.email,
      id: value.id,
    });
  }

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

  handleSubmit = (e) => {
    e.preventDefault();
    if (this.state.name == " " || this.state.email == " ") {
      alert("Please fill out the complete form");
    } else if (this.state.password != this.state.confirm) {
      alert("Password and Confirm Password fields are not matching");
    } else if (this.state.pFlag == 0) {
      const fe = {
        name: this.state.name,
        email: this.state.email,
      };
      axios
        .patch("http://127.0.0.1:8000/logs/profile/" + this.state.id + "/", fe)
        .then((res) => {
          alert("Updated Successfully");
          window.location.href = "/all";
        });
    } else if (this.state.pFlag == 1) {
      const fe = {
        name: this.state.name,
        email: this.state.email,
        password: this.state.password,
      };
      console.log(fe);
      axios
        .patch("http://127.0.0.1:8000/logs/profile/" + this.state.id + "/", fe)
        .then((res) => {
          alert("Updated Successfully");
          window.location.href = "/all";
        });
    }
  };

  handlePassword = (e) => {
    this.state.pFlag = 1;
    document.getElementById("pwd").style.display = "inline";
    document.getElementById(e.target.id).style.display = "none";
  };

  render() {
    return (
      <div className="c1">
        <Nav />

        <div className="simpleDiv">
          <div className="col-md-4 col-sm-4 col-lg-4">
            <h2>Update Info</h2>
            <br />{" "}
            <button
              id="ppp"
              className="btn btn-danger"
              onClick={this.handlePassword}
            >
              Change Password
            </button>
            <form className="form-container" onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label>Name </label>
                <input
                  type="text"
                  name="name"
                  onChange={this.onName}
                  className="form-control"
                  placeholder={this.state.name}
                  aria-describedby="helpId"
                />
                <br />
                <label>Email :</label>
                <input
                  onChange={this.onEmail}
                  type="text"
                  name="Password"
                  className="form-control"
                  placeholder={this.state.email}
                  aria-describedby="helpId"
                />
                <br />
                <div id="pwd" style={{ display: "none" }}>
                  <label>New Password :</label>
                  <input
                    onChange={this.onPassword}
                    type="password"
                    name="Password"
                    className="form-control"
                    placeholder="Enter new Password"
                    aria-describedby="helpId"
                  />
                  <br />
                  <label>Confirm Password :</label>
                  <input
                    onChange={this.onConfirm}
                    type="text"
                    name="Password"
                    className="form-control"
                    placeholder="Re-Enter Password"
                    aria-describedby="helpId"
                  />
                  <br />
                </div>
                <br />
                <input
                  type="submit"
                  value="Update"
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

export default Update;
