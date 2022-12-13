import General
import UI_Update
import Call_Thread
import Communication

# ---------------------------------------------------------------------------- #
def postion_increment(self, direction):
    if (
        direction
        and General.current_position + self.motion_increment_spinBox.value()
        <= General.max_position
    ):
        General.target_position = (
            General.current_position + self.motion_increment_spinBox.value()
        )

    elif (
        not direction
        and General.current_position - self.motion_increment_spinBox.value()
        >= General.min_position
    ):
        General.target_position = (
            General.current_position - self.motion_increment_spinBox.value()
        )
    else:
        return
    UI_Update.motion_target_position_setting_update(self)
    Call_Thread.motion(self)
    General.target_direction = direction
    build_motion_cmd(self)


# ---------------------------------------------------------------------------- #
def move_to_position(self):
    Call_Thread.motion(self)
    if General.target_position > General.current_position:
        General.target_direction = True
    else:
        General.target_direction = False
    build_motion_cmd(self)


# ---------------------------------------------------------------------------- #
def build_motion_cmd(self):
    cmd = (
        "2~1~"
        + str(int(General.target_direction))
        + "~"
        + str(General.motor_interval)
        + "~"
        + str(2 ** (9 - self.motion_speed_dial.value()))
        + "~"
        + str((self.motion_torque_dial.value() * 100))
    )
    Communication.sendCMD(cmd)


# ---------------------------------------------------------------------------- #
def disable_motor():
    General.motion_thread_running = False
    build_cmd = "2~0~1"
    Communication.sendCMD(build_cmd)

# ---------------------------------------------------------------------------- #
def airflow_update(self):
    Communication.sendCMD("4~"+str(int(self.airflow_horizontalSlider.value()*2.55)))