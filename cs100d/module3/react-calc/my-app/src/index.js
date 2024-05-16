import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css'

class Main extends React.Component{
    render () {
        //you knew we'd start with hello world, didn't you?
        return(
            <div className = 'Main'>
                <p>Hello World</p>
            </div>
        )
    }
}

//find the element with id Root in the HTML file, and place our Main class there.
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);