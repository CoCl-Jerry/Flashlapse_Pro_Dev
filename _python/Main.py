import General
import UI_Update
import Imaging
import Sensors
import Motion
import Call_Thread
import Communication
import Lighting

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
        UI_Update.init(self)
        Sensors.init(self)
        Communication.reset_arduino()

        # ---------------------------------------------------------------------------- #
        #                         start of lighting activities                         #
        # ---------------------------------------------------------------------------- #
        self.lighting_brightness_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.lighting_horizontalSlider_changed(self)
        )

        self.lighting_red_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.lighting_horizontalSlider_changed(self)
        )

        self.lighting_green_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.lighting_horizontalSlider_changed(self)
        )

        self.lighting_blue_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.lighting_horizontalSlider_changed(self)
        )

        self.lighting_brightness_spinBox.valueChanged.connect(
            lambda: UI_Update.lighting_spinbox_changed(self)
        )
        self.lighting_red_spinBox.valueChanged.connect(
            lambda: UI_Update.lighting_spinbox_changed(self)
        )
        self.lighting_green_spinBox.valueChanged.connect(
            lambda: UI_Update.lighting_spinbox_changed(self)
        )
        self.lighting_blue_spinBox.valueChanged.connect(
            lambda: UI_Update.lighting_spinbox_changed(self)
        )

        self.lighting_confirm_pushButton.clicked.connect(
            lambda: Lighting.lighting_confirm(self)
        )
        self.lighting_reset_pushButton.clicked.connect(
            lambda: Lighting.lighting_reset(self)
        )

        self.lighting_adaptive_IR_pushButton.clicked.connect(
            lambda: UI_Update.lighting_adaptive_IR_toggle(self)
        )

        self.lighting_start_cycle_pushButton.clicked.connect(
            lambda: Call_Thread.lighting_cycle(self)
        )
        # ---------------------------------------------------------------------------- #
        #                          start of imaging activities                         #
        # ---------------------------------------------------------------------------- #
        self.imaging_sequence_title_lineEdit.textChanged.connect(
            lambda: Imaging.imaging_sequence_title_changed(self)
        )

        self.imaging_add_date_pushButton.clicked.connect(
            lambda: Imaging.imaging_add_date(self)
        )

        self.imaging_capture_interval_spinBox.valueChanged.connect(
            lambda: Imaging.imaging_capture_interval_changed(self)
        )

        self.imaging_sequence_duration_spinBox.valueChanged.connect(
            lambda: Imaging.imaging_sequence_duration_changed(self)
        )
        self.imaging_select_directory_pushButton.clicked.connect(
            lambda: Imaging.imaging_select_directory_pushButton_clicked(self)
        )
        self.imaging_snapshot_pushButton.clicked.connect(
            lambda: Call_Thread.snapshot(self)
        )
        self.imaging_preview_pushButton.clicked.connect(
            lambda: Call_Thread.preview(self)
        )
        self.imaging_rotate_pushButton.clicked.connect(
            lambda: Imaging.imaging_rotate_image_pushButton_clicked(self)
        )
        self.imaging_live_feed_pushButton.clicked.connect(
            lambda: Call_Thread.livefeed(self)
        )
        self.imaging_start_timelapse_pushButton.clicked.connect(
            lambda: Call_Thread.timelapse(self)
        )
        self.imaging_xAxis_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.imaging_AOI_horizontalSlider_changed(self)
        )
        self.imaging_xAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )
        self.imaging_yAxis_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.imaging_AOI_horizontalSlider_changed(self)
        )
        self.imaging_yAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )

        # ---------------------------------------------------------------------------- #
        #                           start of motion activities                          #
        # ---------------------------------------------------------------------------- #
        self.TOF_update_pushButton.clicked.connect(lambda: Sensors.TOF_range(self))
        self.up_pushButton.clicked.connect(
            lambda: Motion.postion_increment(self, False)
        )
        self.down_pushButton.clicked.connect(
            lambda: Motion.postion_increment(self, True)
        )
        self.motion_stop_pushButton.clicked.connect(lambda: Motion.disable_motor())
        self.motion_position_verticalSlider.valueChanged.connect(
            lambda: UI_Update.motion_slider_value_changed(self)
        )
        self.motion_position_verticalSlider.sliderReleased.connect(
            lambda: Motion.move_to_position(self)
        )
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: UI_Update.motion_spinbox_value_changed(self)
        )
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: Motion.move_to_position(self)
        )
        self.motion_speed_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )
        self.motion_torque_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )
        self.airflow_horizontalSlider.sliderReleased.connect(
            lambda: Motion.airflow_update(self)
        )
        self.airflow_horizontalSlider.valueChanged.connect(
            lambda: UI_Update.airflow_slider_changed(self)
        )
        # ---------------------------------------------------------------------------- #
        #                      start of ambient sensor activities                      #
        # ---------------------------------------------------------------------------- #
        self.ambient_sensors_tabWidget.currentChanged.connect(
            lambda: UI_Update.ambient_sensor_tab_update(self)
        )
        self.start_ambient_sensors_pushButton.clicked.connect(
            lambda: Call_Thread.ambient_sensors(self)
        )
        self.ambient_temperature_offset_pushButton.clicked.connect(
            lambda: Sensors.ambient_temperature_offset(self)
        )
        self.ambient_humidity_offset_pushButton.clicked.connect(
            lambda: Sensors.ambient_humidity_offset(self)
        )
        self.ambient_co2_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_co2_calibration(self)
        )
        self.ambient_co2_reset_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_reset_calibration(self)
        )
        self.ambient_o2_reset_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 0)
        )
        self.ambient_o2_21_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 1)
        )
        self.ambient_o2_100_calibration_pushButton.clicked.connect(
            lambda: Sensors.ambient_o2_calibration(self, 2)
        )

        # ---------------------------------------------------------------------------- #
        #                        start of soil sensor activities                       #
        # ---------------------------------------------------------------------------- #
        self.soil_sensors_tabWidget.currentChanged.connect(
            lambda: UI_Update.soil_sensors_tab_update(self)
        )
        self.start_soil_sensors_pushButton.clicked.connect(
            lambda: Call_Thread.soil_sensors(self)
        )
        self.sensor_set_interval_pushButton.clicked.connect(
            lambda: Sensors.sensor_set_interval(self)
        )
        self.soil_temperature_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_water_content_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_EC_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_pH_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_nitrogen_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_phosphorus_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        self.soil_potassium_offset_pushButton.clicked.connect(
            lambda: Sensors.soil_sensor_offset(self)
        )
        # ---------------------------------------------------------------------------- #
        #                          start of export activities                          #
        # ---------------------------------------------------------------------------- #
        self.mainwindow_tabWidget.currentChanged.connect(
            lambda: UI_Update.mainwindow_tab_update(self)
        )
        self.sensor_export_data_pushButton.clicked.connect(
            lambda: Sensors.sensor_export_data(self)
        )


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
