import * as React from 'react';
import { ScrollView } from 'react-native-gesture-handler';
import {
  StyleSheet,
  Text,
  SafeAreaView,
  View
} from 'react-native';

const NewCampaignScreen = () => (
  <ScrollView>
    <SafeAreaView>
      <Text style={{fontSize: 30, padding: 15}}>
        This is the screen where you create a new campaign.
        Yay!
      </Text>
    </SafeAreaView>
  </ScrollView>
)

export default NewCampaignScreen
