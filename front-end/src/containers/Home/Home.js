// **** mahboobeh salmani ****

import React, {Component} from 'react';
import HomeHead from '../../components/Home-head/Home-head';
import classes from './Home.module.css';


class Home extends Component {
    render(){
        return(
            <div className={classes.Home}>
                <HomeHead />
            </div>
        );
    }
}

export default Home;