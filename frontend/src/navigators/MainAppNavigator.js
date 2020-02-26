import * as React from 'react'
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs'
import * as Screens from '../screens'
import { Ionicons, FontAwesome } from '@expo/vector-icons'
import Colors from '../Colors'

const BottomTab = createBottomTabNavigator()

const MainAppNavigator = ({ navigation, route }) => (
  <BottomTab.Navigator initialRouteName='Dashboard'
                       tabBarOptions={{showLabel: false}}>
    <BottomTab.Screen
      name='Dashboard'
      component={Screens.Dashboard}
      options={{
        tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} fontAwesome={true} name="align-left" />,
      }}
    />
    <BottomTab.Screen
      name='New Campaign'
      component={Screens.NewCampaign}
      options={{
        tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-add-circle" />,
      }}
    />
    <BottomTab.Screen
      name='Account'
      component={Screens.UserAccount}
      options={{
        tabBarIcon: ({ focused }) => <TabBarIcon focused={focused} name="md-person" />,
      }}
    />
  </BottomTab.Navigator>
)

const TabBarIcon = (props) => (
  React.createElement(props.fontAwesome ? FontAwesome : Ionicons, {
    name: props.name,
    size: 30,
    style: { marginBottom: -3 },
    color: props.focused ? Colors.tabIconSelected : Colors.tabIconDefault
  })
)

export default MainAppNavigator
