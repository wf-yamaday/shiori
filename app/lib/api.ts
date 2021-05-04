import axios, { AxiosResponse } from 'axios'

const BASE_URL = process.env.API_URL || 'http://localhost:5000'

export async function getOGP(url: string) {
  if(url === '') return Promise.resolve({});
  return axios.get(`https://us-central1-shiori-dev-160df.cloudfunctions.net/getOgp?url=${url}`)
  .then((res) => { console.log('[info]', res.data); return res.data; })
  .catch((err) => { return Promise.reject(err) })
}

export async function getAllBookmarksAsync() {
  return axios.get(`${BASE_URL}/bookmarks`)
  .then((res: AxiosResponse<any>) => { return res.data })
  .catch((err: AxiosResponse<any>) => { return Promise.reject(err) })
}

export async function getBookmarkByIdAsync(id: number) {
  return axios.get(`${BASE_URL}/bookmarks/${id}`)
  .then((res: AxiosResponse<any>) => { return res.data })
  .catch((err: AxiosResponse<any>) => { return Promise.reject(err) })
}
