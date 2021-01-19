import React, { Component } from "react";
import img from "../Images/00.png";
import axios from "axios";
import { Link } from "react-router-dom";
import UserNav from "./UserNav";
class AddLine extends Component {
  state = {
    lineId: "",
    description: "",
  };

  onDesc = (e) => {
    this.setState({ description: e.target.value });
  };
  handleSubmit = (e) => {
    e.preventDefault();
    if (this.state.description == "") {
      alert("Please fill out the description");
    } else {
      const fe = {
        description: this.state.description,
      };
      axios
        .post("http://127.0.0.1:8000/logs/packaging_line/", fe)
        .then((res) => {
          alert("NEW Line ADDED");
          window.location.href = "/allLine";
        });
    }
  };

  render() {
    return (
      <div className="c1">
        <UserNav />
        <div className="simpleDiv">
          <br />
          <br />
          <br /> <h2>Add Packaging line:</h2>
          <div className="col-md-4 col-sm-4 col-lg-4">
            <form className="form-container" onSubmit={this.handleSubmit}>
              <div className="form-group">
                <label>Description : </label>
                <input
                  type="textArea"
                  name="name"
                  onChange={this.onDesc}
                  className="form-control"
                  placeholder="Enter Name"
                  aria-describedby="helpId"
                />
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

export default AddLine;
