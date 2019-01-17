import React,{Component} from 'react';
import {NavLink} from 'react-router-dom';


const Navigation=()=>{
    return(
        <div>
            <NavLink to="/update">Update</NavLink>
            <NavLink to="/delete">Delete</NavLink>
            {/* <NavLink to="/profile">Login</NavLink> */}
        </div>
    );
}
 export default Navigation;