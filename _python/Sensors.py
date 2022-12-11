# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
import adafruit_scd4x  # type: ignore

from DFRobot_EOxygenSensor import *
from PyQt5.QtWidgets import QFileDialog
import csv


import General
import UI_Update
import Call_Thread

# ---------------------------------------------------------------------------- #
def init(self):
    # start of sensor tests and initialization

    # TOF sensor test
    TOF_range(self)
    pass


# ---------------------------------------------------------------------------- #
#                           general sensor functions                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def sensor_set_interval(self):
    General.sensor_capture_interval = self.sensor_set_interval_spinBox.value()


# ---------------------------------------------------------------------------- #
#                             TOF sensor functions                             #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
#                           ambient sensor functions                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def ambient_temperature_offset(self):
    General.ambient_temperature_offset = (
        self.ambient_temperature_offset_doubleSpinBox.value()
    )


# ---------------------------------------------------------------------------- #
def ambient_humidity_offset(self):
    General.ambient_humidity_offset = self.ambient_humidity_offset_doubleSpinBox.value()


# ---------------------------------------------------------------------------- #
def ambient_co2_calibration(self):
    scd4x = adafruit_scd4x.SCD4X(board.I2C())
    scd4x.force_calibration(self.ambient_co2_calibration_spinBox.value())


# ---------------------------------------------------------------------------- #
def ambient_reset_calibration(self):
    print("resetting calibration")
    scd4x = adafruit_scd4x.SCD4X(board.I2C())
    scd4x.factory_reset()


# ---------------------------------------------------------------------------- #
def ambient_o2_calibration(self, mode):
    General.ambient_o2_sensor_calibration_mode = mode
    Call_Thread.ambient_o2_sensor_calibration(self)


# ---------------------------------------------------------------------------- #
#                             soil sensor functions                            #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def hexListConvert(data: str):

    hex_bytes = bytes.fromhex(data)  # Takes a hex string and turns it into a byte array
    #  print(hex_bytes)  # Output: b'\xde\xad\xbe\xef'
    hex_list = list(hex_bytes)
    return hex_list


# ---------------------------------------------------------------------------- #
def crc16_generator_hex(data: list[int]) -> str:
    data = bytearray(data)
    crc = 0xFFFF

    # Calculate CRC-16 checksum for data packet
    for b in data:
        crc ^= b
        for _ in range(0, 8):
            bcarry = crc & 0x0001
            crc >>= 1
            if bcarry:
                crc ^= 0xA001
    msb = crc >> 0x08 & 0xFF
    lsb = crc & 0xFF
    crc_to_send = [hex(lsb), hex(msb)]
    print(crc_to_send)

    return crc_to_send


# ---------------------------------------------------------------------------- #
def hexListConvert(data: str):

    hex_bytes = bytes.fromhex(data)  # Takes a hex string and turns it into a byte array
    #  print(hex_bytes)  # Output: b'\xde\xad\xbe\xef'
    hex_list = list(hex_bytes)
    print(hex_list)

    return hex_list


# ---------------------------------------------------------------------------- #
def crc16_generator_hex(data: list[int]) -> str:
    data = bytearray(data)
    crc = 0xFFFF

    # Calculate CRC-16 checksum for data packet
    for b in data:
        crc ^= b
        for _ in range(0, 8):
            bcarry = crc & 0x0001
            crc >>= 1
            if bcarry:
                crc ^= 0xA001
    msb = crc >> 0x08 & 0xFF
    lsb = crc & 0xFF
    crc_to_send = [hex(msb), hex(lsb)]

    return crc_to_send


# ---------------------------------------------------------------------------- #
def extractor(hex_string):
    length = len(hex_string.strip())
    FDN = 6  # first disposable number of bits
    LDN = 4  # last disposable number of bits
    data_segment_bits = 4  # all bits for the data including the first bit
    data_area_len = length - (FDN + LDN)
    first_data_bit_index = length - (data_area_len + LDN)
    loop_num = int(data_area_len / data_segment_bits)

    keyValues = [
        "TemperatureValue",
        "WaterContentValue",
        "ECValue",
        "PHValue",
        "NitrogenValue",
        "PhosphorusValue",
        "PotassiumValue",
    ]
    dataList = []
    obj = {}
    for i in range(loop_num):
        s_indx = first_data_bit_index + (data_segment_bits * i)
        str_segment = hex_string[s_indx : s_indx + data_segment_bits]
        bytes_segment = bytes.fromhex(str_segment)
        dec_ = int(bytes_segment.hex(), 16)
        obj[keyValues[i]] = dec_
        dataList.append(dec_)
    return obj


# ---------------------------------------------------------------------------- #
def soil_sensor_data_processor(data):
    General.soil_temperature.append(
        round((data["TemperatureValue"] / 100) + General.soil_temperature_offset, 2)
    )
    General.soil_water_content.append(
        round((data["WaterContentValue"] / 100) + General.soil_water_content_offset, 2)
    )
    General.soil_EC.append(round(data["ECValue"] + General.soil_EC_offset, 2))
    General.soil_pH.append(round((data["PHValue"] / 10) + General.soil_pH_offset, 2))
    General.soil_nitrogen.append(
        round(data["NitrogenValue"] + General.soil_nitrogen_offset, 2)
    )
    General.soil_phosphorus.append(
        round(data["PhosphorusValue"] + General.soil_phosphorus_offset, 2)
    )
    General.soil_potassium.append(
        round(data["PotassiumValue"] + General.soil_potassium_offset, 2)
    )


# ---------------------------------------------------------------------------- #
def soil_sensor_offset(self):
    General.soil_temperature_offset = self.soil_temperature_offset_doubleSpinBox.value()
    General.soil_water_content_offset = (
        self.soil_water_content_offset_doubleSpinBox.value()
    )
    General.soil_EC_offset = self.soil_EC_offset_doubleSpinBox.value()
    General.soil_pH_offset = self.soil_pH_offset_doubleSpinBox.value()
    General.soil_nitrogen_offset = self.soil_nitrogen_offset_doubleSpinBox.value()
    General.soil_phosphorus_offset = self.soil_phosphorus_offset_doubleSpinBox.value()
    General.soil_potassium_offset = self.soil_potassium_offset_doubleSpinBox.value()


# ---------------------------------------------------------------------------- #
def sensor_export_data(self):
    try:
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        if self.mainwindow_tabWidget.currentIndex() == 3:
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Save CSV File",
                General.default_storage_directory
                + "/ambient_sensor_data_"
                + General.current_date
                + ".csv",
                "CSV Files (*.csv)",
                options=options,
            )
            if file_name:
                UI_Update.export_UI_update(self, 0)
                export = list(
                    zip(
                        General.ambient_sensor_time_stamp,
                        General.ambient_temperature,
                        General.ambient_humidity,
                        General.ambient_CO2,
                        General.ambient_o2,
                    )
                )
                with open(file_name, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(["Time", "Temperature", "Humidity", "CO2", "O2"])
                    writer.writerows(export)
                    UI_Update.export_UI_update(self, 1)
        elif self.mainwindow_tabWidget.currentIndex() == 4:
            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Save CSV File",
                General.default_storage_directory
                + "/soil_sensor_data_"
                + General.current_date
                + ".csv",
                "CSV Files (*.csv)",
                options=options,
            )
            if file_name:
                UI_Update.export_UI_update(self, 0)
                export = list(
                    zip(
                        General.soil_sensor_time_stamp,
                        General.soil_temperature,
                        General.soil_water_content,
                        General.soil_EC,
                        General.soil_pH,
                        General.soil_nitrogen,
                        General.soil_phosphorus,
                        General.soil_potassium,
                    )
                )
                with open(file_name, "w", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(
                        [
                            "Time",
                            "Temperature",
                            "Water Content",
                            "EC",
                            "pH",
                            "Nitrogen",
                            "Phosphorus",
                            "Potassium",
                        ]
                    )
                    writer.writerows(export)
                    UI_Update.export_UI_update(self, 1)
    except Exception as e:
        print(e, "Export failure, contact Jerry for support")
