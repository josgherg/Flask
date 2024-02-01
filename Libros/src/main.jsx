import React from 'react';
import ReactDOM from 'react-dom/client';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Navbar from './components/Navbar';
import Index from './pages/Index';
import Home from './pages/Home';
import Footer from './components/Footer';

import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
    <Navbar/>
    <Routes>
      <Route path='/' Component={Index}/>
      <Route path='/home' Component={Home}/>
      {//<Route path='/*' Component={Error404} />
      }
    </Routes>
    <Footer/>
    </BrowserRouter>
  </React.StrictMode>
)
