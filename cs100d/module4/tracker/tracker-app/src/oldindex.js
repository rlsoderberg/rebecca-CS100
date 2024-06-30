import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import axios from 'axios';
import { useState } from "react";
import random from 'random';

class Main extends React.Component {
    constructor() {
        //set initial state
        super()
        this.state = {id:null}
        this.urlbase = 'http://127.0.0.1:5000'
    }
          onNext() {
            //setting id to be a random number? i would also need to limit this to the size of img_db
            this.setState({...this.state, id: Math.floor(Math.random())})
        }
        //this, but instead of a url, it just has... a link to a sql image, or something???
        image_function(){
            const images = [
                {
                  image_url:
                    "https://img.freepik.com/free-photo/young-female-jacket-shorts-presenting-comparing-something-looking-confident-front-view_176474-37521.jpg?w=1800&t=st=1693037944~exp=1693038544~hmac=97e967909706f9b73b4b47d521acf54806f4b9b3efab6196bc8a69f07efff554",
                  caption: "Image 1"
                },
            ]
        }
        setImage(){
            //here i want to set off the python thing where it selects for id...
            //and then bring the image back and, as you can see i deleted images, but put it there instead
        }
          render(){
                return (
                <div className="App">
                    <SlideShow images={images} />
                </div>
                );
          }
        }

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);

