import {createReducer} from '../../helpers/redux'
import {GET_LABELS} from '../../constants'

/**
 * @description Label Reducers
 * @param state action 
 */
export const _getLabels = (state, action) => createReducer(GET_LABELS, state, action)
