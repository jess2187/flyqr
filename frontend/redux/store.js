import { createStore, combineReducers } from 'redux'

const preloadedState = {
  auth: {
  },
  campaigns: []
}

const auth = (state = {}, action) => {
  switch (action.type) {
    case 'auth.login':
      return { ...state, email: action.email, token: action.token }
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

const reducer = combineReducers({ auth, campaigns })

export default createStore(reducer, preloadedState)
