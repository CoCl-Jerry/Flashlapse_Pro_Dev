import General
import UI_Update
import Imaging
import Sensors
import Functions

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
        Sensors.init(self)

        # start of imaging activities

        self.imaging_sequence_title_lineEdit.textChanged.connect(
            lambda: Imaging.imaging_sequence_title_changed(self)
        )
        # self.addDate_pushButton.clicked.connect(
        #     lambda: Functions.add_date(self))

        # self.ICI_spinBox.valueChanged.connect(
        #     lambda: Functions.ICI_Change(self))
        # self.ISD_spinBox.valueChanged.connect(
        #     lambda: Functions.ISD_Change(self))
        # self.directory_pushButton.clicked.connect(
        #     lambda: Functions.select_directory(self))

        # self.x_resolution_spinBox.valueChanged.connect(
        #     lambda: Functions.camera_update(self))
        # self.y_resolution_spinBox.valueChanged.connect(
        #     lambda: Functions.camera_update(self))

        # self.xAxis_horizontalSlider.valueChanged.connect(
        #     lambda: Functions.camera_update(self))
        # self.xAxis_horizontalSlider.sliderReleased.connect(
        #     lambda: Call_Thread.start_snapshot(self))

        # self.yAxis_horizontalSlider.valueChanged.connect(
        #     lambda: Functions.camera_update(self))
        # self.yAxis_horizontalSlider.sliderReleased.connect(
        #     lambda: Call_Thread.start_snapshot(self))

        # self.JPG_radioButton.toggled.connect(
        #     lambda: Functions.update_mode(self))
        # self.infraredImaging_checkBox.stateChanged.connect(
        #     lambda: Functions.IR_mode(self))

        # start of motor activities
        self.TOF_update_pushButton.clicked.connect(lambda: Sensors.TOF_range(self))
        self.up_pushButton.clicked.connect(
            lambda: Functions.postion_increment(self, False)
        )
        self.down_pushButton.clicked.connect(
            lambda: Functions.postion_increment(self, True)
        )
        self.motion_stop_pushButton.clicked.connect(lambda: Functions.disable_motor())
        # start of slider activities
        self.motion_position_verticalSlider.valueChanged.connect(
            lambda: UI_Update.motion_slider_value_changed(self)
        )
        self.motion_position_verticalSlider.sliderReleased.connect(
            lambda: Functions.move_to_position(self)
        )
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: UI_Update.motion_spinbox_value_changed(self)
        )
        self.motion_new_position_spinBox.valueChanged.connect(
            lambda: Functions.move_to_position(self)
        )
        self.motion_speed_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )
        self.motion_torque_dial.valueChanged.connect(
            lambda: UI_Update.motion_dials_update(self)
        )
        # end of motor activities

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
        # self.snapshot_pushButton.clicked.connect(
        #     lambda: Call_Thread.start_snapshot(self))
        # self.startImaging_pushButton.clicked.connect(
        #     lambda: Call_Thread.start_timelapse(self))
        # self.preview_pushButton.clicked.connect(
        #     lambda: Call_Thread.start_preview(self))
        #
        # self.rotate_pushButton.clicked.connect(
        #     lambda: Functions.rotate_image(self))
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
