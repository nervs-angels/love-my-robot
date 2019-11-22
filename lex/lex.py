from flask import Flask, request, jsonify, abort, render_template
import cozmo
import inspect
import importlib
import json
import os.path
import os

# from redis import Redis


app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'
json_dummy = {"request_timestamp": "Sun Nov  3 01:42:41 CST 2019",
              "lmr": ["SAY,HI", "MOVE,50,100", "SAY,POO", "CUBE_LIGHT"]}


class State:
    def __init__(self):
        self.ts_file = 'lmr_lex_2019_11_3-11_18'
        self.ts_display = ''
        self.procedure = []


# redis = Redis(host='redis', port=6379)
# subscriber = redis.pubsub(ignore_subscribe_messages=True)
state = State()


# def foo(arg1, arg2):
#     # do something with args
#     a = arg1 + arg2
#     return a
#
#
# lines = inspect.getsource(State)
# print(lines)
# print(type(lines))


def program(robot: cozmo.robot.Robot):
    robot.say_text("that's hot!!!").wait_for_completed()


# cozmo.run_program(program)
#
# transpiled_module = importlib.import_module('.' + state.ts_file, package='transpiled')
# cozmo.run_program(transpiled_module.program_test())


def preprocess(request_body):
    preprocess_ts(request_body)
    preprocess_procedure(request_body)


def preprocess_ts(request_body):
    request_timestamp = request_body['request_timestamp']
    year= request_timestamp[-4:] 
    request_timestamp=request_timestamp[:-4]
    state.ts_display = request_timestamp
    print('preprocess_ts\n' + state.ts_display)
    request_timestamp = "lmr_lex" + request_timestamp + ".py"
    request_timestamp=request_timestamp.replace("Sun"," "+year).replace("Mon"," "+year).replace("Tue"," "+year).replace("Wed"," "+year).replace("Thu"," "+year).replace("Fri"," "+year).replace("Sat"," "+year)
    request_timestamp = request_timestamp.replace("CST", "").replace(":", "-").replace(" ", '_')
    request_timestamp = request_timestamp.replace('Jan', '1').replace("Feb", "2").replace("Mar", "3").replace("Apr",
                                                                                                              "4").replace(
        "May", "5").replace("Jun", "6").replace("Jul", "7").replace("Aug", "8").replace("Sep", "9").replace("Oct",
                                                                                                            "10").replace(
        "Nov", "11").replace("Dec", "12")
    state.ts_file = request_timestamp
    print(state.ts_file)

def preprocess_procedure(request_body):
    array = []
    for command in request_body['lmr']:
        array.append(command)

    array2 = []
    j = 0

    for i in array:
        request_body[j] = i.split(',')
        array2.append(request_body[j])
        j = j + 1
    state.procedure = array2
    print('preprocess_procedure\n' + str(state.procedure))


def process():
    text = transpile(state.procedure)
    export(text)


def transpile(procedure_array):
    use_viewer = False
    drive_off = False
    text = ""
    text += "import cozmo\n\n\ndef program(robot: cozmo.robot.Robot):"
    for command in procedure_array:
        if command[0] == "SAY":
            text += "\n    robot.say_text('" + command[1] + "').wait_for_completed()"
        elif command[0] == "MATH":
            text += "\n    robot.say_text(str(" + command[1] + command[2] + command[3] + ")).wait_for_completed()"
        elif command[0] == "COUNT":
            text += "\n    for i in range(" + command[1] + "):"
            text += "\n        robot.say_text(str(i+1)).wait_for_completed()"
        elif command[0] == "YES":
            text += "\n    robot.say_text('YES').wait_for_completed()"
        elif command[0] == "SOUND":
            text = "import asyncio\nimport time\n" + text
            text += "\n    # Create an array of SongNote objects, consisting of all notes from C2 to C3_Sharp\n    " \
                    "notes = [\n        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.C2_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.F2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.F2_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.G2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.G2_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.C3, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.C3_Sharp, " \
                    "cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, " \
                    "cozmo.song.NoteDurations.Quarter) ]\n\n    # Play the ascending notes\n    robot.play_song(" \
                    "notes, loop_count=1).wait_for_completed()\n\n    # Create an array of SongNote objects, " \
                    "consisting of the C3 pitch with varying durations\n    notes = [\n        cozmo.song.SongNote(" \
                    "cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Half),\n        cozmo.song.SongNote(" \
                    "cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.ThreeQuarter),\n        cozmo.song.SongNote(" \
                    "cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(" \
                    "cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Quarter),\n        cozmo.song.SongNote(" \
                    "cozmo.song.NoteTypes.C3, cozmo.song.NoteDurations.Whole) ]\n\n    # Play the notes with varying " \
                    "durations\n    robot.play_song(notes, loop_count=1).wait_for_completed() "
        elif command[0] == "DRIVE_OFF":
            text = "from cozmo.util import degrees, distance_mm, speed_mmps\n" + text
            text = "import asyncio\nimport time\n" + text
            text += "\n    # If the robot was on the charger, drive them forward and clear of the charger\n    if " \
                    "robot.is_on_charger:\n        # drive off the charger\n        robot.drive_off_charger_contacts(" \
                    ").wait_for_completed()\n        robot.drive_straight(distance_mm(100), speed_mmps(" \
                    "50)).wait_for_completed()\n        # Start moving the lift down\n        robot.move_lift(-3)\n   " \
                    "     # turn around to look at the charger\n        robot.turn_in_place(degrees(" \
                    "180)).wait_for_completed()\n        # Tilt the head to be level\n        robot.set_head_angle(" \
                    "degrees(0)).wait_for_completed()\n        # wait half a second to ensure Cozmo has seen the " \
                    "charger\n        time.sleep(0.5)\n        # drive backwards away from the charger\n        " \
                    "robot.drive_straight(distance_mm(-60), speed_mmps(50)).wait_for_completed()\n\n    # try to find " \
                    "the charger\n    charger = None\n\n    # see if Cozmo already knows where the charger is\n    if " \
                    "robot.world.charger:\n        if robot.world.charger.pose.is_comparable(robot.pose):\n           " \
                    " print('Cozmo already knows where the charger is!')\n            charger = robot.world.charger\n " \
                    "       else:\n            # Cozmo knows about the charger, but the pose is not based on the\n    " \
                    "        # same origin as the robot (e.g. the robot was moved since seeing\n            # the " \
                    "charger) so try to look for the charger first\n            pass\n\n    if not charger:\n        " \
                    "# Tell Cozmo to look around for the charger\n        look_around = robot.start_behavior(" \
                    "cozmo.behavior.BehaviorTypes.LookAroundInPlace)\n        try:\n            charger = " \
                    "robot.world.wait_for_observed_charger(timeout=30)\n            print('Found charger: %s' % " \
                    "charger)\n        except asyncio.TimeoutError:\n            print('Didn't see the charger')\n    " \
                    "    finally:\n            # whether we find it or not, we want to stop the behavior\n            " \
                    "look_around.stop()\n\n    if charger:\n        # Attempt to drive near to the charger, " \
                    "and then stop.\n        action = robot.go_to_object(charger, distance_mm(65.0))\n        " \
                    "action.wait_for_completed()\n        print('Completed action: result = %s' % action)\n        " \
                    "print('Done.') "
            drive_off = True
        elif command[0] == "MOVE":
            text = "from cozmo.util import distance_mm, speed_mmps\n" + text
            text += "\n    robot.drive_straight(distance_mm(" + command[1] + "), speed_mmps(" + command[
                2] + ")).wait_for_completed()"
        elif command[0] == "TURN":
            text = "from cozmo.util import degrees\n" + text
            text += "\n    robot.turn_in_place(degrees(" + command[1] + ")).wait_for_completed()"
        elif command[0] == "LIFT":
            text += "\n    robot.move_lift(" + command[1] + ")"
        elif command[0] == "LIGHTS":
            text += "\n    # set all of Cozmo's backpack lights to color\n    robot.set_all_backpack_lights(" \
                    "cozmo.lights." + command[1] + "_light) "
        elif command[0] == "ANIMATION":
            text += "\n    robot.play_anim_trigger(" + command[1] + ").wait_for_completed()"
        elif command[0] == "CUBE_LIGHT":
            text = "import time\nfrom cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id\n" + text
            text += "\n    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip\n    cube2 = " \
                    "robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart\n    cube3 = " \
                    "robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'\n\n    if cube1 " \
                    "is not None:\n        cube1.set_lights(cozmo.lights.red_light)\n    else:\n        " \
                    "cozmo.logger.warning('Cozmo is not connected to a LightCube1Id cube - check the battery.')\n\n   " \
                    " if cube2 is not None:\n        cube2.set_lights(cozmo.lights.green_light)\n    else:\n        " \
                    "cozmo.logger.warning('Cozmo is not connected to a LightCube2Id cube - check the battery.')\n\n   " \
                    " if cube3 is not None:\n        cube3.set_lights(cozmo.lights.blue_light)\n    else:\n        " \
                    "cozmo.logger.warning('Cozmo is not connected to a LightCube3Id cube - check the battery.')\n\n   " \
                    " # Keep the lights on for 10 seconds until the program exits\n    time.sleep(10) "
        elif command[0] == "PICKUP_CUBE" or command[0] == "DROP_CUBE":
            text += "\n    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)\n    " \
                    "cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, " \
                    "timeout=60)\n    lookaround.stop()\n\n    max_dst, targ = 0, None\n    for cube in cubes:\n      " \
                    "  translation = robot.pose - cube.pose\n        dst = translation.position.x ** 2 + " \
                    "translation.position.y ** 2\n        if dst > max_dst:\n            max_dst, targ = dst, " \
                    "cube\n\n    if len(cubes) < 3:\n        print('Error: need 3 Cubes but only found', len(cubes), " \
                    "'Cube(s)')\n    else:\n        robot.pickup_object(targ, num_retries=3).wait_for_completed()\n "
            use_viewer = True
        elif command[0] == "ROLL_CUBE":
            text = "from cozmo.util import degrees\n" + text
            text.replace("def program", "async def program")
            text += "\n    await robot.set_head_angle(degrees(-5.0)).wait_for_completed()\n\n    print('Cozmo is " \
                    "waiting until he sees a cube')\n    cube = await robot.world.wait_for_observed_light_cube()\n\n  " \
                    "  print('Cozmo found a cube, and will now attempt to roll with it:')\n    # Cozmo will approach " \
                    "the cube he has seen and roll it\n    # check_for_object_on_top=True enforces that Cozmo will " \
                    "not roll cubes with anything on top\n    action = robot.roll_cube(cube, " \
                    "check_for_object_on_top=True, num_retries=2)\n    await action.wait_for_completed()\n    print(" \
                    "'result:', action.result) "
        elif command[0] == "WHEELIE":
            text.replace("def program", "async def program")
            text += "\n    print('Cozmo is waiting until he sees a cube')\n    cube = await " \
                    "robot.world.wait_for_observed_light_cube()\n\n    print('Cozmo found a cube, and will now " \
                    "attempt to pop a wheelie on it')\n\n    action = robot.pop_a_wheelie(cube, num_retries=2)\n    " \
                    "await action.wait_for_completed() "
    if use_viewer is True:
        text += "\n\n\ncozmo.run_program(program, use_viewer=True)"
    elif drive_off is True:
        text += "\n\n\ncozmo.robot.Robot.drive_off_charger_on_connect = False  # Cozmo can stay on charger for " \
                "now\ncozmo.run_program(program, use_viewer=True, force_viewer_on_top=True) "
    else:
        text += "\n\n\ncozmo.run_program(program)"
    return text


def export(text):
    filepath = os.path.join('transpiled', state.ts_file)
    if not os.path.exists('transpiled'):
        os.makedirs('transpiled')
    f = open(filepath, "w")
    f.write(text)
    f.close()


def execute():
    transpiled_module = importlib.import_module('.' + state.ts_file, package='transpiled')
    cozmo.run_program(transpiled_module.program())


print(transpile([['DRIVE_OFF'], ['WHEELIE'], ['ANIMATION', 'DizzyShakeStop']]))
preprocess(json_dummy)
process()
execute()


@app.route("/")
def root():
    # redis.incr('hits')
    # return 'This Compose/Flask demo has been viewed %s time(s).' % redis.get('hits')
    return render_template('index.html')


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
