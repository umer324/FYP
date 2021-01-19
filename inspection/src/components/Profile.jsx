import React, { Component } from "react";
import Nav from "./Nav";
import UserNav from "./UserNav";
class Profile extends Component {
  state = {
    User: {},
  };
  componentDidMount() {
    this.setState({ User: JSON.parse(localStorage.getItem("userT")).user });
  }

  handleEdit = () => {
    sessionStorage.setItem("toUpate", JSON.stringify(this.state.User));
    window.location.href = "/update";
  };

  handleNav = () => {
    if (this.state.User.role == "admin") {
      return <Nav />;
    } else return <UserNav />;
  };

  render() {
    return (
      <div>
        {this.handleNav}
        <div className="bbb">
          <div className="prof">
            <div className="cec">
              <img
                src="data:image/jpeg;base64,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"
                alt=""
              />
            </div>
            <div className="rt">
              <h2>NAME : {this.state.User.name}</h2>
              <h2>EMAIL : {this.state.User.email}</h2>
              <h2>ROLE : {this.state.User.role}</h2>
              <button
                className="btn btn-success btn-sm"
                onClick={this.handleEdit}
              >
                Edit
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Profile;
