import {combineReducers} from 'redux'
import {reducer as form} from 'redux-form'

/* Reducers */
import * as Label from './Label.reducers'

const reducers = combineReducers({
  // 3rd Party Reducers
  form,
  // App Reducers
  ...Label
})
1
export default reducers
