import React from 'react'
import { connect } from 'react-redux'
import { createStackNavigator } from '@react-navigation/stack';
import LoginAndRegistrationScreen from './screens/LoginAndRegistrationScreen'
import FlyerRegistrationScreen from './screens/FlyerRegistrationScreen'
import BottomTabNavigator from './BottomTabNavigator'

const Stack = createStackNavigator()

// TODO: really shouldn't be a stack nav, but this is a hackathon and i dont
// care... it works
// also pendingFlyerCode needs to be moved to somewhere else... or we call this
// component something else. who knows.
const AuthEnforcedNavigator = ({ isAuthenticated, pendingFlyerCode }) => {
  let screen

  if (!isAuthenticated) {
    screen = <Stack.Screen name="Auth" component={LoginAndRegistrationScreen} />
  } else if (pendingFlyerCode) {
    screen = <Stack.Screen name="FlyerRegister" component={FlyerRegistrationScreen} />
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
  isAuthenticated: !!state.auth.token,
  pendingFlyerCode: state.analytics.pending
})

export default connect(mapStateToProps)(AuthEnforcedNavigator)
