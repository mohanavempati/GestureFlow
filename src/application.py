from camera.camera import Camera
from welcomescreen import WelcomeScreen


class Application:

    def __init__(self):
        self.camera = Camera()
        self.welcome = WelcomeScreen(self)

    def start_camera(self):
        self.camera.open()
        self.camera.show_feed()

    def run(self):
        self.welcome.show()
