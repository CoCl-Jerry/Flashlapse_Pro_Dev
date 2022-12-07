# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
from picamera import PiCamera  # type: ignore

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
            if General.current_position < General.target_position:
                while (
                    General.current_position < General.target_position
                    and General.motion_thread_running
                ):
                    while not vl53.data_ready:
                        pass
                    vl53.clear_interrupt()
                    General.current_position = vl53.distance * 10
                    self.sensor_read.emit()
                vl53.stop_ranging()
                self.stop_motor.emit()

            else:
                while (
                    General.current_position > General.target_position
                    and General.motion_thread_running
                ):
                    while not vl53.data_ready:
                        pass
                    vl53.clear_interrupt()
                    General.current_position = vl53.distance * 10
                    self.sensor_read.emit()
                vl53.stop_ranging()
                self.stop_motor.emit()
            General.motion_thread_running = False

        except Exception as e:
            print(e, "TOF sensor failure, contact Jerry for support")
            General.TOF_error = True


class Snap(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        try:
            with PiCamera() as camera:
                camera.zoom = (
                    General.AOI_X,
                    General.AOI_Y,
                    General.AOI_W,
                    General.AOI_H,
                )
                camera.resolution = (350, 350)
                camera._set_rotation(90 * General.imaging_rotation)
                camera.capture("../_temp/snapshot.jpg")
        except Exception as e:
            print(e, "Camera failure, contact Jerry for support")
            General.camera_error = True


class Snap(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        try:
            with PiCamera() as camera:
                camera.zoom = (
                    General.AOI_X,
                    General.AOI_Y,
                    General.AOI_W,
                    General.AOI_H,
                )
                camera.resolution = (General.x_resolution, General.y_resolution)
                camera._set_rotation(90 * General.imaging_rotation)

            if General.image_format:
                camera.capture("../_temp/preview.jpg")
            else:
                camera.capture("../_temp/preview.png")
        except Exception as e:
            print(e, "Camera failure, contact Jerry for support")
            General.camera_error = True
