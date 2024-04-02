# Leap Motion Data Acquisition Application

## Getting Started

### Leap Motion Development

1. Create a virtual environment using conda with **Python 3.8** version by running the command `conda create -n python=3.8 --all`.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Install the LeapC API using `pip install -e leapc-python-api`.
4. Test the installation of the Python binding for the LeapC API successfully by typing `python examples/tracking_event_example.py.`

### GUI Development

1. Using Open Source QtDesigner to design the UI and convert to `.py` code by typing `pyside6-uic leapmotion.ui -o leapmotion_ui.py` and `pyside6-rcc resources.qrc -o resources_rc.py`
