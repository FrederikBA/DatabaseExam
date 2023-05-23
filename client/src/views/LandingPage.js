const LandingPage = () => {
    const username = localStorage.getItem('user')

    const isLoggedIn = () => {
        return localStorage.getItem('jwtToken') !== null;
    }


    return (
        <div className="center">
            {isLoggedIn() ? <h3>Velkommen {username}</h3>
                : <h3>Du er nu logget ud.</h3>}
        </div >
    )
}

export default LandingPage