import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2

class ObjectDetectionApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Object Detection")
        
        self.image_label = tk.Label(self.master)
        self.image_label.pack()
        
        self.detect_button = tk.Button(self.master, text="Detect Objects", command=self.detect_objects)
        self.detect_button.pack()
        
        self.select_image_button = tk.Button(self.master, text="Select Image", command=self.select_image)
        self.select_image_button.pack()
        
    def select_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.display_image(file_path)
        
    def display_image(self, file_path):
        image = Image.open(file_path)
        image = image.resize((400, 300), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        
    def detect_objects(self):
        # Perform object detection on the selected image
        yv()
        # Placeholder for actual object detection code


def main():
    root = tk.Tk()
    app = ObjectDetectionApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
