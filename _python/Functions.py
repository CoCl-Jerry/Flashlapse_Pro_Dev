import General
import UI_Update
import Call_Thread

import smbus


def postion_increment(self, direction):
    if (
        direction
        and General.current_position + self.motion_increment_spinBox.value()
        <= General.max_position
    ):
        General.target_position = (
            General.current_position + self.motion_increment_spinBox.value()
        )

    elif(not direction
        and General.current_position - self.motion_increment_spinBox.value()
        >= General.min_position):
        General.target_position = (
            General.current_position - self.motion_increment_spinBox.value()
        )
    else:
        return
    General.target_direction = direction
    UI_Update.motion_target_position_setting_label_update(self)
    Call_Thread.motion(self)
    build_cmd = "2~1~" + str(int(direction)) + "~64~100"
    sendCMD(build_cmd)


def disable_motor():
    General.motion_thread_running = False
    build_cmd = "2~0~1"
    sendCMD(build_cmd)


def sendCMD(cont):
    print("sending command...\n" + cont)
    temp = cont + "\n"
    while True:
        try:
            bus = smbus.SMBus(1)
            converted = []
            for b in temp:
                converted.append(ord(b))
            bus.write_i2c_block_data(0x08, 0x5E, converted)
            break
        except Exception as e:
            print(e, "I2c command send failure,contact Jerry for support")
        pass
