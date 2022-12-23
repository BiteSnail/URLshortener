import {useState} from "react"
import axios from "axios"

export const MainPage = () => {
    const [realURL, setRealURL] = useState(0);
    const [shortened, setShortened] = useState(0);

    const isRightURL = (urlData) => {
        return new Promise((resolve, reject)=>{
            axios.post("http://localhost:8000/api/verify",{
                origin_url: urlData
            })
            .then(function (response){
                console.log(response.data.result)
                resolve(response.data.result)
            })
            .catch(function (error){
                reject(error)
            })
        })
    }

    const onClickButton = () => {
        console.log(realURL);
        
        isRightURL(realURL)
        .then((isvalid)=>{
            if (isvalid == false){
                console.log('invalid url')
            }
            else{
                axios
                .post("http://localhost:8000/api/exchange",{
                    origin_url: realURL
                })
                .then(function (response) {
                    console.log(response.data.shorten_url, "shorten url")
                    setShortened(response.data.shorten_url);
                })
                .catch(function (error){
                    console.log(error, "error")
                })
            }
        })
        .catch((err)=>{
            console.log(err)
        })
    }

    return (
        <div>
            <header>
                <h1>URL Shorter by BiteSnail</h1>
            </header>
            <nav>

            </nav>
            <article>
                <div>
                    <h2> 너에게 주는 짧은 링크</h2>
                    <p> 단축된 URL을 통해 바이러스를 뿌려보자.</p>
                </div>
                <div>
                    <input type="text" onChange={(e)=>setRealURL(e.target.value)}></input>
                    <button onClick={onClickButton}>URL 단축</button>
                    <p>{shortened}</p>
                </div>
            </article>
            <footer>
                <div>
                    <h6>INFO</h6>
                    <p>made by bitesnail</p>
                    <p>email : rkwoal216@gmail.com</p>
                </div>
            </footer>
        </div>
    );
}