import React from 'react'
import {BrowserRouter as Router, Route, Switch} from 'react-router-dom'
import {PrivateRoute} from './hoc'
import {lhoc} from '../components/layout/index'
import NotFound from '../components/common/NotFound'
import Home from '../components/modules/Home/index'


// Render Routes
export default () => {
  return (
    <Router>
      <Switch>
        <PrivateRoute exact path='/' component={lhoc(Home)} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  )
}
