import React, { Component } from "react";
import img from "../Images/00.png";
import { Link } from "react-router-dom";
import axios from "axios";
import { useHistory } from "react-router-dom";
class UserLogin extends Component {
  state = {
    login: "",
    password: "",
    User: "",
  };

  onlogin = (e) => {
    this.setState({ login: e.target.value });
  };
  onpass = (e) => {
    this.setState({ password: e.target.value });
  };
  handleSubmit = (e) => {
    //  this.props.history.push("/Home");

    e.preventDefault();
    if (this.state.login == "") {
      alert("email field is empty");
    } else if (this.state.password == "") {
      alert("Password Field is empty");
    } else {
      const fe = {
        username: this.state.login,
        password: this.state.password,
      };
      const d = JSON.stringify(fe);

      axios
        .post("http://127.0.0.1:8000/logs/login/", fe)
        .then((res) => {
          localStorage.setItem("userT", JSON.stringify(res.data));

          console.log("fdfr");
          this.props.history.push("/Home");
        })
        .catch((error) =>
          alert("Error in connecting to server...................")
        );
    }
  };

  render() {
    return (
      <div className="c1">
        <h1 id="hh1">Real Time Inspection</h1>
        <div className="container">
          <div
            id="login-row"
            className="row justify-content-center align-items-center"
          >
            <div id="login-column" className="col-md-6">
              <div className="box">
                <div className="shape1"></div>
                <div className="shape2"></div>
                <div className="shape3"></div>
                <div className="shape4"></div>
                <div className="shape5"></div>
                <div className="shape6"></div>
                <div className="shape7"></div>
                <div className="float">
                  <form className="form" onSubmit={this.handleSubmit}>
                    <div className="form-group">
                      <label htmlFor="username" className="text-white">
                        Email:
                      </label>
                      <br></br>
                      <input
                        type="text"
                        name="username"
                        onChange={this.onlogin}
                        id="username"
                        className="form-control"
                      ></input>{" "}
                    </div>
                    <div className="form-group">
                      <label htmlFor="password" className="text-white">
                        Password:
                      </label>
                      <br></br>
                      <input
                        type="password"
                        name="password"
                        id="password"
                        onChange={this.onpass}
                        className="form-control"
                      ></input>
                    </div>
                    <Link to="#" className="forf">
                      forgot password
                    </Link>
                    <br />
                    <br />
                    <div className="form-group">
                      <input
                        type="submit"
                        name="submit"
                        className="btn btn-info btn-md"
                        value="submit"
                      ></input>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
          <script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
        </div>
      </div>
    );
  }
}

export default UserLogin;
