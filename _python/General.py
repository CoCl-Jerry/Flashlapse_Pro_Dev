import time
import General
import smbus  # type: ignore


from PyQt5 import QtGui


def init():
    # start of general definitions
    global current_date
    current_date = time.strftime("%m_%d_%Y")

    global camera_error_image
    camera_error_image = QtGui.QImage("../_image/camera_error.png")

    global communication_error_image
    communication_error_image = QtGui.QImage("../_image/communication_error.png")

    global motor_error_image
    motor_error_image = QtGui.QImage("../_image/motor_error.png")

    global rangefinder_error_image
    rangefinder_error_image = QtGui.QImage("../_image/rangefinder_error.png")

    global soil_sensor_error_image
    soil_sensor_error_image = QtGui.QImage("../_image/soil_sensor_error.png")

    # end of general definitions

    # start of error definitions
    global TOF_error
    TOF_error = False

    global communication_error
    communication_error = False

    global motor_error
    motor_error = False

    global camera_error
    camera_error = False
    # end of error definitions

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

    global AOI_X
    AOI_X = 0
    global AOI_Y
    AOI_Y = 0
    global AOI_W
    AOI_W = 1
    global AOI_H
    AOI_H = 1

    global x_resolution
    x_resolution = 2464
    global y_resolution
    y_resolution = 2464

    global imaging_rotation
    imaging_rotation = 2
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


def sendCMD(cont):
    print("sending command...\n" + cont)
    temp = cont + "\n"
    while True:
        try:
            bus = smbus.SMBus(1)
            converted = []
            for b in temp:
                converted.append(ord(b))
            bus.write_i2c_block_data(0x08, 0x5E, converted)
            break
        except Exception as e:
            General.communication_error = True
            print(e, "communication failure,contact Jerry for support")
        pass
