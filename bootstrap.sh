#!/bin/bash
#
# Installs OpenFaux server dependencies.

set -e

if ! which python > /dev/null
then
  echo -e "\nYou don't have Python."
  echo "Installing Python..."
  sudo apt-get install python -y > /tmp/python-install.log
fi

if ! which pip > /dev/null
then
  echo -e "\nYou don't have Pip."
  echo "Installing Pip..."
  sudo apt-get install python-pip -y > /tmp/pip-install.log
fi

if ! python -c "import twisted" 2> /dev/null
then
  echo -e "\nYou don't have Twisted."
  echo "Installing Twisted..."
  sudo pip install python-twisted>=13.2.0 > /tmp/twisted-install.log
fi


echo -e "\nDone.\n"
