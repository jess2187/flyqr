const API_URL = 'https://flyqr.xyz'

const send = (method, endpoint, params) => {
  let query = []

  for (let p in params) {
    if (params.hasOwnProperty(p)) {
      query.push(encodeURIComponent(p) + '=' + encodeURIComponent(params[p]))
    }
  }

  return fetch(API_URL + endpoint + '?' + query.join('&'), {
    method,
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json'
    }
  })
}

// POST /auth/register
export const register = (email, password) => {
  const res = send('POST', '/auth/register', { email, password })
}

// POST /auth/login
export const login = (email, password) => {
  const res = send('POST', '/auth/login', { email, password })
}

// POST /auth/logout
export const logout = (token) => {
  const res = send('POST', '/auth/logout', { token })
}

// GET /tags/list
export const getMatchingTags = (query) => {
  const res = send('GET', '/tags/list', { query })
}

// GET /tags/self
export const getMyTags = (token) => {

}

// POST /campaigns/new
export const createCampaign = (token, payload, qr_horiz, qr_vert, width, height, camp_name, dest_url) => {}

// GET /campaigns/list
export const getMyCampaigns = (token) => {}

// GET /campaigns/flyers
export const getFlyersForCampaign = (token, camp_id) => {}

// POST /jobs/new
export const enqueueQrCodeGenJob = (token, n, camp_id) => {}

// GET /jobs/status
export const getJobStatus = (token, job_id) => {}
