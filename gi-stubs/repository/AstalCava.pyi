# -*- coding: utf-8 -*-
import enum
from gi.repository import GObject
import typing


class Input(enum.Enum):
    """"""
    FIFO = 0
    PORTAUDIO = 1
    PIPEWIRE = 2
    ALSA = 3
    PULSE = 4
    SNDIO = 5
    SHMEM = 8
    WINSCAP = 9


def get_default() -> Cava:
    """gets the default Cava object.

:return: """
    pass


class Cava(GObject.Object):
    """"""

    @staticmethod
    def get_default() -> Cava:
        """gets the default Cava object.

:return: """
        pass

    def get_active(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_autosens(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_bars(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_channels(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_framerate(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_high_cutoff(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_input(self) -> Input:
        """

:param self: 
:return: """
        pass

    def get_low_cutoff(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_noise_reduction(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_samplerate(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_source(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_stereo(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_values(self) -> typing.Any:
        """

:param self: the AstalCavaCava object
:return: a list of values"""
        pass

    def set_active(self, active: bool=None) -> None:
        """

:param self: 
:param active: 
:return: """
        pass

    def set_autosens(self, autosens: bool=None) -> None:
        """

:param self: 
:param autosens: 
:return: """
        pass

    def set_bars(self, bars: int=None) -> None:
        """

:param self: 
:param bars: 
:return: """
        pass

    def set_channels(self, channels: int=None) -> None:
        """

:param self: 
:param channels: 
:return: """
        pass

    def set_framerate(self, framerate: int=None) -> None:
        """

:param self: 
:param framerate: 
:return: """
        pass

    def set_high_cutoff(self, high_cutoff: int=None) -> None:
        """

:param self: 
:param high_cutoff: 
:return: """
        pass

    def set_input(self, input: Input=None) -> None:
        """

:param self: 
:param input: 
:return: """
        pass

    def set_low_cutoff(self, low_cutoff: int=None) -> None:
        """

:param self: 
:param low_cutoff: 
:return: """
        pass

    def set_noise_reduction(self, noise: float=None) -> None:
        """

:param self: 
:param noise: 
:return: """
        pass

    def set_samplerate(self, samplerate: int=None) -> None:
        """

:param self: 
:param samplerate: 
:return: """
        pass

    def set_source(self, source: str=None) -> None:
        """

:param self: 
:param source: 
:return: """
        pass

    def set_stereo(self, stereo: bool=None) -> None:
        """

:param self: 
:param stereo: 
:return: """
        pass


class CavaClass:
    """"""
    parent_class: GObject.ObjectClass
