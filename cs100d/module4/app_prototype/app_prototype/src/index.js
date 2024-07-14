import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Main extends React.Component {
    constructor() {
        super()
        //Initial data has no user or counts
        this.state = {user: null, usercount: 0, totalcount: 0}
        this.urlbase = 'http://127.0.0.1:5000'
    }
    render() {
        const {user, usercount, totalcount} = this.state
        return (
            <div className='Main'>
                <div className = 'Column1'></div>
                <div className = 'Column2'></div>
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);