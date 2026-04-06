# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import GLib
from gi.repository import AstalBattery
import enum


class State(enum.Enum):
    """"""
    UNKNOWN = 0
    CHARGING = 1
    DISCHARGING = 2
    EMPTY = 3
    FULLY_CHARGED = 4
    PENDING_CHARGE = 5
    PENDING_DISCHARGE = 6


class Technology(enum.Enum):
    """"""
    UNKNOWN = 0
    LITHIUM_ION = 1
    LITHIUM_POLYMER = 2
    LITHIUM_IRON_PHOSPHATE = 3
    LEAD_ACID = 4
    NICKEL_CADMIUM = 5
    NICKEL_METAL_HYDRIDE = 6


class WarningLevel(enum.Enum):
    """"""
    UNKNOWN = 0
    NONE = 1
    DISCHARGING = 2
    LOW = 3
    CRITICIAL = 4
    ACTION = 5


class BatteryLevel(enum.Enum):
    """"""
    UNKNOWN = 0
    NONE = 1
    LOW = 2
    CRITICIAL = 3
    NORMAL = 4
    HIGH = 5
    FULL = 6


class Type(enum.Enum):
    """"""
    UNKNOWN = 0
    LINE_POWER = 1
    BATTERY = 2
    UPS = 3
    MONITOR = 4
    MOUSE = 5
    KEYBOARD = 6
    PDA = 7
    PHONE = 8
    MEDIA_PLAYER = 9
    TABLET = 10
    COMPUTER = 11
    GAMING_INPUT = 12
    PEN = 13
    TOUCHPAD = 14
    MODEM = 15
    NETWORK = 16
    HEADSET = 17
    SPEAKERS = 18
    HEADPHONES = 19
    VIDEO = 20
    OTHER_AUDIO = 21
    REMOVE_CONTROL = 22
    PRINTER = 23
    SCANNER = 24
    CAMERA = 25
    WEARABLE = 26
    TOY = 27
    BLUETOOTH_GENERIC = 28


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalBattery.Device:
    """Get the DisplayDevice.

:return: """
    pass


class Device(GObject.Object):
    """Client for a UPower [device](https://upower.freedesktop.org/docs/Device.html)."""

    @staticmethod
    def get_default() -> AstalBattery.Device:
        """Get the DisplayDevice.

:return: """
        pass

    def __init__(self, path: GLib.ObjectPath=None) -> None:
        """

:param self: 
:param path: 
:return: """
        pass

    @staticmethod
    def new(path: GLib.ObjectPath=None) -> AstalBattery.Device:
        """

:param path: 
:return: """
        pass

    def get_device_type(self) -> AstalBattery.Type:
        """

:param self: 
:return: """
        pass

    def get_native_path(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_vendor(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_model(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_serial(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_update_time(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_power_supply(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_online(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_energy(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_energy_empty(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_energy_full(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_energy_full_design(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_energy_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_voltage(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_charge_cycles(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_luminosity(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_time_to_empty(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_time_to_full(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_percentage(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_temperature(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_is_present(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_state(self) -> AstalBattery.State:
        """

:param self: 
:return: """
        pass

    def get_is_rechargable(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_capacity(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_technology(self) -> AstalBattery.Technology:
        """

:param self: 
:return: """
        pass

    def get_warning_level(self) -> AstalBattery.WarningLevel:
        """

:param self: 
:return: """
        pass

    def get_battery_level(self) -> AstalBattery.BatteryLevel:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_charging(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_is_battery(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_battery_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_device_type_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_device_type_icon(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: DevicePrivate


class DeviceClass:
    """"""
    parent_class: GObject.ObjectClass


class DevicePrivate:
    """"""


class UPower(GObject.Object):
    """Client for the UPower [dbus interface](https://upower.freedesktop.org/docs/UPower.html)."""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalBattery.UPower:
        """

:return: """
        pass

    def get_devices(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_display_device(self) -> AstalBattery.Device:
        """

:param self: 
:return: """
        pass

    def get_daemon_version(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_on_battery(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_lid_is_closed(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_lid_is_present(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_critical_action(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: UPowerPrivate


class UPowerClass:
    """"""
    parent_class: GObject.ObjectClass


class UPowerPrivate:
    """"""
