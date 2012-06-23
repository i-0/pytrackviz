#! /bin/bash

if [ $# -gt 0 ]
then
  DATE=$1
else
  DATE=`date +%Y%m%d`
fi

python -m pdb ./App.py \
  --inputfile ./dot_templates/new_basic_template.dot \
  --date $DATE \
  --configfile mock_basic.conf
