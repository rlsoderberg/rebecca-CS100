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
    burgerselector (){
        document.querySelector('.hamburger-button').addEventListener('click', function() {
            document.querySelector('.nav-links').style.display = 
            (document.querySelector('.nav-links').style.display == 'none') ? 'block' : 'none';
        });
    }
    render() {
        const {user, usercount, totalcount} = this.state
        return (
            <div className='Main'>
                <div className = 'Column1'>
                    <div className='button-div'>
                    <button class="hamburger-button"><img className='burger'src="https://i.ibb.co/ZXJNKSv/smol-pancake.png"></img> </button>
                    </div>
                    <div className = 'intro-div'>
                        <p className = 'name'>Becca Soderberg</p>
                        <p className = 'field'>User Experience and Visual Design</p>
                        <p className = 'bio'>I should really have some sort of bio/intro here...</p>
                        <button class="work-button">Let's Work Together</button>
                        <p className = 'links'>Email me or find me on Linkedin<br></br>Download my resume</p>
                    </div>
                </div>
                <div className = 'Column2'>
                </div>
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);