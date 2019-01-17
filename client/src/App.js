import React, { Component } from 'react';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import NavBar from './components/NavBar'
import Landing from './components/Landing'
import Login from './components/Login'
import Register from './components/Register'
import Profile from './components/Profile'
import OTP from './components/otp'
class App extends Component {
  render() {
    return (
      <Router>
        <div className="App">
       <NavBar/> 
       <Switch>
        <Route exact path="/register" component={Register}/>
        <Route exact path="/login" component={Login}/>
        <Route exact path="/profile" component={Profile}/>
        <Route exact path="/otp"     component={OTP}/>
        </Switch>
        </div>
      </Router>
    );
  }
}

export default App;
