import React from 'react';
import ReactDOM from 'react-dom/client';
import './calc.css';

class Main extends React.Component {
    constructor () {
        super()
        this.state = {display: '0', leftnum: 0, op: ''}
    }

    numberClick(event) {
        const { display } = this.state
        const val = event.target.value
        var newdisplay
        // If there's a 0 there, or some non-number, clear the display
        if (display === '0')
            newdisplay = val
        else
            newdisplay = display + val
        this.setState({...this.state, display: newdisplay})
    }

    ceClick(event) {
        this.setState({...this.state, display: 0, leftnum: 0, op: ''})
    }

    opClick(event) {
        const { display } = this.state
        const leftnum = parseInt(display)
        const op = event.target.value
        var newdisplay = event.target.value
        this.setState({...this.state, display: newdisplay, leftnum: leftnum, op:op})
    }
    eqClick(event) {
        const {display, leftnum, op} = this.state
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

        return (
            <div className='main'>
                <img className='logo' src="https://d2o2figo6ddd0g.cloudfront.net/6/w/31cxsxy4no5n2j/Flagonly.jpg" alt="Whitworth University"/>
                <h1 style={{"textAlign":"center"}}>π-rates Calculator</h1>
                <table className='calc'>
                    <tbody>
                    <tr className='calc'>
                        <td colSpan="5"><span className="display" id="display">{display}</span></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='7' onClick = {numberClick}>7</button></td>
                        <td><button className="number" value='8' onClick = {numberClick}>8</button></td>
                        <td><button className="number" value='9' onClick = {numberClick}>9</button></td>
                        <td><button className="op" onClick = {opClick} value='/'>/</button></td>
                        <td><button className="op" onClick = {opClick} value='?'>?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='4' onClick = {numberClick}>4</button></td>
                        <td><button className="number" value='5' onClick = {numberClick}>5</button></td>
                        <td><button className="number" value='6' onClick = {numberClick}>6</button></td>
                        <td><button className="op" onClick = {opClick} value='*'>*</button></td>
                        <td><button className="op" onClick = {opClick} value='?'>?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='1' onClick = {numberClick}>1</button></td>
                        <td><button className="number" value='2' onClick = {numberClick}>2</button></td>
                        <td><button className="number" value='3' onClick = {numberClick}>3</button></td>
                        <td><button className="op" onClick = {opClick} value='-'>-</button></td>
                        <td><button className="op" onClick = {opClick} value='?'>?</button></td>
                    </tr>
                    <tr>
                        <td><button className="number" value='0' onClick = {numberClick}>0</button></td>
                        <td><button className="op" onClick = {ceClick} value='CE'>CE</button></td>
                        <td><button className="op" onClick = {eqClick} value='='>=</button></td>
                        <td><button className="op" onClick = {opClick} value='+'>+</button></td>
                        <td><button className="op" onClick = {opClick} value='?'>?</button></td>
                    </tr>
                    </tbody>
                </table>
            </div>
        )
    }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);