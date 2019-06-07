import React, {Component} from 'react'
import PropTypes from 'prop-types'

// Decorators
import {bindActionCreators} from 'redux'
import {connect} from 'react-redux'
import {withRouter} from 'react-router-dom'

// Redux Actions
import LabelActions from 'ReduxActions/Label.actions'
import {PENDING, FULFILLED, REJECTED} from 'AppSrc/constants'
import {Card, Col, Row, Alert, Spin, Form, Select, Input, Button} from 'antd'
import Waypoint from 'react-waypoint'

const limit = 20
const FormItem = Form.Item
const Option = Select.Option
const {Meta} = Card
const roa = ['oral', 'topical', 'intravenous', 'dental', 'respiratory', 'ophthalmic', 'intramuscular', 'subcutaneous', 'nasal', 'rectal']

class Home extends Component {
  constructor(){
    super()

    this._loadMoreItems = this._loadMoreItems.bind(this)
    this._renderItems = this._renderItems.bind(this)
    this._renderWaypoint = this._renderWaypoint.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.state = {
      items: [],
      isLoading: false,
      skip: 0,
      search: {}
    }
  }

  handleSubmit(e){
    e.preventDefault()
    this.props.form.validateFields(async (err, values) => {
      if (!err) {
        this.setState({
          isLoading: true,
          items: [],
          skip: 0,
          search: values
        })

        await this.props.getLabels(
          Object.assign(values, {
            skip: 0,
            limit: limit
          }))

        if (this.props._getLabels.status === FULFILLED) {
          let currentItems = this.state.items
          let results = this.props._getLabels.payload.data.results
          results.forEach(row => {
            if (row.openfda.brand_name && row.openfda.generic_name) {
              currentItems.push(row)
            }
          })
    
          this.setState({
            items: currentItems,
            isLoading: false
          })
        }
      }
    })
  }

  async _loadMoreItems() {
    this.setState({
      isLoading: true,
      skip: this.state.skip + 10
    })

    await this.props.getLabels(Object.assign(this.state.search, {
        skip: this.state.skip,
        limit: limit
      }))

    if (this.props._getLabels.status === FULFILLED) {
      let currentItems = this.state.items
      let results = this.props._getLabels.payload.data.results
      results.forEach(row => {
        if (row.openfda.brand_name && row.openfda.generic_name) {
          currentItems.push(row)
        }
      })

      this.setState({
        items: currentItems,
        isLoading: false
      })
    }
  }

  _renderItems() {
    return this.state.items.map(row => {
      return (
        <Col span={8} key={row.id}>
          <Card style={{minHeight: '300px', marginBottom: '10px'}} title={'Brand Name: ' + row.openfda.brand_name}>
            <p><strong>Generic Name:</strong> {row.openfda.generic_name}</p>
            <p><strong>Brand Name:</strong> {row.openfda.brand_name}</p>
            <p><strong>Product Type:</strong> {row.openfda.product_type}</p>
            <p><strong>Route of Administration:</strong> {row.openfda.route}</p>
            <p><strong>Purpose:</strong> {row.purpose}</p>
            <p><strong>Indication and Usage:</strong> {row.indications_and_usage}</p>
            <p><strong>Warnings:</strong> <span style={{color: 'red'}}>{row.warnings}</span></p>
            <p><strong>Active Ingredients:</strong> {row.active_ingredient}</p>
            <p><strong>Inactive Ingredient:</strong> {row.inactive_ingredient}</p>
            <p><strong>Storage and Handling:</strong> {row.storage_and_handling}</p>
          </Card>            
        </Col>    
      )
    })
  }

  _renderWaypoint() {
    if (!this.state.isLoading) {
      return (
        <Waypoint
          onEnter={this._loadMoreItems}
        />
      )
    }
  }

  render() {
    const {getFieldDecorator} = this.props.form
    return (
      <Row>
        <Col span={24}>
          <Form onSubmit={this.handleSubmit} className='login-form'>
            <Row>
              <Col span={12}>
                <FormItem>
                  {getFieldDecorator('generic_name', {
                    rules: [],
                  })(
                    <Input placeholder='Filter by Generic Name' />
                  )}
                </FormItem>
                <FormItem>
                  {getFieldDecorator('brand_name', {
                    rules: [],
                  })(
                    <Input placeholder='Filter by Brand Name' />
                  )}
                </FormItem>
              </Col>
              <Col span={12}>
                <FormItem style={{marginLeft: '10px'}}>
                  {getFieldDecorator('route', {
                    rules: [],
                  })(
                    <Select placeholder='Route of Administration'>
                      <For each='item' index='key' of={roa}>
                        <Option value={item} key={key}>{item}</Option>
                      </For>
                    </Select>
                  )}                  
                </FormItem>
                <FormItem style={{marginLeft: '10px'}}>
                  <Button type='primary' htmlType='submit'>
                    Search
                  </Button>
                </FormItem>                
              </Col>
            </Row>
          </Form>
        </Col>
        <Col span={24}>
          <div className='infinite-scroll-example'>
            <div className='infinite-scroll-example__scrollable-parent'>
              <Row gutter={16} type='flex'>
                {this._renderItems()}
                <If condition={this.props._getLabels.status === PENDING}>
                  <For each='item' index='key' of={[1, 2, 3]}>
                    <Col key={key} span={8}>
                      <Card style={{minHeight: '300px', marginBottom: '10px'}} loading={this.state.isLoading}>                    
                        <Meta
                          title='Loading...'
                          description='Loading...'
                        />
                      </Card>
                    </Col>
                  </For>
                  <Col span={24}>
                    <Spin>
                      <Alert message='Loading...' type='warning' showIcon />
                    </Spin>
                  </Col>              
                </If>
                <If condition={this.props._getLabels.status === REJECTED}>
                  <Col span={24}>
                    <Alert  message='No more products to display”' type='warning' showIcon />
                  </Col>
                </If>
              </Row>
              <div className='infinite-scroll-example__waypoint'>
                {this._renderWaypoint()}
              </div>
            </div>
            <p className='infinite-scroll-example__arrow' />
          </div>
        </Col>
      </Row>
    )
  }
}

// Map all redux reducers to current class
const mapState = state => {
  return {
    _getLabels: state._getLabels
  }
}

// Map all redux actions to current class
const mapDispatch = dispatch => {
  return bindActionCreators({
    getLabels: LabelActions.getLabels
  }, dispatch)
}

Home.propTypes = {
  getLabels: PropTypes.func.isRequired,
  _getLabels: PropTypes.object.isRequired,
  form: PropTypes.object.isRequired
}

export default connect(
  mapState,
  mapDispatch
)(withRouter(Form.create()(Home)))
