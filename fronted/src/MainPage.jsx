import {useState} from "react"
import axios from "axios"
import "./MainPage.Module.scss"

export const MainPage = () => {
    const [realURL, setRealURL] = useState("");
    const [shortened, setShortened] = useState("");
    const [itemname, setItemname] = useState("item1");

    const isRightURL = (urlData) => {
        return new Promise((resolve, reject)=>{
            axios.post("http://localhost:8000/api/verify",{
                origin_url: urlData
            })
            .then(function (response){
                resolve(response.data.result)
            })
            .catch(function (error){
                reject(error)
            })
        })
    }

    const handleCopyClipBoard = async (text) => {
        try {
          await navigator.clipboard.writeText(text);
          alert('클립보드에 링크가 복사되었습니다.');
        } catch (e) {
          alert('복사에 실패하였습니다');
        }
    };

    const onClickButton = () => {
        isRightURL(realURL)
        .then((isvalid)=>{
            if (isvalid === false){
                setItemname("invaliditem")
                setShortened("invlid url")
                console.log('invalid url')
            }
            else{
                setItemname("item1")
                axios
                .post("http://localhost:8000/api/exchange",{
                    origin_url: realURL
                })
                .then(function (response) {
                    try{
                        setShortened(response.data.shorten_url);
                        handleCopyClipBoard(response.data.shorten_url);
                    } catch (e) {

                    }
                    navigator.clipboard.writeText(response.data.shorten_url)
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
        <div className="main-body">
            <div>
                <header>
                    <nav className="main-title">
                        <a href="/" className="home-link">URL Shortener</a>
                        <div>

                        </div>
                    </nav>
                </header>
            </div>
            <div className="container">
                <div>
                    <p>Enter a long URL to make shorten</p>
                </div>
                <div>
                    <input id="realurl" className={itemname} type="text" onChange={(e)=>setRealURL(e.target.value)}></input>
                    <p>{shortened}</p>
                    <button className="inbox1" onClick={onClickButton}>URL 단축</button>
                </div>

            </div>
            <footer>
                <div>
                    <h3>INFO</h3>
                    <p>Email : rkwoal216@gmail.com</p>
                </div>
            </footer>
        </div>
    );
}