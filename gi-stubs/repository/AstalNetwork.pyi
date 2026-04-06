# -*- coding: utf-8 -*-
from gi.repository import NM
from gi.repository import GLib
from gi.repository import Gio
from gi.repository import GObject
import enum
import typing
from gi.repository import AstalNetwork


class Primary(enum.Enum):
    """"""
    UNKNOWN = 0
    WIRED = 1
    WIFI = 2


def primary_to_string(self) -> str:
    """

:param self: 
:return: """
    pass


def primary_from_connection_type(type: str=None) -> AstalNetwork.Primary:
    """

:param type: 
:return: """
    pass


class State(enum.Enum):
    """"""
    UNKNOWN = 0
    ASLEEP = 10
    DISCONNECTED = 20
    DISCONNECTING = 30
    CONNECTING = 40
    CONNECTED_LOCAL = 50
    CONNECTED_SITE = 60
    CONNECTED_GLOBAL = 70


def state_to_string(self) -> str:
    """

:param self: 
:return: """
    pass


class Connectivity(enum.Enum):
    """"""
    UNKNOWN = 0
    NONE = 1
    PORTAL = 2
    LIMITED = 3
    FULL = 4


def connectivity_to_string(self) -> str:
    """

:param self: 
:return: """
    pass


class DeviceState(enum.Enum):
    """"""
    UNKNOWN = 0
    UNMANAGED = 10
    UNAVAILABLE = 20
    DISCONNECTED = 30
    PREPARE = 40
    CONFIG = 50
    NEED_AUTH = 60
    IP_CONFIG = 70
    IP_CHECK = 80
    SECONDARIES = 90
    ACTIVATED = 100
    DEACTIVATING = 110
    FAILED = 120


def device_state_to_string(self) -> str:
    """

:param self: 
:return: """
    pass


class Internet(enum.Enum):
    """"""
    CONNECTED = 0
    CONNECTING = 1
    DISCONNECTED = 2


def internet_from_device(device: NM.Device=None) -> AstalNetwork.Internet:
    """

:param device: 
:return: """
    pass


def internet_to_string(self) -> str:
    """

:param self: 
:return: """
    pass


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalNetwork.Network:
    """

:return: """
    pass


class AccessPoint(GObject.Object):
    """"""

    def get_connections(self) -> typing.Any:
        """

:param self: 
:return: """
        pass

    def get_path(self) -> str:
        """

:param self: 
:return: """
        pass

    def activate(self, password: str=None, _callback_:
        Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None
        ) -> None:
        """Activates the first connection associated with this AccessPoint or creates a new SimpleConnection using "wpa-psk" and activates it. 
Returns whether the connection is the new active connection.

:param self: 
:param password: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def activate_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def get_bandwidth(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_bssid(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_frequency(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_last_seen(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_max_bitrate(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_strength(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_mode(self) -> NM.80211Mode:
        """

:param self: 
:return: """
        pass

    def get_flags(self) -> NM.80211ApFlags:
        """

:param self: 
:return: """
        pass

    def get_rsn_flags(self) -> NM.80211ApSecurityFlags:
        """

:param self: 
:return: """
        pass

    def get_wpa_flags(self) -> NM.80211ApSecurityFlags:
        """

:param self: 
:return: """
        pass

    def get_requires_password(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_ssid(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: AccessPointPrivate
    ap: NM.AccessPoint


class AccessPointClass:
    """"""
    parent_class: GObject.ObjectClass


class AccessPointPrivate:
    """"""


class Network(GObject.Object):
    """"""

    @staticmethod
    def get_default() -> AstalNetwork.Network:
        """

:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalNetwork.Network:
        """

:return: """
        pass

    def get_client(self) -> NM.Client:
        """

:param self: 
:return: """
        pass

    def get_wifi(self) -> AstalNetwork.Wifi:
        """

:param self: 
:return: """
        pass

    def get_wired(self) -> AstalNetwork.Wired:
        """

:param self: 
:return: """
        pass

    def get_primary(self) -> AstalNetwork.Primary:
        """

:param self: 
:return: """
        pass

    def get_connectivity(self) -> AstalNetwork.Connectivity:
        """

:param self: 
:return: """
        pass

    def get_state(self) -> AstalNetwork.State:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: NetworkPrivate


class NetworkClass:
    """"""
    parent_class: GObject.ObjectClass


class NetworkPrivate:
    """"""


class Wifi(GObject.Object):
    """"""

    def scan(self) -> None:
        """

:param self: 
:return: """
        pass

    def deactivate_connection(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def deactivate_connection_finish(self, _res_: Gio.AsyncResult=None
        ) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def get_device(self) -> NM.DeviceWifi:
        """

:param self: 
:return: """
        pass

    def set_device(self, value: NM.DeviceWifi=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_active_connection(self) -> NM.ActiveConnection:
        """

:param self: 
:return: """
        pass

    def get_active_access_point(self) -> AstalNetwork.AccessPoint:
        """

:param self: 
:return: """
        pass

    def get_access_points(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_enabled(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_enabled(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_internet(self) -> AstalNetwork.Internet:
        """

:param self: 
:return: """
        pass

    def get_bandwidth(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_ssid(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_strength(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_frequency(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_state(self) -> AstalNetwork.DeviceState:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_is_hotspot(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_scanning(self) -> bool:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: WifiPrivate


class WifiClass:
    """"""
    parent_class: GObject.ObjectClass


class WifiPrivate:
    """"""


class Wired(GObject.Object):
    """"""

    def get_device(self) -> NM.DeviceEthernet:
        """

:param self: 
:return: """
        pass

    def set_device(self, value: NM.DeviceEthernet=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_speed(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_internet(self) -> AstalNetwork.Internet:
        """

:param self: 
:return: """
        pass

    def get_state(self) -> AstalNetwork.DeviceState:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: WiredPrivate
    connection: NM.ActiveConnection


class WiredClass:
    """"""
    parent_class: GObject.ObjectClass


class WiredPrivate:
    """"""
