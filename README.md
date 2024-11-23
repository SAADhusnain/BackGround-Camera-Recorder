### Cross-Platform Background Camera Recording Utility

A Python class utilizing OpenCV to record camera feed in the background, with a focus on minimizing camera indicator visibility on Windows systems.


### Key Features

**Background Recording**: Records camera feed in a separate thread, allowing your main application to continue uninterrupted.

**Cross-Platform Compatibility**: Although the camera indicator minimization feature is Windows-centric, the recording functionality works on all platforms supported by OpenCV.

**Configurable**: Easily specify the camera index and output filename to suit your application's needs.

**Cleanup on Exit**: Automatically stops recording and releases resources upon system shutdown or when manually instructed to do so.


### Requirements

**Python 3.x**: Tested on Python 3.8 and above. Compatibility with earlier versions is not guaranteed.
**OpenCV**: `pip install opencv-python` to install.
**PyAutoGUI & Other Dependencies**: Automatically installed with OpenCV. If issues arise, ensure you have `pyautogui` and `ctypes` available.
* 


### API Documentation
Class: BackgroundCameraRecorder
1. __init__(camera_index=0, output_filename='output.mp4'): Initializes the recorder with a specified camera index and output filename.
2. start_recording(): Begins the recording process in the background.
3. stop_recording(): Manually stops the ongoing recording and releases system resources.
4. shutdown_hook(): Automatically triggered on system shutdown to ensure clean termination of the recording process.


### Contact
GitHub: SAADhusnain
Email: saaddi456@gmail.com 


### Acknowledgments
OpenCV Team for the incredible computer vision library.
PyAutoGUI for simplifying GUI automation.
The Python Community for their tireless efforts in making Python an absolute joy to work with.
