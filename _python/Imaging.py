import General
import UI_Update


def imaging_sequence_title_changed(self):
    General.imaging_sequence_title = self.imaging_sequence_title_lineEdit.text()
    General.full_storage_directory = (
        General.default_storage_directory + "/" + General.imaging_sequence_title
    )
    self.imaging_storage_directory_label.setText(General.full_storage_directory)
    UI_Update.imaging_validate_input(self)
