class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.__status = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__muted = False
        self.__prev_volume = 0  # Store previous volume level for mute toggling
        
    def power(self):
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Reset mute on power off

    def mute(self):
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__volume = self.__prev_volume
    
    def channel_up(self):
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)  # Correct channel wrap-around

    def channel_down(self):
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > self.MIN_CHANNEL else self.MAX_CHANNEL
    
    def volume_up(self):
        if self.__status and not self.__muted:
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume =  self.__prev_volume + 1        
    
    def volume_down(self):
        if self.__status and not self.__muted:
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume =  self.__prev_volume - 1
    
    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
