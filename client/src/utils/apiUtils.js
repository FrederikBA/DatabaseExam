import axios from "axios";

const URL = 'http://localhost:8000';

const api = () => {

    const getUrl = () => {
        return URL;
    }

    const getAxios = () => {
        return axios.create()
    }

    return {
        getUrl,
        getAxios,
    }
}

export default api();