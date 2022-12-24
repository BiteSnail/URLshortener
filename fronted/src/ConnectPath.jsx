import { useParams } from "react-router-dom";
import { useState } from "react";
import axios from "axios"
import "./MainPage.Module.scss"

export const ConnectPath = () => {
    const params = useParams();
    const [page, setPage] = useState(
    <div>
        <p>사이트로 이동 중입니다.</p>
    </div>)
    axios
        .get("http://localhost:8000/"+params.id,{
        })
        .then(function (response) {
            if(response.data.origin_url === "error"){
                setPage(
                    <div className="main-body">
                        <div>
                            <header>
                                <nav className="main-title">
                                    <a href="/" className="home-link">Page Not found</a>
                                    <div>

                                    </div>
                                </nav>
                            </header>
                        </div>
                        <footer>
                            <div>
                                <h3>INFO</h3>
                                <p>Email : rkwoal216@gmail.com</p>
                            </div>
                        </footer>
                    </div>
                )
            }
            else{
                window.location.href = response.data.origin_url;
            }
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
        page
    )
    
}