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
import $ from 'jquery';
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
// import CardExampleWithoutAvatar from './card_test'

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
        this.state = {

        };
    }
    loadCourses() {
        $.ajax({
            url: '/allcourses',
            dataType: 'json',
            cache: false,
            type: 'GET',
            success: function(data) {
                console.log(data);
                this.setState({data: data});
            }.bind(this),
            error: function(xhr, status, err) {
                console.log("error");
                // console.error(this.props.url, status, err.toString());
            }.bind(this),
        });
    }
    componentDidMount() {
        this.loadCourses();
          setInterval(this.loadCourses, this.props.pollInterval);
    }
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


Main.propTypes = {

};
Main.defaultProps = {

};


export default Main;
