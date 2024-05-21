import React from 'react';
import ReactDOM from 'react-dom/client';
import './calc.css';
import { Button, ButtonType } from './button'

class Main extends React.Component {

    constructor() {
      super()
      this.state = {display: '0', leftnum: 0, op: ''}
  }

  numberClick(event) {
    const { display } = this.state
    const val = event.target.value
    var newdisplay
    if (display === "0")
        newdisplay = val
    else
        newdisplay = display + val
    this.setState({...this.state, display: newdisplay})
  }

    opClick(event) {
      const { display } = this.state
      const leftnum = parseInt(display)
      const op = event.target.value
      this.setState({...this.state, display: '0', leftnum: leftnum, op: op})
  }

    ceClick(event) {
      const { display } = this.state
      this.setState({...this.state, display: '0', leftnum: 0, op: ''})
  }

    eqClick() {
      const {leftnum, op, display } = this.state
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

          this.setState({...this.state, display: res.toString(), leftnum: 0, op: ''})
      }
  }
    render() {

      const { display } = this.state
      const numberClick = this.numberClick.bind(this)
      const opClick = this.opClick.bind(this)
      const ceClick = this.ceClick.bind(this)
      const eqClick = this.eqClick.bind(this)

        return (
            <div className='main'>
                <img className='logo' src="https://d2o2figo6ddd0g.cloudfront.net/6/w/31cxsxy4no5n2j/Flagonly.jpg" alt="Whitworth University"/>
                <h1 style={{"textAlign":"center"}}>π-rates Calculator</h1>
                <table className='calc'>
                    <tbody>
                    <tr className='calc'>
                        <td colspan="5"><span className="display" id="display">{display}</span></td>
                    </tr>
                    <tr>
                        <td><Button type={ButtonType.Number} display="7" onClick={numberClick}/></td>
                        <td><Button type={ButtonType.Number} display="8" onClick={numberClick}/></td>
                        <td><Button type={ButtonType.Number} display="9" onClick={numberClick}/></td>
                        <td><Button type={ButtonType.Number} display="'" onClick={opClick}/></td>
                        <td><button className="op">?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='4'>4</button></td>
                        <td><button className="number" value='5'>5</button></td>
                        <td><button className="number" value='6'>6</button></td>
                        <td><button className="op">*</button></td>
                        <td><button className="op">?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='1'>1</button></td>
                        <td><button className="number" value='2'>2</button></td>
                        <td><button className="number" value='3'>3</button></td>
                        <td><button className="op">-</button></td>
                        <td><button className="op">?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='0'>0</button></td>
                        <td><Button type={ButtonType.Number} display="CE" onClick={ceClick}/></td>
                        <td><Button type={ButtonType.Number} display="=" onClick={eqClick}/></td>
                        <td><button className="op">+</button></td>
                        <td><button className="op">?</button></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        )
    }
<<<<<<< HEAD
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
              <td><Button type={ButtonType.Number} display="7" onClick={numberClick}/></td>
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

  
=======
>>>>>>> 281f552ab116a2766162db4d92e37d3e08b9fe53
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main user='Pete' />);