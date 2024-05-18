import React from 'react';
import reactDOM from 'react-dom/client'
//what is the point of this './' thing??? is that just a more specific way of saying, in the same folder???
import './calc.css'

class Main extends React.Component {
    render () {
        return(
            <div className = 'main'>
                <h1 class = 'title' style="text-align:center">π-rats Calculator</h1>
                <table>
                    <tr>
                        <td><button class="number" onclick="clicknum(this)">7</button></td>
                        <td><button class="number" onclick="clicknum(this)">8</button></td>
                        <td><button class="number" onclick="clicknum(this)">9</button></td>
                        <td><button class="op" onclick="op_click(this)">+</button></td>
                    </tr>
                    <tr>
                        <td><button class="number" onclick="clicknum(this)">4</button></td>
                        <td><button class="number" onclick="clicknum(this)">5</button></td>
                        <td><button class="number" onclick="clicknum(this)">6</button></td>
                        <td><button class="op" onclick="op_click(this)">-</button></td>
                    </tr>
                    <tr>
                        <td><button class="number" onclick="clicknum(this)">1</button></td>
                        <td><button class="number" onclick="clicknum(this)">2</button></td>
                        <td><button class="number" onclick="clicknum(this)">3</button></td>
                        <td><button class="op" onclick="op_click(this)">*</button></td>
                    </tr>
                    <tr>
                        <td><button class="number" onclick="clicknum(this)">0</button></td>
                        <td><button class="number" onclick="clickce()">CE</button></td>
                        <td><button class="op" onclick="eq_click()">=</button></td>
                        <td><button class="op" onclick="op_click(this)">/</button></td>
                    </tr>
                </table>
            </div>
        )
    }
}

//find the element with id Root in the HTML file, and place our Main class there.
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);