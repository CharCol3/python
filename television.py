class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        """
        Initializes the television with all settings in their default state.
        This includes power off, volume and channel set to minimum, and mute off.
        """
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__muted = False
        self.__prev_volume = 0  # Store previous volume level for mute toggling
        
    def power(self) -> None:
        """
        Toggles the power state of the television.
        Turns the TV on if it's off, and off if it's on.
        Automatically un-mutes the TV when powered off.
        """
        self.__status = not self.__status
        if not self.__status:
            self.__muted = False  # Reset mute on power off

    def mute(self) -> None:
        """
        Toggles the mute state only when the television is on.
        When muted, sets the volume to minimum and remembers the previous volume.
        When un-muted, restores the volume to the previous level.
        """
        if self.__status:
            self.__muted = not self.__muted
            if self.__muted:
                self.__prev_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume = self.__prev_volume
    
    def channel_up(self) -> None:
        """
        Increases the channel number by one with wrap-around logic,
        but only when the television is on.
        """
        if self.__status:
            self.__channel = (self.__channel + 1) % (Television.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """
        Decreases the channel number by one with wrap-around logic,
        but only when the television is on.
        """
        if self.__status:
            self.__channel = (self.__channel - 1) if self.__channel > Television.MIN_CHANNEL else Television.MAX_CHANNEL
    
    def volume_up(self) -> None:
        """
        Increases the volume by one, not exceeding the maximum volume.
        Un-mutes the TV if it is muted, before increasing the volume.
        """
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume =  self.__prev_volume + 1
        elif self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    
    def volume_down(self) -> None:
        """
        Decreases the volume by one, not going below the minimum volume.
        Un-mutes the TV if it is muted, before decreasing the volume.
        """
        if self.__status and self.__muted:
            self.__muted = False
            self.__volume =  self.__prev_volume - 1
        elif self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    
    def __str__(self) -> str:
        """
        Returns a string representation of the television's current state,
        showing power status, current channel, and volume level.
        """
        return f"Power = {'On' if self.__status else 'Off'}, Channel = {self.__channel}, Volume = {self.__volume}"