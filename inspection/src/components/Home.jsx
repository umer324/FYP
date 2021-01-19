import React, { Component } from "react";

import { Link } from "react-router-dom";
import Nav from "./Nav";
import Others from "./Others";
import Admin from "./Admin";
import Inspector from './Inspector'
import Axios from "axios";
class Home extends Component {
  state = {
    userCount: {},
    errorDetails: {},
    userT: {},
    token: "",
    role: "",
  };
  componentDidMount() {
    this.setState({
      role: JSON.parse(localStorage.getItem("userT")).user.role,
    });
    this.setState({ userT: JSON.parse(localStorage.getItem("userT")).user });

    Axios.get("http://127.0.0.1:8000/logs/states").then((res) => {
      this.setState({ errorDetails: res.data });
      console.log(res.data);
    });
    Axios.get("http://127.0.0.1:8000/logs/userLength").then((res) => {
      this.setState({ userCount: res.data });
      console.log(res.data);
    });
  }
  render() {
    if (this.state.role == "admin") {
      return <Admin />;
    } else if (this.state.role == "supervisor") {
      return <Others />;
    } else if (this.state.role == "inspector") {
      return <Inspector />;
    } else {
      return <h4>sorry</h4>;
    }
  }
}

export default Home;
