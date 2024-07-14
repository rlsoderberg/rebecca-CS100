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
                <div className = 'Section1'>
                    <div className = 'Column1'>
                        <div className = 'burger-menu'>
                            <button class="hamburger-button"><img className='burger'src="https://i.ibb.co/ZXJNKSv/smol-pancake.png"></img> </button>
                            <div class="nav-links">
                                <a href="#">Home</a>
                                <a href="#">Services</a>
                                <a href="#">Contact</a>
                        </div>
                    </div>
                    <div className = 'outer-text'>
                        <div className = 'inner-text'>
                            <p className = 'name'>Becca Soderberg</p>
                            <p className = 'field'>User Experience and Visual Design</p>
                            <button class="work-button">Let's Work Together</button>
                            <p className = 'links'>Email me or find me on Linkedin<br></br>Download my resume</p>
                        </div>
                    </div>

                </div>
                    <div className = 'Column2'>Column2</div>
                        <div className = 'Section2'>
                        <p>About Me</p>
                        </div>
                        <div className = 'Section3'>
                        <p>Testimonials</p>
                        </div>
                        <div className = 'Section4'>
                            <p>Projects</p>
                        </div>
                        <div className = 'Section5'>
                            <p>Contact Me</p>
                        </div>
                    </div>

            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);