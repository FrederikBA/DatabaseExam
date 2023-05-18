const LandingPage = () => {
    const username = localStorage.getItem('user')

    return (
        <div>
            <h1>Welcome {username}</h1>
        </div >
    )
}

export default LandingPage