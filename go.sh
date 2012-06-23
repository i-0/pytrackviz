#! /bin/bash
#! /bin/bash

if [ $# -gt 0 ]
then
  DATE=$1
else
  DATE=`date +%Y%m%d`
fi
echo ":: ------------------=< instatracks report-generator >=-------------"
echo -n ":: Genrating track report for $DATE..."

# use mock config file if no you don't have access to the production DB
#   --configfile prod.conf\
#   --configfile mock_basic.conf\

python App.py \
  --inputfile ./dot_templates/new_basic_template.dot\
  --configfile mock_basic.conf\
  --date $DATE \
  | dot -Tpng > ./reports/"basic_tracks_$DATE.png"

if [ $? -ne 0 ]
then
  echo ":: Failed!"
  exit 1
fi

echo "Done!"
echo "::"
echo ":: You can find the diagram in the reports folder,"
echo ":: or start an http server with ./serve.sh listening on"
echo "::"
echo "::            http://localhost:8000"
echo "::"
echo ":: ------------------=< Have fun! >=----------------------"
