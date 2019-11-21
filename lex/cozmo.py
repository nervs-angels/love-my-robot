import cozmo, time
from cozmo.objects import LightCube1Id, LightCube2Id, LightCube3Id

def SAY(robot: cozmo.robot.Robot, to_say):
    robot.say_text(to_say).wait_for_completed()

def MATH_SUM(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a)+" plus "+str(b)+" equals "+str(a+b)).wait_for_completed()
    
def MATH_SUB(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a)+" minus "+str(b)+" equals "+str(a-b)).wait_for_completed()
  
def MATH_MULT(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a)+" for "+str(b)+" equals "+str(a-b)).wait_for_completed()

def MATH_DIV(robot: cozmo.robot.Robot, a, b):
    robot.say_text(str(a)+" divided by "+str(b)+" equals "+str(a-b)).wait_for_completed()
          
def COUNT(robot: cozmo.robot.Robot, countnumber):
    for i in range(countnumber):
        robot.say_text(str(i+1)).wait_for_completed()

def YES(robot: cozmo.robot.Robot):
    robot.say_text("Yes").wait_for_completed()
    
def SOUND(robot: cozmo.robot.Robot):
    robot.play_audio(cozmo.audio.AudioEvents.SfxGameWin)
    time.sleep(1.0)

def DRIVE_OFF(robot: cozmo.robot.Robot, ditance, speed):
    if robot.is_on_charger:
        robot.drive_off_charger_contacts().wait_for_completed()
    
def MOVE(robot: cozmo.robot.Robot, ditance, speed):
    robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()

def TURN(robot: cozmo.robot.Robot, degrees):
    robot.turn_in_place(degrees(degrees)).wait_for_completed()
        
def LIFT(robot: cozmo.robot.Robot, radians):
    robot.move_lift(radians)

def LIGHTS(robot: cozmo.robot.Robot, red, green,blue,white,off):
    if(red):
        robot.set_all_backpack_lights(cozmo.lights.red_light)
        time.sleep(2)
    
    if (green):
        robot.set_all_backpack_lights(cozmo.lights.green_light)
        time.sleep(2)
    
    if(blue):
        robot.set_all_backpack_lights(cozmo.lights.blue_light)
        time.sleep(2)
    
    if (white):
        robot.set_center_backpack_lights(cozmo.lights.white_light)
        time.sleep(2)

    else:
        robot.set_all_backpack_lights(cozmo.lights.off_light)
        time.sleep(2)
        
def CUBE_LIGHT(robot: cozmo.robot.Robot):
    cube1 = robot.world.get_light_cube(LightCube1Id)  # looks like a paperclip
    cube2 = robot.world.get_light_cube(LightCube2Id)  # looks like a lamp / heart
    cube3 = robot.world.get_light_cube(LightCube3Id)  # looks like the letters 'ab' over 'T'

    if cube1 is not None:
        cube1.set_lights(cozmo.lights.red_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube1Id cube - check the battery.")

    if cube2 is not None:
        cube2.set_lights(cozmo.lights.green_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube2Id cube - check the battery.")

    if cube3 is not None:
        cube3.set_lights(cozmo.lights.blue_light)
    else:
        cozmo.logger.warning("Cozmo is not connected to a LightCube3Id cube - check the battery.")
    
    time.sleep(10)


        
    
SAY
MATH
COUNT
YES
SOUND
DRIVE_OFF
MOVE
TURN
LIFT
LIGHTS
ANIMATION
CUBE_LIGHT
PICKUP_CUBE
DROP_CUBE
ROLL_CUBE
WHEELIE