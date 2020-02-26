import React, { useState } from 'react'
import { connect } from 'react-redux'
import { createStackNavigator } from '@react-navigation/stack'
import * as Screens from '../screens'
import MainAppNavigator from './MainAppNavigator'

const getRootScreen = (isAuthenticated, pendingFlyerCode) => {
  if (!isAuthenticated) {
    return {
      name: 'Auth',
      component: Screens.LoginAndRegistration
    }
  }

  if (pendingFlyerCode) {
    return {
      name: 'FlyerRegister',
      component: Screens.FlyerRegistration
    }
  }

  return {
    name: 'MainApp',
    component: MainAppNavigator
  }
}

const Stack = createStackNavigator()

const RootNavigator = ({ isAuthenticated, pendingFlyerCode }) => {
  const { name, component } = getRootScreen(isAuthenticated, pendingFlyerCode)

  return (
    <Stack.Navigator headerMode='none'>
      <Stack.Screen name={name} component={component} />
    </Stack.Navigator>
  )
}

const mapStateToProps = (state) => ({
  isAuthenticated: !!state.auth.token,
  pendingFlyerCode: state.analytics.pending
})

export default connect(mapStateToProps)(RootNavigator)
