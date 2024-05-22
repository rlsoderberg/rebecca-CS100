import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import {Button, ButtonType} from './button'

class Main extends React.Component{
  constructor (){
    super ()
    this.state = {display: '0', leftnum: 0, op:''}

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

  ceClick(event) {
    const {display} = this.state
    const val = event.target.value
    console.log('you have clicked something else')
    var newdisplay = '0'
    this.setState ({...this.state, display: newdisplay})
  }

  opClick(event) {
    const {display} = this.state
    const leftnum = parseInt(display)
    const op = event.target.value
    this.setState({...this.state, display: '0', leftnum: leftnum, op: op})
  }

  eqClick() {
    const {leftnum, op, display} = this.state
    if (op !== '') {
      const rightnum = parseInt(display)
      var res = 0
      if (op === '+')
        res = leftnum + rightnum
      else if (op === '-')
        res = leftnum - rightnum
      else if (op === '*')
        res = leftnum * rightnum
      else if (op === '/')
        res = leftnum / rightnum

      this.setState({...this.state, display:res.toString(), leftnum: 0, op: ''})
    }
  }

  render() {
    const { display } = this.state
    const numberClick = this.numberClick.bind(this)
    const ceClick = this.ceClick.bind(this)
    const opClick = this.opClick.bind(this)
    const eqClick = this.eqClick.bind(this)
  
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
              <td><Button type={ButtonType.Number} display="7" onClick={ButtonType.onclick(numberClick)}/></td>
              <td><Button type = {ButtonType.Number} onClick={numberClick} display='8'/></td>
              <td><Button type = {ButtonType.Number} onClick={numberClick} display='9'/></td>
              <td><button class="op" onClick={opClick} value = '+'>+</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='4'>4</button></td>
              <td><button class="number" onClick={numberClick} value='5'>5</button></td>
              <td><button class="number" onClick={numberClick} value='6'>6</button></td>
              <td><button class="op" onClick={opClick} value = '-'>-</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='1'>1</button></td>
              <td><button class="number" onClick={numberClick} value='2'>2</button></td>
              <td><button class="number" onClick={numberClick} value='3'>3</button></td>
              <td><button class="op" onClick={opClick} value = '*'>*</button></td>
            </tr>
            <tr>
              <td><button class="number" onClick={numberClick} value='0'>0</button></td>
              <td><button class="number" onClick={ceClick}>CE</button></td>
              <td><button class="op" onClick={eqClick}>=</button></td>
              <td><button class="op" onClick={opClick} value = '/'>/</button></td>
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