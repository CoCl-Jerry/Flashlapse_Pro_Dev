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
        UI_Update.init(self)
        Sensors.init(self)

        # start of imaging activities

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
        self.imaging_live_feed_pushButton.clicked.connect(
            lambda: Call_Thread.livefeed(self)
        )
        self.imaging_start_timelapse_pushButton.clicked.connect(
            lambda: Call_Thread.timelapse(self)
        )

        self.imaging_xAxis_horizontalSlider.valueChanged.connect(
            lambda: Imaging.imaging_AOI_slider_changed(self)
        )
        self.imaging_xAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )

        self.imaging_yAxis_horizontalSlider.valueChanged.connect(
            lambda: Imaging.imaging_AOI_slider_changed(self)
        )
        self.imaging_yAxis_horizontalSlider.sliderReleased.connect(
            lambda: Call_Thread.snapshot(self)
        )
        # end of imaging activities

        # start of motor activities
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
        # end of motor activities

        # start of sensor activities
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

        # end of sensor activities

        # Call_Thread.sensor_init(self)
        # Commands.init()
        #
        # self.Sensor_tabWidget.currentChanged.connect(
        #     lambda: Functions.printci(self))
        #
        # self.frameErgz_pushButton.clicked.connect(
        #     lambda: Commands.motor_toggle(0, self))
        # self.coreErgz_pushButton.clicked.connect(
        #     lambda: Commands.motor_toggle(1, self))
        #
        # self.frameReverse_pushButton.clicked.connect(
        #     lambda: Commands.reverse_motor(0, self))
        # self.coreReverse_pushButton.clicked.connect(
        #     lambda: Commands.reverse_motor(1, self))
        #

        # self.confirmCycle_pushButton.clicked.connect(
        #     lambda: Call_Thread.start_cycle(self))
        # self.onCycle_spinBox.valueChanged.connect(
        #     lambda: Functions.Cycle_Change(self))
        # self.offCycle_spinBox.valueChanged.connect(
        #     lambda: Functions.Cycle_Change(self))
        #
        # self.frame_spinBox.valueChanged.connect(
        #     lambda: Commands.spin_change(0, self))
        # self.core_spinBox.valueChanged.connect(
        #     lambda: Commands.spin_change(1, self))
        #
        # self.frame_verticalSlider.valueChanged.connect(
        #     lambda: Commands.slider_change(0, self))
        # self.core_verticalSlider.valueChanged.connect(
        #     lambda: Commands.slider_change(1, self))
        #
        # self.frame_verticalSlider.sliderReleased.connect(
        #     lambda: Commands.slider_Released())
        # self.core_verticalSlider.sliderReleased.connect(
        #     lambda: Commands.slider_Released())
        #
        # self.sample_doubleSpinBox.valueChanged.connect(
        #     lambda: Functions.sample_change(self))
        #
        # self.link_pushButton.clicked.connect(lambda: UI_Update.link(self))
        #
        # self.Start_spinBox.valueChanged.connect(
        #     lambda: UI_Update.LED_validate(self))
        # self.End_spinBox.valueChanged.connect(
        #     lambda: UI_Update.LED_validate(self))
        #
        # self.IR_pushButton.clicked.connect(lambda: Commands.IR_toggle(self))
        #
        # self.log_pushButton.clicked.connect(
        #     lambda: Functions.sensor_log(self))
        #
        # self.light_Confirm_pushButton.clicked.connect(
        #     lambda: Commands.light_confirm(self))
        # self.light_Reset_pushButton.clicked.connect(
        #     lambda: Commands.light_reset(self))
        #

        #
        # self.fanSpeed_horizontalSlider.sliderReleased.connect(
        #     lambda: Functions.fanspeed_update(self))
        # self.fanSpeed_horizontalSlider.valueChanged.connect(
        #     lambda: UI_Update.fanlabel_update(self))


def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
