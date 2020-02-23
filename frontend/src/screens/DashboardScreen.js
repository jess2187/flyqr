import React, { useState, useRef } from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text,
  Dimensions,
  StyleSheet,
  Image,
  TouchableHighlight
} from 'react-native'
import Carousel from 'react-native-snap-carousel'

const cards = []
for (let i = 0; i < 100; i++) {
  cards.push({})
}

// const Touchables = ({}) =>{
// // export default class Touchables extends Component {
//   _onPressButton() (
//     alert('You tapped the button!')
//   );

//   _onLongPressButton() (
//     alert('You long-pressed the button!')
//   }
// }

const Card = ({ index }) => {
  return (

    <View style={styles.card}>
      <TouchableHighlight>
      <View style={styles.cardContent}>
        <Image
          style={{width: 300, height: 400, borderTopLeftRadius: 6, borderTopRightRadius: 6 }}
          source={{uri: 'https://3.bp.blogspot.com/-9Fj2BdwXHt8/WnC4baujJHI/AAAAAAAAANk/ogxyp4n0disNkFq59YrOO1lMfiYEXrFRwCK4BGAYYCw/s1600/IMG_5999.jpg'}}/>
        <Text style={{fontSize: 30, padding: 15}}>Flyer  #{index}</Text>
        <Text style={{fontSize: 20, paddingLeft: 15}}>Number of locations: # </Text>
        <Text style={{fontSize: 20, paddingLeft: 15}}>Number of scans: # </Text>
      </View>
      </TouchableHighlight>
    </View>

  )
}



const { width: vpWidth, height: vpHeight } = Dimensions.get('window')

const CardCarousel = (props) => {
  const carouselRef = useRef(null)
  const renderCard = Card

  return (

      <Carousel
        ref={carouselRef}
        data={cards}
        renderItem={renderCard}
        sliderWidth={vpWidth}
        itemWidth={vpWidth}
      />
  )
}

const DashboardScreen = (props) => (
  <SafeAreaView style={styles.container}>
    <Text >CU Game Dev Club
    </Text>
    <CardCarousel />

  </SafeAreaView>
)



export default connect()(DashboardScreen)


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    // alignItems: 'center',
    justifyContent: 'center'
  },
  card: {
    flex: 1,
    margin: 50,
    width: 300,
    alignSelf: 'center',
    // padding:50,
    backgroundColor: 'white',
    borderRadius: 6,
    shadowOffset: {width: 3, height: 3},
    shadowColor: 'black',
    shadowOpacity: 0.3
  },
  cardContent: {
    //  width: 300,
    //  height: 650,
    // backgroundColor: 'blue'
    // padding: 50,
    // alignItems: 'center',
  }
});
