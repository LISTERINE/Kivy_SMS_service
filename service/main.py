#!/usr/bin/python
import kivy
kivy.require('1.0.5')
import os
import time
from json import loads
from android.broadcast import BroadcastReceiver
from jnius import autoclass, cast
from threading import Thread

# get the argument passed. Just for fun.
arg = loads(os.getenv('PYTHON_SERVICE_ARGUMENT'))
print arg

# Better living through autoclass
Byte = autoclass("java.lang.Byte")
Bundle = autoclass("android.os.Bundle")
SmsMessage = autoclass("android.telephony.SmsMessage")

# I don't remember if I need this or not but I'm too lazy
# to get my phone out and redeploy to test right now
sms_manager = autoclass("android.telephony.SmsManager")
sms_manager.getDefault()

def on_sms_received(context, intent):
    # Bundle up the intent extras
    msg_bundle = Bundle(intent.getExtras())
    # Pull out all the pdus
    pdus = [m for m in msg_bundle.get("pdus")]
    # This next line used to do a thing, but doesn't any more.
    # I guess I should take it out
    msg_bytes = [p for p in pdus]
    # Reconstruct the message
    messages = [SmsMessage.createFromPdu(mb) for mb in msg_bytes]
    for m in messages:
        print m.getMessageBody()

# Define the type of action we want to react to
SMS_RECEIVED = "android.provider.Telephony.SMS_RECEIVED"
# Register a call back for that action in a BR
br = BroadcastReceiver(on_sms_received,
                 actions=[SMS_RECEIVED])
# Start the reveiver listening
br.start()

# Keep the service alive
while 1:
    time.sleep(60*5)
