import React from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text
} from 'react-native'

const DashboardScreen = (props) => (
  <SafeAreaView>
    <Text>Dashboard screen..!</Text>
  </SafeAreaView>
)

export default connect()(DashboardScreen)
