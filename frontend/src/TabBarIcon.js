import React from 'react'
import { Ionicons, FontAwesome } from '@expo/vector-icons'
import Colors from './colors'

const TabBarIcon = (props) => {
  const component = props.fontAwesome ? FontAwesome : Ionicons

  return (
    React.createElement(component, {
      name: props.name,
      size: 30,
      style: { marginBottom: -3 },
      color: props.focused ? Colors.tabIconSelected : Colors.tabIconDefault
    })
  )
}

export default TabBarIcon
