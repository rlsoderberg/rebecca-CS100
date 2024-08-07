import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Main extends React.Component {
    constructor() {
        super()
        //Initial data has no user or counts
        this.urlbase = 'http://localhost:4000'
        this.state = {rand:0, id: 0, filename:'', decade:'', source:'', info:'', title:''}
    }

    onImageChange(e) {
        //Keep track of the login value
        this.setState({...this.state, filename: e.target.value}) 
    }   
    
    login() {
            const {user} = this.state
            var url = '/login'
            // Store the user's name in a JSON object
            const body = {'user': user}
            // We're sending JSON data to our server
            const headers = { "Content-Type": "application/json" }
            // Configuration information for the server
            const config = {
                url: url,
                baseURL: this.urlbase,
                method: 'POST',
                headers: headers,
                data: body
            }
    }

    render() {
        /*unsuccessful change attempt
        const {filename, title} = this.state
        //var str = JSON.stringify(contact);
        var id = filename
        console.log(id)
        */
        const {filename, title} = this.state
        //var str = JSON.stringify(contact);
        //var id = str[1]
        //console.log(id)
        console.log(glossary[0])
        console.log(glossary)
        console.log(JSON.stringify(glossary))
        return (
            <div className='Main'>

                <div className = 'img'>
                    <img src = '.\popdecades\{filename}'></img>
                    
                </div>

                <div className = 'desc'>
                    <p>{filename}</p>
                    <button type="button" /*onClick={this.onImageChange.bind(this)}*/>Next Photo</button>
                </div>

                
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);