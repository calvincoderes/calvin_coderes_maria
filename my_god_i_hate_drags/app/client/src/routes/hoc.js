import React from 'react'
import PropTypes from 'prop-types'
import {Route} from 'react-router-dom'

// TEMPORARY
let isLoggedIn = true

// Restricted Route for Authentication
export const PrivateRoute = ({component: Component, ...rest}) => {
  return (
    <Route
      {...rest}
      render={props => {
        return (
          <If condition={isLoggedIn}>
            <Component {...props} />
          </If>
        )
      }}
    />
  )
}

// Static Typing using PropTypes
PrivateRoute.propTypes = {
  component: PropTypes.func.isRequired
}
