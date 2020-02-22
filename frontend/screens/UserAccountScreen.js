import React from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text
} from 'react-native'

const UserAccountScreen = (props) => (
  <SafeAreaView>
    <Text>This is the user account screen!!</Text>
  </SafeAreaView>
)

export default connect()(UserAccountScreen)
