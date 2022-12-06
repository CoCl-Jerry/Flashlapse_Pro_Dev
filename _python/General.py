

def init():

    # start of motor definitions
    global current_speed
    current_speed = 2

    global current_position
    current_position = 0

    global target_position
    target_position = 0

    global max_positon
    max_positon = 155

    global min_positon
    min_positon = 65

    global target_direction
    target_direction = False

    global motion_thread_running
    motion_thread_running = False
    # end of motor definitions

    # start of error definitions
    global TOF_error
    TOF_error = False


