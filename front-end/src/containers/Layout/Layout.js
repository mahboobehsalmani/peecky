// **** mahboobeh salmani ****

import React, {Component} from 'react';
import Toolbar from '../../components/NavBar/Toolbar/Toolbar';
import SideDrawer from '../../components/NavBar/SideDrawer/SideDrawer';

class Layout extends Component {
    state = {
        showSideDrawer: false
    }

    sideDrawerClosedHandler = ()=> {
        this.setState({showSideDrawer: false});
    }

    sidDrawerToggleHandler = () => {
        this.setState ((prevState)=> {
            return {showSideDrawer: !prevState.showSideDrawer};
        });
    }
    

    render(){
        return(
            <div>
                <Toolbar drawerToggleClicked={this.sidDrawerToggleHandler}/>
                <SideDrawer closed={this.sideDrawerClosedHandler}
                open={this.state.showSideDrawer}/>
            </div>
        );
    }
}

export default Layout;

