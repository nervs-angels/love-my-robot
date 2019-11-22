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


def preprocess(request_body):
    preprocess_ts(request_body)
    preprocess_procedure(request_body)


def preprocess_ts(request_body):
    pass


def preprocess_procedure(request_body):
    pass


def process():
    text = transpile(state.procedure)
    export(text)


def transpile(procedure_array):
    text = ""
    text += "import cozmo\n\n\ndef program(robot: cozmo.robot.Robot):"
    for command in procedure_array:
        if command == "SAY":
            pass
        elif command == "MATH":
            pass
        elif command == "COUNT":
            pass
        elif command == "YES":
            pass
        elif command == "SOUND":
            pass
        elif command == "DRIVE_OFF":
            pass
        elif command == "MOVE":
            pass
        elif command == "TURN":
            pass
        elif command == "LIFT":
            pass
        elif command == "LIGHTS":
            pass
        elif command == "ANIMATION":
            pass
        elif command == "CUBE_LIGHT":
            pass
        elif command == "PICKUP_CUBE":
            pass
        elif command == "DROP_CUBE":
            pass
        elif command == "ROLL_CUBE":
            pass
        elif command == "WHEELIE":
            pass
    text += "\n\n\ncozmo.run_program(program)"
    return text


def export(text):
    pass


def execute():
    transpiled_module = importlib.import_module('.' + state.ts_file, package='transpiled')
    cozmo.run_program(transpiled_module.program())


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
