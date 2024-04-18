class Television:
    # Class variables
    minVol = 0
    maxVol = 2
    minChannel = 0
    maxChannel = 3

    def __init__(self):
        # Instance variables
        self.stat = False
        self.muted = False
        self.vol = Television.minVol
        self.channel = Television.minChannel

    def power(self):
        self.stat = not self.stat

    def mute(self):
        if self.stat:
            self.muted = not self.muted

    def channel_up(self):
        if self.stat:
            self.channel = (self.channel + 1) % (Television.maxChannel + 1)

    def channel_down(self):
        if self.stat:
            self.channel = (self.channel - 1) % (Television.maxChannel + 1)

    def volume_up(self):
        if self.stat:
            if self.vol < Television.maxVol:
                self.vol += 1
                if self.muted:
                    self.muted = False

    def volume_down(self):
        if self.stat:
            if self.vol > Television.minVol:
                self.vol -= 1
                if self.muted:
                    self.muted = False

    def __str__(self):
        if self.muted == False:
            return f"Power = {self.stat}, Channel = {self.channel}, Volume = {self.vol}"
        if self.muted == True:
            return f"Power = {self.stat}, Channel = {self.channel}, Volume = 0"

