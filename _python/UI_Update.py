import General
from PyQt5.QtGui import QImage, QPixmap

# start of error UI update
def error_UI_update(self):
    if General.camera_error:
        self.imaging_preview_frame.setPixmap(QPixmap(General.camera_error_image))
        General.camera_error = False
    if General.communication_error:
        self.imaging_preview_frame.setPixmap(QPixmap(General.communication_error_image))
        General.communication_error = False


# end of error UI update

# start of TOF UI update
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


#  end of TOF UI update

# start of imaging UI update


def imaging_validate_input(self):
    General.full_storage_directory = (
        General.default_storage_directory + "/" + General.imaging_sequence_title
    )
    self.imaging_storage_directory_label.setText(General.full_storage_directory)
    if General.current_date not in General.imaging_sequence_title:
        self.imaging_add_date_pushButton.setEnabled(True)
    else:
        self.imaging_add_date_pushButton.setEnabled(False)

    if len(General.imaging_sequence_title) == 0:
        self.imaging_add_date_pushButton.setEnabled(False)

    General.imaging_capture_total = int(
        General.imaging_sequence_duration / General.imaging_capture_interval
    )

    if General.imaging_capture_total > 0 and len(General.imaging_sequence_title) != 0:
        self.imaging_start_timelapse_pushButton.setEnabled(True)
    else:
        self.imaging_start_timelapse_pushButton.setEnabled(False)
    self.imaging_progress_Label.setText(
        "Progress: "
        + str(General.current_image_counter)
        + "/"
        + str(General.imaging_capture_total)
    )
    self.imaging_progress_bar.setValue(General.current_image_counter)


def imaging_frame_toggle(self):
    self.imaging_capture_frame.setEnabled(not self.imaging_capture_frame.isEnabled())


def update_preview_frame(self, file):
    if not General.camera_error:
        self.imaging_progress_Label.setText(
            "Progress: "
            + str(General.current_image_counter)
            + "/"
            + str(General.imaging_capture_total)
        )
        self.imaging_progress_bar.setValue(General.current_image_counter)
        self.imaging_preview_frame.setPixmap(QPixmap(QImage(file)))


def timelapse_UI_update(self):
    if General.timelapse_thread_running:
        self.imaging_start_timelapse_pushButton.setText("END TIMELAPSE")
    else:
        self.imaging_start_timelapse_pushButton.setText("START TIMELAPSE")
    General.current_image_counter = 0


def timelapse_countdown(self):
    self.imaging_countdown_label.setText(
        "Next Image: " + str(General.imaging_countdown_value) + " s"
    )


# end of imaging UI update

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


# end of motion UI update
