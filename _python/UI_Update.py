import General

# initial GUI Update
def init(self):
    if not General.TOF_error:
        self.Rangefinder_data_label.setText(str(General.current_position) + " mm")
    else:
        self.Rangefinder_data_label.setText("Error")
