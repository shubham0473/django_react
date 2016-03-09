import React from 'react';
import Card from 'material-ui/lib/card/card';
import CardActions from 'material-ui/lib/card/card-actions';
import CardHeader from 'material-ui/lib/card/card-header';
import FlatButton from 'material-ui/lib/flat-button';
import CardText from 'material-ui/lib/card/card-text';


class CourseCard extends React.component {
    constructor(props, context) {
        super(props, context);
        // this.handleRequestClose = this.handleRequestClose.bind(this);
        // this._toggleNav = this._toggleNav.bind(this);
    }
    render () {
        var courseNodes = this.props.data.map(function(course){
            return (
                <CardHeader
                  title={course.name}
                  subtitle={course.name}
                  actAsExpander={true}
                  showExpandableButton={true}
                />
                <CardText expandable={true}>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit.
                  Donec mattis pretium massa. Aliquam erat volutpat. Nulla facilisi.
                  Donec vulputate interdum sollicitudin. Nunc lacinia auctor quam sed pellentesque.
                  Aliquam dui mauris, mattis quis lacus id, pellentesque lobortis odio.
                </CardText>
            );
        });
        return (
            <div>
                <Card>
                    {courseNodes}
                </Card>
            </div>
        );
    }
}
