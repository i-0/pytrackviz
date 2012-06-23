# /bin/bash
BASE_DIR=`pwd`
GALLERY=$BASE_DIR"/reports"
PYTHON=/usr/bin/python
cd $GALLERY
$PYTHON -m SimpleHTTPServer
