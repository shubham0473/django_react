import React from 'react';
import ReactDOM from 'react-dom';
import injectTapEventPlugin from 'react-tap-event-plugin';
import Main from './Main'; // Our custom react component

//Needed for onTouchTap
//Can go away when react 1.0 release
//Check this repo:
//https://github.com/zilverline/react-tap-event-plugin
injectTapEventPlugin();

const dummy = [
    {'course_name' : 'dbms'},
    {'course_name' : 'networks'},
    {'course_name' : 'os'},
    {'course_name' : 'ir'},
];

// Render the main app react component into the app div.
// For more details see: https://facebook.github.io/react/docs/top-level-api.html#react.render
ReactDOM.render(<Main data={dummy} url="/allcourses"/>, document.getElementById('app'));
