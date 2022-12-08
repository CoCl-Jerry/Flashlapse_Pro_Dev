# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
import adafruit_scd4x  # type: ignore

import General
import UI_Update


def init(self):
    # start of sensor tests and initialization

    # TOF sensor test
    TOF_range(self)
    pass


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


def ambient_temperature_offset(self):
    scd4x = adafruit_scd4x.SCD4X(board.I2C())
    scd4x.temperature_offset: self.ambient_temperature_offset_doubleSpinBox.value()
    scd4x.persist_settings()
