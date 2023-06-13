#!/bin/bash 
#Program installs required app and library for UPDATE_MODULE
library_t=("gitdb" "typing_extensions" "pygithub" "gitpython");
echo "Welcome in UPDATE_MODULE installer"
echo "Updating system"
sudo apt-get update
sudo apt-get upgrade
echo "Installing python3"
sudo apt-get install python3
echo "Installing pip3"
sudo apt-get install python3-pip
echo "Installing git"
sudo apt-get install git

for i in ${library_t[*]};
do	
	echo -e "\nInstalling "$i"\n";
	sudo pip3 install $i;
done
echo "Everything was installed"

