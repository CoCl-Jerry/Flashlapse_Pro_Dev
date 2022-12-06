# load in sensors
import board
import adafruit_vl53l4cd

import General
import UI_Update

def init(self):
    # start of sensor tests and initialization

    # TOF sensor test
    TOF_range(self)


def TOF_range(self):
    UI_Update.TOF_update_pushButton_toggle(self)
    try:
        vl53 = adafruit_vl53l4cd.VL53L4CD(board.I2C())
        vl53.inter_measurement = 0
        vl53.timing_budget = 200
        vl53.start_ranging()
        while True:
            while not vl53.data_ready:
                pass
            vl53.clear_interrupt()
            General.current_position = vl53.distance * 10
            break
        vl53.stop_ranging()

    except Exception as e:
        print(e, "TOF sensor failure, contact Jerry for support")
        General.TOF_error = True
    UI_Update.TOF_update(self)
    UI_Update.TOF_update_pushButton_toggle(self)
