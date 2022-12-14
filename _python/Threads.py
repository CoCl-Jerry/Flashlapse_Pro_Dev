import os

# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
import adafruit_scd4x  # type: ignore
from picamera import PiCamera  # type: ignore
from DFRobot_EOxygenSensor import *

import General
import Sensors
from PyQt5.QtCore import QThread, pyqtSignal
from time import sleep, perf_counter

# ---------------------------------------------------------------------------- #
#                             threads for lighting                             #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
class Lighting_Cycle(QThread):
    daytime = pyqtSignal()
    nighttime = pyqtSignal()
    countdown = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        while True:
            for x in range(General.lighting_cycle_daytime_value * 60):
                self.countdown.emit()
                General.lighting_cycle_countdown_value = (
                    General.lighting_cycle_daytime_value * 60 - x
                )
                sleep(1)
                if not General.lighting_cycle_thread_running:
                    return
            self.nighttime.emit()
            for x in range(General.lighting_cycle_nighttime_value * 60):
                self.countdown.emit()
                General.lighting_cycle_countdown_value = (
                    General.lighting_cycle_nighttime_value * 60 - x
                )
                sleep(1)
                if not General.lighting_cycle_thread_running:
                    return
            self.daytime.emit()


# ---------------------------------------------------------------------------- #
#                              threads for motion                              #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
#                              thread for imaging                              #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
class Timelapse(QThread):
    imaging = pyqtSignal()
    complete = pyqtSignal()
    countdown = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        try:
            if not os.path.isdir(General.full_storage_directory):
                original_umask = os.umask(0)
                os.mkdir(General.full_storage_directory, mode=0o777)
                os.umask(original_umask)
        except Exception as e:
            print(e, "folder already exsists")
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
            for x in range(General.imaging_capture_interval * 60):
                self.countdown.emit()
                General.imaging_countdown_value = (
                    General.imaging_capture_interval * 60 - x
                )
                sleep(1)
                if not General.timelapse_thread_running:
                    break
            if not General.timelapse_thread_running:
                break
        General.timelapse_thread_running = False


# ---------------------------------------------------------------------------- #
#                          threads for ambient sensors                         #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
class Ambient(QThread):
    ambient_sensor_update = pyqtSignal()
    initialized = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        scd4x = adafruit_scd4x.SCD4X(board.I2C())
        scd4x.start_periodic_measurement()

        SEN0496 = DFRobot_EOxygenSensor_I2C(0x01, E_OXYGEN_ADDRESS_0)

        General.ambient_sensor_initial_time = round(perf_counter(), 2)

        while General.ambient_thread_running:
            if (
                perf_counter()
                - General.ambient_sensor_initial_time
                - General.ambient_sensor_previous_time
                > General.sensor_capture_interval
                or len(General.ambient_sensor_time_stamp) == 0
            ):
                if scd4x.data_ready:
                    General.ambient_sensor_time_stamp.append(
                        round(perf_counter() - General.ambient_sensor_initial_time, 2)
                    )
                    General.ambient_sensor_previous_time = (
                        General.ambient_sensor_time_stamp[-1]
                    )
                    General.ambient_temperature.append(
                        round(scd4x.temperature + General.ambient_temperature_offset, 2)
                    )
                    General.ambient_humidity.append(
                        round(
                            scd4x.relative_humidity + General.ambient_humidity_offset, 2
                        )
                    )
                    General.ambient_CO2.append(scd4x.CO2)
                    General.ambient_o2.append(
                        round(SEN0496.read_oxygen_concentration(), 2)
                    )

                    if len(General.ambient_sensor_time_stamp) == 2:
                        self.initialized.emit()
                    elif len(General.ambient_sensor_time_stamp) > 2:
                        self.ambient_sensor_update.emit()


# ---------------------------------------------------------------------------- #
class o2_sensor_calibration(QThread):
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        SEN0496 = DFRobot_EOxygenSensor_I2C(0x01, E_OXYGEN_ADDRESS_0)
        if General.ambient_o2_sensor_calibration_mode == 0:
            SEN0496.clear_calibration()
        elif General.ambient_o2_sensor_calibration_mode == 1:
            SEN0496.calibration_20_9()

        elif General.ambient_o2_sensor_calibration_mode == 2:
            SEN0496.calibration_99_5()


# ---------------------------------------------------------------------------- #
#                           threads for soil sensors                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
class Soil(QThread):
    soil_sensor_update = pyqtSignal()
    initialized = pyqtSignal()

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self._running = False

    def run(self):
        General.soil_sensor_initial_time = round(perf_counter(), 2)
        soil_sensor_raw_data = []
        soil_sensor_processed_data = []

        while General.soil_thread_running:
            if (
                perf_counter()
                - General.soil_sensor_initial_time
                - General.soil_sensor_previous_time
                > General.sensor_capture_interval
                or len(General.soil_sensor_time_stamp) == 0
            ):
                try:
                    if not General.serial_reference.is_open:
                        General.serial_reference.open()
                    General.serial_reference.write(General.soil_sensor_request)
                    sleep(1)
                    soil_sensor_raw_data = General.serial_reference.read(19).hex()
                    General.serial_reference.close()
                except Exception as e:
                    print(e, "Soil sensor error, retrying...")
                    General.soil_sensor_crc16_check = False

                soil_sensor_processed_data = Sensors.hexListConvert(
                    soil_sensor_raw_data
                )
                if soil_sensor_processed_data:
                    sensor_crc = [
                        hex(soil_sensor_processed_data.pop()),
                        hex(soil_sensor_processed_data.pop()),
                    ]
                    reference_crc = Sensors.crc16_generator_hex(
                        soil_sensor_processed_data
                    )
                    print(reference_crc)
                    print(sensor_crc)

                    if (
                        reference_crc[0] == sensor_crc[0]
                        and reference_crc[1] == sensor_crc[1]
                    ):
                        Sensors.soil_sensor_data_processor(
                            Sensors.extractor(soil_sensor_raw_data)
                        )
                        General.soil_sensor_time_stamp.append(
                            round(perf_counter() - General.soil_sensor_initial_time, 2)
                        )
                        General.soil_sensor_previous_time = (
                            General.soil_sensor_time_stamp[-1]
                        )
                        General.soil_sensor_crc16_check = True
                        if len(General.soil_sensor_time_stamp) == 2:
                            self.initialized.emit()
                        elif len(General.soil_sensor_time_stamp) > 2:
                            self.soil_sensor_update.emit()

                    else:
                        General.soil_sensor_crc16_check = False
                        print("CRC16 check failed, retrying...")
                        time.sleep(5)

                else:
                    print("empty return, retrying...")
