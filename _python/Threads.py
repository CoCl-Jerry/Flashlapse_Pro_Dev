# load in sensors
import board
import adafruit_vl53l4cd

import General
from PyQt5.QtCore import QThread, pyqtSignal


class Motion(QThread):
    stop_motor = pyqtSignal()
    sensor_read = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        try:
            vl53 = adafruit_vl53l4cd.VL53L4CD(board.I2C())
            vl53.inter_measurement = 0
            vl53.timing_budget = 200
            vl53.start_ranging()
            if General.target_direction:
                while (
                    General.current_position <= General.target_position
                    and General.motion_thread_running
                ):
                    while not vl53.data_ready:
                        pass
                    vl53.clear_interrupt()
                    General.current_position = vl53.distance * 10
                    print(General.current_position)
                vl53.stop_ranging()

            else:
                while (
                    General.current_position >= General.target_position
                    and General.motion_thread_running
                ):
                    while not vl53.data_ready:
                        pass
                    vl53.clear_interrupt()
                    General.current_position = vl53.distance * 10
                    print(General.current_position)
                vl53.stop_ranging()

            self.disable_motor.emit()
            General.motion_thread_running = False

        except Exception as e:
            print(e, "TOF sensor failure, contact Jerry for support")
            General.TOF_error = True
