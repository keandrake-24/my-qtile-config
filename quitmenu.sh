#!/bin/bash

password=$(echo "
" | rofi -dmenu -p "Please Input Sudo password")

if [ $password = 2408-2012.kinder ]; then

selected=$(echo "suspend machine
shutdown
restart" | rofi -dmenu -p "Choose an Action Option")

cd $HOME/.config/qtile

echo $selected

echo $password

if [ "$selected"  = shutdown ]; then
	./yesnomenupipe.sh "Are you sure you want to shutdown?"  'echo 2408-2012.kinder' 'sudo -S shutdown -h now' 
elif [ "$selected"  = "suspend machine" ]; then
	./yesnomenu.sh "Are you sure  you want to suspend?" "systemctl suspend"
elif [ "$selected"  = restart ]; then
	./yesnomenupipe.sh "Are you sure you want to restart?" "echo 2408-2012.kinder" "sudo -S  systemctl reboot"

fi
fi
