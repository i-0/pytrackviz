#! /bin/bash
BASE_DIR=`pwd`
PYTHON="python"
TEST_CASES="TestConfiguration.py TestTemplateProcessor.py TestTrackData.py TestTrackSource.py TestLost.py"

for TEST in $TEST_CASES
do
  $PYTHON "$BASE_DIR/$TEST"
  if [ $? -ne 0 ]
  then
	echo ":: TEST FAILED!"
	exit -1
  fi
done

