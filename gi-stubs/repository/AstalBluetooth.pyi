# -*- coding: utf-8 -*-
from gi.repository import AstalBluetooth
from gi.repository import Gio
import typing
from gi.repository import GObject
from gi.repository import GLib
MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalBluetooth.Bluetooth:
    """Gets the default singleton Bluetooth object.

:return: """
    pass


class Adapter(GObject.Object):
    """Object representing an [adapter](https://github.com/RadiusNetworks/bluez/blob/master/doc/adapter-api.txt)."""

    def remove_device(self, device: AstalBluetooth.Device=None) -> None:
        """This removes the remote device and the pairing information.
Possible errors: `InvalidArguments`, `Failed`.

:param self: 
:param device: 
:return: """
        pass

    def start_discovery(self) -> None:
        """This method starts the device discovery procedure.
Possible errors: `NotReady`, `Failed`.

:param self: 
:return: """
        pass

    def stop_discovery(self) -> None:
        """This method will cancel any previous [method@AstalBluetooth.Adapter.start_discovery] procedure.
Possible errors: `NotReady`, `Failed`, `NotAuthorized`.

:param self: 
:return: """
        pass

    def get_uuids(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_discovering(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_modalias(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_class(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_address(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_discoverable(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_discoverable(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_pairable(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_pairable(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_powered(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_powered(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_alias(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_alias(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_discoverable_timeout(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_discoverable_timeout(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_pairable_timeout(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_pairable_timeout(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: AdapterPrivate


class AdapterClass:
    """"""
    parent_class: GObject.ObjectClass


class AdapterPrivate:
    """"""


class Bluetooth(GObject.Object):
    """Manager object for `org.bluez`."""

    @staticmethod
    def get_default() -> AstalBluetooth.Bluetooth:
        """Gets the default singleton Bluetooth object.

:return: """
        pass

    def toggle(self) -> None:
        """Toggle the [property@AstalBluetooth.Adapter:powered] property of the [property@AstalBluetooth.Bluetooth:adapter].

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalBluetooth.Bluetooth:
        """

:return: """
        pass

    def get_is_powered(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_is_connected(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_adapter(self) -> AstalBluetooth.Adapter:
        """

:param self: 
:return: """
        pass

    def get_adapters(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_devices(self) -> GLib.List:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: BluetoothPrivate


class BluetoothClass:
    """"""
    parent_class: GObject.ObjectClass
    device_added: typing.Any
    device_removed: typing.Any
    adapter_added: typing.Any
    adapter_removed: typing.Any


class BluetoothPrivate:
    """"""


class Device(GObject.Object):
    """Object representing a [device](https://github.com/luetzel/bluez/blob/master/doc/device-api.txt)."""

    def connect_device(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """This is a generic method to connect any profiles the remote device supports that can be connected to.
Possible errors: `NotReady`, `Failed`, `InProgress`, `AlreadyConnected`.

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def connect_device_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def disconnect_device(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """This method gracefully disconnects all connected profiles.
Possible errors: `NotConnected`.

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def disconnect_device_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def connect_profile(self, uuid: str=None) -> None:
        """This method connects a specific profile of this device. The UUID provided is the remote service UUID for the profile.
Possible errors: `Failed`, `InProgress`, `InvalidArguments`, `NotAvailable`, `NotReady`.

:param self: 
:param uuid: the remote service UUID.
:return: """
        pass

    def disconnect_profile(self, uuid: str=None) -> None:
        """This method disconnects a specific profile of this device.
Possible errors: `Failed`, `InProgress`, `InvalidArguments`, `NotSupported`.

:param self: 
:param uuid: the remote service UUID.
:return: """
        pass

    def pair(self) -> None:
        """This method will connect to the remote device and initiate pairing.
Possible errors: `InvalidArguments`, `Failed`, `AlreadyExists`, `AuthenticationCanceled`, `AuthenticationFailed`, `AuthenticationRejected`, 
`AuthenticationTimeout`, `ConnectionAttemptFailed`.

:param self: 
:return: """
        pass

    def cancel_pairing(self) -> None:
        """This method can be used to cancel a pairing operation initiated by [method@AstalBluetooth.Device.pair].
Possible errors: `DoesNotExist`, `Failed`.

:param self: 
:return: """
        pass

    def get_uuids(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_connected(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_legacy_pairing(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_paired(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_rssi(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_adapter(self) -> GLib.ObjectPath:
        """

:param self: 
:return: """
        pass

    def get_address(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_icon(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_modalias(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_appearance(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_class(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_connecting(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_blocked(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_blocked(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_trusted(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_trusted(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_battery_percentage(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_alias(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_alias(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: DevicePrivate


class DeviceClass:
    """"""
    parent_class: GObject.ObjectClass


class DevicePrivate:
    """"""
