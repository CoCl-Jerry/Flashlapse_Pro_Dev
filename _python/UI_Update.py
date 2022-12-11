import General
import Lighting
from PyQt5.QtGui import QImage, QPixmap
from pyqtgraph import mkPen  # type: ignore

# ---------------------------------------------------------------------------- #
#                             graph initialization                             #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def graph_init(self):
    styles = {"color": "r", "font-size": "15px"}

    self.ambient_temperature_graphWidget.setBackground("#fbfbfb")
    self.ambient_temperature_graphWidget.showGrid(x=True, y=True)
    self.ambient_temperature_graphWidget.setLabel("left", "Temperature (°C)", **styles)
    self.ambient_temperature_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.ambient_humidity_graphWidget.setBackground("#fbfbfb")
    self.ambient_humidity_graphWidget.showGrid(x=True, y=True)
    self.ambient_humidity_graphWidget.setLabel("left", "Humidity (%)", **styles)
    self.ambient_humidity_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.ambient_co2_graphWidget.setBackground("#fbfbfb")
    self.ambient_co2_graphWidget.showGrid(x=True, y=True)
    self.ambient_co2_graphWidget.setLabel("left", "Carbon Dioxide (PPM)", **styles)
    self.ambient_co2_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.ambient_o2_graphWidget.setBackground("#fbfbfb")
    self.ambient_o2_graphWidget.showGrid(x=True, y=True)
    self.ambient_o2_graphWidget.setLabel("left", "Oxygen (%)", **styles)
    self.ambient_o2_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_temperature_graphWidget.setBackground("#fbfbfb")
    self.soil_temperature_graphWidget.showGrid(x=True, y=True)
    self.soil_temperature_graphWidget.setLabel("left", "Oxygen (%)", **styles)
    self.soil_temperature_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_water_content_graphWidget.setBackground("#fbfbfb")
    self.soil_water_content_graphWidget.showGrid(x=True, y=True)
    self.soil_water_content_graphWidget.setLabel("left", "Water Content (%)", **styles)
    self.soil_water_content_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_EC_graphWidget.setBackground("#fbfbfb")
    self.soil_EC_graphWidget.showGrid(x=True, y=True)
    self.soil_EC_graphWidget.setLabel(
        "left", "Electrical Conductivity (μS/cm)", **styles
    )
    self.soil_EC_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_pH_graphWidget.setBackground("#fbfbfb")
    self.soil_pH_graphWidget.showGrid(x=True, y=True)
    self.soil_pH_graphWidget.setLabel("left", "pH", **styles)
    self.soil_pH_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_nitrogen_graphWidget.setBackground("#fbfbfb")
    self.soil_nitrogen_graphWidget.showGrid(x=True, y=True)
    self.soil_nitrogen_graphWidget.setLabel("left", "Nitrogen (mg/kg)", **styles)
    self.soil_nitrogen_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_phosphorus_graphWidget.setBackground("#fbfbfb")
    self.soil_phosphorus_graphWidget.showGrid(x=True, y=True)
    self.soil_phosphorus_graphWidget.setLabel("left", "Phosphorus (mg/kg)", **styles)
    self.soil_phosphorus_graphWidget.setLabel("bottom", "Time (s)", **styles)

    self.soil_potassium_graphWidget.setBackground("#fbfbfb")
    self.soil_potassium_graphWidget.showGrid(x=True, y=True)
    self.soil_potassium_graphWidget.setLabel("left", "Potassium (mg/kg)", **styles)
    self.soil_potassium_graphWidget.setLabel("bottom", "Time (s)", **styles)


# ---------------------------------------------------------------------------- #
#                                error UI update                               #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def error_UI_update(self):
    if General.camera_error:
        self.imaging_preview_frame.setPixmap(QPixmap(General.camera_error_image))
        General.camera_error = False
    if General.communication_error:
        self.imaging_preview_frame.setPixmap(QPixmap(General.communication_error_image))
        General.communication_error = False


# ---------------------------------------------------------------------------- #
#                              lighting UI update                              #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def lighting_horizontalSlider_changed(self):
    lighting_spinbox_block_signals(self)

    General.lighting_brightness = self.lighting_brightness_horizontalSlider.value()
    General.lighting_red = self.lighting_red_horizontalSlider.value()
    General.lighting_green = self.lighting_green_horizontalSlider.value()
    General.lighting_blue = self.lighting_blue_horizontalSlider.value()

    self.lighting_brightness_spinBox.setValue(General.lighting_brightness)
    self.lighting_red_spinBox.setValue(General.lighting_red)
    self.lighting_green_spinBox.setValue(General.lighting_green)
    self.lighting_blue_spinBox.setValue(General.lighting_blue)

    lighting_spinbox_unblock_signals(self)


# ---------------------------------------------------------------------------- #
def lighting_spinbox_changed(self):
    lighting_horizontalSlider_block_signals(self)

    General.lighting_brightness = self.lighting_brightness_spinBox.value()
    General.lighting_red = self.lighting_red_spinBox.value()
    General.lighting_green = self.lighting_green_spinBox.value()
    General.lighting_blue = self.lighting_blue_spinBox.value()

    self.lighting_brightness_horizontalSlider.setValue(General.lighting_brightness)
    self.lighting_red_horizontalSlider.setValue(General.lighting_red)
    self.lighting_green_horizontalSlider.setValue(General.lighting_green)
    self.lighting_blue_horizontalSlider.setValue(General.lighting_blue)

    lighting_horizontalSlider_unblock_signals(self)


# ---------------------------------------------------------------------------- #
def lighting_update(self):
    lighting_spinbox_block_signals(self)
    lighting_horizontalSlider_block_signals(self)

    self.lighting_brightness_horizontalSlider.setValue(General.lighting_brightness)
    self.lighting_red_horizontalSlider.setValue(General.lighting_red)
    self.lighting_green_horizontalSlider.setValue(General.lighting_green)
    self.lighting_blue_horizontalSlider.setValue(General.lighting_blue)
    self.lighting_brightness_spinBox.setValue(General.lighting_brightness)
    self.lighting_red_spinBox.setValue(General.lighting_red)
    self.lighting_green_spinBox.setValue(General.lighting_green)
    self.lighting_blue_spinBox.setValue(General.lighting_blue)

    lighting_spinbox_unblock_signals(self)
    lighting_horizontalSlider_unblock_signals(self)


# ---------------------------------------------------------------------------- #
def lighting_spinbox_block_signals(self):
    self.lighting_brightness_spinBox.blockSignals(True)
    self.lighting_red_spinBox.blockSignals(True)
    self.lighting_green_spinBox.blockSignals(True)
    self.lighting_blue_spinBox.blockSignals(True)


# ---------------------------------------------------------------------------- #
def lighting_spinbox_unblock_signals(self):
    self.lighting_brightness_spinBox.blockSignals(False)
    self.lighting_red_spinBox.blockSignals(False)
    self.lighting_green_spinBox.blockSignals(False)
    self.lighting_blue_spinBox.blockSignals(False)


# ---------------------------------------------------------------------------- #
def lighting_horizontalSlider_block_signals(self):
    self.lighting_brightness_horizontalSlider.blockSignals(True)
    self.lighting_red_horizontalSlider.blockSignals(True)
    self.lighting_green_horizontalSlider.blockSignals(True)
    self.lighting_blue_horizontalSlider.blockSignals(True)


# ---------------------------------------------------------------------------- #
def lighting_horizontalSlider_unblock_signals(self):
    self.lighting_brightness_horizontalSlider.blockSignals(False)
    self.lighting_red_horizontalSlider.blockSignals(False)
    self.lighting_green_horizontalSlider.blockSignals(False)
    self.lighting_blue_horizontalSlider.blockSignals(False)


# ---------------------------------------------------------------------------- #
def lighting_adaptive_IR_toggle(self):
    if not General.lighting_adaptive_IR:
        self.lighting_adaptive_IR_pushButton.setText("Adaptive IR: OFF")
        General.lighting_adaptive_IR = 1
    else:
        self.lighting_adaptive_IR_pushButton.setText("Adaptive IR: ON")
        General.lighting_adaptive_IR = 0
    Lighting.lighting_adaptive_IR()


# ---------------------------------------------------------------------------- #
#                               motion UI update                               #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
def TOF_update_pushButton_toggle(self):
    self.TOF_update_pushButton.setEnabled(not self.TOF_update_pushButton.isEnabled())


# ---------------------------------------------------------------------------- #
def motion_frames_toggle(self):
    self.motion_control_frame.setEnabled(not self.motion_control_frame.isEnabled())
    self.motion_horizontalSlider_frame.setEnabled(
        not self.motion_horizontalSlider_frame.isEnabled()
    )
    self.motion_settings_frame.setEnabled(not self.motion_settings_frame.isEnabled())


# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
def motion_horizontalSlider_value_changed(self):
    General.target_position = self.motion_position_verticalSlider.value()
    motion_target_position_setting_update(self)


# ---------------------------------------------------------------------------- #
def motion_spinbox_value_changed(self):
    General.target_position = self.motion_new_position_spinBox.value()
    motion_target_position_setting_update(self)


# ---------------------------------------------------------------------------- #
def motion_dials_update(self):
    self.motion_speed_dial_value_label.setText(
        "Speed Level: " + str(self.motion_speed_dial.value())
    )
    self.motion_torque_dial_value_label.setText(
        "Torque Level: " + str(self.motion_torque_dial.value())
    )


# ---------------------------------------------------------------------------- #
#                               imaging UI update                              #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
def imaging_frame_toggle(self):
    self.imaging_capture_frame.setEnabled(not self.imaging_capture_frame.isEnabled())


# ---------------------------------------------------------------------------- #
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


# ---------------------------------------------------------------------------- #
def timelapse_UI_update(self):
    if General.timelapse_thread_running:
        self.imaging_start_timelapse_pushButton.setText("END TIMELAPSE")
    else:
        self.imaging_start_timelapse_pushButton.setText("START TIMELAPSE")
        General.current_image_counter = 0
        General.imaging_countdown_value = 0
        timelapse_countdown(self)
        imaging_validate_input(self)


# ---------------------------------------------------------------------------- #
def timelapse_countdown(self):
    self.imaging_countdown_label.setText(
        "Next Image: " + str(General.imaging_countdown_value) + " s"
    )


# ---------------------------------------------------------------------------- #
def imaging_AOI_horizontalSlider_changed(self):
    self.imaging_xAxis_label.setText(
        "AXIS A: " + str(self.imaging_xAxis_horizontalSlider.sliderPosition() / 100)
    )
    self.imaging_yAxis_label.setText(
        "AXIS B: " + str(self.imaging_yAxis_horizontalSlider.sliderPosition() / 100)
    )


# ---------------------------------------------------------------------------- #
#                           ambient sensor UI update                           #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def ambient_UI_update(self):
    if General.ambient_thread_running:
        self.start_ambient_sensors_pushButton.setText("Stop Ambient Sensors")
    else:
        self.start_ambient_sensors_pushButton.setText("Start Ambient Sensors")
        self.ambient_temperture_value_label.setText("N/A °C")


# ---------------------------------------------------------------------------- #
def ambient_sensor_initialize(self):
    pen = mkPen(color=(197, 5, 12), width=2)
    General.ambient_temperature_graph_ref = self.ambient_temperature_graphWidget.plot(
        General.ambient_sensor_time_stamp, General.ambient_temperature, pen=pen
    )
    General.ambient_humidity_graph_ref = self.ambient_humidity_graphWidget.plot(
        General.ambient_sensor_time_stamp, General.ambient_humidity, pen=pen
    )
    General.ambient_co2_graph_ref = self.ambient_co2_graphWidget.plot(
        General.ambient_sensor_time_stamp, General.ambient_CO2, pen=pen
    )
    General.ambient_o2_graph_ref = self.ambient_o2_graphWidget.plot(
        General.ambient_sensor_time_stamp, General.ambient_o2, pen=pen
    )
    amibient_update_labels(self)


# ---------------------------------------------------------------------------- #
def amibient_update_labels(self):
    self.ambient_temperture_value_label.setText(
        str(General.ambient_temperature[-1]) + " °C"
    )
    self.ambient_humidity_value_label.setText(
        str(General.ambient_humidity[-1]) + " %" + "rH"
    )
    self.ambient_co2_value_label.setText(str(General.ambient_CO2[-1]) + " ppm")
    self.ambient_o2_value_label.setText(str(General.ambient_o2[-1]) + " Vol%")


# ---------------------------------------------------------------------------- #
def ambient_sensor_update(self):
    General.ambient_temperature_graph_ref.setData(
        General.ambient_sensor_time_stamp, General.ambient_temperature
    )
    General.ambient_humidity_graph_ref.setData(
        General.ambient_sensor_time_stamp, General.ambient_humidity
    )
    General.ambient_co2_graph_ref.setData(
        General.ambient_sensor_time_stamp, General.ambient_CO2
    )
    General.ambient_o2_graph_ref.setData(
        General.ambient_sensor_time_stamp, General.ambient_o2
    )
    amibient_update_labels(self)


# ---------------------------------------------------------------------------- #
def ambient_sensor_reset(self):
    self.ambient_temperature_graphWidget.clear()
    self.ambient_humidity_graphWidget.clear()
    self.ambient_co2_graphWidget.clear()
    self.ambient_o2_graphWidget.clear()

    General.ambient_temperature = []
    General.ambient_humidity = []
    General.ambient_CO2 = []
    General.ambient_o2 = []

    General.ambient_sensor_time_stamp = []


# ---------------------------------------------------------------------------- #
def ambient_o2_frame_toggle(self):
    self.ambient_o2_frame.setEnabled(not self.ambient_o2_frame.isEnabled())


# ---------------------------------------------------------------------------- #
#                             soil sensor UI update                            #
# ---------------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #
def soil_UI_update(self):
    if General.soil_thread_running:
        self.start_soil_sensors_pushButton.setText("Stop Soil Sensors")
    else:
        self.start_soil_sensors_pushButton.setText("Start Soil Sensors")
        self.soil_temperture_value_label.setText("N/A °C")
        self.soil_water_content_value_label.setText("N/A %")
        self.soil_EC_value_label.setText("N/A μS/cm")
        self.soil_pH_value_label.setText("N/A")
        self.soil_nitrogen_value_label.setText("N/A mg/kg")
        self.soil_phosphorus_value_label.setText("N/A mg/kg")
        self.soil_potassium_value_label.setText("N/A mg/kg")


# ---------------------------------------------------------------------------- #
def soil_sensor_initialize(self):
    pen = mkPen(color=(197, 5, 12), width=2)
    General.soil_temperature_graph_ref = self.soil_temperature_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_temperature, pen=pen
    )
    General.soil_water_content_graph_ref = self.soil_water_content_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_water_content, pen=pen
    )
    General.soil_EC_graph_ref = self.soil_EC_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_EC, pen=pen
    )
    General.soil_pH_graph_ref = self.soil_pH_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_pH, pen=pen
    )
    General.soil_nitrogen_graph_ref = self.soil_nitrogen_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_nitrogen, pen=pen
    )
    General.soil_phosphorus_graph_ref = self.soil_phosphorus_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_phosphorus, pen=pen
    )
    General.soil_potassium_graph_ref = self.soil_potassium_graphWidget.plot(
        General.soil_sensor_time_stamp, General.soil_potassium, pen=pen
    )

    soil_update_labels(self)


# ---------------------------------------------------------------------------- #
def soil_sensor_update(self):
    General.soil_temperature_graph_ref.setData(
        General.soil_sensor_time_stamp, General.soil_temperature
    )
    General.soil_water_content_graph_ref.setData(
        General.soil_sensor_time_stamp, General.soil_water_content
    )
    General.soil_EC_graph_ref.setData(General.soil_sensor_time_stamp, General.soil_EC)
    General.soil_pH_graph_ref.setData(General.soil_sensor_time_stamp, General.soil_pH)
    General.soil_nitrogen_graph_ref.setData(
        General.soil_sensor_time_stamp, General.soil_nitrogen
    )
    General.soil_phosphorus_graph_ref.setData(
        General.soil_sensor_time_stamp, General.soil_phosphorus
    )
    General.soil_potassium_graph_ref.setData(
        General.soil_sensor_time_stamp, General.soil_potassium
    )
    soil_update_labels(self)


# ---------------------------------------------------------------------------- #
def soil_update_labels(self):
    self.soil_temperature_value_label.setText(str(General.soil_temperature[-1]) + " °C")
    self.soil_water_content_value_label.setText(
        str(General.soil_water_content[-1]) + " °%"
    )
    self.soil_EC_value_label.setText(str(General.soil_EC[-1]) + " μS/cm")
    self.soil_pH_value_label.setText(str(General.soil_pH[-1]))
    self.soil_nitrogen_value_label.setText(str(General.soil_nitrogen[-1]) + " mg/kg")
    self.soil_phosphorus_value_label.setText(
        str(General.soil_phosphorus[-1]) + " mg/kg"
    )
    self.soil_potassium_value_label.setText(str(General.soil_potassium[-1]) + " mg/kg")
