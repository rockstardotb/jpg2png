# jpg2png
To use this module, you must have python3 and several libraries that are used for image conversion (see requirements.txt)

## Prerequisites
Make sure you have either Python3 installed on your computer. The easiest way to determine this is by running 'python3 --version'. If you get a response similar to

Python 3.7.10

then you are all set. Otherwise, download python3 using the following link:

https://www.python.org/downloads/

## Get Started
### Clone the project and checkout the 'clean_slate' branch

    git clone https://github.com/rockstardotb/jpg2png.git
    cd jpg2png/
    
### Next, you will want to create a virtual environment so any dependencies that are needed for this program will be limited to the environment.

#### On Windows
    virtualenv env
    cd env
    Scripts\activate.bat
    cd ../
    pip install -r requirements.txt

#### On Mac/Linux
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt

## Converting jpegs to png
    python3 jpg2png.py
    Note, this will convert any jpegs in the same directory as jpg2png.py to pngformat. If the image files are in another directory, specify that directory using the '--dir' argument. E.g. 'python3 jpg2png.py --dir /path/to/directory'

## Deactivate the environment
    deactivate

## Reactivate the environment
#### On Windows
    cd env
    Scripts\activate.bat
    cd ../

#### On Mac/Linux
    source .env/bin/activate
