import React, { Component } from "react";
import { Link } from "react-router-dom";

class Nav extends Component {
  state = {};
  onLogout = (e) => {
    localStorage.removeItem("user");
    console.log(this.props);
    window.location.href = "/";
    // this.props.history.push('/')
  };
  render() {
    return (
      <nav className=" navbar-expand-lg navbar navbar-dark bg-dark">
        <Link className="navbar-brand" to="/">
          Inspection
        </Link>
        <button
          className="navbar-toggler"
          type="button"
          data-toggle="collapse"
          data-target="#navbarNavDropdown"
          aria-controls="navbarNavDropdown"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span className="navbar-toggler-icon"></span>
        </button>
        <div className="collapse navbar-collapse" id="navbarNavDropdown">
          <ul className="navbar-nav">
            <li className="nav-item active">
              <Link className="nav-link" to="/Home">
                Home <span className="sr-only">(current)</span>
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/profile">
                Profile
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/all">
                VIEW ALL USERS
              </Link>
            </li>
            <li className="nav-item">
              <Link className="nav-link" to="/add">
                Add New User
              </Link>
            </li>
          </ul>
        </div>
        <button
          className="btn btn-outline-danger my-2 my-sm-0"
          onClick={this.onLogout}
        >
          Logout
        </button>
      </nav>
    );
  }
}

export default Nav;
