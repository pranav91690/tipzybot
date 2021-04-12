import './Header.css'
import React from 'react'
import {connect} from 'react-redux'
import {signOut} from '../actions'
import {Redirect} from 'react-router-dom'


class Header extends React.Component{
    // A lifecycle method. Can someting be done Here
    componentDidMount(){

    }

    
    // This is a must method in React!!
    render(){
        return(
            // So this is how we add colors and stuff to div elements!!
            <div id="header-banner-div">
                <div class="ui secondary pointing menu">
                    <div>
                        <h2>Fantasy</h2>
                    </div>
                    <div class="right menu">
                        <div>{this.props.isSignedIn}</div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Header