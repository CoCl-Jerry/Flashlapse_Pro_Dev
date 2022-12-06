import General

# TOF label update
def TOF_update(self):
    if not General.TOF_error:
        self.motion_rangefinder_data_label.setText(str(General.current_position) + " mm")
        self.position_verticalSlider.setValue(General.current_position)
    else:
        self.motion_rangefinder_data_label.setText("Range Finder Error")

def TOF_update_pushButton_toggle(self):
    self.TOF_update_pushButton.setEnabled( False)

# motion UI update 

def motion_control_frame_toggle(self):
    self.motion_control_frame.setEnabled( self.motion_control_frame.isEnabled())

def motion_target_position_setting_label_update(self):
    self.motion_target_position_setting_label.setText(str(General.target_position) + " mm")


    