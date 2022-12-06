import General

# TOF label update
def TOF_update(self):
    if not General.TOF_error:
        self.motion_rangefinder_data_label.setText(
            str(General.current_position) + " mm"
        )
        self.position_verticalSlider.setValue(General.current_position)
    else:
        self.motion_rangefinder_data_label.setText("Range Finder Error")


def TOF_update_pushButton_toggle(self,status):
    self.TOF_update_pushButton.setEnabled(status)
    # self.TOF_update_pushButton.setEnabled(not self.TOF_update_pushButton.isEnabled())
    print(self.TOF_update_pushButton.isEnabled())


# motion UI update


def motion_frames_toggle(self):
    self.motion_control_frame.setEnabled(not self.motion_control_frame.isEnabled())
    self.motion_slider_frame.setEnabled(not self.motion_slider_frame.isEnabled())
    print(self.motion_control_frame.isEnabled())
    print(self.motion_slider_frame.isEnabled())

def motion_target_position_setting_label_update(self):
    self.motion_target_position_setting_label.setText(
        str(General.target_position) + " mm"
    )
