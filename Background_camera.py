import cv2
import threading
import atexit
import ctypes
import platform
import time
import pyautogui

class BackgroundCameraRecorder:
    def __init__(self, camera_index=0, output_filename='output.mp4'):
        """
        Initializes the background camera recorder for Windows.

        :param camera_index: Index of the camera to use (default=0, usually the integrated camera)
        :param output_filename: Filename for the recorded video
        """
        self.camera_index = camera_index
        self.output_filename = output_filename
        self.is_recording = False
        self.cap = None
        self.out = None

        # Register shutdown hook
        atexit.register(self.shutdown_hook)

        # Attempt to minimize camera indicator visibility
        self.os = platform.system()
        if self.os == "Windows":
            # Using CAP_DSHOW to potentially reduce indicator visibility
            self.video_capture_flag = cv2.CAP_DSHOW
            # Basic attempt to suppress camera indicator (limited functionality)
            ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)

    def start_recording(self):
        """
        Starts the camera recording in the background.
        """
        if not self.is_recording:
            self.is_recording = True
            recording_thread = threading.Thread(target=self._record_camera)
            recording_thread.daemon = True  # So that the thread dies when main thread dies
            recording_thread.start()
            print("Background recording started. To stop, run `stop_recording()`")

    def stop_recording(self):
        """
        Stops the ongoing camera recording.
        """
        if self.is_recording:
            self.is_recording = False
            if self.cap.isOpened():
                self.cap.release()
            if self.out is not None:
                self.out.release()
            print("Background recording stopped and resources released.")

    def _record_camera(self):
        """
        The actual camera recording function running in a separate thread.
        """
        # Open the camera with CAP_DSHOW flag
        self.cap = cv2.VideoCapture(self.camera_index, self.video_capture_flag)
        
        # Check if the camera is opened
        if not self.cap.isOpened():
            print("Cannot open camera")
            self.is_recording = False
            return
        
        # Set the frame rate (FPS) for the video
        fps = 30.0
        
        # Get the width and height of the frames
        frame_width = int(self.cap.get(3))
        frame_height = int(self.cap.get(4))
        
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # codec
        self.out = cv2.VideoWriter(self.output_filename, fourcc, fps, (frame_width, frame_height))
        
        print("Recording to", self.output_filename)
        
        while self.is_recording and self.cap.isOpened():
            ret, frame = self.cap.read()
            if not ret:
                print("Cannot receive frame")
                break
            
            # Write the frame to the output video
            self.out.write(frame)
        
        # Release everything when done or stopped
        self.cap.release()
        self.out.release()
        print("Recording saved to", self.output_filename)

    def shutdown_hook(self):
        """
        Hook to stop recording on system shutdown.
        """
        print("System shutdown detected. Stopping recording...")
        self.stop_recording()

# Example usage
if __name__ == "__main__":
    recorder = BackgroundCameraRecorder(0, 'windows_background_record.mp4')
    recorder.start_recording()
    # Simulate other work
    time.sleep(120)  # Wait for 2 minutes before exiting
    # Optional: Stop recording manually before shutdown
    # recorder.stop_recording()
