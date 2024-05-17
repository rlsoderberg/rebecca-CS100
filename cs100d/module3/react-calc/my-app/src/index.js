import React from 'react';
import Draggable from 'react-draggable';
import ReactDOM from 'react-dom/client';
import './index.css'



//multiple functions WITHIN Main, including a constructor, which... does all the consts, basically? right?
class Main extends React.Component{
    constructor(){
        super()

        //the count variable will track how many times the button is clicked
        //since it can change while this component is visible, we hold it in state
        this.state = {'count':0}

        const myImage = new Image(200)
        myImage.src = '../public/earth.png'
        document.body.appendChild(myImage)
    }

    incrementCount(){
        //grab the count value from state, increment it, then update state
        const{count} = this.state
        //when we call setState, our render function will automatically get called
        this.setState({...this.state, count:count+1})
    }

    clicknum(num) {
        var world = document.getElementById('world')
        if (num == 2)
            world.src = '../public/venus.png'
        else if (num == 3)
            world.src = '../public/earth.png'
        else if (num == 4)
            world.src = '../public/mars.png'
    }

    render () {
        //the user's planet is a property to this element
        const {planet} = this.props
        //the click count is in state
        const {count} = this.state
        return(
            //i literally don't know how to comment inside <Draggable>, isn't that weird???
            //so you put your onClicks inside return!!!
            //my clicknum isn't working because it references back to the 'world' image in the html. how do i do images???
            //i'm going to try this javascript thing where you go 'new Image(width)', up in the constructor
            //not working! i think it made that little image error you see to the right of the audio
            //which does lead me to suspect i'm just writing the image address wrong... i'm going to sneak the images in here and check
            //that didn't seem to be it. which at least restores a bit of faith in my address writing skills
            <Draggable>
            <div className = 'Main'>
                <p class = 'HELLO'>Hello {planet}</p>
                <p>{count} clicks</p>
                
                <button onClick={this.incrementCount.bind(this)}>Count</button>

                <tr>
                    <td><button class="number" onclick="clicknum(this)">2</button></td>
                    <td><button class="number" onclick="clicknum(this)">3</button></td>
                    <td><button class="number" onclick="clicknum(this)">4</button></td>
                </tr>
            </div>
            </Draggable>
        )
    }
}


//find the element with id Root in the HTML file, and place our Main class there.
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);