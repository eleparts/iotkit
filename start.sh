#!/bin/sh
COLOR='\033[0;32m' #GREEN
NC='\033[0m'

echo "${COLOR}> Download example files${NC}"

echo "git clone PMS7003 example -> ./examples/05.PMS7003"
git clone https://github.com/eleparts/PMS7003 ./examples/05.PMS7003

echo "git clone blynk_python_GPIO example -> ./blynk_examples/blynk_python_GPIO"
git clone https://github.com/eleparts/blynk_python_GPIO ./blynk_examples/blynk_python_GPIO

echo "cp blynk_python_GPIO_V2.py"
cp ./blynk_examples/blynk_python_GPIO_V2.py ./blynk_examples/blynk_python_GPIO/blynk_python_GPIO_V2.py

echo "git clone blynk_python_PMS7003 example -> ./blynk_examples/blynk_python_PMS7003"
git clone https://github.com/eleparts/blynk_python_PMS7003 ./blynk_examples/blynk_python_PMS7003


echo "${COLOR}> Download library files${NC}"

echo "Download PMS7003.py"
wget -O PMS7003.py https://github.com/eleparts/PMS7003/blob/master/PMS7003.py?raw=true

echo "${COLOR}> insert library${NC}" 

echo "PMS7003 library -> blynk_python_PMS7003" 
cp ./PMS7003.py ./blynk_examples/blynk_python_PMS7003/PMS7003.py

