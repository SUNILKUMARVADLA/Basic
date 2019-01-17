import React,{Component} from 'react'
import {otp} from './UserFunctions'

class OTP extends Component{
    constructor(){
        super()
        this.state={
            otp:''
        }
        this.onDataSubmit = this.onDataSubmit.bind(this)

    }
    // onChange(e)
    // {
    //     this.setState({[e.target.name]:e.target.value})

    // }
    onDataSubmit(e){
        e.preventDefault()

        const check ={
            otp:this.state.otp
        }
        otp(check).then(res=>{
            if(res.error)
            {
                if(res.error.response.status===409){
                    alert("otp is invalid please try again")
                }
            }
            else    
            {   console.log("hello")
                console.log(res)
                this.props.history.push(`/login`)
            }
        })
    }
    render()
    {
        return(
            <div>
                <form onSubmit={this.onDataSubmit}>
               Enter Email <input type="text"  name="otp" value={this.state.otp}onChange={event=>this.setState({otp:event.target.value})} placeholder="Enter Otp" /><br/>
               <input type="submit" value="Submit" /> 
               </form>
            </div>
        );
    }
    
}

export default OTP