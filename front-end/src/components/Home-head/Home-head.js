// **** mahboobeh salmani ****

import React, {Component} from 'react';
import classes from './Home-head.module.css';
import HomeHeadButtons from './Buttons/HomeHeadButtons';

class HomeHead extends Component {
    render(){
        return (
            <div className={classes.Head}>
                <HomeHeadButtons /> 
            </div>

        );
    }
}

export default HomeHead;