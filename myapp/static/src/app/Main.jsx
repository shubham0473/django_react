/**
* In this file, we create a React component
* which incorporates components providedby material-ui.
*/

import React from 'react';
// import {deepOrange500} from 'material-ui/lib/styles/colors';
import AppBar from 'material-ui/lib/app-bar';
import LeftNav from 'material-ui/lib/left-nav';
import MenuItem from 'material-ui/lib/menus/menu-item'
// import LeftBarComponent from './left_nav';
// import NavbarComponent from './main_nav';





class Main extends React.Component {
    constructor(props, context) {
        super(props, context);
        // this.handleRequestClose = this.handleRequestClose.bind(this);
        this._toggleNav = this._toggleNav.bind(this);
    }
    _toggleNav(e){
        e.preventDefault();
        window.console.log("Click!");
        this.refs.leftNav.setState({open: !this.refs.leftNav.props.open});
    }

    render () {
        return (
            <div>
            <LeftNav
            ref="leftNav"
            docked={false}>
            <MenuItem>Menu Item</MenuItem>
            <MenuItem>Menu Item 2</MenuItem>
            </LeftNav>
            <AppBar
            title="Default"
            onLeftIconButtonTouchTap={this._toggleNav}
            isInitiallyOpen={ true }/>
            </div>
        );
    }
    // Event handler for 'change' events coming from store mixins.
    _onChange() {

        this.setState(getState());
    }
}

export default Main;
