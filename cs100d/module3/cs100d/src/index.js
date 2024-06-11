import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

class Main extends React.Component {
  render () {
    return(
      <div className = 'Main'>
        <p>0000000: 792f 3031 2f20 232f 2c73 6179 2066 6f72  y/01/ #/,say for
0000010: 2075 6e70 6163 6b27 2842 3430 2934 272c   unpack'(B40)4',
0000020: 27a4 a011 008a aaa4 1126 9aec aad5 54a8  '........&....T.
0000030: a6a4 0a24 9a27                           ...$.'</p>
      </div>
    )
  }
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Main />);