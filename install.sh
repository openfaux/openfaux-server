#!/bin/bash

set -e

echo "Updates packages. Asks for your password."
sudo apt-get update -y

echo "\nInstall Python"
sudo apt-get install python -y

echo "\nInstall pip"
sudo apt-get install python-pip

# echo "\nInstall WebApp2"
# sudo pip install webapp2>=2.5.1

# echo "\nInstall Paste"
# sudo pip install Paste>=1.7.5

# echo "\nInstall WebOb"
# sudo pip install WebOb>=1.2.3

echo "\nInstall Twisted"
sudo pip install python-twisted>=13.2.0

echo -e "\n- - - - - -\n"
echo -e "Now we are going to print some information to check that everything is done:\n"

if [ `python --version` ]; then
	echo "Python is installed"
else
	echo "Python is not installed"
fi

if [ `pip --version` ]; then
	echo "pip is installed"
else
	echo "pip is not installed"
fi

if [  !`python -c "import webapp2;webapp2.__version__"` ]; then
	echo "WebApp2 is installed"
else
	echo "WebApp2 is not installed"
fi

if [  !`python -c "import paste;"` ]; then
	echo "Paste is installed"
else
	echo "Paste is not installed"
fi

if [ !`python -c "import webob;"` ]; then
	echo "WebOb is installed"
else
	echo "WebOb is not installed"
fi

if [ !`python -c "import twisted;twisted.version"` ]; then
	echo "Twisted is installed"
else
	echo "Twisted is not installed"
fi
echo -e "\n- - - - - -\n"

echo "If the versions match, everything is installed correctly. If the versions 
don't match or errors are shown, something went wrong with the automated process 
and we will help you do the installation the manual way at the event.

Congrats!
                                                                                 
