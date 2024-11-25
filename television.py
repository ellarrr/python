
class Television:
    """
    Television remote controls
    Class Variables
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self):
        """
        Set instance variables
        """
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL

    def power(self):
        """
        Function to turn TV on/off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        """
        Function to turn mute on//off
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
            else:
                self.__muted = True

    def channel_up(self):
        """
        Function to increase channel
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Function to decrease channel
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Function to increase volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Function to decrease volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Return string
        :return: Power, status. and volume
        """
        tv_status = 'True' if self.__status else 'False'
        tv_muted = '0' if self.__muted else f'{self.__volume}'
        return f"Power = {tv_status}, Channel = {self.__channel}, Volume = {tv_muted}"



