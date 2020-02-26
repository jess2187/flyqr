import React, { useState, useEffect } from 'react'
import { StyleSheet, View, Linking } from 'react-native'
import { registerRootComponent, SplashScreen } from 'expo'
import { NavigationContainer } from '@react-navigation/native'
import { Provider } from 'react-redux'
import Store from './Store'
import * as Navigators from './navigators'

const App = (props) => {
  const [isLoadingComplete, setLoadingComplete] = useState(false)

  useEffect(() => {
    const loadResourcesAndDataAsync = async () => {
      try {
        SplashScreen.preventAutoHide()
      } catch (e) {
        console.warn(e)
      } finally {
        setLoadingComplete(true)
        SplashScreen.hide()
      }
    }

    loadResourcesAndDataAsync()

    Linking.addEventListener('url', handleLinkIntoApp)

    return () => {
      Linking.removeEventListener('url', handleLinkIntoApp)
    }
  })

  if (!isLoadingComplete && !props.skipLoadingScreen) {
    return null
  }

  return (
    <Provider store={Store}>
      <View style={styles.container}>
        <NavigationContainer>
          <Navigators.Root />
        </NavigationContainer>
      </View>
    </Provider>
  )
}

const handleLinkIntoApp = ({ url }) => {

  /* TODO: Clean up this mess and properly parse the url.
   *
   * Here we assume the url looks like:
   *
   *   exp://exp.host/@evanram/flyqr?code=s3cr3tc0d3
   */

  const code = url.split('?')[1].split('=')[1]
  Store.dispatch({ type: 'analytics.registerFlyer', code })
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff'
  }
})

registerRootComponent(App)
