# jpg2png
To use this module, you must have python3 and several libraries that are used for image conversion (see requirements.txt)

Note, all commands are run either in the Terminal on Mac/Linux, or the Command Prompt on Windows.

## Prerequisites
Make sure you have Python3.9 or newer and pip installed on your computer. The easiest way to determine this is by running 'python3.9 --version' and 'pip --version'. If you get a response similar to

Python 3.9.0

pip 21.0.1 from /Users/rockstardotb/lib/python3.9/site-packages/pip (python 3.9)

then you are all set. Otherwise, download python3 using the following link:

https://www.python.org/downloads/

and/or pip using the following link:

https://pip.pypa.io/en/stable/installing/

Note, if you are using a Windows machine, you also need to download git if you don't already have it:

https://www.computerhope.com/issues/ch001927.htm#install

## Get Started
### Clone the project

    git clone https://github.com/rockstardotb/jpg2png.git
    cd jpg2png/
    
### Next, you will want to create a virtual environment so any dependencies that are needed for this program will be limited to the environment.

#### On Windows
    virtualenv env
    cd env
    Scripts\activate.bat
    cd ../
    pip install --upgrade pip
    pip install -r requirements.txt

#### On Mac/Linux
    python3.9 -m venv .env
    source .env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt

#### If you are unable to create a virtual environment, make sure it is installed. 

    pip install virtualenv

## Converting jpegs to png
    python jpg2png.py

Note, this will convert any jpegs in the same directory as jpg2png.py to png format. If the image files are in another directory, specify that directory using the '--dir' argument. E.g. 'python jpg2png.py --dir /path/to/directory'

## Deactivate the environment
    deactivate

## Reactivate the environment
#### On Windows
    cd env
    Scripts\activate.bat
    cd ../

#### On Mac/Linux
    source .env/bin/activate
    
Note, you will have to reactivate your environment before using the jpg2png module if you deactivate your environment or close the terminal or command prompt window where your environment was last activated.
