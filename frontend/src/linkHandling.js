import store from './store'

export const handleLinkIntoApp = ({ url }) => {
  // hacky...
  // exp://exp.host/@evanram/flyqr?code=s3cr3tc0d3
  const code = url.split('?')[1].split('=')[1]
  store.dispatch({ type: 'analytics.registerFlyer', code })
}
