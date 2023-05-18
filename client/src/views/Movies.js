import React, { useState, useEffect } from 'react';
import apiUtils from '../utils/apiUtils';


const Movies = () => {
    const [posts, setPosts] = useState([]);
    const [isLoading, setIsLoading] = useState(false);
    const [currentPage, setCurrentPage] = useState(1);
    const [postsPerPage, setPostsPerPage] = useState(10);

    useEffect(() => {
        const getPosts = async () => {
            const response = await apiUtils.getAxios().post('https://jsonplaceholder.typicode.com/posts')
            setPosts(response.data)
            setIsLoading(false)
        }
    }, []);

    console.log(posts);
    return (
        <div className="center">
            <h1>Movies</h1>
        </div>
    )
}

export default Movies