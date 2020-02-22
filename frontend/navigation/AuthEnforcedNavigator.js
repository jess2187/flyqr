import React from 'react'
import { connect } from 'react-redux'
import { createStackNavigator } from '@react-navigation/stack';
import LoginAndRegistrationScreen from '../screens/LoginAndRegistrationScreen'
import BottomTabNavigator from './BottomTabNavigator'

const Stack = createStackNavigator()

// TODO: really shouldn't be a stack nav, but this is a hackathon and i dont
// care... it works
const AuthEnforcedNavigator = ({ isAuthenticated }) => {
  let screen

  if (!isAuthenticated) {
    screen = <Stack.Screen name="Auth" component={LoginAndRegistrationScreen} />
  } else {
    screen = <Stack.Screen name="MainApp" component={BottomTabNavigator} />
  }

  return (
    <Stack.Navigator headerMode='none'>
      {screen}
    </Stack.Navigator>
  )
}

const mapStateToProps = (state, ownProps) => ({
  isAuthenticated: !!state.auth.token
})

export default connect(mapStateToProps)(AuthEnforcedNavigator)
