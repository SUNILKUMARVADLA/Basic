import React from 'react';
import {update} from './UserFunctions'
class Update extends React.Component
{
    constructor(props)
    {
        super(props);
    this.state ={first_name:'',last_name:'',contact_num:''};
    }
    onDataSubmit = event =>
    {
        event.preventDefault()
        const User ={
            first_name:this.state.first_name,
            last_name:this.state.last_name,
            contact_num:this.state.contact_num
        }
        update(User).then(res=>{
                console.log(res)
                alert("sucessfully updated")
        })

    }
    render()
    {
        return(
            <div>
                <form methods="PUT" onSubmit={this.onDataSubmit}>
               Enter First Name: <input type="text"  name="first_name" value={this.state.first_name}onChange={event=>this.setState({first_name:event.target.value})} placeholder="Enter Name" /><br/>
               Enter LastName: <input type="text"  name="last_name" value={this.state.last_name} onChange={event=>this.setState({last_name:event.target.value})} placeholder="Enter job" /><br/>
               Enter LastName: <input type="text"  name="contact_num" value={this.state.contact_num} onChange={event=>this.setState({contact_num:event.target.value})} placeholder="Enter job" /><br/>

               <input type="submit" value="Submit" /> 
               </form>
            </div>
        );
    }
}
export default Update