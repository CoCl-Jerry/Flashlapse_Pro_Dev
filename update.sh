sudo rm -r /home/pi/Documents/Flashlapse_Pro_Dev
if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
	cd /home/pi/Documents/backup/Flashlapse_Pro_Dev
	git pull
fi
sudo cp -r /home/pi/Documents/backup/Flashlapse_Pro_Dev /home/pi/Documents
