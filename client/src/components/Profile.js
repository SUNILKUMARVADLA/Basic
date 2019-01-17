import React,{Component} from 'react';
import jwt_decode from 'jwt-decode';
import {BrowserRouter as Router,Route,Switch} from 'react-router-dom';
import Navigation from './Navigation';
import Update from './Update';
import Delete from './Delete';
class Profile extends Component{
    constructor(){
        super()
        this.state={
            email:''
        }
    }
    componentDidMount(){
        const token=localStorage.usertoken
        const decoded=jwt_decode(token)
        console.log(decoded)
        this.setState({
            email:decoded.email
        })
    }
    render(){
        return(
        <Router>
        <div className="App">
        <div>{this.state.email}</div>
       <Navigation/> 
       <Switch>
        <Route exact path="/update" component={Update}/>
        <Route exact path="/delete" component={Delete}/>
        </Switch>
        </div>
      </Router>
        );
    }
}

export default Profile;