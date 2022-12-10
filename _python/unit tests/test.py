import time
import serial


# ser = serial.Serial(
#     port="/dev/ttyUSB0",
#     baudrate=4800,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1,
# )

bt = [0x01, 0x03, 0x02, 0x00, 0x00, 0x07, 0x05, 0xB0]
# bt = [0x01,0x03,0x00, 0x1e, 0x00, 0x01, 0xb5, 0x0cc]
# bt =[0xfe, 0x86, 0x9e, 0xfe, 0xfe, 0x06, 0x66, 0xfe, 0x18]

req_b = bytes(bt)
print("TEST:", bt)

line = []

while True:
    ser = serial.Serial(
        port="/dev/ttyS0",
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
    )
    ser.write(bt)
    line = ser.readline()
    ser.flushInput()
    print(line.hex())
    time.sleep(2)
    ser.close()
