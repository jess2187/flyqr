import React from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text,
  Button
} from 'react-native'

const LoginAndRegistrationScreen = ({ doFakeLogin }) => (
  <SafeAreaView>
    <Text>Login and Registration Screen</Text>
    <Button onPress={doFakeLogin} title='Login' />
  </SafeAreaView>
)

const mapDispatchToProps = (dispatch) => ({
  doFakeLogin: () => dispatch({
      type: 'auth.login',
      email: 'foo@example.com',
      token: 'ey-this-token-is-fake'
    })
})

export default connect(null, mapDispatchToProps)(LoginAndRegistrationScreen)
