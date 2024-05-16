import React from 'react';
import Draggable from 'react-draggable';
import ReactDOM from 'react-dom/client';
import './index.css'

/*
function clicknum(num) {
    var world = document.getElementById('world')
    if (num == 2)
        world.src = '../public/venus.png'
    else if (num == 3)
        world.src = '../public/earth.png'
    else if (num == 4)
        world.src = '../public/mars.png'
}
*/

//so what's the difference between writing something in Main and writing it in the HTML???
class Main extends React.Component{
    render () {
        //you knew we'd start with hello world, didn't you?
        return(
            <Draggable>
            <div className = 'Hello'>
                <p class = 'HELLO'>Hello</p>
            </div>
            </Draggable>
        )
    }
}


//find the element with id Root in the HTML file, and place our Main class there.
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);