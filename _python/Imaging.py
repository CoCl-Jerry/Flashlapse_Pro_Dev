import General
import UI_Update


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