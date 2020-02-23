import * as React from 'react';
import { ScrollView } from 'react-native-gesture-handler';
import {
  StyleSheet,
  Text,
  SafeAreaView,
  View, 
  Button
} from 'react-native';

const NewCampaignScreen = () => (
  <SafeAreaView>
    <View>
    <Text style={{fontSize: 30, padding: 15}}>
      This is the screen where you create a new campaign.
      Yay!
    </Text>
    </View>
    <View style={{alignSelf: 'center', justifyContent: 'flex-end'}}>
    <Button
          title="Upload"
          style = {{paddingRight: 15, backgroundColor:'blue'}}
          // color = 'powderblue'
          // onPress={() => Alert.alert('Simple Button pressed')}
        />
        </View>
    
  </SafeAreaView>
)

export default NewCampaignScreen

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