void motorStatus() {
  digitalWrite(EN_PIN, commands[2]);
}

void setMotor() {
  digitalWrite(DIR_PIN, commands[2]);
  //Motor.microsteps(commands[3]);
  interval = commands[3];
  microstep = commands[4];
  current=(commands[5]);  
  ms_change = true;
  digitalWrite(EN_PIN, LOW);
}
