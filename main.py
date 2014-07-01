#!/usr/bin/python
import kivy
kivy.require('1.0.5')
from kivy.app import App
from android import AndroidService
from json import dumps

class ServiceExample(App):

    def start_service(self):
        # Make a thing to test passing vars to the service
        appdict = {"string": "Hello!",
                   "int": 1,
                   "list": [1,2,3,4,5]}
        # JSON. every. day.
        dumpd = dumps(appdict)
        # Makin' that service
        self.service = AndroidService('Sevice example', 'service is running')
        # This just starts the service. I shouldn't need a comment here.
        self.service.start(dumpd)

    def stop_service(self):
        self.service.stop()

if __name__ == "__main__":
    ServiceExample().start_service()
