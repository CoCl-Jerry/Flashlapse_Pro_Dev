import General
import Communication
import UI_Update

# ---------------------------------------------------------------------------- #


def lighting_confirm(self):
    if (
        self.lighting_inner_ring_checkBox.isChecked()
        and self.lighting_outer_ring_checkBox.isChecked()
    ):
        build_lighting_cmd(3)
    elif self.lighting_inner_ring_checkBox.isChecked():
        build_lighting_cmd(2)
    elif self.lighting_outer_ring_checkBox.isChecked():
        build_lighting_cmd(1)


# ---------------------------------------------------------------------------- #
def lighting_reset(self):
    General.lighting_red = 0
    General.lighting_green = 0
    General.lighting_blue = 0
    General.lighting_brightness = 100
    build_lighting_cmd(0)
    UI_Update.lighting_update(self)


# ---------------------------------------------------------------------------- #
def lighting_adaptive_IR(self):
    Communication.sendCMD("3~" + str(General.lighting_adaptive_IR))
    Communication.sendCMD(
        "4~"+str(int(self.airflow_horizontalSlider.value()*2.55)))


# ---------------------------------------------------------------------------- #
def build_lighting_cmd(mode):
    if mode == 0:
        cmd = "1~0"
    elif mode == 1:
        cmd = (
            "1~1~0~60"
            + "~"
            + str(General.lighting_red)
            + "~"
            + str(General.lighting_green)
            + "~"
            + str(General.lighting_blue)
            + "~"
            + str(General.lighting_brightness)
        )
    elif mode == 2:
        cmd = (
            "1~1~60~108"
            + "~"
            + str(General.lighting_red)
            + "~"
            + str(General.lighting_green)
            + "~"
            + str(General.lighting_blue)
            + "~"
            + str(General.lighting_brightness)
        )
    elif mode == 3:
        cmd = (
            "1~1~0~108"
            + "~"
            + str(General.lighting_red)
            + "~"
            + str(General.lighting_green)
            + "~"
            + str(General.lighting_blue)
            + "~"
            + str(General.lighting_brightness)
        )
    Communication.sendCMD(cmd)
    General.lighting_commands_list.append(cmd)
    Communication.sendCMD("1~2")


def lighting_cycle_nighttime():
    Communication.sendCMD("1~0")


def lighting_cycle_daytime():
    for x in General.lighting_commands_list:
        Communication.sendCMD(x)
    Communication.sendCMD("1~2")
