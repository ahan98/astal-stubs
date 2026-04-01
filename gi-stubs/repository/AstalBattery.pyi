from gi.repository import GObject as GObject

class State:
    UNKNOWN: int
    CHARGING: int
    DISCHARGING: int
    EMPTY: int
    FULLY_CHARGED: int
    PENDING_CHARGE: int
    PENDING_DISCHARGE: int

class Technology:
    UNKNOWN: int
    LITHIUM_ION: int
    LITHIUM_POLYMER: int
    LITHIUM_IRON_PHOSPHATE: int
    LEAD_ACID: int
    NICKEL_CADMIUM: int
    NICKEL_METAL_HYDRIDE: int

class WarningLevel:
    UNKNOWN: int
    NONE: int
    DISCHARGING: int
    LOW: int
    CRITICIAL: int
    ACTION: int

class BatteryLevel:
    UNKNOWN: int
    NONE: int
    LOW: int
    CRITICIAL: int
    NORMAL: int
    HIGH: int
    FULL: int

class Type:
    UNKNOWN: int
    LINE_POWER: int
    BATTERY: int
    UPS: int
    MONITOR: int
    MOUSE: int
    KEYBOARD: int
    PDA: int
    PHONE: int
    MEDIA_PLAYER: int
    TABLET: int
    COMPUTER: int
    GAMING_INPUT: int
    PEN: int
    TOUCHPAD: int
    MODEM: int
    NETWORK: int
    HEADSET: int
    SPEAKERS: int
    HEADPHONES: int
    VIDEO: int
    OTHER_AUDIO: int
    REMOVE_CONTROL: int
    PRINTER: int
    SCANNER: int
    CAMERA: int
    WEARABLE: int
    TOY: int
    BLUETOOTH_GENERIC: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Get the DisplayDevice.
    @returns: 
    @rtype: AstalBattery.Device
    """

class Device(GObject.Object):
    """Client for a UPower [device](https://upower.freedesktop.org/docs/Device.html)."""
    def __init__(self, path=None) -> None:
        """        
        @type path: GLib.ObjectPath
        @returns: Newly created Device
        @rtype: Device
        """
    @staticmethod
    def new(path=None):
        """        
        @type path: GLib.ObjectPath
        @returns: Newly created Device
        @rtype: Device
        """
    @staticmethod
    def get_default():
        """        Get the DisplayDevice.
        @returns: 
        @rtype: AstalBattery.Device
        """
    def get_device_type(self):
        """        
        @returns: 
        @rtype: AstalBattery.Type
        """
    def get_native_path(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_vendor(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_model(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_serial(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_update_time(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_power_supply(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_online(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_energy(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_energy_empty(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_energy_full(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_energy_full_design(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_energy_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_voltage(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_charge_cycles(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_luminosity(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_time_to_empty(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_time_to_full(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_percentage(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_temperature(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_is_present(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_state(self):
        """        
        @returns: 
        @rtype: AstalBattery.State
        """
    def get_is_rechargable(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_capacity(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_technology(self):
        """        
        @returns: 
        @rtype: AstalBattery.Technology
        """
    def get_warning_level(self):
        """        
        @returns: 
        @rtype: AstalBattery.WarningLevel
        """
    def get_battery_level(self):
        """        
        @returns: 
        @rtype: AstalBattery.BatteryLevel
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_charging(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_is_battery(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_battery_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_device_type_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_device_type_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class DeviceClass:
    @property
    def parent_class(self): ...

class DevicePrivate: ...

class UPower(GObject.Object):
    """Client for the UPower [dbus interface](https://upower.freedesktop.org/docs/UPower.html)."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created UPower
        @rtype: UPower
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created UPower
        @rtype: UPower
        """
    def get_devices(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_display_device(self):
        """        
        @returns: 
        @rtype: AstalBattery.Device
        """
    def get_daemon_version(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_on_battery(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_lid_is_closed(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_lid_is_present(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_critical_action(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class UPowerClass:
    @property
    def parent_class(self): ...

class UPowerPrivate: ...
