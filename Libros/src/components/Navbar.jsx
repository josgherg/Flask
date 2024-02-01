import {NavLink } from "react-router-dom";
import Logo from './Logo.jsx';

function Navbar(){

    return(
        <nav className="navbar">
            <div id="" className="navbarInner">
                <div className='navbar1'>
                    <NavLink  className={ ({isActive })=> isActive?'active':' '} to='/'>
                        <Logo/>
                    </NavLink>
                </div>
                {//<div className='navbar2'></div>     
                }
                <div className='navbar3'>
                    <form className='buscarForm'>       
                        <input className='iptBuscar' type="text" />
                        <button className='iptBtnBuscar' type="button">
                            <span className="material-symbols-outlined icono">search</span>
                        </button>
                    </form>
                </div>
                <div className='navbar4'>
                    <NavLink  className={ ({isActive })=> isActive?'active':' '} to='/home'>
                        <button className='btnUsuario'>
                            <span className="material-symbols-outlined icono">account_circle</span>
                        </button>
                    </NavLink>
                </div>
            </div>
        </nav>
    )
}

export default Navbar;

