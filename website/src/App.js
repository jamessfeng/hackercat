import React, {Component} from 'react';
import logo from './logo.svg';
import './App.css';
import { base } from "./components/base";
import Background from "./Background.png";




class App extends Component  {
  render() {
    return (


      <div className="App">
        <img src = {Background}/>
        <p>
          hello!
        </p>
      </div>
    );
  }
}

function HelloWorld () {
  
  console.log("CLICKED!");

  return (
    <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            HELLO WORLD!
          </p>


      </header>
    </div>

    )

}



class Test extends Component  {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            Edit <code>src/App.js</code> and save to reload.

          </p>


      </header>
    </div>
    );
  }
}

export default App;

