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

hbs = exphbs.create({
    defaultLayout: 'main',

    //custom helpers
    helpers: {
        json: function(obj) {
            return new Handlebars.SafeString(JSON.stringify(obj))
         }
    }
});

//view engine
app.engine('handlebars',hbs.engine);
app.set('view engine', 'handlebars');

//body-parser
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended:false}));

//method-override
app.use(methodOverride('_method'));

//commands to be sent to LEX
app.get('/', function(req,res,next){
    res.render('code')
});



app.listen(port,function(){
    console.log(`server started on port ${port}`)
});



