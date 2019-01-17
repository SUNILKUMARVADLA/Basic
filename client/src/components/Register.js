import React,{Component} from 'react'
import {register} from './UserFunctions'
import Button from '@material-ui/core/Button';

class Register extends Component{
    constructor(){
        super()
        this.state={
            email:'',
            password:'',
            pnum:''
        }
        this.onDataSubmit = this.onDataSubmit.bind(this)

    }
    // onChange(e)
    // {
    //     this.setState({[e.target.name]:e.target.value})

    // }
    onDataSubmit(e){
        e.preventDefault()

        const newUser ={
            email:this.state.email,
            password:this.state.password,
            pnum:this.state.pnum
        }
        register(newUser).then(res=>{
            if(res.error)
            {
                if(res.error.response.status===409){
                    alert("already existed")
                }
            }
            else    
            {   console.log("hello")
                console.log(res)
                alert("Enter OTP Next And Check Your Email")
                this.props.history.push(`/otp`)
            }
        })
    }
    render()
    {
        return(
            <div>
                <form onSubmit={this.onDataSubmit}>
               Enter Email <input type="text"  name="email" value={this.state.email}onChange={event=>this.setState({email:event.target.value})} placeholder="Enter Email" /><br/>
               Enter Password<input type="password"  name="pasword" value={this.state.password} onChange={event=>this.setState({password:event.target.value})} placeholder="Enter Password" /><br/>
               Enter Phonenumber<input type="text"  name="pnum" value={this.state.pnum} onChange={event=>this.setState({pnum:event.target.value})} placeholder="Enter Password" /><br/>
               <input type="submit" value="Submit" /> 
               </form>
            </div>
        );
    }
    
}

export default Register