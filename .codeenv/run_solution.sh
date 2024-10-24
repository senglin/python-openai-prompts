#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ ! -f "/tmp/.setup_finished" ]; then
    echo "The setup is not finished yet. Try again in a few seconds." >&2
    exit 1
fi

cd ${SCRIPT_DIR}/..

source .env

export API_KEY

python .codeenv/.run_llm.py prompt.md system.md
