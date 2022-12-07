import os

# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
from picamera import PiCamera  # type: ignore

import General
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep


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


class Preview(QThread):
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


class Livefeed(QThread):
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
                camera.start_preview()
                sleep(General.live_duration)
        except Exception as e:
            print(e, "Camera failure, contact Jerry for support")
            General.camera_error = True


class Timelapse(QThread):
    imaging = pyqtSignal()
    complete = pyqtSignal()
    countdown = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        if not os.path.isdir(General.full_storage_directory):
            original_umask = os.umask(0)
            os.mkdir(General.full_storage_directory, mode=0o777)
            os.umask(original_umask)
        for i in range(General.imaging_capture_total):
            General.current_image_counter = i + 1
            General.current_full_file_name = General.full_file_name % (i + 1)
            self.imaging.emit()
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
                    camera.capture(General.current_full_file_name)
                    self.complete.emit()
            except Exception as e:
                print(e, "Camera failure, contact Jerry for support")
                General.camera_error = True
            for x in range(General.imaging_capture_interval):
                self.countdown.emit()
                General.imaging_countdown_value = General.imaging_capture_interval - x
                sleep(1)
                if not General.timelapse_thread_running:
                    break
            if not General.timelapse_thread_running:
                break
            General.timelapse_thread_running = False
