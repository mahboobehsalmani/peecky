import React from 'react';
import logo from './logo.svg';
import './App.css';
import Home from './containers/Home/Home';
import Layout from './containers/Layout/Layout';
import Spinner from './components/UI/Spinner/Spinner';



function App() {
  return (
    <div>
      <Layout/>
      <Home />
    </div>
  );
}

export default App;
