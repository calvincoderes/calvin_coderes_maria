import React from 'react'
import PropTypes from 'prop-types'
import {Layout} from 'antd'

const {Content} = Layout

export const lhoc = WrappedComponent => {
    return class LHOC extends React.Component {  
      render() {
        return (
          <Layout>
            <Content style={{padding: '0 50px'}}>
              <Layout style={{padding: '24px 0', background: '#fff'}}>
                <Content style={{padding: '0 24px', minHeight: 280}}>
                  <WrappedComponent {...this.props} />
                </Content>
              </Layout>
            </Content>
          </Layout>
        )
      }
    }
}


// Static Typing using PropTypes
lhoc.propTypes = {
  WrappedComponent: PropTypes.any
}
