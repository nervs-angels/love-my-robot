import cozmo


def program_test(robot: cozmo.robot.Robot):
    robot.say_text("IT'S HAPPENING!!!").wait_for_completed()


cozmo.run_program(program_test)