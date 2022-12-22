import { Route, Routes } from "react-router-dom";
import { MainPage } from "./MainPage";
import { ConnectPath} from "./ConnectPath";

export const App = () => {    
    return (
        <div className="App">
            <Routes>
                <Route path="/:id" element= {<ConnectPath />}/>
                <Route path="/" element = {<MainPage/>}/>
            </Routes>
        </div>
    );
}