import React from "react";
import Profile from './components/Profile'
import { BrowserRouter as Router, Route } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./Css/style.css";
import UserLogin from "./components/UserLogin";
import Home from "./components/Home"
import Graphs from "./components/Graphs"
import BarChart from "./components/BarChart"
import AllUsers from './components/AllUsers'
import AddNew from './components/AddNew'
import Statistics from './components/Statistics'
import Update from './components/Update'
import AddLine from './components/AddLine'
import AllLines from './components/AllLines'
import AddControls from './components/AddControls'
import AllControls from './components/AllControls'
import InspectorControls from './components/InspectorControls'

function App() {
  return (
    <div>
      <Router>
        <Route path="/" exact component={UserLogin} />
        <Route path="/graph" exact component={Graphs} />
        <Route path="/graph2" exact component={BarChart} />
        <Route path="/userLogin" exact component={UserLogin} />
        <Route path="/Home" exact component={Home} />
        <Route path="/profile" exact component={Profile} />
        <Route path="/all" exact component={AllUsers} />
        <Route path="/add" exact component={AddNew} />
        <Route path="/statistics" exact component={Statistics} />
        <Route path="/update" exact component={Update} />
        <Route path="/addLine" exact component={AddLine} />
        <Route path="/allLine" exact component={AllLines} />
        <Route path="/addControls" exact component={AddControls} />
        <Route path="/allControls" exact component={AllControls} />
        <Route path="/insControls" exact component={InspectorControls} />

      </Router>
    </div>
  );
}

export default App;
