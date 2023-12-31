echo off
echo Welcome in UPDATE_MODULE installer
echo Installing pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
echo Installing python library
pip3 install gitdb
pip3 install pygithub
pip3 install gitpython
pip3 install typing_extensions
pip3 install requests
echo if you don't install python you can do it here: https://www.python.org/downloads/
echo if you don't install git you can do it here: https://gitforwindows.org/
pause