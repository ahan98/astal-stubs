from gi.repository import GObject as GObject

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Gets the default singleton Bluetooth object.
    @returns: 
    @rtype: AstalBluetooth.Bluetooth
    """

class Adapter(GObject.Object):
    """Object representing an [adapter](https://github.com/RadiusNetworks/bluez/blob/master/doc/adapter-api.txt)."""
    def remove_device(self, device=None):
        """        This removes the remote device and the pairing information.
        Possible errors: `InvalidArguments`, `Failed`.
        @type device: AstalBluetooth.Device
        @returns: 
        @rtype: None
        """
    def start_discovery(self):
        """        This method starts the device discovery procedure.
        Possible errors: `NotReady`, `Failed`.
        @returns: 
        @rtype: None
        """
    def stop_discovery(self):
        """        This method will cancel any previous [method@AstalBluetooth.Adapter.start_discovery] procedure.
        Possible errors: `NotReady`, `Failed`, `NotAuthorized`.
        @returns: 
        @rtype: None
        """
    def get_uuids(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_discovering(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_modalias(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_class(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_address(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_discoverable(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_discoverable(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_pairable(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_pairable(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_powered(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_powered(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_alias(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_alias(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_discoverable_timeout(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_discoverable_timeout(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_pairable_timeout(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_pairable_timeout(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class AdapterClass:
    @property
    def parent_class(self): ...

class AdapterPrivate: ...

class Bluetooth(GObject.Object):
    """Manager object for `org.bluez`."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Bluetooth
        @rtype: Bluetooth
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Bluetooth
        @rtype: Bluetooth
        """
    @staticmethod
    def get_default():
        """        Gets the default singleton Bluetooth object.
        @returns: 
        @rtype: AstalBluetooth.Bluetooth
        """
    def toggle(self):
        """        Toggle the [property@AstalBluetooth.Adapter:powered] property of the [property@AstalBluetooth.Bluetooth:adapter].
        @returns: 
        @rtype: None
        """
    def get_is_powered(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_is_connected(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_adapter(self):
        """        
        @returns: 
        @rtype: AstalBluetooth.Adapter
        """
    def get_adapters(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_devices(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class BluetoothClass:
    @property
    def parent_class(self): ...
    @property
    def device_added(self): ...
    @property
    def device_removed(self): ...
    @property
    def adapter_added(self): ...
    @property
    def adapter_removed(self): ...

class BluetoothPrivate: ...

class Device(GObject.Object):
    """Object representing a [device](https://github.com/luetzel/bluez/blob/master/doc/device-api.txt)."""
    def connect_device(self, _callback_=None, _callback__target=None):
        """        This is a generic method to connect any profiles the remote device supports that can be connected to.
        Possible errors: `NotReady`, `Failed`, `InProgress`, `AlreadyConnected`.
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def connect_device_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def disconnect_device(self, _callback_=None, _callback__target=None):
        """        This method gracefully disconnects all connected profiles.
        Possible errors: `NotConnected`.
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def disconnect_device_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def connect_profile(self, uuid=None):
        """        This method connects a specific profile of this device. The UUID provided is the remote service UUID for the profile.
        Possible errors: `Failed`, `InProgress`, `InvalidArguments`, `NotAvailable`, `NotReady`.
        @param uuid: the remote service UUID.
        @type uuid: str
        @returns: 
        @rtype: None
        """
    def disconnect_profile(self, uuid=None):
        """        This method disconnects a specific profile of this device.
        Possible errors: `Failed`, `InProgress`, `InvalidArguments`, `NotSupported`.
        @param uuid: the remote service UUID.
        @type uuid: str
        @returns: 
        @rtype: None
        """
    def pair(self):
        """        This method will connect to the remote device and initiate pairing.
        Possible errors: `InvalidArguments`, `Failed`, `AlreadyExists`, `AuthenticationCanceled`, `AuthenticationFailed`, `AuthenticationRejected`, 
        `AuthenticationTimeout`, `ConnectionAttemptFailed`.
        @returns: 
        @rtype: None
        """
    def cancel_pairing(self):
        """        This method can be used to cancel a pairing operation initiated by [method@AstalBluetooth.Device.pair].
        Possible errors: `DoesNotExist`, `Failed`.
        @returns: 
        @rtype: None
        """
    def get_uuids(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_connected(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_legacy_pairing(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_paired(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_rssi(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_adapter(self):
        """        
        @returns: 
        @rtype: GLib.ObjectPath
        """
    def get_address(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_modalias(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_appearance(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_class(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_connecting(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_blocked(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_blocked(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_trusted(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_trusted(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_battery_percentage(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_alias(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_alias(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class DeviceClass:
    @property
    def parent_class(self): ...

class DevicePrivate: ...
