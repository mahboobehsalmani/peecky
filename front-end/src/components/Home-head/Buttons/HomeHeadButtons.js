// **** mahboobeh salmani ****

import React, {Component} from 'react';
import classes from './HomeHeadButtons.module.css';
import res from '../../../assets/icons/icon-res.png';
import cafe from '../../../assets/icons/icon-cafe.png';
import hotel from '../../../assets/icons/icon-hotel.png';
import shop from '../../../assets/icons/icon-shop.png';




class HomeHeadButtons extends Component {

    render(){
        const leftStyle= {
                'border-left-width': '3px'
        }
        return(
            <div>
                <button className={classes.btn}>
                    <img src={res}/>
                    <p>رستوران</p>
                </button>
                <button className={classes.btn}>
                    <img src={cafe}/>
                    <p>کافی شاپ</p>
                </button>
                <button className={classes.btn}>
                    <img src={hotel}/>
                    <p>هتل</p>
                </button>
                <button className={classes.btn} >
                    <img src={shop}/>
                    <p>فروشگاه</p>
                </button>
            </div>
        );
    }
}

export default HomeHeadButtons;