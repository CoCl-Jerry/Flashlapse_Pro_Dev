import General
import smbus  # type: ignore

# ------------------ for sending i2c commands to the arduino ----------------- #
# def sendCMD(cont):
#     print("sending command...\n" + cont)
#     temp = cont + "\n"
#     while True:
#         try:
#             bus = smbus.SMBus(1)
#             converted = []
#             for b in temp:
#                 converted.append(ord(b))
#             bus.write_i2c_block_data(0x08, 0x5E, converted)
#             break
#         except Exception as e:
#             General.communication_error = True
#             print(e, "communication failure,contact Jerry for support")
#         pass


def sendCMD(cont):
    print("sending command...\n" + cont)
    temp = cont + "\n"
    try:
        bus = smbus.SMBus(1)
        converted = []
        for b in temp:
            converted.append(ord(b))
        bus.write_i2c_block_data(0x08, 0x5E, converted)
    except Exception as e:
        General.communication_error = True
        print(e, "i2c Communication error, skipping command")


def reset_arduino():
    sendCMD("0")
