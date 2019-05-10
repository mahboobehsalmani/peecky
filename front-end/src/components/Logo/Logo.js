// **** mahboobeh salmani ****

import React, {Component} from 'react';

import LogoWhite from '../../assets/images/peecky-logo-white.png';
import LogoRed from '../../assets/images/peecky-logo-red.png';

import classes from './Logo.module.css';

class logo extends Component {
    state = {
        red: false
    }
    
    render(){


        let Logo = null;
        if(this.props.isRed){
            Logo=LogoRed;
        }
        if(!this.props.isRed){
            Logo=LogoWhite;
        }
        return(
            <div className={classes.Logo}>
            <img src={Logo} />
        </div>
        );
    }
}


export default logo;