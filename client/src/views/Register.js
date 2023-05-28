import { useState } from 'react';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import apiUtils from '../utils/apiUtils';

const Register = () => {
    const [loginCredentials, setLoginCredentials] = useState({ first_name: "", last_name: "", username: "", password: "" });

    const URL = apiUtils.getUrl()

    const register = async () => {
        try {
            const response = await apiUtils.getAxios().post(URL + '/register', {
                first_name: loginCredentials.first_name,
                last_name: loginCredentials.last_name,
                username: loginCredentials.username,
                password: loginCredentials.password
            })
            registerNotifySuccess()
        } catch (error) {
            registerNotifyError()
        }
    }


    // Toast
    const registerNotifySuccess = () => {
        toast.success('Din bruger er oprettet!', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    const registerNotifyError = () => {
        toast.error('Der opstod en fejl, din bruger blev ikke oprettet', { position: toast.POSITION.BOTTOM_RIGHT });
    };

    const onChange = (evt) => {
        setLoginCredentials({ ...loginCredentials, [evt.target.id]: evt.target.value })
        console.log(loginCredentials);
    }

    return (
        <div className="center">
            <form onChange={onChange} >
                <input className="registerInput" type="text" placeholder="Fornavn" id="first_name" />
                <br></br>
                <input className="registerInput" type="text" placeholder="Efternavn" id="last_name" />
                <br></br>
                <input className="registerInput" type="text" placeholder="Brugernavn" id="username" />
                <br></br>
                <input className="registerInput" type="text" placeholder="Adgangskode" id="password" />
                <br></br>
                <br></br>
            </form>
            <button className="loginButton" onClick={register}>Opret bruger</button>
            <ToastContainer />
        </div >
    )
}

export default Register