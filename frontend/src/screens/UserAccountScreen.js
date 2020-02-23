import React from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text,
  StyleSheet,
  Button
} from 'react-native'
import * as API from '../api'

const UserAccountScreen = (props) => (
  <SafeAreaView style={styles.container}>
    <View style ={{alignItems: 'flex-end', paddingRight:10}}>
    <Button
          title="Logout"
          style = {{paddingRight: 15, alignSelf: 'flex-end', backgroundColor:'blue'}}
          onPress={async () => await API.logout()}
      
        />
    </View>
    <View style={styles.info}>
      <Text style={{fontSize: 40, paddingBottom: 20, alignSelf: 'center',}}>Organization Info</Text>

      <Text style={{fontSize: 20, color: 'gray'}}>Organization Name</Text>
      <Text style={{fontSize: 25, paddingBottom: 10}}>CU Game Dev Club</Text>

      <Text style={{fontSize: 20, color: 'gray'}}>Organization Email</Text>
      <Text style={{fontSize: 25, paddingBottom: 10}}>cugamedev@colorado.edu</Text>

      <Text style={{fontSize: 20, color: 'gray'}}>Number of Campaigns</Text>
      <Text style={{fontSize: 25, paddingBottom: 10}}>5</Text>

      <Text style={{fontSize: 20, color: 'gray'}}>Number of Total Scans</Text>
      <Text style={{fontSize: 25, paddingBottom: 10}}>62</Text>
    </View>

  </SafeAreaView>
)

const mapStateToProps = (state) => ({
  pendingFlyerCode: state.analytics.pending
})

export default connect(mapStateToProps)(UserAccountScreen)

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // alignItems: 'center',
    //justifyContent: 'center'
  },
  info: {

    // marginLeft: 5,
    // marginLeft: 5,
    // width: 300,
    alignSelf: 'center',
    paddingTop:100,
    // backgroundColor: 'powderblue',
    // borderRadius: 6,
    // alignItems: 'center',


  },
  cardContent: {
    //  width: 300,
    //  height: 650,
    // backgroundColor: 'blue'
    // padding: 50,
    // alignItems: 'center',
  }
});
