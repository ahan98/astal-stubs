from gi.repository import GObject as GObject

class Primary:
    UNKNOWN: int
    WIRED: int
    WIFI: int

def primary_to_string(self):
    """    
    @returns: 
    @rtype: str
    """
def primary_from_connection_type(type=None):
    """    
    @type type: str
    @returns: 
    @rtype: AstalNetwork.Primary
    """

class State:
    UNKNOWN: int
    ASLEEP: int
    DISCONNECTED: int
    DISCONNECTING: int
    CONNECTING: int
    CONNECTED_LOCAL: int
    CONNECTED_SITE: int
    CONNECTED_GLOBAL: int

def state_to_string(self):
    """    
    @returns: 
    @rtype: str
    """

class Connectivity:
    UNKNOWN: int
    NONE: int
    PORTAL: int
    LIMITED: int
    FULL: int

def connectivity_to_string(self):
    """    
    @returns: 
    @rtype: str
    """

class DeviceState:
    UNKNOWN: int
    UNMANAGED: int
    UNAVAILABLE: int
    DISCONNECTED: int
    PREPARE: int
    CONFIG: int
    NEED_AUTH: int
    IP_CONFIG: int
    IP_CHECK: int
    SECONDARIES: int
    ACTIVATED: int
    DEACTIVATING: int
    FAILED: int

def device_state_to_string(self):
    """    
    @returns: 
    @rtype: str
    """

class Internet:
    CONNECTED: int
    CONNECTING: int
    DISCONNECTED: int

def internet_from_device(device=None):
    """    
    @type device: NM.Device
    @returns: 
    @rtype: AstalNetwork.Internet
    """
def internet_to_string(self):
    """    
    @returns: 
    @rtype: str
    """

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    
    @returns: 
    @rtype: AstalNetwork.Network
    """

class AccessPoint(GObject.Object):
    def get_connections(self):
        """        
        @rtype: None
        """
    def get_path(self):
        """        
        @returns: 
        @rtype: str
        """
    def activate(self, password=None, _callback_=None, _callback__target=None):
        '''        Activates the first connection associated with this AccessPoint or creates a new SimpleConnection using "wpa-psk" and activates it. 
        Returns whether the connection is the new active connection.
        @type password: str
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        '''
    def activate_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def get_bandwidth(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_bssid(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_frequency(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_last_seen(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_max_bitrate(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_strength(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_mode(self):
        """        
        @returns: 
        @rtype: NM.80211Mode
        """
    def get_flags(self):
        """        
        @returns: 
        @rtype: NM.80211ApFlags
        """
    def get_rsn_flags(self):
        """        
        @returns: 
        @rtype: NM.80211ApSecurityFlags
        """
    def get_wpa_flags(self):
        """        
        @returns: 
        @rtype: NM.80211ApSecurityFlags
        """
    def get_requires_password(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_ssid(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...
    @property
    def ap(self): ...

class AccessPointClass:
    @property
    def parent_class(self): ...

class AccessPointPrivate: ...

class Network(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Network
        @rtype: Network
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Network
        @rtype: Network
        """
    @staticmethod
    def get_default():
        """        
        @returns: 
        @rtype: AstalNetwork.Network
        """
    def get_client(self):
        """        
        @returns: 
        @rtype: NM.Client
        """
    def get_wifi(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Wifi
        """
    def get_wired(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Wired
        """
    def get_primary(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Primary
        """
    def get_connectivity(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Connectivity
        """
    def get_state(self):
        """        
        @returns: 
        @rtype: AstalNetwork.State
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class NetworkClass:
    @property
    def parent_class(self): ...

class NetworkPrivate: ...

class Wifi(GObject.Object):
    def scan(self):
        """        
        @returns: 
        @rtype: None
        """
    def deactivate_connection(self, _callback_=None, _callback__target=None):
        """        
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def deactivate_connection_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def get_device(self):
        """        
        @returns: 
        @rtype: NM.DeviceWifi
        """
    def set_device(self, value=None):
        """        
        @type value: NM.DeviceWifi
        @returns: 
        @rtype: None
        """
    def get_active_connection(self):
        """        
        @returns: 
        @rtype: NM.ActiveConnection
        """
    def get_active_access_point(self):
        """        
        @returns: 
        @rtype: AstalNetwork.AccessPoint
        """
    def get_access_points(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_enabled(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_enabled(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_internet(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Internet
        """
    def get_bandwidth(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_ssid(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_strength(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_frequency(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_state(self):
        """        
        @returns: 
        @rtype: AstalNetwork.DeviceState
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_is_hotspot(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_scanning(self):
        """        
        @returns: 
        @rtype: bool
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class WifiClass:
    @property
    def parent_class(self): ...

class WifiPrivate: ...

class Wired(GObject.Object):
    def get_device(self):
        """        
        @returns: 
        @rtype: NM.DeviceEthernet
        """
    def set_device(self, value=None):
        """        
        @type value: NM.DeviceEthernet
        @returns: 
        @rtype: None
        """
    def get_speed(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_internet(self):
        """        
        @returns: 
        @rtype: AstalNetwork.Internet
        """
    def get_state(self):
        """        
        @returns: 
        @rtype: AstalNetwork.DeviceState
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...
    @property
    def connection(self): ...

class WiredClass:
    @property
    def parent_class(self): ...

class WiredPrivate: ...
