import General
import UI_Update
from PyQt5.QtWidgets import QFileDialog


def imaging_sequence_title_changed(self):
    General.imaging_sequence_title = self.imaging_sequence_title_lineEdit.text()
    UI_Update.imaging_validate_input(self)


def imaging_add_date(self):
    General.imaging_sequence_title = (
        General.imaging_sequence_title + "_" + General.current_date
    )
    self.imaging_sequence_title_lineEdit.setText(General.imaging_sequence_title)
    UI_Update.imaging_validate_input(self)


def imaging_capture_interval_changed(self):
    General.imaging_capture_interval = self.imaging_capture_interval_spinBox.value()
    UI_Update.imaging_validate_input(self)


def imaging_sequence_duration_changed(self):
    General.imaging_sequence_duration = self.imaging_sequence_duration_spinBox.value()
    UI_Update.imaging_validate_input(self)


def imaging_select_directory_pushButton_clicked(self):
    temp = str(QFileDialog.getExistingDirectory(self, "Select Directory", "/media/pi"))
    if len(temp) != 0:
        General.full_storage_directory = temp + "/" + General.imaging_sequence_title
    UI_Update.imaging_validate_input(self)


def imaging_settings_update(self):
    General.AOI_X = self.imaging_xAxis_horizontalSlider.sliderPosition() / 100
    General.AOI_Y = self.imaging_xAxis_horizontalSlider.sliderPosition() / 100
    General.AOI_W = self.imaging_yAxis_horizontalSlider.sliderPosition() / 100
    General.AOI_H = self.imaging_yAxis_horizontalSlider.sliderPosition() / 100

    General.x_resolution = self.imaging_x_resolution_spinBox.value()
    General.y_resolution = self.imaging_y_resolution_spinBox.value()
