import time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id
from cozmo.util import distance_mm, speed_mmps
import cozmo


def program(robot: cozmo.robot.Robot):
    robot.say_text('HI').wait_for_completed()
    robot.drive_straight(distance_mm(50), speed_mmps(100)).wait_for_completed()
    robot.say_text('POO').wait_for_completed()
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning('Cozmo is not connected to a LightCube1Id cube - check the battery.')

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning('Cozmo is not connected to a LightCube2Id cube - check the battery.')

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning('Cozmo is not connected to a LightCube3Id cube - check the battery.')

    # Keep the lights on for 10 seconds until the program exits
    time.sleep(10) 


cozmo.run_program(program)