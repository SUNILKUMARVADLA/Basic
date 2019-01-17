import React,{Component} from 'react'
import {login} from './UserFunctions'

class Login extends Component{
    constructor(){
        super()
        this.state={
            email:'',
            password:''
        }
        this.onDataSubmit = this.onDataSubmit.bind(this)

    }
    // onChange(e)
    // {
    //     this.setState({[e.target.name]:e.target.value})

    // }
    onDataSubmit(e){
        e.preventDefault()

        const user ={
            email:this.state.email,
            password:this.state.password
        }
        login(user).then(res=>{
            if(res.error)
            {
                if(res.error.response.status===404){
                    alert("Not found")
                }
                if(res.error.response.status===401){
                    alert("Inavalid Password ")
                }
                if(res.error.response.status===400){
                    alert("please Confirm")
                }


            }
            else
            {
                console.log("hello")
                console.log(res)
                this.props.history.push(`/profile`)
            }
        })
    }
    render()
    {
        return(
            <div>
                <form onSubmit={this.onDataSubmit}>
               Enter Email <input type="text"  name="email" value={this.state.email}onChange={event=>this.setState({email:event.target.value})} placeholder="Enter Email" /><br/>
               Enter Password<input type="password"  name="job" value={this.state.password} onChange={event=>this.setState({password:event.target.value})} placeholder="Enter Password" /><br/>
               <input type="submit" value="Submit" /> 
               </form>
            </div>
        );
    }
    
}

export default Login;