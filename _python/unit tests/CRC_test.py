# def crc16_generator_hex(data: list[int]) -> str:
#     """CRC-16-MODBUS Hex Algorithm
#     Parameters
#     ----------
#     data : list[int]
#         Data packets received.
#     Returns
#     -------
#     str
#         CRC as hex string

#     Raises
#     ----------
#     ValueError
#         If data packet in each index contains a byte > 256
#     """
#     data = bytearray(data)
#     crc = 0xFFFF

#     # Calculate CRC-16 checksum for data packet
#     for b in data:
#         crc ^= b
#         for _ in range(0, 8):
#             bcarry = crc & 0x0001
#             crc >>= 1
#             if bcarry:
#                 crc ^= 0xA001
#     msb = crc >> 0x08 & 0xFF
#     lsb = crc & 0xFF
#     crc_to_send = [hex(lsb), hex(msb)]
#     print(crc_to_send)

#     return crc_to_send


# def hexListConvert(data):
#     hex_bytes = bytes.fromhex(data)

#     print(hex_bytes)  # Output: b'\xde\xad\xbe\xef'

#     hex_list = list(hex_bytes)
#     print(hex_list)  # Output: [222, 173, 190, 239]

#     return hex_list


# if __name__ == "__main__":
#     data = "01030e08b7082300e400380066001d00478c0b"
#     temp_list = hexListConvert(data)
#     highbit = temp_list.pop()
#     lowbit = temp_list.pop()
#     print("L:", lowbit, "H:", highbit)
#     crc_list = crc16_generator_hex(temp_list)
#     if (highbit == crc_list[1]) and (lowbit == crc_list[0]):
#         print("True")
#     # if crc16_generator_hex(hexListConvert(data)) == hex(0x8C0B):
#     #     print("True")
