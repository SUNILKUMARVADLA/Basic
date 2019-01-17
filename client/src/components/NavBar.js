import React,{Component} from 'react';
import {NavLink} from 'react-router-dom';


const NavBar=()=>{
    return(
        <div>
            <NavLink to="/register">Register</NavLink>
            <NavLink to="/login">Login</NavLink>
            {/* <NavLink to="/profile">Login</NavLink> */}
        </div>
    );
}
 export default NavBar;