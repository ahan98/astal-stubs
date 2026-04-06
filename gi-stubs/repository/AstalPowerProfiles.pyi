# -*- coding: utf-8 -*-
from gi.repository import AstalPowerProfiles
import typing
from gi.repository import GObject
MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalPowerProfiles.PowerProfiles:
    """

:return: """
    pass


class PowerProfiles(GObject.Object):
    """Client for <ulink url="https://freedesktop-team.pages.debian.net/power-profiles-daemon/gdbus-org.freedesktop.UPower.PowerProfiles.html">
  PowerProfiles</ulink>."""

    @staticmethod
    def get_default() -> AstalPowerProfiles.PowerProfiles:
        """Gets the default singleton PowerProfiles instance.

:return: """
        pass

    def hold_profile(self, profile: str=None, reason: str=None,
        application_id: str=None) -> int:
        """This forces the passed profile (either 'power-saver' or 'performance') to be activated until either the caller 
quits, [method@AstalPowerProfiles.PowerProfiles.release_profile] is called, or the [property@
AstalPowerProfiles.PowerProfiles:active_profile] is changed by the user. When conflicting profiles are requested to be held, the 'power-saver
' profile will be activated in preference to the 'performance' profile. Those holds will be automatically cancelled if the user 
manually switches to another profile, and the [signal@AstalPowerProfiles.PowerProfiles::profile_released] signal will be emitted.

:param self: 
:param profile: 
:param reason: 
:param application_id: 
:return: """
        pass

    def release_profile(self, cookie: int=None) -> None:
        """This removes the hold that was set on a profile.

:param self: 
:param cookie: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalPowerProfiles.PowerProfiles:
        """

:return: """
        pass

    def get_active_profile(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_active_profile(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_actions(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_active_profile_holds(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_performance_degraded(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_profiles(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_version(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: PowerProfilesPrivate


class PowerProfilesClass:
    """"""
    parent_class: GObject.ObjectClass


class PowerProfilesPrivate:
    """"""


class Profile:
    """"""
    profile: str
    cpu_driver: str
    platform_driver: str
    driver: str


class Hold:
    """"""
    application_id: str
    profile: str
    reason: str
