import time
from PyQt5 import QtGui
import serial  # type: ignore


def init():

    # ---------------------------------------------------------------------------- #
    #                         start of general declarations                        #
    # ---------------------------------------------------------------------------- #
    global current_date
    current_date = time.strftime("%m_%d_%Y")

    global serial_reference
    serial_reference = serial.Serial(
        port="/dev/ttyUSB_RS485",
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5,
    )

    # ---------------------------------------------------------------------------- #
    #                       start of thread flag declarations                      #
    # ---------------------------------------------------------------------------- #
    global motion_thread_running
    motion_thread_running = False

    global timelapse_thread_running
    timelapse_thread_running = False

    global ambient_thread_running
    ambient_thread_running = False

    global soil_thread_running
    soil_thread_running = False

    global lighting_cycle_thread_running
    lighting_cycle_thread_running = False

    # ---------------------------------------------------------------------------- #
    #                       start of error flag declarations                       #
    # ---------------------------------------------------------------------------- #
    global TOF_error
    TOF_error = False

    global communication_error
    communication_error = False

    global motor_error
    motor_error = False

    global camera_error
    camera_error = False

    global rangefinder_error
    rangefinder_error = False

    global soil_sensor_error
    soil_sensor_error = False

    global storage_critical_error
    storage_critical_error = False

    # ---------------------------------------------------------------------------- #
    #                       start of error image declarations                      #
    # ---------------------------------------------------------------------------- #
    global communication_error_image
    communication_error_image = QtGui.QImage(
        "../_image/communication_error.png")

    global motor_error_image
    motor_error_image = QtGui.QImage("../_image/motor_error.png")

    global camera_error_image
    camera_error_image = QtGui.QImage("../_image/camera_error.png")

    global rangefinder_error_image
    rangefinder_error_image = QtGui.QImage("../_image/rangefinder_error.png")

    global soil_sensor_error_image
    soil_sensor_error_image = QtGui.QImage("../_image/soil_sensor_error.png")

    global storage_critical_error_image
    storage_critical_error_image = QtGui.QImage(
        "../_image/storage_critical_error.png")

    # ---------------------------------------------------------------------------- #
    #                        start of lighting declarations                        #
    # ---------------------------------------------------------------------------- #
    global lighting_brightness
    lighting_brightness = 100

    global lighting_red
    lighting_red = 0

    global lighting_green
    lighting_green = 0

    global lighting_blue
    lighting_blue = 0

    global lighting_adaptive_IR
    lighting_adaptive_IR = 0

    global lighting_cycle_countdown_value
    lighting_cycle_countdown_value = 0

    global lighting_cycle_daytime_value
    lighting_cycle_daytime_value = 1

    global lighting_cycle_nighttime_value
    lighting_cycle_nighttime_value = 1

    global lighting_commands_list
    lighting_commands_list = []

    # ---------------------------------------------------------------------------- #
    #                         start of imaging declarations                        #
    # ---------------------------------------------------------------------------- #
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

    # ---------------------------------------------------------------------------- #
    #                         start of motion declarations                         #
    # ---------------------------------------------------------------------------- #
    global current_speed
    current_speed = 3

    global current_position
    current_position = 0

    global motor_interval
    motor_interval = 50

    global target_position
    target_position = 0

    global target_direction
    target_direction = 0

    global max_position
    max_position = 135

    global min_position
    min_position = 65

    # ---------------------------------------------------------------------------- #
    #                     start of general sensor declarations                     #
    # ---------------------------------------------------------------------------- #
    global sensor_capture_interval
    sensor_capture_interval = 60

    # ---------------------------------------------------------------------------- #
    #                     start of ambient sensor declarations                     #
    # ---------------------------------------------------------------------------- #
    global ambient_sensor_time_stamp
    ambient_sensor_time_stamp = []

    global ambient_temperature
    ambient_temperature = []

    global ambient_humidity
    ambient_humidity = []

    global ambient_CO2
    ambient_CO2 = []

    global ambient_o2
    ambient_o2 = []

    global ambient_sensor_initial_time
    ambient_sensor_initial_time = 0

    global ambient_sensor_previous_time
    ambient_sensor_previous_time = 0

    global ambient_temperature_offset
    ambient_temperature_offset = 0

    global ambient_humidity_offset
    ambient_humidity_offset = 0

    global ambient_o2_sensor_calibration_mode
    ambient_o2_sensor_calibration_mode = 0

    # ---------------------------------------------------------------------------- #
    #                       start of soil sensor declarations                      #
    # ---------------------------------------------------------------------------- #

    global soil_sensor_request
    soil_sensor_request = bytes(
        [0x01, 0x03, 0x02, 0x00, 0x00, 0x07, 0x05, 0xB0])

    global soil_sensor_time_stamp
    soil_sensor_time_stamp = []

    global soil_temperature
    soil_temperature = []

    global soil_water_content
    soil_water_content = []

    global soil_EC
    soil_EC = []

    global soil_pH
    soil_pH = []

    global soil_nitrogen
    soil_nitrogen = []

    global soil_phosphorus
    soil_phosphorus = []

    global soil_potassium
    soil_potassium = []

    global soil_sensor_initial_time
    soil_sensor_initial_time = 0

    global soil_sensor_previous_time
    soil_sensor_previous_time = 0

    global soil_sensor_crc16_check
    soil_sensor_crc16_check = True

    global soil_temperature_offset
    soil_temperature_offset = 0

    global soil_water_content_offset
    soil_water_content_offset = 0

    global soil_EC_offset
    soil_EC_offset = 0

    global soil_pH_offset
    soil_pH_offset = 0

    global soil_nitrogen_offset
    soil_nitrogen_offset = 0

    global soil_phosphorus_offset
    soil_phosphorus_offset = 0

    global soil_potassium_offset
    soil_potassium_offset = 0

    # ---------------------------------------------------------------------------- #
    #                     start of graph reference declarations                    #
    # ---------------------------------------------------------------------------- #
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

    global soil_water_content_graph_ref
    soil_water_content_graph_ref = ""

    global soil_EC_graph_ref
    soil_EC_graph_ref = ""

    global soil_pH_graph_ref
    soil_pH_graph_ref = ""

    global soil_nitrogen_graph_ref
    soil_nitrogen_graph_ref = ""

    global soil_phosphorus_graph_ref
    soil_phosphorus_graph_ref = ""

    global soil_potassium_graph_ref
    soil_potassium_graph_ref = ""
