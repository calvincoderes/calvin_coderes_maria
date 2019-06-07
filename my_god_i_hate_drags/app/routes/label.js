const express = require('express')

// API
const {callApi} = require('../libraries/Api')
const {LabelEndpoint} = require('../endpoints/fda')

// Libraries
const multer = require('../libraries/Multer')
const util = require('util')

// Library Configurations
const router = express.Router()
const noUploadForm = multer.multerFields()

// Route Middlewares
router.use(noUploadForm)

// Get users
router.get('/', async(req, res, next) => {
  try {
    // Query Strings
    let qs = {
      skip: Number(req.query.skip),
      limit: Number(req.query.limit)
    }

    let filter = []
    if ('generic_name' in req.query) {
      filter.push('openfda.generic_name:"' + req.query.generic_name + '"')
    }
    if ('brand_name' in req.query) {
      filter.push('openfda.brand_name:"' + req.query.brand_name + '"')
    }
    if ('route' in req.query) {
      filter.push('openfda.route:"' + req.query.route + '"')
    }

    // API Call
    const results = await callApi({
      method: 'GET',
      url: LabelEndpoint.GetAll + '?search=' + filter.join('+AND+'),
      qs: qs,
      json: true,
      headers: {
        Accept: 'application/json'
      }
    })
  
    res.status(results.statusCode).json(results)
  } catch (e) {
    let err = new Error(e)
    err.status = 500
    next(err)
  }
})

module.exports = router
