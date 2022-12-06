

def init():

    # start of motor definitions
    global current_speed
    current_speed = 2

    global current_position
    current_position = 0

    global target_position
    target_position = 0

    global current_direction
    current_direction = False
    # end of motor definitions

    # start of error definitions
    global TOF_error
    TOF_error = False


