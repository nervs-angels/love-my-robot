const express = require('express')
const redis = require('redis')
const port = 8080
const app = express()
const publisher = redis.createClient({
    host: 'redis',
    port: 6379
})

//Set initial visits
//publisher.set('visits', 0);


//defining the root endpoint
app.get('/', (req, res) => {
    publisher.publish('request-timestamp', 'noviembre 21');
    res.send("Publishing an Event using Redis");
    // client.get('visits', (err, visits) => {
    //     res.send('Number of visits is: ' + visits)
    //     client.set('visits', parseInt(visits) + 1)
    // })
})

//specifying the listening port
app.listen(port, ()=>{
    console.log(`Example app listening on port ${port}!`)
})