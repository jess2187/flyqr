import store from './store'

const API_URL = 'https://881c6e7a.ngrok.io' //'https://flyqr.xyz'

const send = async (method, endpoint, params) => {
  let query = []

  for (let p in params) {
    if (params.hasOwnProperty(p)) {
      query.push(encodeURIComponent(p) + '=' + encodeURIComponent(params[p]))
    }
  }

  try {
    const resp = await fetch(API_URL + endpoint + '?' + query.join('&'), {
      method,
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json'
      }
    })


    const body = await resp.json()

    return { body, status: resp.status }
  } catch (e) {
    // No Content (204) responses were causing errors so lets just hack this
    // away....!
    return { clientError: e, status: 204 /* lol */ }
  }
}

// POST /auth/register
export const register = async (name, email, password) => {
  const res = await send('POST', '/auth/register', { name, email, password })
  return res.status == 204
}

// POST /auth/login
export const login = async (email, password) => {
  const res = await send('POST', '/auth/login', { email, password })

  if (res.status == 200) {
    store.dispatch({ type: 'auth.login', email, ...res.body })
  } else {
    alert('Bad login.')
  }
}

// POST /auth/logout
export const logout = async (token) => {
  const res = await send('POST', '/auth/logout', { token })

  if (res.status == 204) {
    store.dispatch({ type: 'auth.logout' })
  }
}

// GET /tags/list
export const getMatchingTags = (query) => {
  const res = send('GET', '/tags/list', { query })
}

// GET /tags/self
export const getMyTags = (token) => {
  const res = send('GET', '/tags/self', { token })
}

// POST /campaigns/new
export const createCampaign = (token, payload, qr_horiz, qr_vert, width, height, camp_name, dest_url) => {
  // TODO this one is kinda tricky
}

// GET /campaigns/list
export const getMyCampaigns = async (token) => {
  const res = await send('GET', '/campaigns/list', { token })

  if (res.status == 200) {
    store.dispatch({ type: 'campaigns.overwrite', campaigns: res.body.campaigns })
  }
}

// GET /campaigns/flyers
export const getFlyersForCampaign = (token, camp_id) => {
  const res = send('GET', '/campaigns/flyers', { token, camp_id })

  if (res.status == 200) {
    store.dispatch({ type: 'campaigns.getFlyers', camp_id, ...res.body })
  }
}

// POST /jobs/new
export const enqueueQrCodeGenJob = (token, n, camp_id) => {
  const res = send('POST', '/jobs/new', { token, n, camp_id })
}

// GET /jobs/status
export const getJobStatus = (token, job_id) => {
  const res = send('GET', '/jobs/status', { token, job_id })
}
