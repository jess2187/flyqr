import React, { useState, useRef } from 'react'
import { connect } from 'react-redux'
import {
  SafeAreaView,
  View,
  Text,
  Dimensions
} from 'react-native'
import Carousel from 'react-native-snap-carousel'

const cards = []
for (let i = 0; i < 100; i++) {
  cards.push({})
}

const Card = ({ index }) => (
  <View style={{margin:50, backgroundColor: 'red'}}><Text style={{fontSize: 20}}>I am a card #{index}</Text></View>
)

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
  <SafeAreaView>
    <Text>Dashboard screen..!</Text>
    <CardCarousel />
  </SafeAreaView>
)

export default connect()(DashboardScreen)
