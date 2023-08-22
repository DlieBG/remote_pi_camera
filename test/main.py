from picamera2 import Picamera2
from PIL import Image

camera = Picamera2()
camera.start()
camera.switch_mode(camera.create_still_configuration())

image = camera.capture_file()
pil = Image(image)



camera.close()
