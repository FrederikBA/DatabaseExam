import { useNavigate } from "react-router-dom";

const OrderConfirmation = () => {
    const navigate = useNavigate()

    const navigateProfile = () => {
        navigate("/profile/" + localStorage.getItem('userId'))
    }

    return (
        <div className="center">
            <h1>Tak for din ordre!</h1>
            <button onClick={navigateProfile} className="orderConfirmationButton">Se dine film</button>
        </div>
    )
}

export default OrderConfirmation