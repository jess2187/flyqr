import { createStore, combineReducers } from 'redux'

const preloadedState = {
  auth: {},
  campaigns: [],
  analytics: {},
}

const auth = (state = {}, action) => {
  switch (action.type) {
    case 'auth.login':
      return { ...state, email: action.email, token: action.token }
    case 'auth.logout':
      return { ...state, email: null, token: null }
  }

  return state
}

const campaigns = (state = [], action) => {
  switch (action.type) {
    case 'campaigns.overwrite':
      return [...action.campaigns]
    case 'campaigns.add':
      return [...state, action.campaign]
  }

  return state
}

const analytics = (state = {}, action) => {
  switch (action.type) {
    case 'analytics.registerFlyer':
      return { ...state, pending: action.code }
    case 'analytics.finishRegistration':
      return { ...state, pending: null }
  }

  return state
}

const reducer = combineReducers({ auth, campaigns, analytics })

export default createStore(reducer, preloadedState)
