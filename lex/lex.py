from flask import Flask, request, jsonify, abort
import cozmo
import inspect
import importlib

# from redis import Redis


app = Flask(__name__)


class State:
    def __init__(self):
        self.ts_file = 'lmr_lex_2019_11_3-11_18'
        self.ts_display = ''
        self.procedure = []


# redis = Redis(host='redis', port=6379)
# subscriber = redis.pubsub(ignore_subscribe_messages=True)
state = State()


def foo(arg1, arg2):
    # do something with args
    a = arg1 + arg2
    return a


lines = inspect.getsource(State)
print(lines)
print(type(lines))


def program(robot: cozmo.robot.Robot):
    robot.say_text("that's hot!!!").wait_for_completed()


cozmo.run_program(program)

transpiled_module = importlib.import_module('.' + state.ts_file, package='transpiled')
cozmo.run_program(transpiled_module.program_test())


@app.route("/")
def root():
    # redis.incr('hits')
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    return 'hola soy grut'


@app.route("/lex", methods=['POST'])
def lex():
    # for message in subscriber.listen():
    #     rip = message['channel']
    #     return 'blabla' % rip

    request_body = request.get_json()
    if not request.json or not 'lmr' in request.json:
        abort(400)
    preprocess(request_body)
    process()
    execute()
    return 201


if __name__ == "__main__":
    # subscriber.subscribe('request-timestamp')
    app.run(host="0.0.0.0", debug=True)
