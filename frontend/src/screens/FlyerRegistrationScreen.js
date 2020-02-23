import React from 'react'
import { connect } from 'react-redux'
import {
  View,
  Text,
  SafeAreaView,
  Button,
  Picker,
  StyleSheet
} from 'react-native'

// https://facebook.github.io/react-native/docs/picker
const FlyerRegistrationScreen = ({ pendingFlyerCode, removePendingFn }) => (
  <SafeAreaView style={styles.container}>
    <View style={styles.info}>
      <Text style={styles.code}>"{pendingFlyerCode}"</Text>
      <Text style={styles.heading}>Current Building</Text>
      <Picker>
        <Picker.Item label="UMC" />
        <Picker.Item label="Engineering" />
        <Picker.Item label="Norlin" />
        <Picker.Item label="C4C" />
      </Picker>
      <Text style={styles.heading}>Current Floor</Text>
      <Picker>
        <Picker.Item label="2B" />
        <Picker.Item label="1B" />
        <Picker.Item label="1" />
        <Picker.Item label="2" />
      </Picker>
      <Button onPress={removePendingFn} title='Register this flyer' />
    </View>
  </SafeAreaView>
)

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff'
  },
  info: {
    marginLeft: 50,
    marginRight: 50,
    paddingTop: 100
  },
  code: {
    fontSize: 40,
    color: 'black',
    alignSelf: 'center',
    marginBottom: 50,
    fontStyle: 'italic',
  },
  heading: {
    fontSize: 20,
    color: 'gray',
    alignSelf: 'center',
  }
})

const mapStateToProps = (state) => ({
  pendingFlyerCode: state.analytics.pending
})

const mapDispatchToProps = (dispatch) => ({
  removePendingFn: () => dispatch({ type: 'analytics.finishRegistration' })
})

export default connect(mapStateToProps, mapDispatchToProps)(FlyerRegistrationScreen)
