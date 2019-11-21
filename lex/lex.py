from flask import Flask, request, jsonify, abort
from redis import Redis
import json
import time

app = Flask(__name__)
# redis = Redis(host='redis', port=6379)
# subscriber = redis.pubsub(ignore_subscribe_messages=True)



@app.route("/")
def root():
    # redis.incr('hits')
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')


@app.route("/lex", methods = ['POST'])
def lex():
    # for message in subscriber.listen():
    #     rip = message['channel']
    #     return 'blabla' % rip

    request_body = request.get_json()
    if not request.json or not 'lmr' in request.json:
        abort(400)

    return 201


if __name__ == "__main__":
    # subscriber.subscribe('request-timestamp')
    app.run(host="0.0.0.0", debug=True)
