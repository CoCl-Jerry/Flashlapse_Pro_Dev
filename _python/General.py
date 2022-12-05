# load in sensors
import board
import adafruit_vl53l4cd


def init():

    # start of motor definitions
    global current_speed
    current_speed = 2

    global current_position
    current_position = ""

    global target_position
    target_position = 0

    global current_direction
    current_direction = False
    # end of motor definitions

    # start of error definitions
    global TOF_error
    TOF_error = False

    # start of sensor tests and initialization

    # TOF sensor test
    try:
        vl53 = adafruit_vl53l4cd.VL53L4CD(board.I2C())
        vl53.inter_measurement = 0
        vl53.timing_budget = 200
        vl53.start_ranging()
        while True:
            while not vl53.data_ready:
                pass
            vl53.clear_interrupt()
            current_position = vl53.distance * 10
            break
        vl53.stop_ranging()

    except Exception as e:
        print(e, "TOF sensor failure, contact Jerry for support")
        TOF_error = True
        current_position = "Error"
