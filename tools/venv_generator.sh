#!/bin/bash

# It can be used for local testing of Backend.
# Inside the Dockerfile the "3.10.4" Python version is used.
# The Python3.10.4 is recommended to use for Virtual Environment generation.

set -o errexit
set -o nounset
set -o pipefail

#################### CONFIGURATION ############################
SCRIPT_FULL_PATH_INIT_VENV=$(readlink -f "${0}")
SCRIPT_DIR_INIT_VENV="${SCRIPT_FULL_PATH_INIT_VENV%/*}"
SCRIPT_PARENT_DIR_INIT_VENV="${SCRIPT_DIR_INIT_VENV%/*}"

python3 -m venv "${SCRIPT_DIR_INIT_VENV}/../venv"
source "${SCRIPT_DIR_INIT_VENV}/../venv/bin/activate"
pip install pip==22.2 setuptools==63.2.0 wheel==0.37.1 --upgrade --no-cache-dir --force-reinstall
pip install -r "${SCRIPT_PARENT_DIR_INIT_VENV}/src/backend/requirements.txt"