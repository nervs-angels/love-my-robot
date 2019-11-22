import cozmo
import time

micozmo = cozmo

def SAY(robot: cozmo.robot.Robot):
    robot.say_text("Hello Fernanda").wait_for_completed()


def MATH_SUM(robot: cozmo.robot.Robot):
    robot.say_text(str(1) + " plus " + str(2) + " equals " + str(1 + 2)).wait_for_completed()


def MATH_SUB(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a) + " minus " + str(b) + " equals " + str(a - b)).wait_for_completed()


def MATH_MULT(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a) + " for " + str(b) + " equals " + str(a - b)).wait_for_completed()


def MATH_DIV(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a) + " divided by " + str(b) + " equals " + str(a - b)).wait_for_completed()


def COUNT(robot: cozmo.robot.Robot, countnumber):
    for i in range(countnumber):
        robot.say_text(str(i + 1)).wait_for_completed()


def YES(robot: cozmo.robot.Robot):
    robot.say_text("Yes").wait_for_completed()


def SOUND(robot: cozmo.robot.Robot):
    robot.play_audio(cozmo.audio.AudioEvents.SfxGameWin)
    time.sleep(1.0)


def DRIVE_OFF(robot: cozmo.robot.Robot, ditance, speed):
    if robot.is_on_charger:
        robot.drive_off_charger_contacts().wait_for_completed()



def TURN(robot: cozmo.robot.Robot, degrees):
    robot.turn_in_place(degrees(degrees)).wait_for_completed()


def LIFT(robot: cozmo.robot.Robot, radians):
    robot.move_lift(radians)


def LIGHTS(robot: cozmo.robot.Robot, red, green, blue, white, off):
    if (red):
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        time.sleep(2)

    if (green):
        robot.set_all_backpack_lights(cozmo.lights.green_light)
        time.sleep(2)

    if (blue):
        robot.set_all_backpack_lights(cozmo.lights.blue_light)
        time.sleep(2)

    if (white):
        robot.set_center_backpack_lights(cozmo.lights.white_light)
        time.sleep(2)

    else:
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(2)


def ANIMATION(robot: cozmo.robot.Robot,
              animation):  ## FrustratedByFailureMajor, AcknowledgeFaceInitPause, CodeLabCow, DizzyShakeStop, DriveLoopAngry
    robot.play_anim(name=animation).wait_for_completed()


def PICKUP_CUBE(robot: cozmo.robot.Robot, cube):
    lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
    cubes = robot.world.wait_until_observe_num_objects(num=3, object_type=cozmo.objects.LightCube, timeout=60)
    robot.pickup_object(cubes[cube], num_retries=3).wait_for_completed()
    lookaround.stop()
