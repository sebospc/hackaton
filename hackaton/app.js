const express = require("express");
const bodyParser = require('body-parser');
const app = express();


app.use(express.static('public'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));



app.get('/', function (req, res) {
    res.sendFile(__dirname + "/public/login.html")
})

app.listen(3000);

module.exports = app