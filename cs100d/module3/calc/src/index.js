import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Main extends React.Component{
  constructor (){
    super ()
    this.state = {display: '0'}

  }

  numberClick (event){
    const {display} = this.state
    const val = event.target.value
    var newdisplay
    if (display === '0')
      newdisplay = val
    else
      newdisplay = display + val
    this.setState ({...this.state, display: newdisplay})
  }

  otherClick(event) {
    const val = event.target.value
    console.log('you have clicked something else')
    var newdisplay = '0'
    this.setState ({...this.state, display: newdisplay})
  }

  render() {
    const { display } = this.state
    const numberClick = this.numberClick.bind(this)
    const otherClick = this.otherClick.bind(this)
  
    return(
      <div class = 'center'>
        <img src = 'calc-fav.png' class = 'calc-pic'></img>
        <p class = 'title'>REACT<br></br>CALC</p>

        <div class = 'calc-box'>
          <div class="display-bg">
            <td colspan="5"><span className="display" id="display">{display}</span></td>
					</div>
          <table>
            <tr>
              <td><button class="number" onClick={numberClick} value='7'>7</button></td>
              <td><button class="number" onClick={numberClick} value='8'>8</button></td>
              <td><button class="number" onClick={numberClick} value='9'>9</button></td>
              <td><button class="op" onclick={otherClick}>+</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='4'>4</button></td>
              <td><button class="number" onClick={numberClick} value='5'>5</button></td>
              <td><button class="number" onClick={numberClick} value='6'>6</button></td>
              <td><button class="op" onClick={otherClick}>-</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='1'>1</button></td>
              <td><button class="number" onClick={numberClick} value='2'>2</button></td>
              <td><button class="number" onClick={numberClick} value='3'>3</button></td>
              <td><button class="op" onClick={otherClick}>*</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='0'>0</button></td>
              <td><button class="number" onClick={otherClick}>CE</button></td>
              <td><button class="op" onClick={otherClick}>=</button></td>
              <td><button class="op" onClick={otherClick}>/</button></td>
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