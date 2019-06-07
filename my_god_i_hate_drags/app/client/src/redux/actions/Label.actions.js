import axios from 'axios'
import {GET_LABELS} from '../../constants'

/**
@description Get User
@param params
*/
const getLabels = params => {
  return {
    type: GET_LABELS,
    payload: axios.get(`/api/label`, {params: params})
  }
}


export default {
  getLabels
}
