#!/bin/bash
#
# Installs OpenFaux server dependencies.

set -e

if ! which python > /dev/null
then
  echo -e "\nOh. You don't have Python."
  echo "Installing Python..."
  sudo apt-get install python -y > /tmp/python-install.log
fi

if ! which pip > /dev/null
then
  echo -e "\nOh. You don't have Pip."
  echo "Installing Pip..."
  sudo apt-get install python-pip -y > /tmp/pip-install.log
fi

if ! python -c "import twisted" 2> /dev/null
then
  echo -e "\nOh. You don't have Twisted."
  echo "Installing Twisted..."
  sudo pip install python-twisted>=13.2.0 > /tmp/twisted-install.log
fi

if ! python -c "import webapp2" 2> /dev/null
then
  echo -e "\nOh. You don't have WebApp2."
  echo -e "Installing WebApp2..."
  sudo pip install webapp2>=2.5.1 > /tmp/webapp2-install.log
fi

if ! python -c "import paste" 2> /dev/null
then
  echo -e "\nOh. You don't have Paste."
  echo "Installing Paste..."
  sudo pip install Paste>=1.7.5 > /tmp/paste-install.log
fi

if ! python -c "import webob" 2> /dev/null
then
  echo -e "\nOh. You don't have WebOb."
  echo "Installing WebOb..."
  sudo pip install WebOb>=1.2.3 > /tmp/webob-install.log
fi

echo -e "\nDone.\n"