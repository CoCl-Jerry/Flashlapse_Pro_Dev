import General
import UI_Update
import Imaging
import Sensors
import Motion
import Call_Thread

# import Commands
# import Threads

# import Functions
# import Call_Thread
# import os
# import time

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

import Flashlapse_Pro_UI


class MainWindow(QMainWindow, Flashlapse_Pro_UI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)

        General.init()
        UI_Update.graph_init(self)
        Sensors.init(self)

        # ---------------------------------------------------------------------------- #
        #                          start of imaging activities                         #
        # ---------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------- #
        self.imaging_sequence_title_lineEdit.textChanged.connect(
            lambda: Imaging.imaging_sequence_title_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_add_date_pushButton.clicked.connect(
            lambda: Imaging.imaging_add_date(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_capture_interval_spinBox.valueChanged.connect(
            lambda: Imaging.imaging_capture_interval_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_sequence_duration_spinBox.valueChanged.connect(
            lambda: Imaging.imaging_sequence_duration_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_select_directory_pushButton.clicked.connect(
            lambda: Imaging.imaging_select_directory_pushButton_clicked(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_snapshot_pushButton.clicked.connect(
            lambda: Call_Thread.snapshot(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_preview_pushButton.clicked.connect(
            lambda: Call_Thread.preview(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_rotate_pushButton.clicked.connect(
            lambda: Imaging.imaging_rotate_image_pushButton_clicked(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_live_feed_pushButton.clicked.connect(
            lambda: Call_Thread.livefeed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_start_timelapse_pushButton.clicked.connect(
            lambda: Call_Thread.timelapse(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_xAxis_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.imaging_AOI_slider_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_xAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_yAxis_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.imaging_AOI_slider_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.imaging_yAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )

        # ---------------------------------------------------------------------------- #
        #                           start of motor activities                          #
        # ---------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------- #
        self.TOF_update_pushButton.clicked.connect(lambda: Sensors.TOF_range(self))
        # ---------------------------------------------------------------------------- #
        self.up_pushButton.clicked.connect(
            lambda: Motion.postion_increment(self, False)
        )
        # ---------------------------------------------------------------------------- #
        self.down_pushButton.clicked.connect(
            lambda: Motion.postion_increment(self, True)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_stop_pushButton.clicked.connect(lambda: Motion.disable_motor())
        # ---------------------------------------------------------------------------- #
        self.motion_position_verticalSlider.valueChanged.connect(
            lambda: UI_Update.motion_slider_value_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_position_verticalSlider.sliderReleased.connect(
            lambda: Motion.move_to_position(self)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: UI_Update.motion_spinbox_value_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: Motion.move_to_position(self)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_speed_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )
        # ---------------------------------------------------------------------------- #
        self.motion_torque_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )

        # ---------------------------------------------------------------------------- #
        #                      start of ambient sensor activities                      #
        # ---------------------------------------------------------------------------- #
        # ---------------------------------------------------------------------------- #
        self.start_ambient_sensors_pushButton.clicked.connect(
            lambda: Call_Thread.ambient_sensors(self)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_temperature_offset_pushButton.clicked.connect(
            lambda: Sensors.ambient_temperature_offset(self)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_humidity_offset_pushButton.clicked.connect(
            lambda: Sensors.ambient_humidity_offset(self)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_co2_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_co2_calibration(self)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_o2_reset_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 0)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_o2_21_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 1)
        )
        # ---------------------------------------------------------------------------- #
        self.ambient_o2_100_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 2)
        )

        # ---------------------------------------------------------------------------- #
        #                        start of soil sensor activities                       #
        # ---------------------------------------------------------------------------- #
        self.start_soil_sensors_pushButton.clicked.connect(
            lambda: Call_Thread.soil_sensors(self)
        )


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
