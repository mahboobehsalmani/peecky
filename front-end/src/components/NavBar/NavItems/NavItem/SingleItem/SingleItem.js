// **** mahboobeh salmani ****

import React, { Component } from 'react';
import classes from './SingleItem.module.css';


class SingleItem extends Component {

    render(){
        return(
            <div className={classes.SingleItem}>
                <img src={this.props.itemImage}/>
                <p>{this.props.children}</p>
            </div>
        );
    }
}

export default SingleItem;