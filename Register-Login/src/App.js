import React from 'react'
import Login from './components/Login';
import {BrowserRouter as Router, Routes ,Route } from 'react-router-dom';
import Register from './components/Register';
import Home from './components/Home';



function App() {
  return (
    <Router>
        <Routes>
        <Route exact path='/' element={<Login/>} />
        <Route exact path='/Register' element={<Register/>} />
        <Route exact path='/Home' element={<Home/>} />
        
    </Routes>
  </Router>
   
  )
}

export default App