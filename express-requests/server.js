const express = require('express');
const cors = require('cors');

const app = express();
app.use(cors());

const axios = require('axios');
const fs = require('fs');
const path = require('path');
const FormData = require("form-data");

app.get('', async (req, res) => {

    console.log('sending request from requests server')
    const form = new FormData();
    const stream = fs.createReadStream(__dirname + '/image.jpeg');
    form.append('image', stream);
    const formHeaders = form.getHeaders();

    axios.post('http://flask-classifier:5000/predict', form, {
        headers: {
            ...formHeaders,
        },
    })
        .then(resp => { res.status(200).json(resp.data) })
        .catch(error => { console.log(error.code) })
})

module.exports = app;
