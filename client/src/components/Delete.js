import React from 'react';
import {del} from './UserFunctions'
const Delete =()=>{
    del().then(res=>{
        if(!res.error){
            console.log(res)
            alert("Deleted")
        }
    })
}
export default Delete