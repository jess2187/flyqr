import React, { useState, useRef, useEffect } from 'react'
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
import * as API from '../api'

const Metrics = ({ bestBuilding, totalHits }) => (
  <View>
    <Text>{bestBuilding}</Text>
    <Text>Top Building</Text>
    <Text>{totalHits}</Text>
    <Text>Total Hits</Text>
  </View>
)

const Card = ({ index, item }) => {
  let { dest_url, id, name, thumb_url } = item

  if (!thumb_url) {
    // aww...
    thumb_url = 'http://placekitten.com/200/' + (400 + index * 4)
  }

  return (
    <View style={styles.card}>
      <TouchableHighlight>
      <View style={styles.cardContent}>
        <Image
          style={{width: 300, height: 400, borderTopLeftRadius: 6, borderTopRightRadius: 6 }}
          source={{uri: thumb_url}}/>
        <Text style={{fontSize: 30, padding: 15}}>{name}</Text>
        <Text style={{fontSize: 20, paddingLeft: 15, color: 'gray'}}>({dest_url})</Text>
        <Metrics bestBuilding="Gemmil Math" totalHits={420} />
      </View>
      </TouchableHighlight>
    </View>
  )
}

const { width: vpWidth, height: vpHeight } = Dimensions.get('window')

const CardCarousel = ({ campaigns }) => {
  const carouselRef = useRef()

  return (
    <Carousel
      ref={carouselRef}
      data={campaigns}
      renderItem={Card}
      sliderWidth={vpWidth}
      itemWidth={vpWidth}
    />
  )
}

const DashboardScreen = ({ token, dataIsStale, campaigns }) => {
  useEffect(() => {
    if (dataIsStale) {
      (async () => (await API.getMyCampaigns(token)))()
    }

    for (let c of campaigns) {
      if (!c.flyers) {
        (async () => (await API.getFlyersForCampaign(token, c.camp_id)))()
      }
    }
  })

  return (
    <SafeAreaView style={styles.container}>
      <Text>CU Game Dev Club
      </Text>
      <CardCarousel campaigns={campaigns} />
    </SafeAreaView>
  )
}

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

const mapStateToProps = (state) => ({
  dataIsStale: true, // TODO: we need a good time and reason for when to update the stale data
  campaigns: state.campaigns,
  token: state.auth.token,
})

const mapDispatchToProps = (dispatch) => ({

})

export default connect(mapStateToProps, mapDispatchToProps)(DashboardScreen)
