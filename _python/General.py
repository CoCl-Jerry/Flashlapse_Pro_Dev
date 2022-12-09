import time
from PyQt5 import QtGui
import serial  # type: ignore


def init():
    # start of general definitions
    global current_date
    current_date = time.strftime("%m_%d_%Y")

    global ser
    ser = serial.Serial(
        port="/dev/ttyS0",
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
    )

    global soil_sensor_request
    soil_sensor_request = bytes([0x01, 0x03, 0x02, 0x00, 0x00, 0x07, 0x05, 0xB0])

    global soil_data
    soil_data = ""
    # end of general definitions

    # start of error definitions
    global TOF_error
    TOF_error = False

    global communication_error
    communication_error = False

    global communication_error_image
    communication_error_image = QtGui.QImage("../_image/communication_error.png")

    global motor_error
    motor_error = False

    global motor_error_image
    motor_error_image = QtGui.QImage("../_image/motor_error.png")

    global camera_error
    camera_error = False

    global camera_error_image
    camera_error_image = QtGui.QImage("../_image/camera_error.png")

    global rangefinder_error
    rangefinder_error = False

    global rangefinder_error_image
    rangefinder_error_image = QtGui.QImage("../_image/rangefinder_error.png")

    global soil_sensor_error
    soil_sensor_error = False

    global soil_sensor_error_image
    soil_sensor_error_image = QtGui.QImage("../_image/soil_sensor_error.png")
    # end of error definitions

    # start of imaging definitions
    global imaging_capture_total
    imaging_capture_total = 5

    global imaging_capture_interval
    imaging_capture_interval = 1

    global imaging_sequence_duration
    imaging_sequence_duration = 5

    global imaging_countdown_value
    imaging_countdown_value = 0

    global current_image_counter
    current_image_counter = 0

    global imaging_sequence_title
    imaging_sequence_title = ""

    global full_file_name
    full_file_name = ""

    global current_full_file_name
    current_full_file_name = ""

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

    global image_format
    image_format = 1

    global live_duration
    live_duration = 5

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

    # end of motor definitions

    # start of sensor definitions
    global ambient_temperature
    ambient_temperature = []

    global soil_temperature
    soil_temperature = []

    global ambient_humidity
    ambient_humidity = []

    global ambient_CO2
    ambient_CO2 = []

    global ambient_o2
    ambient_o2 = []

    global ambient_sensor_time_points
    ambient_sensor_time_points = []

    global soil_sensor_time_points
    soil_sensor_time_points = []

    global ambient_sensor_previous_time
    ambient_sensor_previous_time = 0

    global ambient_temperature_offset
    ambient_temperature_offset = 0

    global ambient_humidity_offset
    ambient_humidity_offset = 0

    global ambient_sensor_initial_time
    ambient_sensor_initial_time = 0

    global soil_sensor_initial_time
    soil_sensor_initial_time = 0

    global sensor_capture_interval
    sensor_capture_interval = 5

    global ambient_o2_sensor_calibration_mode
    ambient_o2_sensor_calibration_mode = 0
    # end of sensor definitions

    # start of graph definitions
    global ambient_temperature_graph_ref
    ambient_temperature_graph_ref = ""

    global ambient_humidity_graph_ref
    ambient_humidity_graph_ref = ""

    global ambient_co2_graph_ref
    ambient_co2_graph_ref = ""

    global ambient_o2_graph_ref
    ambient_o2_graph_ref = ""

    global soil_temperature_graph_ref
    soil_temperature_graph_ref = ""
    # end of graph definitions

    # start of thread flag definitions
    global motion_thread_running
    motion_thread_running = False

    global timelapse_thread_running
    timelapse_thread_running = False

    global ambient_thread_running
    ambient_thread_running = False

    global soil_thread_running
    soil_thread_running = False
