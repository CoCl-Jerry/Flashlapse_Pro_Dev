# load in sensors
import board  # type: ignore
import adafruit_vl53l4cd  # type: ignore
import adafruit_scd4x  # type: ignore
from DFRobot_EOxygenSensor import *

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
def extractor(hex_string):
    length = len(hex_string.strip())
    FDN = 6  # first disposable number of bits
    LDN = 0  # last disposable number of bits
    data_segment_bits = 4  # all bits for the data including the first bit
    data_area_len = length - (FDN + LDN)
    first_data_bit_index = length - (data_area_len + LDN)
    loop_num = int(data_area_len / data_segment_bits)

    # '''
    # INDEX) [DATA KEY]: following response frame format
    # 0) Temperature value
    # 1) Water content
    # 2) EC value
    # 3) PH value
    # 4) nitrogen content
    # 5) phosphorus value
    # 6) Potassium value
    # '''
    keyValues = [
        "TemperatureValue",
        "WaterContent",
        "ECValue",
        "PHValue",
        "NitrogenValue",
        "PhosphorusValue",
        "PotassiumValue",
        "CRC16",
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
def hexListConvert(data: str):

    hex_bytes = bytes.fromhex(data)  # Takes a hex string and turns it into a byte array
    #  print(hex_bytes)  # Output: b'\xde\xad\xbe\xef'
    hex_list = list(hex_bytes)
    print(hex_list)

    return hex_list
