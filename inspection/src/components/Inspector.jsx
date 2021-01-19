import React, { Component } from "react";

import { Link } from "react-router-dom";
import InspectorNav from "./InspectorNav";
import Axios from "axios";
class Inspector extends Component {
  state = {
    userCount: {},
    errorDetails: {},
  };
  componentDidMount() {
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
    return (
      <div className="homee">
        <InspectorNav />

        <hr />
        <table>
          <tr>
            <td>
              <div className="card">
                <img
                  className="card-img-top"
                  src="https://www.kindpng.com/picc/m/495-4952535_create-digital-profile-icon-blue-user-profile-icon.png"
                ></img>
                <div className="card-body ">
                  <h3>batches Available for testing : 12</h3>
                </div>
              </div>
            </td>
            <td>
              <div className="card">
                <img
                  className="card-img-top"
                  src="data:image/jpeg;base64,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"
                ></img>
                <div className="card-body ">
                  <h4 className="card-title">
                    total packets scanned:12
                    <br />
                    valid packets:10
                    <br />
                    invalid packets:2
                  </h4>
                  <h5>this is remaining</h5>
                  <h5>statistics remaining</h5>
                  <Link to="/statistics" className="btn btn-primary">
                    View Lines
                  </Link>
                </div>
              </div>
            </td>
          </tr>
        </table>
      </div>
    );
  }
}

export default Inspector;
