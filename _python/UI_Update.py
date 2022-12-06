import General

# TOF label update
def TOF_update(self):
    if not General.TOF_error:
        self.motion_rangefinder_data_label.setText(
            str(int(General.current_position)) + " mm"
        )
        if General.target_position == 0:
            General.target_position = General.current_position
            motion_target_position_setting_update(self)
    else:
        self.motion_rangefinder_data_label.setText("Range Finder Error")


def TOF_update_pushButton_toggle(self):
    self.TOF_update_pushButton.setEnabled(not self.TOF_update_pushButton.isEnabled())


# TOF_update complete

# motion UI update
def motion_frames_toggle(self):
    self.motion_control_frame.setEnabled(not self.motion_control_frame.isEnabled())
    self.motion_slider_frame.setEnabled(not self.motion_slider_frame.isEnabled())
    self.motion_settings_frame.setEnabled(not self.motion_settings_frame.isEnabled())


def motion_target_position_setting_update(self):
    self.motion_target_position_setting_label.setText(
        str(int(General.target_position)) + " mm"
    )

    self.motion_position_verticalSlider.blockSignals(True)
    self.motion_new_position_spinBox.blockSignals(True)

    self.motion_position_verticalSlider.setValue(General.target_position)
    self.motion_new_position_spinBox.setValue(General.target_position)

    self.motion_new_position_spinBox.blockSignals(False)
    self.motion_position_verticalSlider.blockSignals(False)


def motion_slider_value_changed(self):
    General.target_position = self.motion_position_verticalSlider.value()
    motion_target_position_setting_update(self)


def motion_spinbox_value_changed(self):
    General.target_position = self.motion_new_position_spinBox.value()
    motion_target_position_setting_update(self)


def motion_dials_update(self):
    self.motion_speed_dial_value_label.setText(
        "Speed Level: " + str(self.motion_speed_dial.value())
    )
    self.motion_torque_dial_value_label.setText(
        "Torque Level: " + str(self.motion_torque_dial.value())
    )
