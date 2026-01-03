#!/usr/bin/bash

# Include opencv tools
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release -DBUILD_APPS=ON -DBUILD_EXAMPLES=ON

make -j$(nproc)
sudo make install