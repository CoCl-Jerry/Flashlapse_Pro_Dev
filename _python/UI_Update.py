import General

# TOF label update
def TOF_update(self):
    if not General.TOF_error:
        self.rangefinder_data_label.setText(str(General.current_position) + " mm")
    else:
        self.rangefinder_data_label.setText("Range Finder Error")