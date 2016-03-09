/**
* In this file, we create a React component
* which incorporates components providedby material-ui.
*/

import React from 'react';
// import {deepOrange500} from 'material-ui/lib/styles/colors';
import AppBar from 'material-ui/lib/app-bar';
import LeftNav from 'material-ui/lib/left-nav';
import MenuItem from 'material-ui/lib/menus/menu-item';
import Avatar from 'material-ui/lib/avatar';
import {
    blue300,
    indigo900,
    orange200,
    deepOrange300,
    pink400,
    purple500,
} from 'material-ui/lib/styles/colors';
import List from 'material-ui/lib/lists/list';
import ListItem from 'material-ui/lib/lists/list-item';
import ActionGrade from 'material-ui/lib/svg-icons/action/grade';
import ActionInfo from 'material-ui/lib/svg-icons/action/info';
import ContentInbox from 'material-ui/lib/svg-icons/content/inbox';
import ContentDrafts from 'material-ui/lib/svg-icons/content/drafts';
import ContentSend from 'material-ui/lib/svg-icons/content/send';
import Divider from 'material-ui/lib/divider';
import CourseCard from './card'

// import LeftBarComponent from './left_nav';
// import NavbarComponent from './main_nav';


const styles = {
    avatar: {
        textAlign: 'center',
    },
};


class Main extends React.Component {
    constructor(props, context) {
        super(props, context);
        // this.handleRequestClose = this.handleRequestClose.bind(this);
        this._toggleNav = this._toggleNav.bind(this);
    },
    getInitialState: function() {
        return {data: []};
    },
    loadCommentsFromServer: function() {
        $.ajax({
            url: this.props.url,
            dataType: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.error(this.props.url, status, err.toString());
            }.bind(this)
        });
    },
    componentDidMount: function() {
      this.loadCommentsFromServer();
    //   setInterval(this.loadCommentsFromServer, this.props.pollInterval);
    },
    _toggleNav(e){
        e.preventDefault();
        window.console.log("Click!");
        this.refs.leftNav.setState({open: !this.refs.leftNav.props.open});
    }

    _showCourse(e){
        e.preventDefault();
        window.console.log("clicked on course");
    }
    render () {
        return (
            <div>
                <LeftNav
                    ref="leftNav"
                    docked={false}>
                    <Avatar
                        color={deepOrange300}
                        backgroundColor={purple500}
                        size={70}
                        style={styles.avatar}
                        >
                        A
                    </Avatar>
                    <List>
                        <ListItem primaryText="Inbox" leftIcon={<ContentInbox />} />
                        <ListItem primaryText="Starred" leftIcon={<ActionGrade />} />
                        <ListItem primaryText="Sent mail" leftIcon={<ContentSend />} />
                        <ListItem primaryText="Drafts" leftIcon={<ContentDrafts />} />
                        <ListItem primaryText="Inbox" leftIcon={<ContentInbox />} />
                    </List>
                </LeftNav>
                <AppBar
                    title="Default"
                    onLeftIconButtonTouchTap={this._toggleNav}
                    isInitiallyOpen={ true }/>
                <CourseCard data={this.props.data}/>

            </div>
        );
    }

}

export default Main;
