import axios from 'axios'

export const register = newUser => {
    console.log("this is register")
    return axios
    .post("users/register",{
        email:newUser.email,
        password:newUser.password,
        pnum:newUser.pnum
    })
    .then(response=>{
        console.log("Registred")
        console.log(response)
        return response
    }).catch(err=>{
        return{error:err}
    })
}
export const otp = check => {
    console.log("this is OTP")
    return axios
    .post("users/otp",{
        otp:check.otp
    })
    .then(response=>{
        console.log("OTP sucess")
        console.log(response)
        return response
    }).catch(err=>{
        console.log("error")
        return{error:err}
    })
}
export const login = user => {
    return axios
    .post("users/login",{
        email:user.email,
        password:user.password
    })
    .then(response=>{
        localStorage.setItem('usertoken',response.data.token)
        console.log(response)
        return response.data.token
    })
    .catch(err=>{
        return{error:err}
    })
}
export const update = user => {
    return axios
    .put(`/users/update`,{

        first_name:user.first_name,
        last_name:user.last_name,
        contact_num:user.contact_num
    },{
         headers: 
            {
                Authorization: `Bearer ${localStorage.getItem('usertoken')}`
         
            }
    })
    .then(response=>{
        console.log(response)
        return response
    })
    .catch(err=>{
        return err
    })
}
export const del = () => {
    return axios
    .delete(`/users/delete`,{
         headers: 
            {
                Authorization: `Bearer ${localStorage.getItem('usertoken')}`
         
            }
    })
    .then(response=>{
        return response
    })
    .catch(err=>{
        return err
    })
}

