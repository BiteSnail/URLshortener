import { useParams } from "react-router-dom";
import axios from "axios"

export const ConnectPath = () => {
    const params = useParams();

    axios
        .get("http://localhost:8000/"+params.id,{
        })
        .then(function (response) {
            const url = response.data.origin_url
            window.location.href = url;
        })
        .catch(function (error) {
            return (
            <div>
                <p>서버가 응답하지 않습니다.</p>
                <p>{error}</p>
            </div>
            )
        })
    
    return (
        <div>
            <p>사이트로 이동 중입니다.</p>
        </div>
    )
    
}