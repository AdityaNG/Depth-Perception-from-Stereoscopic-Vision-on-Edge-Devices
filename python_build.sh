make shared_library -j12
cp bin/stereo_vision.so stereo_vision/bin/stereo_vision.so
python3 -m pip install .
