#!/bin/bash
# script for travis

export PYTHONPATH=$(pwd)/tools/pylib/:$PYTHONPATH
cd ./examples
./test_suite_make && ./test_suite
