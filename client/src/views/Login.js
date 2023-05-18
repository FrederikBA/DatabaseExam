import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import apiUtils from "../utils/apiUtils"


const Login = ({ onLogin }) => {
  const [loginCredentials, setLoginCredentials] = useState({ username: "", password: "" });
  const [loginError, setLoginError] = useState("");

  const navigate = useNavigate();

  const URL = apiUtils.getUrl()

  const login = async (evt) => {
    evt.preventDefault()
    try {
      const res = await apiUtils.getAxios().post(URL + '/login', {
        username: loginCredentials.username,
        password: loginCredentials.password
      })
      localStorage.setItem('jwtToken', res.data.access_token)
      localStorage.setItem('user', loginCredentials.username)
      navigate('/landing-page')
      onLogin()
    } catch (error) {
      setLoginError(error.response.data.message)
    }
  }

  const onChange = (evt) => {
    setLoginCredentials({ ...loginCredentials, [evt.target.id]: evt.target.value })
  }

  return (
    <div className="center">
      <p className="errorMessage">{loginError}</p>
      <form onChange={onChange} >
        <input className="loginInput" placeholder="Brugernavn" id="username" />
        <br></br>
        <input className="loginInput" type="password" placeholder="Adgangskode" id="password" />
        <br></br>
        <button className="loginButton" onClick={login}>Log ind</button>
      </form>
    </div >
  )
}


export default Login