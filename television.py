class Television:
    # Class variables
    minVol: int = 0
    maxVol: int = 2
    minChannel: int = 0
    maxChannel: int = 3

    def __init__(self):
        """
        Initialzing private variables
        """
        self.__stat: bool = False
        self.__muted: bool = False
        self.__vol = Television.minVol
        self.__channel = Television.minChannel

    def power(self):
        """
        This function turns the tv on if off, and off if on,
        """
        self.__stat = not self.__stat

    def mute(self):
        """
        This function mutes the tv if unmuted, and unmutes if muted
        """
        if self.__stat:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        This function moves the channel up, for a maximum of 3
        """
        if self.__stat:
            self.__channel = (self.__channel + 1) % (Television.maxChannel + 1)

    def channel_down(self):
        """
        This function moves the channel down, for a minimum of 0
        """
        if self.__stat:
            self.__channel = (self.__channel - 1) % (Television.maxChannel + 1)

    def volume_up(self):
        """
        This function turns the volume up, for a maximum of 2
        """
        if self.__stat:
            if self.__vol < Television.maxVol:
                self.__vol += 1
                if self.__muted:
                    self.__muted = False

    def volume_down(self):
        """
        This function turns the volume down, for a minimum of 0
        """
        if self.__stat:
            if self.__vol > Television.minVol:
                self.__vol -= 1
                if self.__muted:
                    self.__muted = False

    def __str__(self):
        """
        Prints tv status, including power, channel, and volume, showing 0 if muted.
        """
        if self.__muted == False:
            return f"Power = {self.__stat}, Channel = {self.__channel}, Volume = {self.__vol}"
        if self.__muted == True:
            return f"Power = {self.__stat}, Channel = {self.__channel}, Volume = 0"

