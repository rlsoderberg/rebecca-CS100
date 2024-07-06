import React from 'react';
import ReactDOM from 'react-dom/client';
import axios from 'axios';
import './index.css';
import {filename, decade, copyright, info, title, img_path} from './fetch_data.py';

class Main extends React.Component {
    constructor() {
        super()
        this.urlbase = 'http://127.0.0.1:5000'     // localhost
        //this.urlbase = 'https://flask-service.2346o2l3anjri.us-west-2.cs.amazonlightsail.com'
        this.state = {user: '', usercount: 0, totalcount: 0}
    }
    resetdb() {
        axios.get(this.urlbase + '/resetdb').then((resp) => {
            alert(resp.data)
        })
    }
    onLoginChange(e) {
        this.setState({...this.state, user: e.target.value})
    }
    login() {
        const {user} = this.state
        var url = '/login'
        const body = {'user': user}
        const headers = { "Content-Type": "application/json" }
        const config = {
            url: url,
            baseURL: this.urlbase,
            method: 'POST',
            headers: headers,
            data: body
        }
        axios(config).then((resp) => {
            this.setState({...this.state, 
                usercount: resp.data['user count'], 
                totalcount: resp.data['total count']
            })
        }).catch(error => {
            console.log(error)
        })
    }
    render() {
        const {user, usercount, totalcount} = this.state
        return (
            <div className='Main'>
                <img src = {img_path} alt= {title} width="600"></img>
                <p>{title}</p>
            </div>
            )           
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);