import time


def init():
    # start of general definitions
    global current_date
    current_date = time.strftime("%m_%d_%Y")

    # end of general definitions

    # start of imaging definitions
    global imaging_capture_total
    imaging_capture_total = 1

    global imaging_capture_interval
    imaging_capture_interval = 1

    global imaging_sequence_duration
    imaging_sequence_duration = 1

    global current_image_counter
    current_image_counter = 0

    global imaging_sequence_title
    imaging_sequence_title = ""

    global full_storage_directory
    full_storage_directory = ""

    global default_storage_directory
    default_storage_directory = "/home/pi/Desktop"

    # end of imaging definitions

    # start of motor definitions
    global current_speed
    current_speed = 2

    global current_position
    current_position = 0

    global motor_interval
    motor_interval = 50

    global target_position
    target_position = 0

    global target_direction
    target_direction = 0

    global max_position
    max_position = 155

    global min_position
    min_position = 65

    global motion_thread_running
    motion_thread_running = False
    # end of motor definitions

    # start of error definitions
    global TOF_error
    TOF_error = False
