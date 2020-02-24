import React, { useRef, useState } from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text,
  Button,
  TouchableOpacity,
  StyleSheet,
  TextInput
} from 'react-native'
import * as API from '../api'

// NOTE: do not look at this code please
const LoginAndRegistrationScreen = ({ doFakeLogin }) => {
  const [flipState, setFlipState] = useState('registration')
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [disabled, setDisabled] = useState(false)

  const changeViews = () => {
    if (flipState == 'registration') {
      setFlipState('login')
    } else {
      setFlipState('registration')
    }
  }

  const submit = async () => {
    if ((flipState == 'registration' && !name) || !email || !password) {
      alert('Please provide your credentials.')
      return
    }

    if (flipState == 'registration') {
      await API.register(name, email, password)
    }

    API.login(email, password)
  }

  let title, opposite
  if (flipState == 'registration') {
    title = 'Register'
    opposite = 'Sign in'
  } else {
    title = 'Sign in'
    opposite = 'Register'
  }

  return (
    <SafeAreaView disabled={disabled} style={styles.container}>
      <View>
        <Text style={styles.header}>{title}</Text>
        { flipState == 'registration' &&
            <TextInput onChangeText={setName} style={styles.field} placeholder="Organization Name" />
        }
        <TextInput onChangeText={setEmail} style={styles.field} placeholder="Email" />
        <TextInput onChangeText={setPassword} secureTextEntry={true} style={styles.field} placeholder="Password" />
        <Button style={styles.performAction} onPress={submit} title="Submit" />
        <Button onPress={changeViews} title={'or, '+opposite.toLowerCase()} />
      </View>
    </SafeAreaView>
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'white',
    justifyContent: 'center',
  },
  header: {
    alignSelf: 'center',
    fontSize: 50,
  },
  field: {
    alignSelf: 'center',
    marginLeft: 50,
    marginRight: 50,
    marginTop: 30,
    marginBottom: 10,
    borderColor: 'gray',
    borderWidth: 1,
    borderRadius: 10,
    padding: 10,
    alignSelf: 'stretch',
  },
  performAction: {
    borderColor: 'gray',
    borderWidth: 2,
    borderRadius: 10,
    padding: 10,
  },
})

export default LoginAndRegistrationScreen
