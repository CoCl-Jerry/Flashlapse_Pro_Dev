void motorStatus() {
  digitalWrite(EN_PIN, commands[2]);
}

void setMotor() {
  digitalWrite(DIR_PIN, commands[2]);
  //Motor.microsteps(commands[3]);
  microstep = commands[3];
  interval = commands[4];
  ms_change = true;
  digitalWrite(EN_PIN, LOW);
}
