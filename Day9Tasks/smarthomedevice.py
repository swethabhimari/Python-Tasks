#Smart home devices-Multiplt Inheritance
class WifiDevice:
    def wifi(self):
        print("WIFI connected")
class VoiceAssistance:
    def voice(self):
        print("voice control enabled")
class SmartSpeaker(WifiDevice,VoiceAssistance):
    def display(self):
        print("Smart Speaker ready")
s=SmartSpeaker()
s.wifi()
s.voice()
s.display()