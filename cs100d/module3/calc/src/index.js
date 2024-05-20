import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

class Main extends React.Component{
  constructor (){
    super ()
    this.state = {display: '0'}

    //const numberClick = this.numberClick.bind(this)

  }

  numberClick (event){
    const {display} = this.state
    const val = event.target.value
    var newdisplay
    if (display === '0') {
      newdisplay = val
    }
    else
      newdisplay = display + val
    this.setState ({...this.state, display: newdisplay})
  }

  render() {
    const { display } = this.state
    const numberClick = this.numberClick.bind(this)
    return(
      <div class = 'center'>
        <img src = 'calc-fav.png' class = 'calc'></img>
        <p class = 'title'>REACT<br></br>CALC</p>
        <p class = 'HELLO'>Hello {display}</p>
        <div class = 'calc'>
          <table>
            <tr>
              <td colspan="5"><span className="display" id="display">{display}</span></td>
            </tr>
            <tr>
              <td><button className="number" onClick={numberClick} value='7'>7</button></td>
              <td><button className="number" onClick={numberClick} value='8'>8</button></td>
              <td><button className="number" onClick={numberClick} value='9'>9</button></td>
            </tr>
          </table>
        </div>
      </div>
    )
  }

  
}

//wait, what's the difference between App.js and index.js??? do i even need app.js???
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Main />)