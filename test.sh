#!/usr/bin/env bash

# Exit on any error
set -e


if [[ $TRAVIS != 'true' ]]; then

  VENV_NAME=".venv"
  if ! [ -e "${VENV_NAME}/bin/activate" ]; then
    echo "Creating virtualenv..."
    virtualenv ${VENV_NAME}
  fi

  source "${VENV_NAME}/bin/activate"

  echo "Installing requirements..."
  pip install -q -r requirements.txt -r requirements-tests.txt

fi

echo "Cleaning .pyc files..."
find . -iname "*.pyc" -delete

echo "Running tests..."
nosetests --with-coverage --cover-erase --cover-package=jenkins_plugin_change_detector

echo "Running flake8..."
flake8 jenkins_plugin_change_detector/ tests/

echo "Done!!"
