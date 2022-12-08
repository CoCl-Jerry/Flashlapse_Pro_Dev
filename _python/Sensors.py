# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
import adafruit_scd4x  # type: ignore
from DFRobot_EOxygenSensor import *

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
    General.ambient_temperature_offset = (
        self.ambient_temperature_offset_doubleSpinBox.value()
    )


def ambient_humidity_offset(self):
    General.ambient_humidity_offset = self.ambient_humidity_offset_doubleSpinBox.value()


def ambient_co2_calibration(self):
    scd4x = adafruit_scd4x.SCD4X(board.I2C())
    scd4x.force_calibration(self.ambient_co2_calibration_spinBox.value())


def ambient_o2_calibration(mode):
    with DFRobot_EOxygenSensor_I2C(0x01, E_OXYGEN_ADDRESS_0) as SEN0496:
        if mode == 0:
            if SEN0496.oxygen.clear_calibration() == 1:
                print("calibration reset success!\n")
        elif mode == 1:
            if SEN0496.calibration_20_9() == 1:
                print("20.9 calibration success!\n")
        elif mode == 2:
            if SEN0496.calibration_99_5() == 1:
                print("99.5 calibration success!\n")
