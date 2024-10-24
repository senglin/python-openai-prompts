#!/bin/sh

pip install openai===1.52.2          # Oct 23, 2024
pip install azure-identity===1.19.0  # Oct 8, 2024

touch /tmp/.setup_finished
