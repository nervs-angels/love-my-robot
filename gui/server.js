const express = require('express');
const exphbs = require('express-handlebars');
const path = require('path');
var bodyParser = require('body-parser');
const methodOverride = require('method-override')
const redis = require('redis')

//define port
const port = 8080;

//init app
const app = express();

//
app.use(express.static('public'))

//view engine
app.engine('handlebars',exphbs({defaultLayout: 'main'}));
app.set('view engine', 'handlebars');

//body-parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

//method-override
app.use(methodOverride('_method'));

app.get('/', function(req,res,next){
    res.render('code')
});



app.listen(port,function(){
    console.log(`server started on port ${port}`)
});

