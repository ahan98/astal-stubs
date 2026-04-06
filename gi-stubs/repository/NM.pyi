# -*- coding: utf-8 -*-
import enum
from gi.repository import GLib
import typing
from gi.repository import Gio
from gi.repository import GObject


# NOTE: The runtime name is '80211ApFlags' (invalid Python identifier).
# Access at runtime via: getattr(NM, '80211ApFlags')
class NM80211ApFlags(enum.Enum):
    """802.11 access point flags."""
    NONE = 0
    PRIVACY = 1
    WPS = 2
    WPS_PBC = 4
    WPS_PIN = 8


# NOTE: The runtime name is '80211ApSecurityFlags' (invalid Python identifier).
# Access at runtime via: getattr(NM, '80211ApSecurityFlags')
class NM80211ApSecurityFlags(enum.Enum):
    """802.11 access point security and authentication flags.  These flags describe
the current security requirements of an access point as determined from the
access point's beacon."""
    NONE = 0
    PAIR_WEP40 = 1
    PAIR_WEP104 = 2
    PAIR_TKIP = 4
    PAIR_CCMP = 8
    GROUP_WEP40 = 16
    GROUP_WEP104 = 32
    GROUP_TKIP = 64
    GROUP_CCMP = 128
    KEY_MGMT_PSK = 256
    KEY_MGMT_802_1X = 512
    KEY_MGMT_SAE = 1024
    KEY_MGMT_OWE = 2048
    KEY_MGMT_OWE_TM = 4096
    KEY_MGMT_EAP_SUITE_B_192 = 8192


# NOTE: The runtime name is '80211Mode' (invalid Python identifier).
# Access at runtime via: getattr(NM, '80211Mode')
class NM80211Mode(enum.Enum):
    """Indicates the 802.11 mode an access point or device is currently in."""
    UNKNOWN = 0
    ADHOC = 1
    INFRA = 2
    AP = 3
    MESH = 4


ACCESS_POINT_BANDWIDTH = 'bandwidth'
ACCESS_POINT_BSSID = 'bssid'
ACCESS_POINT_FLAGS = 'flags'
ACCESS_POINT_FREQUENCY = 'frequency'
ACCESS_POINT_HW_ADDRESS = 'hw-address'
ACCESS_POINT_LAST_SEEN = 'last-seen'
ACCESS_POINT_MAX_BITRATE = 'max-bitrate'
ACCESS_POINT_MODE = 'mode'
ACCESS_POINT_RSN_FLAGS = 'rsn-flags'
ACCESS_POINT_SSID = 'ssid'
ACCESS_POINT_STRENGTH = 'strength'
ACCESS_POINT_WPA_FLAGS = 'wpa-flags'
ACTIVE_CONNECTION_CONNECTION = 'connection'
ACTIVE_CONNECTION_CONTROLLER = 'controller'
ACTIVE_CONNECTION_DEFAULT = 'default'
ACTIVE_CONNECTION_DEFAULT6 = 'default6'
ACTIVE_CONNECTION_DEVICES = 'devices'
ACTIVE_CONNECTION_DHCP4_CONFIG = 'dhcp4-config'
ACTIVE_CONNECTION_DHCP6_CONFIG = 'dhcp6-config'
ACTIVE_CONNECTION_ID = 'id'
ACTIVE_CONNECTION_IP4_CONFIG = 'ip4-config'
ACTIVE_CONNECTION_IP6_CONFIG = 'ip6-config'
ACTIVE_CONNECTION_MASTER = 'master'
ACTIVE_CONNECTION_SPECIFIC_OBJECT_PATH = 'specific-object-path'
ACTIVE_CONNECTION_STATE = 'state'
ACTIVE_CONNECTION_STATE_FLAGS = 'state-flags'
ACTIVE_CONNECTION_TYPE = 'type'
ACTIVE_CONNECTION_UUID = 'uuid'
ACTIVE_CONNECTION_VPN = 'vpn'


class ActivationStateFlags(enum.Enum):
    """Flags describing the current activation state."""
    NONE = 0
    IS_CONTROLLER = 1
    IS_PORT = 2
    LAYER2_READY = 4
    IP4_READY = 8
    IP6_READY = 16
    CONTROLLER_HAS_PORTS = 32
    LIFETIME_BOUND_TO_PROFILE_VISIBILITY = 64
    EXTERNAL = 128


class ActiveConnectionState(enum.Enum):
    """#NMActiveConnectionState values indicate the state of a connection to a
specific network while it is starting, connected, or disconnecting from that
network."""
    UNKNOWN = 0
    ACTIVATING = 1
    ACTIVATED = 2
    DEACTIVATING = 3
    DEACTIVATED = 4


class ActiveConnectionStateReason(enum.Enum):
    """Active connection state reasons."""
    UNKNOWN = 0
    NONE = 1
    USER_DISCONNECTED = 2
    DEVICE_DISCONNECTED = 3
    SERVICE_STOPPED = 4
    IP_CONFIG_INVALID = 5
    CONNECT_TIMEOUT = 6
    SERVICE_START_TIMEOUT = 7
    SERVICE_START_FAILED = 8
    NO_SECRETS = 9
    LOGIN_FAILED = 10
    CONNECTION_REMOVED = 11
    DEPENDENCY_FAILED = 12
    DEVICE_REALIZE_FAILED = 13
    DEVICE_REMOVED = 14


class AgentManagerError(enum.Enum):
    """Errors returned from the secret-agent manager.

These errors may be returned from operations that could cause secrets to be
requested (such as nm_client_activate_connection()), and correspond to D-Bus
errors in the "org.freedesktop.NetworkManager.AgentManager" namespace."""
    FAILED = 0
    PERMISSIONDENIED = 1
    INVALIDIDENTIFIER = 2
    NOTREGISTERED = 3
    NOSECRETS = 4
    USERCANCELED = 5


BRIDGE_VLAN_VID_MAX = '4094'
BRIDGE_VLAN_VID_MIN = '1'


class BluetoothCapabilities(enum.Enum):
    """#NMBluetoothCapabilities values indicate the usable capabilities of a
Bluetooth device."""
    NONE = 0
    DUN = 1
    NAP = 2


CHECKPOINT_CREATED = 'created'
CHECKPOINT_DEVICES = 'devices'
CHECKPOINT_ROLLBACK_TIMEOUT = 'rollback-timeout'
CLIENT_ACTIVATING_CONNECTION = 'activating-connection'
CLIENT_ACTIVE_CONNECTIONS = 'active-connections'
CLIENT_ACTIVE_CONNECTION_ADDED = 'active-connection-added'
CLIENT_ACTIVE_CONNECTION_REMOVED = 'active-connection-removed'
CLIENT_ALL_DEVICES = 'all-devices'
CLIENT_ANY_DEVICE_ADDED = 'any-device-added'
CLIENT_ANY_DEVICE_REMOVED = 'any-device-removed'
CLIENT_CAN_MODIFY = 'can-modify'
CLIENT_CAPABILITIES = 'capabilities'
CLIENT_CHECKPOINTS = 'checkpoints'
CLIENT_CONNECTIONS = 'connections'
CLIENT_CONNECTION_ADDED = 'connection-added'
CLIENT_CONNECTION_REMOVED = 'connection-removed'
CLIENT_CONNECTIVITY = 'connectivity'
CLIENT_CONNECTIVITY_CHECK_AVAILABLE = 'connectivity-check-available'
CLIENT_CONNECTIVITY_CHECK_ENABLED = 'connectivity-check-enabled'
CLIENT_CONNECTIVITY_CHECK_URI = 'connectivity-check-uri'
CLIENT_DBUS_CONNECTION = 'dbus-connection'
CLIENT_DBUS_NAME_OWNER = 'dbus-name-owner'
CLIENT_DEVICES = 'devices'
CLIENT_DEVICE_ADDED = 'device-added'
CLIENT_DEVICE_REMOVED = 'device-removed'
CLIENT_DNS_CONFIGURATION = 'dns-configuration'
CLIENT_DNS_MODE = 'dns-mode'
CLIENT_DNS_RC_MANAGER = 'dns-rc-manager'
CLIENT_HOSTNAME = 'hostname'
CLIENT_INSTANCE_FLAGS = 'instance-flags'
CLIENT_METERED = 'metered'
CLIENT_NETWORKING_ENABLED = 'networking-enabled'
CLIENT_NM_RUNNING = 'nm-running'
CLIENT_PERMISSIONS_STATE = 'permissions-state'
CLIENT_PERMISSION_CHANGED = 'permission-changed'
CLIENT_PRIMARY_CONNECTION = 'primary-connection'
CLIENT_RADIO_FLAGS = 'radio-flags'
CLIENT_STARTUP = 'startup'
CLIENT_STATE = 'state'
CLIENT_VERSION = 'version'
CLIENT_VERSION_INFO = 'version-info'
CLIENT_WIMAX_ENABLED = 'wimax-enabled'
CLIENT_WIMAX_HARDWARE_ENABLED = 'wimax-hardware-enabled'
CLIENT_WIRELESS_ENABLED = 'wireless-enabled'
CLIENT_WIRELESS_HARDWARE_ENABLED = 'wireless-hardware-enabled'
CLIENT_WWAN_ENABLED = 'wwan-enabled'
CLIENT_WWAN_HARDWARE_ENABLED = 'wwan-hardware-enabled'
CONNECTION_CHANGED = 'changed'
CONNECTION_NORMALIZE_PARAM_IP4_CONFIG_METHOD = 'ip4-config-method'
CONNECTION_NORMALIZE_PARAM_IP6_CONFIG_METHOD = 'ip6-config-method'
CONNECTION_SECRETS_CLEARED = 'secrets-cleared'
CONNECTION_SECRETS_UPDATED = 'secrets-updated'


class Capability(enum.Enum):
    """#NMCapability names the numbers in the Capabilities property.
Capabilities are positive numbers. They are part of stable API
and a certain capability number is guaranteed not to change.

The range 0x7000 - 0x7FFF of capabilities is guaranteed not to be
used by upstream NetworkManager. It could thus be used for downstream
extensions."""
    TEAM = 1
    OVS = 2


class CheckpointCreateFlags(enum.Enum):
    """The flags for CheckpointCreate call"""
    NONE = 0
    DESTROY_ALL = 1
    DELETE_NEW_CONNECTIONS = 2
    DISCONNECT_NEW_DEVICES = 4
    ALLOW_OVERLAPPING = 8
    NO_PRESERVE_EXTERNAL_PORTS = 16
    TRACK_INTERNAL_GLOBAL_DNS = 32


class ClientError(enum.Enum):
    """Describes errors that may result from operations involving a #NMClient.

D-Bus operations may also return errors from other domains, including
#NMManagerError, #NMSettingsError, #NMAgentManagerError, and #NMConnectionError."""
    FAILED = 0
    MANAGER_NOT_RUNNING = 1
    OBJECT_CREATION_FAILED = 2


class ClientInstanceFlags(enum.Enum):
    """"""
    NONE = 0
    NO_AUTO_FETCH_PERMISSIONS = 1
    INITIALIZED_GOOD = 2
    INITIALIZED_BAD = 4


class ClientPermission(enum.Enum):
    """#NMClientPermission values indicate various permissions that NetworkManager
clients can obtain to perform certain tasks on behalf of the current user."""
    NONE = 0
    ENABLE_DISABLE_NETWORK = 1
    ENABLE_DISABLE_WIFI = 2
    ENABLE_DISABLE_WWAN = 3
    ENABLE_DISABLE_WIMAX = 4
    SLEEP_WAKE = 5
    NETWORK_CONTROL = 6
    WIFI_SHARE_PROTECTED = 7
    WIFI_SHARE_OPEN = 8
    SETTINGS_MODIFY_SYSTEM = 9
    SETTINGS_MODIFY_OWN = 10
    SETTINGS_MODIFY_HOSTNAME = 11
    SETTINGS_MODIFY_GLOBAL_DNS = 12
    RELOAD = 13
    CHECKPOINT_ROLLBACK = 14
    ENABLE_DISABLE_STATISTICS = 15
    ENABLE_DISABLE_CONNECTIVITY_CHECK = 16
    WIFI_SCAN = 17
    LAST = 17


class ClientPermissionResult(enum.Enum):
    """#NMClientPermissionResult values indicate what authorizations and permissions
the user requires to obtain a given #NMClientPermission"""
    UNKNOWN = 0
    YES = 1
    AUTH = 2
    NO = 3


class ConnectionError(enum.Enum):
    """Describes errors that may result from operations involving a #NMConnection
or its #NMSettings.

These errors may be returned directly from #NMConnection and #NMSetting
methods, or may be returned from D-Bus operations (eg on #NMClient or
#NMDevice), where they correspond to errors in the
"org.freedesktop.NetworkManager.Settings.Connection" namespace."""
    FAILED = 0
    SETTINGNOTFOUND = 1
    PROPERTYNOTFOUND = 2
    PROPERTYNOTSECRET = 3
    MISSINGSETTING = 4
    INVALIDSETTING = 5
    MISSINGPROPERTY = 6
    INVALIDPROPERTY = 7


class ConnectionMultiConnect(enum.Enum):
    """"""
    DEFAULT = 0
    SINGLE = 1
    MANUAL_MULTIPLE = 2
    MULTIPLE = 3


class ConnectionSerializationFlags(enum.Enum):
    """These flags determine which properties are serialized when calling
nm_connection_to_dbus()."""
    ALL = 0
    WITH_NON_SECRET = 1
    NO_SECRETS = 1
    WITH_SECRETS = 2
    ONLY_SECRETS = 2
    WITH_SECRETS_AGENT_OWNED = 4
    WITH_SECRETS_SYSTEM_OWNED = 8
    WITH_SECRETS_NOT_SAVED = 16


class ConnectivityState(enum.Enum):
    """"""
    UNKNOWN = 0
    NONE = 1
    PORTAL = 2
    LIMITED = 3
    FULL = 4


class CryptoError(enum.Enum):
    """Cryptography-related errors that can be returned from some nm-utils methods,
and some #NMSetting8021x operations."""
    FAILED = 0
    INVALID_DATA = 1
    INVALID_PASSWORD = 2
    UNKNOWN_CIPHER = 3
    DECRYPTION_FAILED = 4
    ENCRYPTION_FAILED = 5


DBUS_INTERFACE = 'org.freedesktop.NetworkManager'
DBUS_INTERFACE_DNS_MANAGER = 'org.freedesktop.NetworkManager.DnsManager'
DBUS_INTERFACE_SETTINGS = 'org.freedesktop.NetworkManager.Settings'
DBUS_INTERFACE_SETTINGS_CONNECTION = (
    'org.freedesktop.NetworkManager.Settings.Connection')
DBUS_INTERFACE_SETTINGS_CONNECTION_SECRETS = (
    'org.freedesktop.NetworkManager.Settings.Connection.Secrets')
DBUS_INTERFACE_VPN = 'org.freedesktop.NetworkManager.VPN.Manager'
DBUS_INTERFACE_VPN_CONNECTION = 'org.freedesktop.NetworkManager.VPN.Connection'
DBUS_INVALID_VPN_CONNECTION = (
    'org.freedesktop.NetworkManager.VPNConnections.InvalidVPNConnection')
DBUS_NO_ACTIVE_VPN_CONNECTION = (
    'org.freedesktop.NetworkManager.VPNConnections.NoActiveVPNConnection')
DBUS_NO_VPN_CONNECTIONS = (
    'org.freedesktop.NetworkManager.VPNConnections.NoVPNConnections')
DBUS_PATH = '/org/freedesktop/NetworkManager'
DBUS_PATH_AGENT_MANAGER = '/org/freedesktop/NetworkManager/AgentManager'
DBUS_PATH_DNS_MANAGER = '/org/freedesktop/NetworkManager/DnsManager'
DBUS_PATH_SECRET_AGENT = '/org/freedesktop/NetworkManager/SecretAgent'
DBUS_PATH_SETTINGS = '/org/freedesktop/NetworkManager/Settings'
DBUS_PATH_SETTINGS_CONNECTION = (
    '/org/freedesktop/NetworkManager/Settings/Connection')
DBUS_PATH_VPN = '/org/freedesktop/NetworkManager/VPN/Manager'
DBUS_PATH_VPN_CONNECTION = '/org/freedesktop/NetworkManager/VPN/Connection'
DBUS_SERVICE = 'org.freedesktop.NetworkManager'
DBUS_VPN_ALREADY_STARTED = 'AlreadyStarted'
DBUS_VPN_ALREADY_STOPPED = 'AlreadyStopped'
DBUS_VPN_BAD_ARGUMENTS = 'BadArguments'
DBUS_VPN_ERROR_PREFIX = 'org.freedesktop.NetworkManager.VPN.Error'
DBUS_VPN_INTERACTIVE_NOT_SUPPORTED = 'InteractiveNotSupported'
DBUS_VPN_SIGNAL_CONNECT_FAILED = 'ConnectFailed'
DBUS_VPN_SIGNAL_IP4_CONFIG = 'IP4Config'
DBUS_VPN_SIGNAL_IP_CONFIG_BAD = 'IPConfigBad'
DBUS_VPN_SIGNAL_LAUNCH_FAILED = 'LaunchFailed'
DBUS_VPN_SIGNAL_LOGIN_BANNER = 'LoginBanner'
DBUS_VPN_SIGNAL_LOGIN_FAILED = 'LoginFailed'
DBUS_VPN_SIGNAL_STATE_CHANGE = 'StateChange'
DBUS_VPN_SIGNAL_VPN_CONFIG_BAD = 'VPNConfigBad'
DBUS_VPN_STARTING_IN_PROGRESS = 'StartingInProgress'
DBUS_VPN_STOPPING_IN_PROGRESS = 'StoppingInProgress'
DBUS_VPN_WRONG_STATE = 'WrongState'
DEVICE_6LOWPAN_HW_ADDRESS = 'hw-address'
DEVICE_6LOWPAN_PARENT = 'parent'
DEVICE_ACTIVE_CONNECTION = 'active-connection'
DEVICE_ADSL_CARRIER = 'carrier'
DEVICE_AUTOCONNECT = 'autoconnect'
DEVICE_AVAILABLE_CONNECTIONS = 'available-connections'
DEVICE_BOND_CARRIER = 'carrier'
DEVICE_BOND_HW_ADDRESS = 'hw-address'
DEVICE_BOND_SLAVES = 'slaves'
DEVICE_BRIDGE_CARRIER = 'carrier'
DEVICE_BRIDGE_HW_ADDRESS = 'hw-address'
DEVICE_BRIDGE_SLAVES = 'slaves'
DEVICE_BT_CAPABILITIES = 'bt-capabilities'
DEVICE_BT_HW_ADDRESS = 'hw-address'
DEVICE_BT_NAME = 'name'
DEVICE_CAPABILITIES = 'capabilities'
DEVICE_DEVICE_TYPE = 'device-type'
DEVICE_DHCP4_CONFIG = 'dhcp4-config'
DEVICE_DHCP6_CONFIG = 'dhcp6-config'
DEVICE_DRIVER = 'driver'
DEVICE_DRIVER_VERSION = 'driver-version'
DEVICE_DUMMY_HW_ADDRESS = 'hw-address'
DEVICE_ETHERNET_CARRIER = 'carrier'
DEVICE_ETHERNET_HW_ADDRESS = 'hw-address'
DEVICE_ETHERNET_PERMANENT_HW_ADDRESS = 'perm-hw-address'
DEVICE_ETHERNET_S390_SUBCHANNELS = 's390-subchannels'
DEVICE_ETHERNET_SPEED = 'speed'
DEVICE_FIRMWARE_MISSING = 'firmware-missing'
DEVICE_FIRMWARE_VERSION = 'firmware-version'
DEVICE_GENERIC_HW_ADDRESS = 'hw-address'
DEVICE_GENERIC_TYPE_DESCRIPTION = 'type-description'
DEVICE_HSR_MULTICAST_SPEC = 'multicast-spec'
DEVICE_HSR_PORT1 = 'port1'
DEVICE_HSR_PORT2 = 'port2'
DEVICE_HSR_PRP = 'prp'
DEVICE_HSR_SUPERVISION_ADDRESS = 'supervision-address'
DEVICE_HW_ADDRESS = 'hw-address'
DEVICE_INFINIBAND_CARRIER = 'carrier'
DEVICE_INFINIBAND_HW_ADDRESS = 'hw-address'
DEVICE_INTERFACE = 'interface'
DEVICE_INTERFACE_FLAGS = 'interface-flags'
DEVICE_IP4_CONFIG = 'ip4-config'
DEVICE_IP4_CONNECTIVITY = 'ip4-connectivity'
DEVICE_IP6_CONFIG = 'ip6-config'
DEVICE_IP6_CONNECTIVITY = 'ip6-connectivity'
DEVICE_IPVLAN_MODE = 'mode'
DEVICE_IPVLAN_PARENT = 'parent'
DEVICE_IPVLAN_PRIVATE = 'private'
DEVICE_IPVLAN_VEPA = 'vepa'
DEVICE_IP_INTERFACE = 'ip-interface'
DEVICE_IP_TUNNEL_ENCAPSULATION_LIMIT = 'encapsulation-limit'
DEVICE_IP_TUNNEL_FLAGS = 'flags'
DEVICE_IP_TUNNEL_FLOW_LABEL = 'flow-label'
DEVICE_IP_TUNNEL_FWMARK = 'fwmark'
DEVICE_IP_TUNNEL_INPUT_KEY = 'input-key'
DEVICE_IP_TUNNEL_LOCAL = 'local'
DEVICE_IP_TUNNEL_MODE = 'mode'
DEVICE_IP_TUNNEL_OUTPUT_KEY = 'output-key'
DEVICE_IP_TUNNEL_PARENT = 'parent'
DEVICE_IP_TUNNEL_PATH_MTU_DISCOVERY = 'path-mtu-discovery'
DEVICE_IP_TUNNEL_REMOTE = 'remote'
DEVICE_IP_TUNNEL_TOS = 'tos'
DEVICE_IP_TUNNEL_TTL = 'ttl'
DEVICE_LLDP_NEIGHBORS = 'lldp-neighbors'
DEVICE_MACSEC_CIPHER_SUITE = 'cipher-suite'
DEVICE_MACSEC_ENCODING_SA = 'encoding-sa'
DEVICE_MACSEC_ENCRYPT = 'encrypt'
DEVICE_MACSEC_ES = 'es'
DEVICE_MACSEC_HW_ADDRESS = 'hw-address'
DEVICE_MACSEC_ICV_LENGTH = 'icv-length'
DEVICE_MACSEC_INCLUDE_SCI = 'include-sci'
DEVICE_MACSEC_PARENT = 'parent'
DEVICE_MACSEC_PROTECT = 'protect'
DEVICE_MACSEC_REPLAY_PROTECT = 'replay-protect'
DEVICE_MACSEC_SCB = 'scb'
DEVICE_MACSEC_SCI = 'sci'
DEVICE_MACSEC_VALIDATION = 'validation'
DEVICE_MACSEC_WINDOW = 'window'
DEVICE_MACVLAN_HW_ADDRESS = 'hw-address'
DEVICE_MACVLAN_MODE = 'mode'
DEVICE_MACVLAN_NO_PROMISC = 'no-promisc'
DEVICE_MACVLAN_PARENT = 'parent'
DEVICE_MACVLAN_TAP = 'tap'
DEVICE_MANAGED = 'managed'
DEVICE_METERED = 'metered'
DEVICE_MODEM_APN = 'apn'
DEVICE_MODEM_CURRENT_CAPABILITIES = 'current-capabilities'
DEVICE_MODEM_DEVICE_ID = 'device-id'
DEVICE_MODEM_MODEM_CAPABILITIES = 'modem-capabilities'
DEVICE_MODEM_OPERATOR_CODE = 'operator-code'
DEVICE_MTU = 'mtu'
DEVICE_NM_PLUGIN_MISSING = 'nm-plugin-missing'
DEVICE_OLPC_MESH_ACTIVE_CHANNEL = 'active-channel'
DEVICE_OLPC_MESH_COMPANION = 'companion'
DEVICE_OLPC_MESH_HW_ADDRESS = 'hw-address'
DEVICE_OVS_BRIDGE_SLAVES = 'slaves'
DEVICE_OVS_PORT_SLAVES = 'slaves'
DEVICE_PATH = 'path'
DEVICE_PHYSICAL_PORT_ID = 'physical-port-id'
DEVICE_PORTS = 'ports'
DEVICE_PRODUCT = 'product'
DEVICE_REAL = 'real'
DEVICE_STATE = 'state'
DEVICE_STATE_REASON = 'state-reason'
DEVICE_TEAM_CARRIER = 'carrier'
DEVICE_TEAM_CONFIG = 'config'
DEVICE_TEAM_HW_ADDRESS = 'hw-address'
DEVICE_TEAM_SLAVES = 'slaves'
DEVICE_TUN_GROUP = 'group'
DEVICE_TUN_HW_ADDRESS = 'hw-address'
DEVICE_TUN_MODE = 'mode'
DEVICE_TUN_MULTI_QUEUE = 'multi-queue'
DEVICE_TUN_NO_PI = 'no-pi'
DEVICE_TUN_OWNER = 'owner'
DEVICE_TUN_VNET_HDR = 'vnet-hdr'
DEVICE_UDI = 'udi'
DEVICE_VENDOR = 'vendor'
DEVICE_VETH_PEER = 'peer'
DEVICE_VLAN_CARRIER = 'carrier'
DEVICE_VLAN_HW_ADDRESS = 'hw-address'
DEVICE_VLAN_PARENT = 'parent'
DEVICE_VLAN_VLAN_ID = 'vlan-id'
DEVICE_VRF_TABLE = 'table'
DEVICE_VXLAN_AGEING = 'ageing'
DEVICE_VXLAN_CARRIER = 'carrier'
DEVICE_VXLAN_DST_PORT = 'dst-port'
DEVICE_VXLAN_GROUP = 'group'
DEVICE_VXLAN_HW_ADDRESS = 'hw-address'
DEVICE_VXLAN_ID = 'id'
DEVICE_VXLAN_L2MISS = 'l2miss'
DEVICE_VXLAN_L3MISS = 'l3miss'
DEVICE_VXLAN_LEARNING = 'learning'
DEVICE_VXLAN_LIMIT = 'limit'
DEVICE_VXLAN_LOCAL = 'local'
DEVICE_VXLAN_PARENT = 'parent'
DEVICE_VXLAN_PROXY = 'proxy'
DEVICE_VXLAN_RSC = 'rsc'
DEVICE_VXLAN_SRC_PORT_MAX = 'src-port-max'
DEVICE_VXLAN_SRC_PORT_MIN = 'src-port-min'
DEVICE_VXLAN_TOS = 'tos'
DEVICE_VXLAN_TTL = 'ttl'
DEVICE_WIFI_ACCESS_POINTS = 'access-points'
DEVICE_WIFI_ACTIVE_ACCESS_POINT = 'active-access-point'
DEVICE_WIFI_BITRATE = 'bitrate'
DEVICE_WIFI_CAPABILITIES = 'wireless-capabilities'
DEVICE_WIFI_HW_ADDRESS = 'hw-address'
DEVICE_WIFI_LAST_SCAN = 'last-scan'
DEVICE_WIFI_MODE = 'mode'
DEVICE_WIFI_P2P_HW_ADDRESS = 'hw-address'
DEVICE_WIFI_P2P_PEERS = 'peers'
DEVICE_WIFI_P2P_WFDIES = 'wfdies'
DEVICE_WIFI_PERMANENT_HW_ADDRESS = 'perm-hw-address'
DEVICE_WIMAX_ACTIVE_NSP = 'active-nsp'
DEVICE_WIMAX_BSID = 'bsid'
DEVICE_WIMAX_CENTER_FREQUENCY = 'center-frequency'
DEVICE_WIMAX_CINR = 'cinr'
DEVICE_WIMAX_HW_ADDRESS = 'hw-address'
DEVICE_WIMAX_NSPS = 'nsps'
DEVICE_WIMAX_RSSI = 'rssi'
DEVICE_WIMAX_TX_POWER = 'tx-power'
DEVICE_WIREGUARD_FWMARK = 'fwmark'
DEVICE_WIREGUARD_LISTEN_PORT = 'listen-port'
DEVICE_WIREGUARD_PUBLIC_KEY = 'public-key'
DEVICE_WPAN_HW_ADDRESS = 'hw-address'
DHCP_CONFIG_FAMILY = 'family'
DHCP_CONFIG_OPTIONS = 'options'


class DeviceCapabilities(enum.Enum):
    """General device capability flags."""
    NONE = 0
    NM_SUPPORTED = 1
    CARRIER_DETECT = 2
    IS_SOFTWARE = 4
    SRIOV = 8


class DeviceError(enum.Enum):
    """Device-related errors.

These errors may be returned directly from #NMDevice methods, or may be
returned from D-Bus operations (where they correspond to errors in the
"org.freedesktop.NetworkManager.Device" namespace)."""
    FAILED = 0
    CREATIONFAILED = 1
    INVALIDCONNECTION = 2
    INCOMPATIBLECONNECTION = 3
    NOTACTIVE = 4
    NOTSOFTWARE = 5
    NOTALLOWED = 6
    SPECIFICOBJECTNOTFOUND = 7
    VERSIONIDMISMATCH = 8
    MISSINGDEPENDENCIES = 9
    INVALIDARGUMENT = 10


class DeviceInterfaceFlags(enum.Enum):
    """Flags for a network interface."""
    UP = 1
    LOWER_UP = 2
    PROMISC = 4
    CARRIER = 65536
    LLDP_CLIENT_ENABLED = 131072


class DeviceModemCapabilities(enum.Enum):
    """#NMDeviceModemCapabilities values indicate the generic radio access
technology families a modem device supports.  For more information on the
specific access technologies the device supports use the ModemManager D-Bus
API."""
    NONE = 0
    POTS = 1
    CDMA_EVDO = 2
    GSM_UMTS = 4
    LTE = 8
    _5GNR = 64


class DeviceReapplyFlags(enum.Enum):
    """Flags for the Reapply() D-Bus call of a device and
nm_device_reapply_async()."""
    NONE = 0
    PRESERVE_EXTERNAL_IP = 1


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


class DeviceStateReason(enum.Enum):
    """Device state change reason codes"""
    NONE = 0
    UNKNOWN = 1
    NOW_MANAGED = 2
    NOW_UNMANAGED = 3
    CONFIG_FAILED = 4
    IP_CONFIG_UNAVAILABLE = 5
    IP_CONFIG_EXPIRED = 6
    NO_SECRETS = 7
    SUPPLICANT_DISCONNECT = 8
    SUPPLICANT_CONFIG_FAILED = 9
    SUPPLICANT_FAILED = 10
    SUPPLICANT_TIMEOUT = 11
    PPP_START_FAILED = 12
    PPP_DISCONNECT = 13
    PPP_FAILED = 14
    DHCP_START_FAILED = 15
    DHCP_ERROR = 16
    DHCP_FAILED = 17
    SHARED_START_FAILED = 18
    SHARED_FAILED = 19
    AUTOIP_START_FAILED = 20
    AUTOIP_ERROR = 21
    AUTOIP_FAILED = 22
    MODEM_BUSY = 23
    MODEM_NO_DIAL_TONE = 24
    MODEM_NO_CARRIER = 25
    MODEM_DIAL_TIMEOUT = 26
    MODEM_DIAL_FAILED = 27
    MODEM_INIT_FAILED = 28
    GSM_APN_FAILED = 29
    GSM_REGISTRATION_NOT_SEARCHING = 30
    GSM_REGISTRATION_DENIED = 31
    GSM_REGISTRATION_TIMEOUT = 32
    GSM_REGISTRATION_FAILED = 33
    GSM_PIN_CHECK_FAILED = 34
    FIRMWARE_MISSING = 35
    REMOVED = 36
    SLEEPING = 37
    CONNECTION_REMOVED = 38
    USER_REQUESTED = 39
    CARRIER = 40
    CONNECTION_ASSUMED = 41
    SUPPLICANT_AVAILABLE = 42
    MODEM_NOT_FOUND = 43
    BT_FAILED = 44
    GSM_SIM_NOT_INSERTED = 45
    GSM_SIM_PIN_REQUIRED = 46
    GSM_SIM_PUK_REQUIRED = 47
    GSM_SIM_WRONG = 48
    INFINIBAND_MODE = 49
    DEPENDENCY_FAILED = 50
    BR2684_FAILED = 51
    MODEM_MANAGER_UNAVAILABLE = 52
    SSID_NOT_FOUND = 53
    SECONDARY_CONNECTION_FAILED = 54
    DCB_FCOE_FAILED = 55
    TEAMD_CONTROL_FAILED = 56
    MODEM_FAILED = 57
    MODEM_AVAILABLE = 58
    SIM_PIN_INCORRECT = 59
    NEW_ACTIVATION = 60
    PARENT_CHANGED = 61
    PARENT_MANAGED_CHANGED = 62
    OVSDB_FAILED = 63
    IP_ADDRESS_DUPLICATE = 64
    IP_METHOD_UNSUPPORTED = 65
    SRIOV_CONFIGURATION_FAILED = 66
    PEER_NOT_FOUND = 67
    DEVICE_HANDLER_FAILED = 68
    UNMANAGED_BY_DEFAULT = 69
    UNMANAGED_EXTERNAL_DOWN = 70
    UNMANAGED_LINK_NOT_INIT = 71
    UNMANAGED_QUITTING = 72
    UNMANAGED_SLEEPING = 73
    UNMANAGED_MANAGER_DISABLED = 73
    UNMANAGED_USER_CONF = 74
    UNMANAGED_USER_EXPLICIT = 75
    UNMANAGED_USER_SETTINGS = 76
    UNMANAGED_USER_UDEV = 77
    NETWORKING_OFF = 78
    MODEM_NO_OPERATOR_CODE = 79


class DeviceType(enum.Enum):
    """#NMDeviceType values indicate the type of hardware represented by a
device object."""
    UNKNOWN = 0
    ETHERNET = 1
    WIFI = 2
    UNUSED1 = 3
    UNUSED2 = 4
    BT = 5
    OLPC_MESH = 6
    WIMAX = 7
    MODEM = 8
    INFINIBAND = 9
    BOND = 10
    VLAN = 11
    ADSL = 12
    BRIDGE = 13
    GENERIC = 14
    TEAM = 15
    TUN = 16
    IP_TUNNEL = 17
    MACVLAN = 18
    VXLAN = 19
    VETH = 20
    MACSEC = 21
    DUMMY = 22
    PPP = 23
    OVS_INTERFACE = 24
    OVS_PORT = 25
    OVS_BRIDGE = 26
    WPAN = 27
    _6LOWPAN = 28
    WIREGUARD = 29
    WIFI_P2P = 30
    VRF = 31
    LOOPBACK = 32
    HSR = 33
    IPVLAN = 34


class DeviceWifiCapabilities(enum.Enum):
    """802.11 specific device encryption and authentication capabilities."""
    NONE = 0
    CIPHER_WEP40 = 1
    CIPHER_WEP104 = 2
    CIPHER_TKIP = 4
    CIPHER_CCMP = 8
    WPA = 16
    RSN = 32
    AP = 64
    ADHOC = 128
    FREQ_VALID = 256
    FREQ_2GHZ = 512
    FREQ_5GHZ = 1024
    FREQ_6GHZ = 2048
    MESH = 4096
    IBSS_RSN = 8192


class DhcpHostnameFlags(enum.Enum):
    """#NMDhcpHostnameFlags describe flags related to the DHCP hostname and
FQDN."""
    NONE = 0
    FQDN_SERV_UPDATE = 1
    FQDN_ENCODED = 2
    FQDN_NO_UPDATE = 4
    FQDN_CLEAR_FLAGS = 8


ETHTOOL_OPTNAME_CHANNELS_COMBINED = 'channels-combined'
ETHTOOL_OPTNAME_CHANNELS_OTHER = 'channels-other'
ETHTOOL_OPTNAME_CHANNELS_RX = 'channels-rx'
ETHTOOL_OPTNAME_CHANNELS_TX = 'channels-tx'
ETHTOOL_OPTNAME_COALESCE_ADAPTIVE_RX = 'coalesce-adaptive-rx'
ETHTOOL_OPTNAME_COALESCE_ADAPTIVE_TX = 'coalesce-adaptive-tx'
ETHTOOL_OPTNAME_COALESCE_PKT_RATE_HIGH = 'coalesce-pkt-rate-high'
ETHTOOL_OPTNAME_COALESCE_PKT_RATE_LOW = 'coalesce-pkt-rate-low'
ETHTOOL_OPTNAME_COALESCE_RX_FRAMES = 'coalesce-rx-frames'
ETHTOOL_OPTNAME_COALESCE_RX_FRAMES_HIGH = 'coalesce-rx-frames-high'
ETHTOOL_OPTNAME_COALESCE_RX_FRAMES_IRQ = 'coalesce-rx-frames-irq'
ETHTOOL_OPTNAME_COALESCE_RX_FRAMES_LOW = 'coalesce-rx-frames-low'
ETHTOOL_OPTNAME_COALESCE_RX_USECS = 'coalesce-rx-usecs'
ETHTOOL_OPTNAME_COALESCE_RX_USECS_HIGH = 'coalesce-rx-usecs-high'
ETHTOOL_OPTNAME_COALESCE_RX_USECS_IRQ = 'coalesce-rx-usecs-irq'
ETHTOOL_OPTNAME_COALESCE_RX_USECS_LOW = 'coalesce-rx-usecs-low'
ETHTOOL_OPTNAME_COALESCE_SAMPLE_INTERVAL = 'coalesce-sample-interval'
ETHTOOL_OPTNAME_COALESCE_STATS_BLOCK_USECS = 'coalesce-stats-block-usecs'
ETHTOOL_OPTNAME_COALESCE_TX_FRAMES = 'coalesce-tx-frames'
ETHTOOL_OPTNAME_COALESCE_TX_FRAMES_HIGH = 'coalesce-tx-frames-high'
ETHTOOL_OPTNAME_COALESCE_TX_FRAMES_IRQ = 'coalesce-tx-frames-irq'
ETHTOOL_OPTNAME_COALESCE_TX_FRAMES_LOW = 'coalesce-tx-frames-low'
ETHTOOL_OPTNAME_COALESCE_TX_USECS = 'coalesce-tx-usecs'
ETHTOOL_OPTNAME_COALESCE_TX_USECS_HIGH = 'coalesce-tx-usecs-high'
ETHTOOL_OPTNAME_COALESCE_TX_USECS_IRQ = 'coalesce-tx-usecs-irq'
ETHTOOL_OPTNAME_COALESCE_TX_USECS_LOW = 'coalesce-tx-usecs-low'
ETHTOOL_OPTNAME_EEE_ENABLED = 'eee-enabled'
ETHTOOL_OPTNAME_FEATURE_ESP_HW_OFFLOAD = 'feature-esp-hw-offload'
ETHTOOL_OPTNAME_FEATURE_ESP_TX_CSUM_HW_OFFLOAD = (
    'feature-esp-tx-csum-hw-offload')
ETHTOOL_OPTNAME_FEATURE_FCOE_MTU = 'feature-fcoe-mtu'
ETHTOOL_OPTNAME_FEATURE_GRO = 'feature-gro'
ETHTOOL_OPTNAME_FEATURE_GSO = 'feature-gso'
ETHTOOL_OPTNAME_FEATURE_HIGHDMA = 'feature-highdma'
ETHTOOL_OPTNAME_FEATURE_HW_TC_OFFLOAD = 'feature-hw-tc-offload'
ETHTOOL_OPTNAME_FEATURE_L2_FWD_OFFLOAD = 'feature-l2-fwd-offload'
ETHTOOL_OPTNAME_FEATURE_LOOPBACK = 'feature-loopback'
ETHTOOL_OPTNAME_FEATURE_LRO = 'feature-lro'
ETHTOOL_OPTNAME_FEATURE_MACSEC_HW_OFFLOAD = 'feature-macsec-hw-offload'
ETHTOOL_OPTNAME_FEATURE_NTUPLE = 'feature-ntuple'
ETHTOOL_OPTNAME_FEATURE_RX = 'feature-rx'
ETHTOOL_OPTNAME_FEATURE_RXHASH = 'feature-rxhash'
ETHTOOL_OPTNAME_FEATURE_RXVLAN = 'feature-rxvlan'
ETHTOOL_OPTNAME_FEATURE_RX_ALL = 'feature-rx-all'
ETHTOOL_OPTNAME_FEATURE_RX_FCS = 'feature-rx-fcs'
ETHTOOL_OPTNAME_FEATURE_RX_GRO_HW = 'feature-rx-gro-hw'
ETHTOOL_OPTNAME_FEATURE_RX_GRO_LIST = 'feature-rx-gro-list'
ETHTOOL_OPTNAME_FEATURE_RX_UDP_GRO_FORWARDING = 'feature-rx-udp-gro-forwarding'
ETHTOOL_OPTNAME_FEATURE_RX_UDP_TUNNEL_PORT_OFFLOAD = (
    'feature-rx-udp_tunnel-port-offload')
ETHTOOL_OPTNAME_FEATURE_RX_VLAN_FILTER = 'feature-rx-vlan-filter'
ETHTOOL_OPTNAME_FEATURE_RX_VLAN_STAG_FILTER = 'feature-rx-vlan-stag-filter'
ETHTOOL_OPTNAME_FEATURE_RX_VLAN_STAG_HW_PARSE = 'feature-rx-vlan-stag-hw-parse'
ETHTOOL_OPTNAME_FEATURE_SG = 'feature-sg'
ETHTOOL_OPTNAME_FEATURE_TLS_HW_RECORD = 'feature-tls-hw-record'
ETHTOOL_OPTNAME_FEATURE_TLS_HW_RX_OFFLOAD = 'feature-tls-hw-rx-offload'
ETHTOOL_OPTNAME_FEATURE_TLS_HW_TX_OFFLOAD = 'feature-tls-hw-tx-offload'
ETHTOOL_OPTNAME_FEATURE_TSO = 'feature-tso'
ETHTOOL_OPTNAME_FEATURE_TX = 'feature-tx'
ETHTOOL_OPTNAME_FEATURE_TXVLAN = 'feature-txvlan'
ETHTOOL_OPTNAME_FEATURE_TX_CHECKSUM_FCOE_CRC = 'feature-tx-checksum-fcoe-crc'
ETHTOOL_OPTNAME_FEATURE_TX_CHECKSUM_IPV4 = 'feature-tx-checksum-ipv4'
ETHTOOL_OPTNAME_FEATURE_TX_CHECKSUM_IPV6 = 'feature-tx-checksum-ipv6'
ETHTOOL_OPTNAME_FEATURE_TX_CHECKSUM_IP_GENERIC = (
    'feature-tx-checksum-ip-generic')
ETHTOOL_OPTNAME_FEATURE_TX_CHECKSUM_SCTP = 'feature-tx-checksum-sctp'
ETHTOOL_OPTNAME_FEATURE_TX_ESP_SEGMENTATION = 'feature-tx-esp-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_FCOE_SEGMENTATION = 'feature-tx-fcoe-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_GRE_CSUM_SEGMENTATION = (
    'feature-tx-gre-csum-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_GRE_SEGMENTATION = 'feature-tx-gre-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_GSO_LIST = 'feature-tx-gso-list'
ETHTOOL_OPTNAME_FEATURE_TX_GSO_PARTIAL = 'feature-tx-gso-partial'
ETHTOOL_OPTNAME_FEATURE_TX_GSO_ROBUST = 'feature-tx-gso-robust'
ETHTOOL_OPTNAME_FEATURE_TX_IPXIP4_SEGMENTATION = (
    'feature-tx-ipxip4-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_IPXIP6_SEGMENTATION = (
    'feature-tx-ipxip6-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_NOCACHE_COPY = 'feature-tx-nocache-copy'
ETHTOOL_OPTNAME_FEATURE_TX_SCATTER_GATHER = 'feature-tx-scatter-gather'
ETHTOOL_OPTNAME_FEATURE_TX_SCATTER_GATHER_FRAGLIST = (
    'feature-tx-scatter-gather-fraglist')
ETHTOOL_OPTNAME_FEATURE_TX_SCTP_SEGMENTATION = 'feature-tx-sctp-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_TCP6_SEGMENTATION = 'feature-tx-tcp6-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_TCP_ECN_SEGMENTATION = (
    'feature-tx-tcp-ecn-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_TCP_MANGLEID_SEGMENTATION = (
    'feature-tx-tcp-mangleid-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_TCP_SEGMENTATION = 'feature-tx-tcp-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_TUNNEL_REMCSUM_SEGMENTATION = (
    'feature-tx-tunnel-remcsum-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_UDP_SEGMENTATION = 'feature-tx-udp-segmentation'
ETHTOOL_OPTNAME_FEATURE_TX_UDP_TNL_CSUM_SEGMENTATION = (
    'feature-tx-udp_tnl-csum-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_UDP_TNL_SEGMENTATION = (
    'feature-tx-udp_tnl-segmentation')
ETHTOOL_OPTNAME_FEATURE_TX_VLAN_STAG_HW_INSERT = (
    'feature-tx-vlan-stag-hw-insert')
ETHTOOL_OPTNAME_FEC_MODE = 'fec-mode'
ETHTOOL_OPTNAME_PAUSE_AUTONEG = 'pause-autoneg'
ETHTOOL_OPTNAME_PAUSE_RX = 'pause-rx'
ETHTOOL_OPTNAME_PAUSE_TX = 'pause-tx'
ETHTOOL_OPTNAME_RING_RX = 'ring-rx'
ETHTOOL_OPTNAME_RING_RX_JUMBO = 'ring-rx-jumbo'
ETHTOOL_OPTNAME_RING_RX_MINI = 'ring-rx-mini'
ETHTOOL_OPTNAME_RING_TX = 'ring-tx'


class IPAddressCmpFlags(enum.Enum):
    """Compare flags for nm_ip_address_cmp_full()."""
    NONE = 0
    WITH_ATTRS = 1


class IPRoutingRuleAsStringFlags(enum.Enum):
    """"""
    NONE = 0
    AF_INET = 1
    AF_INET6 = 2
    VALIDATE = 4


class IPTunnelFlags(enum.Enum):
    """IP tunnel flags."""
    NONE = 0
    IP6_IGN_ENCAP_LIMIT = 1
    IP6_USE_ORIG_TCLASS = 2
    IP6_USE_ORIG_FLOWLABEL = 4
    IP6_MIP6_DEV = 8
    IP6_RCV_DSCP_COPY = 16
    IP6_USE_ORIG_FWMARK = 32


class IPTunnelMode(enum.Enum):
    """The tunneling mode."""
    UNKNOWN = 0
    IPIP = 1
    GRE = 2
    SIT = 3
    ISATAP = 4
    VTI = 5
    IP6IP6 = 6
    IPIP6 = 7
    IP6GRE = 8
    VTI6 = 9
    GRETAP = 10
    IP6GRETAP = 11


IP_ADDRESS_ATTRIBUTE_LABEL = 'label'
IP_CONFIG_ADDRESSES = 'addresses'
IP_CONFIG_DOMAINS = 'domains'
IP_CONFIG_FAMILY = 'family'
IP_CONFIG_GATEWAY = 'gateway'
IP_CONFIG_NAMESERVERS = 'nameservers'
IP_CONFIG_ROUTES = 'routes'
IP_CONFIG_SEARCHES = 'searches'
IP_CONFIG_WINS_SERVERS = 'wins-servers'
IP_ROUTE_ATTRIBUTE_ADVMSS = 'advmss'
IP_ROUTE_ATTRIBUTE_CWND = 'cwnd'
IP_ROUTE_ATTRIBUTE_FROM = 'from'
IP_ROUTE_ATTRIBUTE_INITCWND = 'initcwnd'
IP_ROUTE_ATTRIBUTE_INITRWND = 'initrwnd'
IP_ROUTE_ATTRIBUTE_LOCK_ADVMSS = 'lock-advmss'
IP_ROUTE_ATTRIBUTE_LOCK_CWND = 'lock-cwnd'
IP_ROUTE_ATTRIBUTE_LOCK_INITCWND = 'lock-initcwnd'
IP_ROUTE_ATTRIBUTE_LOCK_INITRWND = 'lock-initrwnd'
IP_ROUTE_ATTRIBUTE_LOCK_MTU = 'lock-mtu'
IP_ROUTE_ATTRIBUTE_LOCK_WINDOW = 'lock-window'
IP_ROUTE_ATTRIBUTE_MTU = 'mtu'
IP_ROUTE_ATTRIBUTE_ONLINK = 'onlink'
IP_ROUTE_ATTRIBUTE_QUICKACK = 'quickack'
IP_ROUTE_ATTRIBUTE_RTO_MIN = 'rto_min'
IP_ROUTE_ATTRIBUTE_SCOPE = 'scope'
IP_ROUTE_ATTRIBUTE_SRC = 'src'
IP_ROUTE_ATTRIBUTE_TABLE = 'table'
IP_ROUTE_ATTRIBUTE_TOS = 'tos'
IP_ROUTE_ATTRIBUTE_TYPE = 'type'
IP_ROUTE_ATTRIBUTE_WEIGHT = 'weight'
IP_ROUTE_ATTRIBUTE_WINDOW = 'window'


class KeyfileHandlerFlags(enum.Enum):
    """Flags for customizing nm_keyfile_read() and nm_keyfile_write().

Currently no flags are implemented."""
    NONE = 0


class KeyfileHandlerType(enum.Enum):
    """The type of the callback for %NMKeyfileReadHandler and %NMKeyfileWriteHandler.
Depending on the type, you can interpret %NMKeyfileHandlerData."""
    WARN = 1
    WRITE_CERT = 2


class KeyfileWarnSeverity(enum.Enum):
    """The severity level of %NM_KEYFILE_HANDLER_TYPE_WARN events."""
    DEBUG = 1000
    INFO = 2000
    INFO_MISSING_FILE = 2901
    WARN = 3000


LLDP_ATTR_CHASSIS_ID = 'chassis-id'
LLDP_ATTR_CHASSIS_ID_TYPE = 'chassis-id-type'
LLDP_ATTR_DESTINATION = 'destination'
LLDP_ATTR_IEEE_802_1_PPVID = 'ieee-802-1-ppvid'
LLDP_ATTR_IEEE_802_1_PPVIDS = 'ieee-802-1-ppvids'
LLDP_ATTR_IEEE_802_1_PPVID_FLAGS = 'ieee-802-1-ppvid-flags'
LLDP_ATTR_IEEE_802_1_PVID = 'ieee-802-1-pvid'
LLDP_ATTR_IEEE_802_1_VID = 'ieee-802-1-vid'
LLDP_ATTR_IEEE_802_1_VLANS = 'ieee-802-1-vlans'
LLDP_ATTR_IEEE_802_1_VLAN_NAME = 'ieee-802-1-vlan-name'
LLDP_ATTR_IEEE_802_3_MAC_PHY_CONF = 'ieee-802-3-mac-phy-conf'
LLDP_ATTR_IEEE_802_3_MAX_FRAME_SIZE = 'ieee-802-3-max-frame-size'
LLDP_ATTR_IEEE_802_3_POWER_VIA_MDI = 'ieee-802-3-power-via-mdi'
LLDP_ATTR_MANAGEMENT_ADDRESSES = 'management-addresses'
LLDP_ATTR_MUD_URL = 'mud-url'
LLDP_ATTR_PORT_DESCRIPTION = 'port-description'
LLDP_ATTR_PORT_ID = 'port-id'
LLDP_ATTR_PORT_ID_TYPE = 'port-id-type'
LLDP_ATTR_RAW = 'raw'
LLDP_ATTR_SYSTEM_CAPABILITIES = 'system-capabilities'
LLDP_ATTR_SYSTEM_DESCRIPTION = 'system-description'
LLDP_ATTR_SYSTEM_NAME = 'system-name'
LLDP_DEST_NEAREST_BRIDGE = 'nearest-bridge'
LLDP_DEST_NEAREST_CUSTOMER_BRIDGE = 'nearest-customer-bridge'
LLDP_DEST_NEAREST_NON_TPMR_BRIDGE = 'nearest-non-tpmr-bridge'
MAJOR_VERSION = '1'
MICRO_VERSION = '0'
MINOR_VERSION = '56'


class ManagerError(enum.Enum):
    """Errors related to the main "network management" interface of NetworkManager.
These may be returned from #NMClient methods that invoke D-Bus operations on
the "org.freedesktop.NetworkManager" interface, and correspond to D-Bus
errors in that namespace."""
    FAILED = 0
    PERMISSIONDENIED = 1
    UNKNOWNCONNECTION = 2
    UNKNOWNDEVICE = 3
    CONNECTIONNOTAVAILABLE = 4
    CONNECTIONNOTACTIVE = 5
    CONNECTIONALREADYACTIVE = 6
    DEPENDENCYFAILED = 7
    ALREADYASLEEPORAWAKE = 8
    ALREADYENABLEDORDISABLED = 9
    UNKNOWNLOGLEVEL = 10
    UNKNOWNLOGDOMAIN = 11
    INVALIDARGUMENTS = 12
    MISSINGPLUGIN = 13


class ManagerReloadFlags(enum.Enum):
    """Flags for the manager Reload() call."""
    CONF = 1
    DNS_RC = 2
    DNS_FULL = 4


class Metered(enum.Enum):
    """The NMMetered enum has two different purposes: one is to configure
"connection.metered" setting of a connection profile in #NMSettingConnection, and
the other is to express the actual metered state of the #NMDevice at a given moment.

For the connection profile only #NM_METERED_UNKNOWN, #NM_METERED_NO
and #NM_METERED_YES are allowed.

The device's metered state at runtime is determined by the profile
which is currently active. If the profile explicitly specifies #NM_METERED_NO
or #NM_METERED_YES, then the device's metered state is as such.
If the connection profile leaves it undecided at #NM_METERED_UNKNOWN (the default),
then NetworkManager tries to guess the metered state, for example based on the
device type or on DHCP options (like Android devices exposing a "ANDROID_METERED"
DHCP vendor option). This then leads to either #NM_METERED_GUESS_NO or #NM_METERED_GUESS_YES.

Most applications probably should treat the runtime state #NM_METERED_GUESS_YES
like #NM_METERED_YES, and all other states as not metered.

Note that the per-device metered states are then combined to a global metered
state. This is basically the metered state of the device with the best default
route. However, that generalization of a global metered state may not be correct
if the default routes for IPv4 and IPv6 are on different devices, or if policy
routing is configured. In general, the global metered state tries to express whether
the traffic is likely metered, but since that depends on the traffic itself,
there is not one answer in all cases. Hence, an application may want to consider
the per-device's metered states."""
    UNKNOWN = 0
    YES = 1
    NO = 2
    GUESS_YES = 3
    GUESS_NO = 4


class MptcpFlags(enum.Enum):
    """"""
    NONE = 0
    DISABLED = 1
    ENABLED = 2
    ALSO_WITHOUT_SYSCTL = 4
    ALSO_WITHOUT_DEFAULT_ROUTE = 8
    SIGNAL = 16
    SUBFLOW = 32
    BACKUP = 64
    FULLMESH = 128
    LAMINAR = 256


OBJECT_CLIENT = 'client'
OBJECT_PATH = 'path'
REMOTE_CONNECTION_DBUS_CONNECTION = 'dbus-connection'
REMOTE_CONNECTION_FILENAME = 'filename'
REMOTE_CONNECTION_FLAGS = 'flags'
REMOTE_CONNECTION_PATH = 'path'
REMOTE_CONNECTION_UNSAVED = 'unsaved'
REMOTE_CONNECTION_VERSION_ID = 'version-id'
REMOTE_CONNECTION_VISIBLE = 'visible'


class RadioFlags(enum.Enum):
    """Flags related to radio interfaces."""
    NONE = 0
    WLAN_AVAILABLE = 1
    WWAN_AVAILABLE = 2


class RollbackResult(enum.Enum):
    """The result of a checkpoint Rollback() operation for a specific device."""
    OK = 0
    ERR_NO_DEVICE = 1
    ERR_DEVICE_UNMANAGED = 2
    ERR_FAILED = 3


SECRET_AGENT_OLD_AUTO_REGISTER = 'auto-register'
SECRET_AGENT_OLD_CAPABILITIES = 'capabilities'
SECRET_AGENT_OLD_DBUS_CONNECTION = 'dbus-connection'
SECRET_AGENT_OLD_IDENTIFIER = 'identifier'
SECRET_AGENT_OLD_REGISTERED = 'registered'
SECRET_TAG_DYNAMIC_CHALLENGE = 'x-dynamic-challenge:'
SECRET_TAG_DYNAMIC_CHALLENGE_ECHO = 'x-dynamic-challenge-echo:'
SECRET_TAG_VPN_MSG = 'x-vpn-message:'
SETTING_6LOWPAN_PARENT = 'parent'
SETTING_6LOWPAN_SETTING_NAME = '6lowpan'
SETTING_802_1X_ALTSUBJECT_MATCHES = 'altsubject-matches'
SETTING_802_1X_ANONYMOUS_IDENTITY = 'anonymous-identity'
SETTING_802_1X_AUTH_TIMEOUT = 'auth-timeout'
SETTING_802_1X_CA_CERT = 'ca-cert'
SETTING_802_1X_CA_CERT_PASSWORD = 'ca-cert-password'
SETTING_802_1X_CA_CERT_PASSWORD_FLAGS = 'ca-cert-password-flags'
SETTING_802_1X_CA_PATH = 'ca-path'
SETTING_802_1X_CERT_SCHEME_PREFIX_PATH = 'file://'
SETTING_802_1X_CERT_SCHEME_PREFIX_PKCS11 = 'pkcs11:'
SETTING_802_1X_CLIENT_CERT = 'client-cert'
SETTING_802_1X_CLIENT_CERT_PASSWORD = 'client-cert-password'
SETTING_802_1X_CLIENT_CERT_PASSWORD_FLAGS = 'client-cert-password-flags'
SETTING_802_1X_DOMAIN_MATCH = 'domain-match'
SETTING_802_1X_DOMAIN_SUFFIX_MATCH = 'domain-suffix-match'
SETTING_802_1X_EAP = 'eap'
SETTING_802_1X_IDENTITY = 'identity'
SETTING_802_1X_OPENSSL_CIPHERS = 'openssl-ciphers'
SETTING_802_1X_OPTIONAL = 'optional'
SETTING_802_1X_PAC_FILE = 'pac-file'
SETTING_802_1X_PASSWORD = 'password'
SETTING_802_1X_PASSWORD_FLAGS = 'password-flags'
SETTING_802_1X_PASSWORD_RAW = 'password-raw'
SETTING_802_1X_PASSWORD_RAW_FLAGS = 'password-raw-flags'
SETTING_802_1X_PHASE1_AUTH_FLAGS = 'phase1-auth-flags'
SETTING_802_1X_PHASE1_FAST_PROVISIONING = 'phase1-fast-provisioning'
SETTING_802_1X_PHASE1_PEAPLABEL = 'phase1-peaplabel'
SETTING_802_1X_PHASE1_PEAPVER = 'phase1-peapver'
SETTING_802_1X_PHASE2_ALTSUBJECT_MATCHES = 'phase2-altsubject-matches'
SETTING_802_1X_PHASE2_AUTH = 'phase2-auth'
SETTING_802_1X_PHASE2_AUTHEAP = 'phase2-autheap'
SETTING_802_1X_PHASE2_CA_CERT = 'phase2-ca-cert'
SETTING_802_1X_PHASE2_CA_CERT_PASSWORD = 'phase2-ca-cert-password'
SETTING_802_1X_PHASE2_CA_CERT_PASSWORD_FLAGS = 'phase2-ca-cert-password-flags'
SETTING_802_1X_PHASE2_CA_PATH = 'phase2-ca-path'
SETTING_802_1X_PHASE2_CLIENT_CERT = 'phase2-client-cert'
SETTING_802_1X_PHASE2_CLIENT_CERT_PASSWORD = 'phase2-client-cert-password'
SETTING_802_1X_PHASE2_CLIENT_CERT_PASSWORD_FLAGS = (
    'phase2-client-cert-password-flags')
SETTING_802_1X_PHASE2_DOMAIN_MATCH = 'phase2-domain-match'
SETTING_802_1X_PHASE2_DOMAIN_SUFFIX_MATCH = 'phase2-domain-suffix-match'
SETTING_802_1X_PHASE2_PRIVATE_KEY = 'phase2-private-key'
SETTING_802_1X_PHASE2_PRIVATE_KEY_PASSWORD = 'phase2-private-key-password'
SETTING_802_1X_PHASE2_PRIVATE_KEY_PASSWORD_FLAGS = (
    'phase2-private-key-password-flags')
SETTING_802_1X_PHASE2_SUBJECT_MATCH = 'phase2-subject-match'
SETTING_802_1X_PIN = 'pin'
SETTING_802_1X_PIN_FLAGS = 'pin-flags'
SETTING_802_1X_PRIVATE_KEY = 'private-key'
SETTING_802_1X_PRIVATE_KEY_PASSWORD = 'private-key-password'
SETTING_802_1X_PRIVATE_KEY_PASSWORD_FLAGS = 'private-key-password-flags'
SETTING_802_1X_SETTING_NAME = '802-1x'
SETTING_802_1X_SUBJECT_MATCH = 'subject-match'
SETTING_802_1X_SYSTEM_CA_CERTS = 'system-ca-certs'
SETTING_ADSL_ENCAPSULATION = 'encapsulation'
SETTING_ADSL_ENCAPSULATION_LLC = 'llc'
SETTING_ADSL_ENCAPSULATION_VCMUX = 'vcmux'
SETTING_ADSL_PASSWORD = 'password'
SETTING_ADSL_PASSWORD_FLAGS = 'password-flags'
SETTING_ADSL_PROTOCOL = 'protocol'
SETTING_ADSL_PROTOCOL_IPOATM = 'ipoatm'
SETTING_ADSL_PROTOCOL_PPPOA = 'pppoa'
SETTING_ADSL_PROTOCOL_PPPOE = 'pppoe'
SETTING_ADSL_SETTING_NAME = 'adsl'
SETTING_ADSL_USERNAME = 'username'
SETTING_ADSL_VCI = 'vci'
SETTING_ADSL_VPI = 'vpi'
SETTING_BLUETOOTH_BDADDR = 'bdaddr'
SETTING_BLUETOOTH_SETTING_NAME = 'bluetooth'
SETTING_BLUETOOTH_TYPE = 'type'
SETTING_BLUETOOTH_TYPE_DUN = 'dun'
SETTING_BLUETOOTH_TYPE_NAP = 'nap'
SETTING_BLUETOOTH_TYPE_PANU = 'panu'
SETTING_BOND_OPTIONS = 'options'
SETTING_BOND_OPTION_ACTIVE_SLAVE = 'active_slave'
SETTING_BOND_OPTION_AD_ACTOR_SYSTEM = 'ad_actor_system'
SETTING_BOND_OPTION_AD_ACTOR_SYS_PRIO = 'ad_actor_sys_prio'
SETTING_BOND_OPTION_AD_SELECT = 'ad_select'
SETTING_BOND_OPTION_AD_USER_PORT_KEY = 'ad_user_port_key'
SETTING_BOND_OPTION_ALL_SLAVES_ACTIVE = 'all_slaves_active'
SETTING_BOND_OPTION_ARP_ALL_TARGETS = 'arp_all_targets'
SETTING_BOND_OPTION_ARP_INTERVAL = 'arp_interval'
SETTING_BOND_OPTION_ARP_IP_TARGET = 'arp_ip_target'
SETTING_BOND_OPTION_ARP_MISSED_MAX = 'arp_missed_max'
SETTING_BOND_OPTION_ARP_VALIDATE = 'arp_validate'
SETTING_BOND_OPTION_BALANCE_SLB = 'balance-slb'
SETTING_BOND_OPTION_DOWNDELAY = 'downdelay'
SETTING_BOND_OPTION_FAIL_OVER_MAC = 'fail_over_mac'
SETTING_BOND_OPTION_LACP_ACTIVE = 'lacp_active'
SETTING_BOND_OPTION_LACP_RATE = 'lacp_rate'
SETTING_BOND_OPTION_LP_INTERVAL = 'lp_interval'
SETTING_BOND_OPTION_MIIMON = 'miimon'
SETTING_BOND_OPTION_MIN_LINKS = 'min_links'
SETTING_BOND_OPTION_MODE = 'mode'
SETTING_BOND_OPTION_NS_IP6_TARGET = 'ns_ip6_target'
SETTING_BOND_OPTION_NUM_GRAT_ARP = 'num_grat_arp'
SETTING_BOND_OPTION_NUM_UNSOL_NA = 'num_unsol_na'
SETTING_BOND_OPTION_PACKETS_PER_SLAVE = 'packets_per_slave'
SETTING_BOND_OPTION_PEER_NOTIF_DELAY = 'peer_notif_delay'
SETTING_BOND_OPTION_PRIMARY = 'primary'
SETTING_BOND_OPTION_PRIMARY_RESELECT = 'primary_reselect'
SETTING_BOND_OPTION_RESEND_IGMP = 'resend_igmp'
SETTING_BOND_OPTION_TLB_DYNAMIC_LB = 'tlb_dynamic_lb'
SETTING_BOND_OPTION_UPDELAY = 'updelay'
SETTING_BOND_OPTION_USE_CARRIER = 'use_carrier'
SETTING_BOND_OPTION_XMIT_HASH_POLICY = 'xmit_hash_policy'
SETTING_BOND_PORT_PRIO = 'prio'
SETTING_BOND_PORT_QUEUE_ID = 'queue-id'
SETTING_BOND_PORT_SETTING_NAME = 'bond-port'
SETTING_BOND_SETTING_NAME = 'bond'
SETTING_BRIDGE_AGEING_TIME = 'ageing-time'
SETTING_BRIDGE_FORWARD_DELAY = 'forward-delay'
SETTING_BRIDGE_GROUP_ADDRESS = 'group-address'
SETTING_BRIDGE_GROUP_FORWARD_MASK = 'group-forward-mask'
SETTING_BRIDGE_HELLO_TIME = 'hello-time'
SETTING_BRIDGE_MAC_ADDRESS = 'mac-address'
SETTING_BRIDGE_MAX_AGE = 'max-age'
SETTING_BRIDGE_MULTICAST_HASH_MAX = 'multicast-hash-max'
SETTING_BRIDGE_MULTICAST_LAST_MEMBER_COUNT = 'multicast-last-member-count'
SETTING_BRIDGE_MULTICAST_LAST_MEMBER_INTERVAL = (
    'multicast-last-member-interval')
SETTING_BRIDGE_MULTICAST_MEMBERSHIP_INTERVAL = 'multicast-membership-interval'
SETTING_BRIDGE_MULTICAST_QUERIER = 'multicast-querier'
SETTING_BRIDGE_MULTICAST_QUERIER_INTERVAL = 'multicast-querier-interval'
SETTING_BRIDGE_MULTICAST_QUERY_INTERVAL = 'multicast-query-interval'
SETTING_BRIDGE_MULTICAST_QUERY_RESPONSE_INTERVAL = (
    'multicast-query-response-interval')
SETTING_BRIDGE_MULTICAST_QUERY_USE_IFADDR = 'multicast-query-use-ifaddr'
SETTING_BRIDGE_MULTICAST_ROUTER = 'multicast-router'
SETTING_BRIDGE_MULTICAST_SNOOPING = 'multicast-snooping'
SETTING_BRIDGE_MULTICAST_STARTUP_QUERY_COUNT = 'multicast-startup-query-count'
SETTING_BRIDGE_MULTICAST_STARTUP_QUERY_INTERVAL = (
    'multicast-startup-query-interval')
SETTING_BRIDGE_PORT_HAIRPIN_MODE = 'hairpin-mode'
SETTING_BRIDGE_PORT_PATH_COST = 'path-cost'
SETTING_BRIDGE_PORT_PRIORITY = 'priority'
SETTING_BRIDGE_PORT_SETTING_NAME = 'bridge-port'
SETTING_BRIDGE_PORT_VLANS = 'vlans'
SETTING_BRIDGE_PRIORITY = 'priority'
SETTING_BRIDGE_SETTING_NAME = 'bridge'
SETTING_BRIDGE_STP = 'stp'
SETTING_BRIDGE_VLANS = 'vlans'
SETTING_BRIDGE_VLAN_DEFAULT_PVID = 'vlan-default-pvid'
SETTING_BRIDGE_VLAN_FILTERING = 'vlan-filtering'
SETTING_BRIDGE_VLAN_PROTOCOL = 'vlan-protocol'
SETTING_BRIDGE_VLAN_STATS_ENABLED = 'vlan-stats-enabled'
SETTING_CDMA_MTU = 'mtu'
SETTING_CDMA_NUMBER = 'number'
SETTING_CDMA_PASSWORD = 'password'
SETTING_CDMA_PASSWORD_FLAGS = 'password-flags'
SETTING_CDMA_SETTING_NAME = 'cdma'
SETTING_CDMA_USERNAME = 'username'
SETTING_CONNECTION_AUTH_RETRIES = 'auth-retries'
SETTING_CONNECTION_AUTOCONNECT = 'autoconnect'
SETTING_CONNECTION_AUTOCONNECT_PORTS = 'autoconnect-ports'
SETTING_CONNECTION_AUTOCONNECT_PRIORITY = 'autoconnect-priority'
SETTING_CONNECTION_AUTOCONNECT_PRIORITY_DEFAULT = '0'
SETTING_CONNECTION_AUTOCONNECT_PRIORITY_MAX = '999'
SETTING_CONNECTION_AUTOCONNECT_PRIORITY_MIN = '-999'
SETTING_CONNECTION_AUTOCONNECT_RETRIES = 'autoconnect-retries'
SETTING_CONNECTION_AUTOCONNECT_SLAVES = 'autoconnect-slaves'
SETTING_CONNECTION_CONTROLLER = 'controller'
SETTING_CONNECTION_DNSSEC = 'dnssec'
SETTING_CONNECTION_DNS_OVER_TLS = 'dns-over-tls'
SETTING_CONNECTION_DOWN_ON_POWEROFF = 'down-on-poweroff'
SETTING_CONNECTION_GATEWAY_PING_TIMEOUT = 'gateway-ping-timeout'
SETTING_CONNECTION_ID = 'id'
SETTING_CONNECTION_INTERFACE_NAME = 'interface-name'
SETTING_CONNECTION_IP_PING_ADDRESSES = 'ip-ping-addresses'
SETTING_CONNECTION_IP_PING_ADDRESSES_REQUIRE_ALL = (
    'ip-ping-addresses-require-all')
SETTING_CONNECTION_IP_PING_TIMEOUT = 'ip-ping-timeout'
SETTING_CONNECTION_LLDP = 'lldp'
SETTING_CONNECTION_LLMNR = 'llmnr'
SETTING_CONNECTION_MASTER = 'master'
SETTING_CONNECTION_MDNS = 'mdns'
SETTING_CONNECTION_METERED = 'metered'
SETTING_CONNECTION_MPTCP_FLAGS = 'mptcp-flags'
SETTING_CONNECTION_MUD_URL = 'mud-url'
SETTING_CONNECTION_MULTI_CONNECT = 'multi-connect'
SETTING_CONNECTION_PERMISSIONS = 'permissions'
SETTING_CONNECTION_PORT_TYPE = 'port-type'
SETTING_CONNECTION_READ_ONLY = 'read-only'
SETTING_CONNECTION_SECONDARIES = 'secondaries'
SETTING_CONNECTION_SETTING_NAME = 'connection'
SETTING_CONNECTION_SLAVE_TYPE = 'slave-type'
SETTING_CONNECTION_STABLE_ID = 'stable-id'
SETTING_CONNECTION_TIMESTAMP = 'timestamp'
SETTING_CONNECTION_TYPE = 'type'
SETTING_CONNECTION_UUID = 'uuid'
SETTING_CONNECTION_WAIT_ACTIVATION_DELAY = 'wait-activation-delay'
SETTING_CONNECTION_WAIT_DEVICE_TIMEOUT = 'wait-device-timeout'
SETTING_CONNECTION_ZONE = 'zone'
SETTING_DCB_APP_FCOE_FLAGS = 'app-fcoe-flags'
SETTING_DCB_APP_FCOE_MODE = 'app-fcoe-mode'
SETTING_DCB_APP_FCOE_PRIORITY = 'app-fcoe-priority'
SETTING_DCB_APP_FIP_FLAGS = 'app-fip-flags'
SETTING_DCB_APP_FIP_PRIORITY = 'app-fip-priority'
SETTING_DCB_APP_ISCSI_FLAGS = 'app-iscsi-flags'
SETTING_DCB_APP_ISCSI_PRIORITY = 'app-iscsi-priority'
SETTING_DCB_FCOE_MODE_FABRIC = 'fabric'
SETTING_DCB_FCOE_MODE_VN2VN = 'vn2vn'
SETTING_DCB_PRIORITY_BANDWIDTH = 'priority-bandwidth'
SETTING_DCB_PRIORITY_FLOW_CONTROL = 'priority-flow-control'
SETTING_DCB_PRIORITY_FLOW_CONTROL_FLAGS = 'priority-flow-control-flags'
SETTING_DCB_PRIORITY_GROUP_BANDWIDTH = 'priority-group-bandwidth'
SETTING_DCB_PRIORITY_GROUP_FLAGS = 'priority-group-flags'
SETTING_DCB_PRIORITY_GROUP_ID = 'priority-group-id'
SETTING_DCB_PRIORITY_STRICT_BANDWIDTH = 'priority-strict-bandwidth'
SETTING_DCB_PRIORITY_TRAFFIC_CLASS = 'priority-traffic-class'
SETTING_DCB_SETTING_NAME = 'dcb'
SETTING_DNS_OPTION_ATTEMPTS = 'attempts'
SETTING_DNS_OPTION_DEBUG = 'debug'
SETTING_DNS_OPTION_EDNS0 = 'edns0'
SETTING_DNS_OPTION_INET6 = 'inet6'
SETTING_DNS_OPTION_INTERNAL_NO_ADD_EDNS0 = '_no-add-edns0'
SETTING_DNS_OPTION_INTERNAL_NO_ADD_TRUST_AD = '_no-add-trust-ad'
SETTING_DNS_OPTION_IP6_BYTESTRING = 'ip6-bytestring'
SETTING_DNS_OPTION_IP6_DOTINT = 'ip6-dotint'
SETTING_DNS_OPTION_NDOTS = 'ndots'
SETTING_DNS_OPTION_NO_AAAA = 'no-aaaa'
SETTING_DNS_OPTION_NO_CHECK_NAMES = 'no-check-names'
SETTING_DNS_OPTION_NO_IP6_DOTINT = 'no-ip6-dotint'
SETTING_DNS_OPTION_NO_RELOAD = 'no-reload'
SETTING_DNS_OPTION_NO_TLD_QUERY = 'no-tld-query'
SETTING_DNS_OPTION_ROTATE = 'rotate'
SETTING_DNS_OPTION_SINGLE_REQUEST = 'single-request'
SETTING_DNS_OPTION_SINGLE_REQUEST_REOPEN = 'single-request-reopen'
SETTING_DNS_OPTION_TIMEOUT = 'timeout'
SETTING_DNS_OPTION_TRUST_AD = 'trust-ad'
SETTING_DNS_OPTION_USE_VC = 'use-vc'
SETTING_DUMMY_SETTING_NAME = 'dummy'
SETTING_ETHTOOL_SETTING_NAME = 'ethtool'
SETTING_GENERIC_DEVICE_HANDLER = 'device-handler'
SETTING_GENERIC_SETTING_NAME = 'generic'
SETTING_GSM_APN = 'apn'
SETTING_GSM_AUTO_CONFIG = 'auto-config'
SETTING_GSM_DEVICE_ID = 'device-id'
SETTING_GSM_DEVICE_UID = 'device-uid'
SETTING_GSM_HOME_ONLY = 'home-only'
SETTING_GSM_INITIAL_EPS_BEARER_APN = 'initial-eps-bearer-apn'
SETTING_GSM_INITIAL_EPS_BEARER_CONFIGURE = 'initial-eps-bearer-configure'
SETTING_GSM_INITIAL_EPS_BEARER_NOAUTH = 'initial-eps-bearer-noauth'
SETTING_GSM_INITIAL_EPS_BEARER_PASSWORD = 'initial-eps-bearer-password'
SETTING_GSM_INITIAL_EPS_BEARER_PASSWORD_FLAGS = (
    'initial-eps-bearer-password-flags')
SETTING_GSM_INITIAL_EPS_BEARER_REFUSE_CHAP = 'initial-eps-bearer-refuse-chap'
SETTING_GSM_INITIAL_EPS_BEARER_REFUSE_EAP = 'initial-eps-bearer-refuse-eap'
SETTING_GSM_INITIAL_EPS_BEARER_REFUSE_MSCHAP = (
    'initial-eps-bearer-refuse-mschap')
SETTING_GSM_INITIAL_EPS_BEARER_REFUSE_MSCHAPV2 = (
    'initial-eps-bearer-refuse-mschapv2')
SETTING_GSM_INITIAL_EPS_BEARER_REFUSE_PAP = 'initial-eps-bearer-refuse-pap'
SETTING_GSM_INITIAL_EPS_BEARER_USERNAME = 'initial-eps-bearer-username'
SETTING_GSM_MTU = 'mtu'
SETTING_GSM_NETWORK_ID = 'network-id'
SETTING_GSM_NUMBER = 'number'
SETTING_GSM_PASSWORD = 'password'
SETTING_GSM_PASSWORD_FLAGS = 'password-flags'
SETTING_GSM_PIN = 'pin'
SETTING_GSM_PIN_FLAGS = 'pin-flags'
SETTING_GSM_SETTING_NAME = 'gsm'
SETTING_GSM_SIM_ID = 'sim-id'
SETTING_GSM_SIM_OPERATOR_ID = 'sim-operator-id'
SETTING_GSM_USERNAME = 'username'
SETTING_HOSTNAME_FROM_DHCP = 'from-dhcp'
SETTING_HOSTNAME_FROM_DNS_LOOKUP = 'from-dns-lookup'
SETTING_HOSTNAME_ONLY_FROM_DEFAULT = 'only-from-default'
SETTING_HOSTNAME_PRIORITY = 'priority'
SETTING_HOSTNAME_SETTING_NAME = 'hostname'
SETTING_HSR_INTERLINK = 'interlink'
SETTING_HSR_MULTICAST_SPEC = 'multicast-spec'
SETTING_HSR_PORT1 = 'port1'
SETTING_HSR_PORT2 = 'port2'
SETTING_HSR_PROTOCOL_VERSION = 'protocol-version'
SETTING_HSR_PRP = 'prp'
SETTING_HSR_SETTING_NAME = 'hsr'
SETTING_INFINIBAND_MAC_ADDRESS = 'mac-address'
SETTING_INFINIBAND_MTU = 'mtu'
SETTING_INFINIBAND_PARENT = 'parent'
SETTING_INFINIBAND_P_KEY = 'p-key'
SETTING_INFINIBAND_SETTING_NAME = 'infiniband'
SETTING_INFINIBAND_TRANSPORT_MODE = 'transport-mode'
SETTING_IP4_CONFIG_DHCP_CLIENT_ID = 'dhcp-client-id'
SETTING_IP4_CONFIG_DHCP_FQDN = 'dhcp-fqdn'
SETTING_IP4_CONFIG_DHCP_IPV6_ONLY_PREFERRED = 'dhcp-ipv6-only-preferred'
SETTING_IP4_CONFIG_DHCP_VENDOR_CLASS_IDENTIFIER = (
    'dhcp-vendor-class-identifier')
SETTING_IP4_CONFIG_LINK_LOCAL = 'link-local'
SETTING_IP4_CONFIG_METHOD_AUTO = 'auto'
SETTING_IP4_CONFIG_METHOD_DISABLED = 'disabled'
SETTING_IP4_CONFIG_METHOD_LINK_LOCAL = 'link-local'
SETTING_IP4_CONFIG_METHOD_MANUAL = 'manual'
SETTING_IP4_CONFIG_METHOD_SHARED = 'shared'
SETTING_IP4_CONFIG_SETTING_NAME = 'ipv4'
SETTING_IP6_CONFIG_ADDR_GEN_MODE = 'addr-gen-mode'
SETTING_IP6_CONFIG_DHCP_DUID = 'dhcp-duid'
SETTING_IP6_CONFIG_DHCP_PD_HINT = 'dhcp-pd-hint'
SETTING_IP6_CONFIG_IP6_PRIVACY = 'ip6-privacy'
SETTING_IP6_CONFIG_METHOD_AUTO = 'auto'
SETTING_IP6_CONFIG_METHOD_DHCP = 'dhcp'
SETTING_IP6_CONFIG_METHOD_DISABLED = 'disabled'
SETTING_IP6_CONFIG_METHOD_IGNORE = 'ignore'
SETTING_IP6_CONFIG_METHOD_LINK_LOCAL = 'link-local'
SETTING_IP6_CONFIG_METHOD_MANUAL = 'manual'
SETTING_IP6_CONFIG_METHOD_SHARED = 'shared'
SETTING_IP6_CONFIG_MTU = 'mtu'
SETTING_IP6_CONFIG_RA_TIMEOUT = 'ra-timeout'
SETTING_IP6_CONFIG_SETTING_NAME = 'ipv6'
SETTING_IP6_CONFIG_TEMP_PREFERRED_LIFETIME = 'temp-preferred-lifetime'
SETTING_IP6_CONFIG_TEMP_VALID_LIFETIME = 'temp-valid-lifetime'
SETTING_IP6_CONFIG_TOKEN = 'token'
SETTING_IPVLAN_MODE = 'mode'
SETTING_IPVLAN_PARENT = 'parent'
SETTING_IPVLAN_PRIVATE = 'private'
SETTING_IPVLAN_SETTING_NAME = 'ipvlan'
SETTING_IPVLAN_VEPA = 'vepa'
SETTING_IP_CONFIG_ADDRESSES = 'addresses'
SETTING_IP_CONFIG_AUTO_ROUTE_EXT_GW = 'auto-route-ext-gw'
SETTING_IP_CONFIG_DAD_TIMEOUT = 'dad-timeout'
SETTING_IP_CONFIG_DAD_TIMEOUT_MAX = '30000'
SETTING_IP_CONFIG_DHCP_DSCP = 'dhcp-dscp'
SETTING_IP_CONFIG_DHCP_HOSTNAME = 'dhcp-hostname'
SETTING_IP_CONFIG_DHCP_HOSTNAME_FLAGS = 'dhcp-hostname-flags'
SETTING_IP_CONFIG_DHCP_IAID = 'dhcp-iaid'
SETTING_IP_CONFIG_DHCP_REJECT_SERVERS = 'dhcp-reject-servers'
SETTING_IP_CONFIG_DHCP_SEND_HOSTNAME = 'dhcp-send-hostname'
SETTING_IP_CONFIG_DHCP_SEND_HOSTNAME_V2 = 'dhcp-send-hostname-v2'
SETTING_IP_CONFIG_DHCP_SEND_RELEASE = 'dhcp-send-release'
SETTING_IP_CONFIG_DHCP_TIMEOUT = 'dhcp-timeout'
SETTING_IP_CONFIG_DNS = 'dns'
SETTING_IP_CONFIG_DNS_OPTIONS = 'dns-options'
SETTING_IP_CONFIG_DNS_PRIORITY = 'dns-priority'
SETTING_IP_CONFIG_DNS_SEARCH = 'dns-search'
SETTING_IP_CONFIG_FORWARDING = 'forwarding'
SETTING_IP_CONFIG_GATEWAY = 'gateway'
SETTING_IP_CONFIG_IGNORE_AUTO_DNS = 'ignore-auto-dns'
SETTING_IP_CONFIG_IGNORE_AUTO_ROUTES = 'ignore-auto-routes'
SETTING_IP_CONFIG_MAY_FAIL = 'may-fail'
SETTING_IP_CONFIG_METHOD = 'method'
SETTING_IP_CONFIG_NEVER_DEFAULT = 'never-default'
SETTING_IP_CONFIG_REPLACE_LOCAL_RULE = 'replace-local-rule'
SETTING_IP_CONFIG_REQUIRED_TIMEOUT = 'required-timeout'
SETTING_IP_CONFIG_ROUTED_DNS = 'routed-dns'
SETTING_IP_CONFIG_ROUTES = 'routes'
SETTING_IP_CONFIG_ROUTE_METRIC = 'route-metric'
SETTING_IP_CONFIG_ROUTE_TABLE = 'route-table'
SETTING_IP_CONFIG_ROUTING_RULES = 'routing-rules'
SETTING_IP_CONFIG_SHARED_DHCP_LEASE_TIME = 'shared-dhcp-lease-time'
SETTING_IP_CONFIG_SHARED_DHCP_RANGE = 'shared-dhcp-range'
SETTING_IP_TUNNEL_ENCAPSULATION_LIMIT = 'encapsulation-limit'
SETTING_IP_TUNNEL_FLAGS = 'flags'
SETTING_IP_TUNNEL_FLOW_LABEL = 'flow-label'
SETTING_IP_TUNNEL_FWMARK = 'fwmark'
SETTING_IP_TUNNEL_INPUT_KEY = 'input-key'
SETTING_IP_TUNNEL_LOCAL = 'local'
SETTING_IP_TUNNEL_MODE = 'mode'
SETTING_IP_TUNNEL_MTU = 'mtu'
SETTING_IP_TUNNEL_OUTPUT_KEY = 'output-key'
SETTING_IP_TUNNEL_PARENT = 'parent'
SETTING_IP_TUNNEL_PATH_MTU_DISCOVERY = 'path-mtu-discovery'
SETTING_IP_TUNNEL_REMOTE = 'remote'
SETTING_IP_TUNNEL_SETTING_NAME = 'ip-tunnel'
SETTING_IP_TUNNEL_TOS = 'tos'
SETTING_IP_TUNNEL_TTL = 'ttl'
SETTING_LINK_GRO_MAX_SIZE = 'gro-max-size'
SETTING_LINK_GSO_MAX_SEGMENTS = 'gso-max-segments'
SETTING_LINK_GSO_MAX_SIZE = 'gso-max-size'
SETTING_LINK_SETTING_NAME = 'link'
SETTING_LINK_TX_QUEUE_LENGTH = 'tx-queue-length'
SETTING_LOOPBACK_MTU = 'mtu'
SETTING_LOOPBACK_SETTING_NAME = 'loopback'
SETTING_MACSEC_ENCRYPT = 'encrypt'
SETTING_MACSEC_MKA_CAK = 'mka-cak'
SETTING_MACSEC_MKA_CAK_FLAGS = 'mka-cak-flags'
SETTING_MACSEC_MKA_CAK_LENGTH = '32'
SETTING_MACSEC_MKA_CKN = 'mka-ckn'
SETTING_MACSEC_MKA_CKN_LENGTH = '64'
SETTING_MACSEC_MODE = 'mode'
SETTING_MACSEC_OFFLOAD = 'offload'
SETTING_MACSEC_PARENT = 'parent'
SETTING_MACSEC_PORT = 'port'
SETTING_MACSEC_SEND_SCI = 'send-sci'
SETTING_MACSEC_SETTING_NAME = 'macsec'
SETTING_MACSEC_VALIDATION = 'validation'
SETTING_MACVLAN_MODE = 'mode'
SETTING_MACVLAN_PARENT = 'parent'
SETTING_MACVLAN_PROMISCUOUS = 'promiscuous'
SETTING_MACVLAN_SETTING_NAME = 'macvlan'
SETTING_MACVLAN_TAP = 'tap'
SETTING_MATCH_DRIVER = 'driver'
SETTING_MATCH_INTERFACE_NAME = 'interface-name'
SETTING_MATCH_KERNEL_COMMAND_LINE = 'kernel-command-line'
SETTING_MATCH_PATH = 'path'
SETTING_MATCH_SETTING_NAME = 'match'
SETTING_NAME = 'name'
SETTING_OLPC_MESH_CHANNEL = 'channel'
SETTING_OLPC_MESH_DHCP_ANYCAST_ADDRESS = 'dhcp-anycast-address'
SETTING_OLPC_MESH_SETTING_NAME = '802-11-olpc-mesh'
SETTING_OLPC_MESH_SSID = 'ssid'
SETTING_OVS_BRIDGE_DATAPATH_TYPE = 'datapath-type'
SETTING_OVS_BRIDGE_FAIL_MODE = 'fail-mode'
SETTING_OVS_BRIDGE_MCAST_SNOOPING_ENABLE = 'mcast-snooping-enable'
SETTING_OVS_BRIDGE_RSTP_ENABLE = 'rstp-enable'
SETTING_OVS_BRIDGE_SETTING_NAME = 'ovs-bridge'
SETTING_OVS_BRIDGE_STP_ENABLE = 'stp-enable'
SETTING_OVS_DPDK_DEVARGS = 'devargs'
SETTING_OVS_DPDK_LSC_INTERRUPT = 'lsc-interrupt'
SETTING_OVS_DPDK_N_RXQ = 'n-rxq'
SETTING_OVS_DPDK_N_RXQ_DESC = 'n-rxq-desc'
SETTING_OVS_DPDK_N_TXQ_DESC = 'n-txq-desc'
SETTING_OVS_DPDK_SETTING_NAME = 'ovs-dpdk'
SETTING_OVS_EXTERNAL_IDS_DATA = 'data'
SETTING_OVS_EXTERNAL_IDS_SETTING_NAME = 'ovs-external-ids'
SETTING_OVS_INTERFACE_OFPORT_REQUEST = 'ofport-request'
SETTING_OVS_INTERFACE_SETTING_NAME = 'ovs-interface'
SETTING_OVS_INTERFACE_TYPE = 'type'
SETTING_OVS_OTHER_CONFIG_DATA = 'data'
SETTING_OVS_OTHER_CONFIG_SETTING_NAME = 'ovs-other-config'
SETTING_OVS_PATCH_PEER = 'peer'
SETTING_OVS_PATCH_SETTING_NAME = 'ovs-patch'
SETTING_OVS_PORT_BOND_DOWNDELAY = 'bond-downdelay'
SETTING_OVS_PORT_BOND_MODE = 'bond-mode'
SETTING_OVS_PORT_BOND_UPDELAY = 'bond-updelay'
SETTING_OVS_PORT_LACP = 'lacp'
SETTING_OVS_PORT_SETTING_NAME = 'ovs-port'
SETTING_OVS_PORT_TAG = 'tag'
SETTING_OVS_PORT_TRUNKS = 'trunks'
SETTING_OVS_PORT_VLAN_MODE = 'vlan-mode'
SETTING_PARAM_FUZZY_IGNORE = '2048'
SETTING_PARAM_REQUIRED = '512'
SETTING_PARAM_SECRET = '1024'
SETTING_PPPOE_PARENT = 'parent'
SETTING_PPPOE_PASSWORD = 'password'
SETTING_PPPOE_PASSWORD_FLAGS = 'password-flags'
SETTING_PPPOE_SERVICE = 'service'
SETTING_PPPOE_SETTING_NAME = 'pppoe'
SETTING_PPPOE_USERNAME = 'username'
SETTING_PPP_BAUD = 'baud'
SETTING_PPP_CRTSCTS = 'crtscts'
SETTING_PPP_LCP_ECHO_FAILURE = 'lcp-echo-failure'
SETTING_PPP_LCP_ECHO_INTERVAL = 'lcp-echo-interval'
SETTING_PPP_MPPE_STATEFUL = 'mppe-stateful'
SETTING_PPP_MRU = 'mru'
SETTING_PPP_MTU = 'mtu'
SETTING_PPP_NOAUTH = 'noauth'
SETTING_PPP_NOBSDCOMP = 'nobsdcomp'
SETTING_PPP_NODEFLATE = 'nodeflate'
SETTING_PPP_NO_VJ_COMP = 'no-vj-comp'
SETTING_PPP_REFUSE_CHAP = 'refuse-chap'
SETTING_PPP_REFUSE_EAP = 'refuse-eap'
SETTING_PPP_REFUSE_MSCHAP = 'refuse-mschap'
SETTING_PPP_REFUSE_MSCHAPV2 = 'refuse-mschapv2'
SETTING_PPP_REFUSE_PAP = 'refuse-pap'
SETTING_PPP_REQUIRE_MPPE = 'require-mppe'
SETTING_PPP_REQUIRE_MPPE_128 = 'require-mppe-128'
SETTING_PPP_SETTING_NAME = 'ppp'
SETTING_PREFIX_DELEGATION_SETTING_NAME = 'prefix-delegation'
SETTING_PREFIX_DELEGATION_SUBNET_ID = 'subnet-id'
SETTING_PROXY_BROWSER_ONLY = 'browser-only'
SETTING_PROXY_METHOD = 'method'
SETTING_PROXY_PAC_SCRIPT = 'pac-script'
SETTING_PROXY_PAC_URL = 'pac-url'
SETTING_PROXY_SETTING_NAME = 'proxy'
SETTING_SERIAL_BAUD = 'baud'
SETTING_SERIAL_BITS = 'bits'
SETTING_SERIAL_PARITY = 'parity'
SETTING_SERIAL_SEND_DELAY = 'send-delay'
SETTING_SERIAL_SETTING_NAME = 'serial'
SETTING_SERIAL_STOPBITS = 'stopbits'
SETTING_SRIOV_AUTOPROBE_DRIVERS = 'autoprobe-drivers'
SETTING_SRIOV_ESWITCH_ENCAP_MODE = 'eswitch-encap-mode'
SETTING_SRIOV_ESWITCH_INLINE_MODE = 'eswitch-inline-mode'
SETTING_SRIOV_ESWITCH_MODE = 'eswitch-mode'
SETTING_SRIOV_PRESERVE_ON_DOWN = 'preserve-on-down'
SETTING_SRIOV_SETTING_NAME = 'sriov'
SETTING_SRIOV_TOTAL_VFS = 'total-vfs'
SETTING_SRIOV_VFS = 'vfs'
SETTING_TC_CONFIG_QDISCS = 'qdiscs'
SETTING_TC_CONFIG_SETTING_NAME = 'tc'
SETTING_TC_CONFIG_TFILTERS = 'tfilters'
SETTING_TEAM_CONFIG = 'config'
SETTING_TEAM_LINK_WATCHERS = 'link-watchers'
SETTING_TEAM_MCAST_REJOIN_COUNT = 'mcast-rejoin-count'
SETTING_TEAM_MCAST_REJOIN_INTERVAL = 'mcast-rejoin-interval'
SETTING_TEAM_NOTIFY_MCAST_COUNT_ACTIVEBACKUP_DEFAULT = '1'
SETTING_TEAM_NOTIFY_PEERS_COUNT = 'notify-peers-count'
SETTING_TEAM_NOTIFY_PEERS_COUNT_ACTIVEBACKUP_DEFAULT = '1'
SETTING_TEAM_NOTIFY_PEERS_INTERVAL = 'notify-peers-interval'
SETTING_TEAM_PORT_CONFIG = 'config'
SETTING_TEAM_PORT_LACP_KEY = 'lacp-key'
SETTING_TEAM_PORT_LACP_PRIO = 'lacp-prio'
SETTING_TEAM_PORT_LACP_PRIO_DEFAULT = '255'
SETTING_TEAM_PORT_LINK_WATCHERS = 'link-watchers'
SETTING_TEAM_PORT_PRIO = 'prio'
SETTING_TEAM_PORT_QUEUE_ID = 'queue-id'
SETTING_TEAM_PORT_QUEUE_ID_DEFAULT = '-1'
SETTING_TEAM_PORT_SETTING_NAME = 'team-port'
SETTING_TEAM_PORT_STICKY = 'sticky'
SETTING_TEAM_RUNNER = 'runner'
SETTING_TEAM_RUNNER_ACTIVE = 'runner-active'
SETTING_TEAM_RUNNER_ACTIVEBACKUP = 'activebackup'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY = 'runner-agg-select-policy'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY_BANDWIDTH = 'bandwidth'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY_COUNT = 'count'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY_LACP_PRIO = 'lacp_prio'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY_LACP_PRIO_STABLE = 'lacp_prio_stable'
SETTING_TEAM_RUNNER_AGG_SELECT_POLICY_PORT_CONFIG = 'port_config'
SETTING_TEAM_RUNNER_BROADCAST = 'broadcast'
SETTING_TEAM_RUNNER_FAST_RATE = 'runner-fast-rate'
SETTING_TEAM_RUNNER_HWADDR_POLICY = 'runner-hwaddr-policy'
SETTING_TEAM_RUNNER_HWADDR_POLICY_BY_ACTIVE = 'by_active'
SETTING_TEAM_RUNNER_HWADDR_POLICY_ONLY_ACTIVE = 'only_active'
SETTING_TEAM_RUNNER_HWADDR_POLICY_SAME_ALL = 'same_all'
SETTING_TEAM_RUNNER_LACP = 'lacp'
SETTING_TEAM_RUNNER_LOADBALANCE = 'loadbalance'
SETTING_TEAM_RUNNER_MIN_PORTS = 'runner-min-ports'
SETTING_TEAM_RUNNER_RANDOM = 'random'
SETTING_TEAM_RUNNER_ROUNDROBIN = 'roundrobin'
SETTING_TEAM_RUNNER_SYS_PRIO = 'runner-sys-prio'
SETTING_TEAM_RUNNER_SYS_PRIO_DEFAULT = '65535'
SETTING_TEAM_RUNNER_TX_BALANCER = 'runner-tx-balancer'
SETTING_TEAM_RUNNER_TX_BALANCER_INTERVAL = 'runner-tx-balancer-interval'
SETTING_TEAM_RUNNER_TX_BALANCER_INTERVAL_DEFAULT = '50'
SETTING_TEAM_RUNNER_TX_HASH = 'runner-tx-hash'
SETTING_TEAM_SETTING_NAME = 'team'
SETTING_TUN_GROUP = 'group'
SETTING_TUN_MODE = 'mode'
SETTING_TUN_MULTI_QUEUE = 'multi-queue'
SETTING_TUN_OWNER = 'owner'
SETTING_TUN_PI = 'pi'
SETTING_TUN_SETTING_NAME = 'tun'
SETTING_TUN_VNET_HDR = 'vnet-hdr'
SETTING_USER_DATA = 'data'
SETTING_USER_SETTING_NAME = 'user'
SETTING_VETH_PEER = 'peer'
SETTING_VETH_SETTING_NAME = 'veth'
SETTING_VLAN_EGRESS_PRIORITY_MAP = 'egress-priority-map'
SETTING_VLAN_FLAGS = 'flags'
SETTING_VLAN_ID = 'id'
SETTING_VLAN_INGRESS_PRIORITY_MAP = 'ingress-priority-map'
SETTING_VLAN_PARENT = 'parent'
SETTING_VLAN_PROTOCOL = 'protocol'
SETTING_VLAN_SETTING_NAME = 'vlan'
SETTING_VPN_DATA = 'data'
SETTING_VPN_PERSISTENT = 'persistent'
SETTING_VPN_SECRETS = 'secrets'
SETTING_VPN_SERVICE_TYPE = 'service-type'
SETTING_VPN_SETTING_NAME = 'vpn'
SETTING_VPN_TIMEOUT = 'timeout'
SETTING_VPN_USER_NAME = 'user-name'
SETTING_VRF_SETTING_NAME = 'vrf'
SETTING_VRF_TABLE = 'table'
SETTING_VXLAN_AGEING = 'ageing'
SETTING_VXLAN_DESTINATION_PORT = 'destination-port'
SETTING_VXLAN_ID = 'id'
SETTING_VXLAN_L2_MISS = 'l2-miss'
SETTING_VXLAN_L3_MISS = 'l3-miss'
SETTING_VXLAN_LEARNING = 'learning'
SETTING_VXLAN_LIMIT = 'limit'
SETTING_VXLAN_LOCAL = 'local'
SETTING_VXLAN_PARENT = 'parent'
SETTING_VXLAN_PROXY = 'proxy'
SETTING_VXLAN_REMOTE = 'remote'
SETTING_VXLAN_RSC = 'rsc'
SETTING_VXLAN_SETTING_NAME = 'vxlan'
SETTING_VXLAN_SOURCE_PORT_MAX = 'source-port-max'
SETTING_VXLAN_SOURCE_PORT_MIN = 'source-port-min'
SETTING_VXLAN_TOS = 'tos'
SETTING_VXLAN_TTL = 'ttl'
SETTING_WIFI_P2P_PEER = 'peer'
SETTING_WIFI_P2P_SETTING_NAME = 'wifi-p2p'
SETTING_WIFI_P2P_WFD_IES = 'wfd-ies'
SETTING_WIFI_P2P_WPS_METHOD = 'wps-method'
SETTING_WIMAX_MAC_ADDRESS = 'mac-address'
SETTING_WIMAX_NETWORK_NAME = 'network-name'
SETTING_WIMAX_SETTING_NAME = 'wimax'
SETTING_WIRED_ACCEPT_ALL_MAC_ADDRESSES = 'accept-all-mac-addresses'
SETTING_WIRED_AUTO_NEGOTIATE = 'auto-negotiate'
SETTING_WIRED_CLONED_MAC_ADDRESS = 'cloned-mac-address'
SETTING_WIRED_DUPLEX = 'duplex'
SETTING_WIRED_GENERATE_MAC_ADDRESS_MASK = 'generate-mac-address-mask'
SETTING_WIRED_MAC_ADDRESS = 'mac-address'
SETTING_WIRED_MAC_ADDRESS_BLACKLIST = 'mac-address-blacklist'
SETTING_WIRED_MAC_ADDRESS_DENYLIST = 'mac-address-denylist'
SETTING_WIRED_MTU = 'mtu'
SETTING_WIRED_PORT = 'port'
SETTING_WIRED_S390_NETTYPE = 's390-nettype'
SETTING_WIRED_S390_OPTIONS = 's390-options'
SETTING_WIRED_S390_SUBCHANNELS = 's390-subchannels'
SETTING_WIRED_SETTING_NAME = '802-3-ethernet'
SETTING_WIRED_SPEED = 'speed'
SETTING_WIRED_WAKE_ON_LAN = 'wake-on-lan'
SETTING_WIRED_WAKE_ON_LAN_PASSWORD = 'wake-on-lan-password'
SETTING_WIREGUARD_FWMARK = 'fwmark'
SETTING_WIREGUARD_IP4_AUTO_DEFAULT_ROUTE = 'ip4-auto-default-route'
SETTING_WIREGUARD_IP6_AUTO_DEFAULT_ROUTE = 'ip6-auto-default-route'
SETTING_WIREGUARD_LISTEN_PORT = 'listen-port'
SETTING_WIREGUARD_MTU = 'mtu'
SETTING_WIREGUARD_PEERS = 'peers'
SETTING_WIREGUARD_PEER_ROUTES = 'peer-routes'
SETTING_WIREGUARD_PRIVATE_KEY = 'private-key'
SETTING_WIREGUARD_PRIVATE_KEY_FLAGS = 'private-key-flags'
SETTING_WIREGUARD_SETTING_NAME = 'wireguard'
SETTING_WIRELESS_AP_ISOLATION = 'ap-isolation'
SETTING_WIRELESS_BAND = 'band'
SETTING_WIRELESS_BSSID = 'bssid'
SETTING_WIRELESS_CHANNEL = 'channel'
SETTING_WIRELESS_CHANNEL_WIDTH = 'channel-width'
SETTING_WIRELESS_CLONED_MAC_ADDRESS = 'cloned-mac-address'
SETTING_WIRELESS_GENERATE_MAC_ADDRESS_MASK = 'generate-mac-address-mask'
SETTING_WIRELESS_HIDDEN = 'hidden'
SETTING_WIRELESS_MAC_ADDRESS = 'mac-address'
SETTING_WIRELESS_MAC_ADDRESS_BLACKLIST = 'mac-address-blacklist'
SETTING_WIRELESS_MAC_ADDRESS_DENYLIST = 'mac-address-denylist'
SETTING_WIRELESS_MAC_ADDRESS_RANDOMIZATION = 'mac-address-randomization'
SETTING_WIRELESS_MODE = 'mode'
SETTING_WIRELESS_MODE_ADHOC = 'adhoc'
SETTING_WIRELESS_MODE_AP = 'ap'
SETTING_WIRELESS_MODE_INFRA = 'infrastructure'
SETTING_WIRELESS_MODE_MESH = 'mesh'
SETTING_WIRELESS_MTU = 'mtu'
SETTING_WIRELESS_POWERSAVE = 'powersave'
SETTING_WIRELESS_RATE = 'rate'
SETTING_WIRELESS_SECURITY_AUTH_ALG = 'auth-alg'
SETTING_WIRELESS_SECURITY_FILS = 'fils'
SETTING_WIRELESS_SECURITY_GROUP = 'group'
SETTING_WIRELESS_SECURITY_KEY_MGMT = 'key-mgmt'
SETTING_WIRELESS_SECURITY_LEAP_PASSWORD = 'leap-password'
SETTING_WIRELESS_SECURITY_LEAP_PASSWORD_FLAGS = 'leap-password-flags'
SETTING_WIRELESS_SECURITY_LEAP_USERNAME = 'leap-username'
SETTING_WIRELESS_SECURITY_PAIRWISE = 'pairwise'
SETTING_WIRELESS_SECURITY_PMF = 'pmf'
SETTING_WIRELESS_SECURITY_PROTO = 'proto'
SETTING_WIRELESS_SECURITY_PSK = 'psk'
SETTING_WIRELESS_SECURITY_PSK_FLAGS = 'psk-flags'
SETTING_WIRELESS_SECURITY_SETTING_NAME = '802-11-wireless-security'
SETTING_WIRELESS_SECURITY_WEP_KEY0 = 'wep-key0'
SETTING_WIRELESS_SECURITY_WEP_KEY1 = 'wep-key1'
SETTING_WIRELESS_SECURITY_WEP_KEY2 = 'wep-key2'
SETTING_WIRELESS_SECURITY_WEP_KEY3 = 'wep-key3'
SETTING_WIRELESS_SECURITY_WEP_KEY_FLAGS = 'wep-key-flags'
SETTING_WIRELESS_SECURITY_WEP_KEY_TYPE = 'wep-key-type'
SETTING_WIRELESS_SECURITY_WEP_TX_KEYIDX = 'wep-tx-keyidx'
SETTING_WIRELESS_SECURITY_WPS_METHOD = 'wps-method'
SETTING_WIRELESS_SEEN_BSSIDS = 'seen-bssids'
SETTING_WIRELESS_SETTING_NAME = '802-11-wireless'
SETTING_WIRELESS_SSID = 'ssid'
SETTING_WIRELESS_TX_POWER = 'tx-power'
SETTING_WIRELESS_WAKE_ON_WLAN = 'wake-on-wlan'
SETTING_WPAN_CHANNEL = 'channel'
SETTING_WPAN_CHANNEL_DEFAULT = '-1'
SETTING_WPAN_MAC_ADDRESS = 'mac-address'
SETTING_WPAN_PAGE = 'page'
SETTING_WPAN_PAGE_DEFAULT = '-1'
SETTING_WPAN_PAN_ID = 'pan-id'
SETTING_WPAN_SETTING_NAME = 'wpan'
SETTING_WPAN_SHORT_ADDRESS = 'short-address'
SRIOV_VF_ATTRIBUTE_MAC = 'mac'
SRIOV_VF_ATTRIBUTE_MAX_TX_RATE = 'max-tx-rate'
SRIOV_VF_ATTRIBUTE_MIN_TX_RATE = 'min-tx-rate'
SRIOV_VF_ATTRIBUTE_SPOOF_CHECK = 'spoof-check'
SRIOV_VF_ATTRIBUTE_TRUST = 'trust'


class SecretAgentCapabilities(enum.Enum):
    """#NMSecretAgentCapabilities indicate various capabilities of the agent."""
    NONE = 0
    VPN_HINTS = 1
    LAST = 1


class SecretAgentError(enum.Enum):
    """#NMSecretAgentError values are passed by secret agents back to NetworkManager
when they encounter problems retrieving secrets on behalf of NM. They
correspond to errors in the "org.freedesktop.NetworkManager.SecretManager"
namespace.

Client APIs such as nm_client_activate_connection() will not see these error
codes; instead, the secret agent manager will translate them to the
corresponding #NMAgentManagerError codes."""
    FAILED = 0
    PERMISSIONDENIED = 1
    INVALIDCONNECTION = 2
    USERCANCELED = 3
    AGENTCANCELED = 4
    NOSECRETS = 5


class SecretAgentGetSecretsFlags(enum.Enum):
    """#NMSecretAgentGetSecretsFlags values modify the behavior of a GetSecrets request."""
    NONE = 0
    ALLOW_INTERACTION = 1
    REQUEST_NEW = 2
    USER_REQUESTED = 4
    WPS_PBC_ACTIVE = 8
    ONLY_SYSTEM = 2147483648
    NO_ERRORS = 1073741824


class Setting8021xAuthFlags(enum.Enum):
    """#NMSetting8021xAuthFlags values indicate which authentication settings
should be used.

Before 1.22, this was wrongly marked as a enum and not as a flags
type."""
    NONE = 0
    TLS_1_0_DISABLE = 1
    TLS_1_1_DISABLE = 2
    TLS_1_2_DISABLE = 4
    TLS_DISABLE_TIME_CHECKS = 8
    TLS_1_3_DISABLE = 16
    TLS_1_0_ENABLE = 32
    TLS_1_1_ENABLE = 64
    TLS_1_2_ENABLE = 128
    TLS_1_3_ENABLE = 256
    ALL = 511


class Setting8021xCKFormat(enum.Enum):
    """#NMSetting8021xCKFormat values indicate the general type of a certificate
or private key"""
    UNKNOWN = 0
    X509 = 1
    RAW_KEY = 2
    PKCS12 = 3


class Setting8021xCKScheme(enum.Enum):
    """#NMSetting8021xCKScheme values indicate how a certificate or private key is
stored in the setting properties, either as a blob of the item's data, or as
a path to a certificate or private key file on the filesystem"""
    UNKNOWN = 0
    BLOB = 1
    PATH = 2
    PKCS11 = 3


class SettingCompareFlags(enum.Enum):
    """These flags modify the comparison behavior when comparing two settings or
two connections."""
    EXACT = 0
    FUZZY = 1
    IGNORE_ID = 2
    IGNORE_SECRETS = 4
    IGNORE_AGENT_OWNED_SECRETS = 8
    IGNORE_NOT_SAVED_SECRETS = 16
    DIFF_RESULT_WITH_DEFAULT = 32
    DIFF_RESULT_NO_DEFAULT = 64
    IGNORE_TIMESTAMP = 128


class SettingConnectionAutoconnectSlaves(enum.Enum):
    """#NMSettingConnectionAutoconnectSlaves values indicate whether slave connections
should be activated when controller is activated."""
    DEFAULT = -1
    NO = 0
    YES = 1


class SettingConnectionDnsOverTls(enum.Enum):
    """#NMSettingConnectionDnsOverTls values indicate whether DNSOverTls should be enabled."""
    DEFAULT = -1
    NO = 0
    OPPORTUNISTIC = 1
    YES = 2


class SettingConnectionDnssec(enum.Enum):
    """#NMSettingConnectionDnssec values indicate whether DNSSEC should be enabled."""
    DEFAULT = -1
    NO = 0
    ALLOW_DOWNGRADE = 1
    YES = 2


class SettingConnectionDownOnPoweroff(enum.Enum):
    """#NMSettingConnectionDownOnPoweroff indicates whether the connection will be
brought down before the system is powered off."""
    DEFAULT = -1
    NO = 0
    YES = 1


class SettingConnectionLldp(enum.Enum):
    """#NMSettingConnectionLldp values indicate whether LLDP should be enabled."""
    DEFAULT = -1
    DISABLE = 0
    ENABLE_RX = 1


class SettingConnectionLlmnr(enum.Enum):
    """#NMSettingConnectionLlmnr values indicate whether LLMNR should be enabled."""
    DEFAULT = -1
    NO = 0
    RESOLVE = 1
    YES = 2


class SettingConnectionMdns(enum.Enum):
    """#NMSettingConnectionMdns values indicate whether mDNS should be enabled."""
    DEFAULT = -1
    NO = 0
    RESOLVE = 1
    YES = 2


class SettingDcbFlags(enum.Enum):
    """DCB feature flags."""
    NONE = 0
    ENABLE = 1
    ADVERTISE = 2
    WILLING = 4


class SettingDiffResult(enum.Enum):
    """These values indicate the result of a setting difference operation."""
    UNKNOWN = 0
    IN_A = 1
    IN_B = 2
    IN_A_DEFAULT = 4
    IN_B_DEFAULT = 8


class SettingEthtoolFecMode(enum.Enum):
    """These flags modify the ethtool FEC(Forward Error Correction) mode."""
    AUTO = 2
    OFF = 4
    RS = 8
    BASER = 16
    LLRS = 32


class SettingHsrProtocolVersion(enum.Enum):
    """#NMSettingHsrProtocolVersion values indicate the HSR protocol version."""
    DEFAULT = -1
    HSR_2010 = 0
    HSR_2012 = 1


class SettingIP4DhcpIpv6OnlyPreferred(enum.Enum):
    """#NMSettingIP4DhcpIpv6OnlyPreferred values specify if the "IPv6-Only Preferred"
option (RFC 8925) for DHCPv4 is enabled."""
    DEFAULT = -1
    NO = 0
    YES = 1


class SettingIP4LinkLocal(enum.Enum):
    """#NMSettingIP4LinkLocal values indicate whether IPv4 link-local address protocol should be enabled."""
    DEFAULT = 0
    AUTO = 1
    DISABLED = 2
    ENABLED = 3
    FALLBACK = 4


class SettingIP6ConfigAddrGenMode(enum.Enum):
    """#NMSettingIP6ConfigAddrGenMode controls how the Interface Identifier for
RFC4862 Stateless Address Autoconfiguration is created."""
    EUI64 = 0
    STABLE_PRIVACY = 1
    DEFAULT_OR_EUI64 = 2
    DEFAULT = 3


class SettingIP6ConfigPrivacy(enum.Enum):
    """#NMSettingIP6ConfigPrivacy values indicate if and how IPv6 Privacy
Extensions are used (RFC4941)."""
    UNKNOWN = -1
    DISABLED = 0
    PREFER_PUBLIC_ADDR = 1
    PREFER_TEMP_ADDR = 2


class SettingIPConfigForwarding(enum.Enum):
    """#NMSettingIPConfigForwarding indicates whether to configure sysctl
interface-specific forwarding. When enabled, the interface will act
as a router to forward the packet from one interface to another."""
    DEFAULT = -1
    NO = 0
    YES = 1
    AUTO = 2


class SettingIPConfigRoutedDns(enum.Enum):
    """#NMSettingIPConfigRoutedDns indicates whether routes are added
automatically for each DNS that is associated with this connection."""
    DEFAULT = -1
    NO = 0
    YES = 1


class SettingIpvlanMode(enum.Enum):
    """"""
    UNKNOWN = 0
    L2 = 1
    L3 = 2
    L3S = 3


class SettingMacRandomization(enum.Enum):
    """Controls if and how the MAC address of a device is randomzied."""
    DEFAULT = 0
    NEVER = 1
    ALWAYS = 2


class SettingMacsecMode(enum.Enum):
    """#NMSettingMacsecMode controls how the CAK (Connectivity Association Key) used
in MKA (MACsec Key Agreement) is obtained."""
    PSK = 0
    EAP = 1


class SettingMacsecOffload(enum.Enum):
    """These flags control the MACsec offload mode."""
    DEFAULT = -1
    OFF = 0
    PHY = 1
    MAC = 2


class SettingMacsecValidation(enum.Enum):
    """#NMSettingMacsecValidation specifies a validation mode for incoming frames."""
    DISABLE = 0
    CHECK = 1
    STRICT = 2


class SettingMacvlanMode(enum.Enum):
    """"""
    UNKNOWN = 0
    VEPA = 1
    BRIDGE = 2
    PRIVATE = 3
    PASSTHRU = 4
    SOURCE = 5


class SettingOvsDpdkLscInterrupt(enum.Enum):
    """#NMSettingOvsDpdkLscInterrupt indicates whether the interface uses interrupts
or poll mode for Link State Change (LSC) detection on the OVS DPDK interface."""
    IGNORE = -1
    DISABLED = 0
    ENABLED = 1


class SettingProxyMethod(enum.Enum):
    """The Proxy method."""
    NONE = 0
    AUTO = 1


class SettingSecretFlags(enum.Enum):
    """These flags indicate specific behavior related to handling of a secret.  Each
secret has a corresponding set of these flags which indicate how the secret
is to be stored and/or requested when it is needed."""
    NONE = 0
    AGENT_OWNED = 1
    NOT_SAVED = 2
    NOT_REQUIRED = 4


class SettingSerialParity(enum.Enum):
    """The parity setting of a serial port."""
    NONE = 0
    EVEN = 1
    ODD = 2


class SettingTunMode(enum.Enum):
    """#NMSettingTunMode values indicate the device type (TUN/TAP)"""
    UNKNOWN = 0
    TUN = 1
    TAP = 2


class SettingWiredWakeOnLan(enum.Enum):
    """Options for #NMSettingWired:wake-on-lan. Note that not all options
are supported by all devices."""
    PHY = 2
    UNICAST = 4
    MULTICAST = 8
    BROADCAST = 16
    ARP = 32
    MAGIC = 64
    DEFAULT = 1
    IGNORE = 32768


class SettingWirelessChannelWidth(enum.Enum):
    """Indicates the wireless channel width."""
    AUTO = 0
    _20MHZ = 20
    _40MHZ = 40
    _80MHZ = 80


class SettingWirelessPowersave(enum.Enum):
    """These flags indicate whether wireless powersave must be enabled."""
    DEFAULT = 0
    IGNORE = 1
    DISABLE = 2
    ENABLE = 3


class SettingWirelessSecurityFils(enum.Enum):
    """These flags indicate whether FILS must be enabled."""
    DEFAULT = 0
    DISABLE = 1
    OPTIONAL = 2
    REQUIRED = 3


class SettingWirelessSecurityPmf(enum.Enum):
    """These flags indicate whether PMF must be enabled."""
    DEFAULT = 0
    DISABLE = 1
    OPTIONAL = 2
    REQUIRED = 3


class SettingWirelessSecurityWpsMethod(enum.Enum):
    """Configure the use of WPS by a connection while it activates.

Note: prior to 1.16, this was a GEnum type instead of a GFlags type
although, with the same numeric values."""
    DEFAULT = 0
    DISABLED = 1
    AUTO = 2
    PBC = 4
    PIN = 8


class SettingWirelessWakeOnWLan(enum.Enum):
    """Options for #NMSettingWireless:wake-on-wlan. Note that not all options
are supported by all devices."""
    ANY = 2
    DISCONNECT = 4
    MAGIC = 8
    GTK_REKEY_FAILURE = 16
    EAP_IDENTITY_REQUEST = 32
    _4WAY_HANDSHAKE = 64
    RFKILL_RELEASE = 128
    TCP = 256
    ALL = 510
    DEFAULT = 1
    IGNORE = 32768


class SettingsAddConnection2Flags(enum.Enum):
    """Numeric flags for the "flags" argument of AddConnection2() D-Bus API."""
    NONE = 0
    TO_DISK = 1
    IN_MEMORY = 2
    BLOCK_AUTOCONNECT = 32


class SettingsConnectionFlags(enum.Enum):
    """Flags describing the current activation state."""
    NONE = 0
    UNSAVED = 1
    NM_GENERATED = 2
    VOLATILE = 4
    EXTERNAL = 8


class SettingsError(enum.Enum):
    """Errors related to the settings/persistent configuration interface of
NetworkManager.

These may be returned from #NMClient methods that invoke D-Bus operations on
the "org.freedesktop.NetworkManager.Settings" interface, and correspond to
D-Bus errors in that namespace."""
    FAILED = 0
    PERMISSIONDENIED = 1
    NOTSUPPORTED = 2
    INVALIDCONNECTION = 3
    READONLYCONNECTION = 4
    UUIDEXISTS = 5
    INVALIDHOSTNAME = 6
    INVALIDARGUMENTS = 7
    VERSIONIDMISMATCH = 8
    NOTSUPPORTEDBYPLUGIN = 9
    FEATUREDISABLED = 10
    FEATUREREMOVED = 11


class SettingsUpdate2Flags(enum.Enum):
    """"""
    NONE = 0
    TO_DISK = 1
    IN_MEMORY = 2
    IN_MEMORY_DETACHED = 4
    IN_MEMORY_ONLY = 8
    VOLATILE = 16
    BLOCK_AUTOCONNECT = 32
    NO_REAPPLY = 64


class SriovEswitchEncapMode(enum.Enum):
    """"""
    PRESERVE = -1
    NONE = 0
    BASIC = 1


class SriovEswitchInlineMode(enum.Enum):
    """"""
    PRESERVE = -1
    NONE = 0
    LINK = 1
    NETWORK = 2
    TRANSPORT = 3


class SriovEswitchMode(enum.Enum):
    """"""
    PRESERVE = -1
    LEGACY = 0
    SWITCHDEV = 1


class SriovPreserveOnDown(enum.Enum):
    """"""
    DEFAULT = -1
    NO = 0
    YES = 1


class SriovVFVlanProtocol(enum.Enum):
    """#NMSriovVFVlanProtocol indicates the VLAN protocol to use."""
    _1Q = 0
    _1AD = 1


class State(enum.Enum):
    """#NMState values indicate the current overall networking state."""
    UNKNOWN = 0
    ASLEEP = 10
    DISABLED = 10
    DISCONNECTED = 20
    DISCONNECTING = 30
    CONNECTING = 40
    CONNECTED_LOCAL = 50
    CONNECTED_SITE = 60
    CONNECTED_GLOBAL = 70


TEAM_LINK_WATCHER_ARP_PING = 'arp_ping'
TEAM_LINK_WATCHER_ETHTOOL = 'ethtool'
TEAM_LINK_WATCHER_NSNA_PING = 'nsna_ping'


class TeamLinkWatcherArpPingFlags(enum.Enum):
    """"""
    VALIDATE_ACTIVE = 2
    VALIDATE_INACTIVE = 4
    SEND_ALWAYS = 8


class Ternary(enum.Enum):
    """An boolean value that can be overridden by a default."""
    DEFAULT = -1
    FALSE = 0
    TRUE = 1


UTILS_HWADDR_LEN_MAX = '20'


class UtilsSecurityType(enum.Enum):
    """Describes generic security mechanisms that 802.11 access points may offer.
Used with nm_utils_security_valid() for checking whether a given access
point is compatible with a network device."""
    INVALID = 0
    NONE = 1
    STATIC_WEP = 2
    LEAP = 3
    DYNAMIC_WEP = 4
    WPA_PSK = 5
    WPA_ENTERPRISE = 6
    WPA2_PSK = 7
    WPA2_ENTERPRISE = 8
    SAE = 9
    OWE = 10
    WPA3_SUITE_B_192 = 11


VLAN_FLAGS_ALL = '15'
VPN_CONNECTION_BANNER = 'banner'
VPN_CONNECTION_VPN_STATE = 'vpn-state'
VPN_DBUS_PLUGIN_INTERFACE = 'org.freedesktop.NetworkManager.VPN.Plugin'
VPN_DBUS_PLUGIN_PATH = '/org/freedesktop/NetworkManager/VPN/Plugin'
VPN_EDITOR_PLUGIN_DESCRIPTION = 'description'
VPN_EDITOR_PLUGIN_NAME = 'name'
VPN_EDITOR_PLUGIN_SERVICE = 'service'
VPN_PLUGIN_CAN_PERSIST = 'can-persist'
VPN_PLUGIN_CONFIG_BANNER = 'banner'
VPN_PLUGIN_CONFIG_EXT_GATEWAY = 'gateway'
VPN_PLUGIN_CONFIG_HAS_IP4 = 'has-ip4'
VPN_PLUGIN_CONFIG_HAS_IP6 = 'has-ip6'
VPN_PLUGIN_CONFIG_MTU = 'mtu'
VPN_PLUGIN_CONFIG_PROXY_PAC = 'pac'
VPN_PLUGIN_CONFIG_TUNDEV = 'tundev'
VPN_PLUGIN_INFO_FILENAME = 'filename'
VPN_PLUGIN_INFO_KEYFILE = 'keyfile'
VPN_PLUGIN_INFO_KF_GROUP_CONNECTION = 'VPN Connection'
VPN_PLUGIN_INFO_KF_GROUP_GNOME = 'GNOME'
VPN_PLUGIN_INFO_KF_GROUP_LIBNM = 'libnm'
VPN_PLUGIN_INFO_NAME = 'name'
VPN_PLUGIN_IP4_CONFIG_ADDRESS = 'address'
VPN_PLUGIN_IP4_CONFIG_DNS = 'dns'
VPN_PLUGIN_IP4_CONFIG_DOMAIN = 'domain'
VPN_PLUGIN_IP4_CONFIG_DOMAINS = 'domains'
VPN_PLUGIN_IP4_CONFIG_INT_GATEWAY = 'internal-gateway'
VPN_PLUGIN_IP4_CONFIG_MSS = 'mss'
VPN_PLUGIN_IP4_CONFIG_NBNS = 'nbns'
VPN_PLUGIN_IP4_CONFIG_NEVER_DEFAULT = 'never-default'
VPN_PLUGIN_IP4_CONFIG_PREFIX = 'prefix'
VPN_PLUGIN_IP4_CONFIG_PRESERVE_ROUTES = 'preserve-routes'
VPN_PLUGIN_IP4_CONFIG_PTP = 'ptp'
VPN_PLUGIN_IP4_CONFIG_ROUTES = 'routes'
VPN_PLUGIN_IP6_CONFIG_ADDRESS = 'address'
VPN_PLUGIN_IP6_CONFIG_DNS = 'dns'
VPN_PLUGIN_IP6_CONFIG_DOMAIN = 'domain'
VPN_PLUGIN_IP6_CONFIG_DOMAINS = 'domains'
VPN_PLUGIN_IP6_CONFIG_INT_GATEWAY = 'internal-gateway'
VPN_PLUGIN_IP6_CONFIG_MSS = 'mss'
VPN_PLUGIN_IP6_CONFIG_NEVER_DEFAULT = 'never-default'
VPN_PLUGIN_IP6_CONFIG_PREFIX = 'prefix'
VPN_PLUGIN_IP6_CONFIG_PRESERVE_ROUTES = 'preserve-routes'
VPN_PLUGIN_IP6_CONFIG_PTP = 'ptp'
VPN_PLUGIN_IP6_CONFIG_ROUTES = 'routes'
VPN_PLUGIN_OLD_DBUS_SERVICE_NAME = 'service-name'
VPN_PLUGIN_OLD_STATE = 'state'
VPN_SERVICE_PLUGIN_DBUS_SERVICE_NAME = 'service-name'
VPN_SERVICE_PLUGIN_DBUS_WATCH_PEER = 'watch-peer'
VPN_SERVICE_PLUGIN_STATE = 'state'


class VersionInfoCapability(enum.Enum):
    """The numeric values represent the bit index of the capability. These capabilities
can be queried in the "VersionInfo" D-Bus property."""
    SYNC_ROUTE_WITH_TABLE = 0
    IP4_FORWARDING = 1
    SRIOV_PRESERVE_ON_DOWN = 2


class VlanFlags(enum.Enum):
    """#NMVlanFlags values control the behavior of the VLAN interface."""
    REORDER_HEADERS = 1
    GVRP = 2
    LOOSE_BINDING = 4
    MVRP = 8


class VlanPriorityMap(enum.Enum):
    """A selector for traffic priority maps; these map Linux SKB priorities
to 802.1p priorities used in VLANs."""
    INGRESS_MAP = 0
    EGRESS_MAP = 1


class VpnConnectionState(enum.Enum):
    """VPN connection states"""
    UNKNOWN = 0
    PREPARE = 1
    NEED_AUTH = 2
    CONNECT = 3
    IP_CONFIG_GET = 4
    ACTIVATED = 5
    FAILED = 6
    DISCONNECTED = 7


class VpnConnectionStateReason(enum.Enum):
    """VPN connection state reasons"""
    UNKNOWN = 0
    NONE = 1
    USER_DISCONNECTED = 2
    DEVICE_DISCONNECTED = 3
    SERVICE_STOPPED = 4
    IP_CONFIG_INVALID = 5
    CONNECT_TIMEOUT = 6
    SERVICE_START_TIMEOUT = 7
    SERVICE_START_FAILED = 8
    NO_SECRETS = 9
    LOGIN_FAILED = 10
    CONNECTION_REMOVED = 11


class VpnEditorPluginCapability(enum.Enum):
    """Flags that indicate certain capabilities of the plugin to editor programs."""
    NONE = 0
    IMPORT = 1
    EXPORT = 2
    IPV6 = 4
    NO_EDITOR = 8


class VpnPluginError(enum.Enum):
    """Returned by the VPN service plugin to indicate errors. These codes correspond
to errors in the "org.freedesktop.NetworkManager.VPN.Error" namespace."""
    FAILED = 0
    STARTINGINPROGRESS = 1
    ALREADYSTARTED = 2
    STOPPINGINPROGRESS = 3
    ALREADYSTOPPED = 4
    WRONGSTATE = 5
    BADARGUMENTS = 6
    LAUNCHFAILED = 7
    INVALIDCONNECTION = 8
    INTERACTIVENOTSUPPORTED = 9


class VpnPluginFailure(enum.Enum):
    """VPN plugin failure reasons"""
    LOGIN_FAILED = 0
    CONNECT_FAILED = 1
    BAD_IP_CONFIG = 2


class VpnServiceState(enum.Enum):
    """VPN daemon states"""
    UNKNOWN = 0
    INIT = 1
    SHUTDOWN = 2
    STARTING = 3
    STARTED = 4
    STOPPING = 5
    STOPPED = 6


WIFI_P2P_PEER_FLAGS = 'flags'
WIFI_P2P_PEER_HW_ADDRESS = 'hw-address'
WIFI_P2P_PEER_LAST_SEEN = 'last-seen'
WIFI_P2P_PEER_MANUFACTURER = 'manufacturer'
WIFI_P2P_PEER_MODEL = 'model'
WIFI_P2P_PEER_MODEL_NUMBER = 'model-number'
WIFI_P2P_PEER_NAME = 'name'
WIFI_P2P_PEER_SERIAL = 'serial'
WIFI_P2P_PEER_STRENGTH = 'strength'
WIFI_P2P_PEER_WFD_IES = 'wfd-ies'
WIMAX_NSP_NAME = 'name'
WIMAX_NSP_NETWORK_TYPE = 'network-type'
WIMAX_NSP_SIGNAL_QUALITY = 'signal-quality'
WIREGUARD_PEER_ATTR_ALLOWED_IPS = 'allowed-ips'
WIREGUARD_PEER_ATTR_ENDPOINT = 'endpoint'
WIREGUARD_PEER_ATTR_PERSISTENT_KEEPALIVE = 'persistent-keepalive'
WIREGUARD_PEER_ATTR_PRESHARED_KEY = 'preshared-key'
WIREGUARD_PEER_ATTR_PRESHARED_KEY_FLAGS = 'preshared-key-flags'
WIREGUARD_PEER_ATTR_PUBLIC_KEY = 'public-key'
WIREGUARD_PUBLIC_KEY_LEN = '32'
WIREGUARD_SYMMETRIC_KEY_LEN = '32'


class WepKeyType(enum.Enum):
    """The #NMWepKeyType values specify how any WEP keys present in the setting
are interpreted.  There are no standards governing how to hash the various WEP
key/passphrase formats into the actual WEP key.  Unfortunately some WEP keys
can be interpreted in multiple ways, requiring the setting to specify how to
interpret the any WEP keys.  For example, the key "732f2d712e4a394a375d366931"
is both a valid Hexadecimal WEP key and a WEP passphrase.  Further, many
ASCII keys are also valid WEP passphrases, but since passphrases and ASCII
keys are hashed differently to determine the actual WEP key the type must be
specified."""
    UNKNOWN = 0
    KEY = 1
    PASSPHRASE = 2


class WimaxNspNetworkType(enum.Enum):
    """WiMAX network type."""
    UNKNOWN = 0
    HOME = 1
    PARTNER = 2
    ROAMING_PARTNER = 3


def agent_manager_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def bridge_vlan_from_str(str: str=None) -> BridgeVlan:
    """Parses the string representation of the queueing
discipline to a %NMBridgeVlan instance.

:param str: the string representation of a bridge VLAN
:return: the %NMBridgeVlan or %NULL"""
    pass


def client_error_quark() -> GLib.Quark:
    """Registers an error quark for #NMClient if necessary.

:return: the error quark used for #NMClient errors."""
    pass


def conn_wireguard_import(filename: str=None) -> Connection:
    """

:param filename: name of the file to attempt to read into a new #NMConnection
:return: a new #NMConnection imported from @path, or %NULL on error or if the file with @filename was not recognized as a WireGuard config"""
    pass


def connection_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def crypto_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def device_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def dns_server_validate(str: str=None, family: int=None) -> bool:
    """Validates a DNS name server string.

:param str: the string containing the DNS server
:param family: the IP address family (%AF_INET for IPv4, %AF_INET6 for IPv6,   %AF_UNSPEC to accept both IPv4 and IPv6)
:return: %TRUE if the name server is valid, %FALSE otherwise"""
    pass


def ethtool_optname_is_channels(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for a channels setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ethtool_optname_is_coalesce(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for a coalesce setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ethtool_optname_is_eee(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for an eee setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ethtool_optname_is_feature(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for an offload feature.

:param optname: the option name to check
:return: %TRUE, if @optname is valid  Note that nm_ethtool_optname_is_feature() was first added to the libnm header files in 1.14.0 but forgot to actually add to the library. This happened belatedly in 1.20.0 and the stable versions 1.18.2, 1.16.4 and 1.14.8 (with linker version "libnm_1_14_8")."""
    pass


def ethtool_optname_is_fec(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for a fec setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ethtool_optname_is_pause(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for a pause setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ethtool_optname_is_ring(optname: str=None) -> bool:
    """Checks whether @optname is a valid option name for a ring setting.

:param optname: the option name to check
:return: %TRUE, if @optname is valid"""
    pass


def ip_route_attribute_validate(name: str=None, value: GLib.Variant=None,
    family: int=None, known: bool=None) -> bool:
    """Validates a route attribute, i.e. checks that the attribute is a known one
and the value is of the correct type and well-formed.

:param name: the attribute name
:param value: the attribute value
:param family: IP address family of the route
:param known: on return, whether the attribute name is a known one
:return: %TRUE if the attribute is valid, %FALSE otherwise"""
    pass


def ip_route_get_variant_attribute_spec() -> VariantAttributeSpec:
    """

:return: the specifiers for route attributes"""
    pass


def ip_routing_rule_from_string(str: str=None, to_string_flags:
    IPRoutingRuleAsStringFlags=None, extra_args: GLib.HashTable=None
    ) -> IPRoutingRule:
    """

:param str: the string representation to convert to an #NMIPRoutingRule
:param to_string_flags: #NMIPRoutingRuleAsStringFlags for controlling the   string conversion.
:param extra_args: extra arguments for controlling the string   conversion. Currently, not extra arguments are supported.
:return: the new #NMIPRoutingRule or %NULL on error."""
    pass


def keyfile_read(keyfile: GLib.KeyFile=None, base_dir: str=None,
    handler_flags: KeyfileHandlerFlags=None, handler: KeyfileReadHandler=
    None, user_data: typing.Any=None) -> Connection:
    """Tries to create a NMConnection from a keyfile. The resulting keyfile is
not normalized and might not even verify.

:param keyfile: the keyfile from which to create the connection
:param base_dir: when reading certificates from files with relative name,   the relative path is made absolute using @base_dir. This must   be an absolute path.
:param handler_flags: the #NMKeyfileHandlerFlags.
:param handler: read handler
:param user_data: user data for read handler
:return: on success, returns the created connection."""
    pass


def keyfile_write(connection: Connection=None, handler_flags:
    KeyfileHandlerFlags=None, handler: KeyfileWriteHandler=None, user_data:
    typing.Any=None) -> GLib.KeyFile:
    """@connection should verify as a valid profile according to
nm_connection_verify(). If it does not verify, the keyfile may
be incomplete and the parser may not be able to fully recreate
the original profile.

:param connection: the #NMConnection to persist to keyfile.
:param handler_flags: the #NMKeyfileHandlerFlags.
:param handler: optional handler for events and   to override the default behavior.
:param user_data: argument for @handler.
:return: a new #GKeyFile or %NULL on error."""
    pass


def manager_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def range_from_str(str: str=None) -> Range:
    """Parses the string representation of the range to create a %NMRange
instance.

:param str: the string representation of a range
:return: the %NMRange or %NULL"""
    pass


def secret_agent_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def settings_error_quark() -> GLib.Quark:
    """

:return: """
    pass


def sriov_vf_attribute_validate(name: str=None, value: GLib.Variant=None,
    known: bool=None) -> bool:
    """Validates a VF attribute, i.e. checks that the attribute is a known one,
the value is of the correct type and well-formed.

:param name: the attribute name
:param value: the attribute value
:param known: on return, whether the attribute name is a known one
:return: %TRUE if the attribute is valid, %FALSE otherwise"""
    pass


def utils_ap_mode_security_valid(type: UtilsSecurityType=None, wifi_caps:
    DeviceWifiCapabilities=None) -> bool:
    """Given a set of device capabilities, and a desired security type to check
against, determines whether the combination of device capabilities and
desired security type are valid for AP/Hotspot connections.

:param type: the security type to check device capabilities against, e.g. #NMU_SEC_STATIC_WEP
:param wifi_caps: bitfield of the capabilities of the specific Wi-Fi device, e.g. #NM_WIFI_DEVICE_CAP_CIPHER_WEP40
:return: %TRUE if the device capabilities are compatible with the desired @type, %FALSE if they are not."""
    pass


def utils_base64secret_decode(base64_key: str=None, required_key_len: int=
    None, out_key: int=None) -> bool:
    """

:param base64_key: the (possibly invalid) base64 encode key.
:param required_key_len: the expected (binary) length of the key after   decoding. If the length does not match, the validation fails.
:param out_key: an optional output buffer for the binary   key. If given, it will be filled with exactly @required_key_len   bytes.
:return: %TRUE if the input key is a valid base64 encoded key
   with @required_key_len bytes."""
    pass


def utils_bin2hexstr(src: typing.Any=None, len: int=None, final_len: int=None
    ) -> str:
    """Converts the byte array @src into a hexadecimal string. If @final_len is
greater than -1, the returned string is terminated at that index
(returned_string[final_len] == '\\0'),

:param src: an array of bytes
:param len: the length of the @src array
:param final_len: an index where to cut off the returned string, or -1
:return: the textual form of @bytes"""
    pass


def utils_bond_mode_int_to_string(mode: int=None) -> str:
    """Convert bonding mode from integer value to descriptive name.
See https://www.kernel.org/doc/Documentation/networking/bonding.txt for
available modes.

:param mode: bonding mode as a numeric value
:return: bonding mode string, or NULL on error"""
    pass


def utils_bond_mode_string_to_int(mode: str=None) -> int:
    """Convert bonding mode from string representation to numeric value.
See https://www.kernel.org/doc/Documentation/networking/bonding.txt for
available modes.
The @mode string can be either a descriptive name or a number (as string).

:param mode: bonding mode as string
:return: numeric bond mode, or -1 on error"""
    pass


def utils_check_virtual_device_compatibility(virtual_type: GType=None,
    other_type: GType=None) -> bool:
    """Determines if a connection of type @virtual_type can (in the
general case) work with connections of type @other_type.

If @virtual_type is %NM_TYPE_SETTING_VLAN, then this checks if
@other_type is a valid type for the parent of a VLAN.

If @virtual_type is a "controller" type (eg, %NM_TYPE_SETTING_BRIDGE),
then this checks if @other_type is a valid type for a port of that
controller.

Note that even if this returns %TRUE it is not guaranteed that
<emphasis>every</emphasis> connection of type @other_type is
compatible with @virtual_type; it may depend on the exact
configuration of the two connections, or on the capabilities of an
underlying device driver.

:param virtual_type: a virtual connection type
:param other_type: a connection type to test against @virtual_type
:return: %TRUE or %FALSE"""
    pass


def utils_copy_cert_as_user(filename: str=None, user: str=None) -> str:
    """Reads @filename on behalf of user @user and writes the
content to a new file in /run/NetworkManager/cert/.
The new file has permission 600 and is owned by root.

This function is useful for VPN plugins that run as root and need
to verify that the user owning the connection (the one listed in the
connection.permissions property) can access the file.

:param filename: the file name of the certificate or key to copy
:param user: the user to impersonate when reading the file
:return: the name of the new temporary file. Or %NULL
   if an error occurred, including when the given user can't access the
   file."""
    pass


def utils_ensure_gtypes() -> None:
    """This ensures that all NMSetting GTypes are created. For example,
after this call, g_type_from_name("NMSettingConnection") will work.

This cannot fail and does nothing if the type already exists.

:return: """
    pass


def utils_enum_from_str(type: GType=None, str: str=None, out_value: int=
    None, err_token: str=None) -> bool:
    """Converts a string to the matching enum value.

If the enum is a %G_TYPE_FLAGS the function returns the logical OR of values
matching the comma-separated tokens in the string; if an unknown token is found
the function returns %FALSE and stores a pointer to a newly allocated string
containing the unrecognized token in @err_token.

:param type: the %GType of the enum
:param str: the input string
:param out_value: the output value
:param err_token: location to store   the first unrecognized token
:return: %TRUE if the conversion was successful, %FALSE otherwise"""
    pass


def utils_enum_get_values(type: GType=None, _from: int=None, to: int=None
    ) -> typing.Any:
    """Returns the list of possible values for a given enum.

:param type: the %GType of the enum
:param _from: the first element to be returned
:param to: the last element to be returned
:return: a NULL-terminated dynamically-allocated array of static strings or %NULL on error"""
    pass


def utils_enum_to_str(type: GType=None, value: int=None) -> str:
    """Converts an enum value to its string representation. If the enum is a
%G_TYPE_FLAGS the function returns a comma-separated list of matching values.
If the value has no corresponding string representation, it is converted
to a number. For enums it is converted to a decimal number, for flags
to an (unsigned) hex number.

:param type: the %GType of the enum
:param value: the value to be translated
:return: a newly allocated string or %NULL"""
    pass


def utils_escape_ssid(ssid: typing.Any=None, len: int=None) -> str:
    """This function does a quick printable character conversion of the SSID, simply
replacing embedded NULLs and non-printable characters with the hexadecimal
representation of that character.  Intended for debugging only, should not
be used for display of SSIDs.

Warning: this function uses a static buffer. It is not thread-safe. Don't
  use this function.

:param ssid: pointer to a buffer containing the SSID data
:param len: length of the SSID data in @ssid
:return: pointer to the escaped SSID, which uses an internal static buffer and will be overwritten by subsequent calls to this function"""
    pass


def utils_file_is_certificate(filename: str=None) -> bool:
    """Tests if @filename has a valid extension for an X.509 certificate file
(".cer", ".crt", ".der", or ".pem"), and contains a certificate in a format
recognized by NetworkManager.

:param filename: name of the file to test
:return: %TRUE if the file is a certificate, %FALSE if it is not"""
    pass


def utils_file_is_pkcs12(filename: str=None) -> bool:
    """Tests if @filename is a PKCS#<!-- -->12 file.

:param filename: name of the file to test
:return: %TRUE if the file is PKCS#<!-- -->12, %FALSE if it is not"""
    pass


def utils_file_is_private_key(filename: str=None, out_encrypted: bool=None
    ) -> bool:
    """Tests if @filename has a valid extension for an X.509 private key file
(".der", ".key", ".pem", or ".p12"), and contains a private key in a format
recognized by NetworkManager.

:param filename: name of the file to test
:param out_encrypted: on return, whether the file is encrypted
:return: %TRUE if the file is a private key, %FALSE if it is not"""
    pass


def utils_file_search_in_paths(progname: str=None, try_first: str=None,
    paths: str=None, file_test_flags: GLib.FileTest=None, predicate:
    UtilsFileSearchInPathsPredicate=None, user_data: typing.Any=None) -> str:
    """Searches for a @progname file in a list of search @paths.

:param progname: the helper program name, like "iptables"   Must be a non-empty string, without path separator (/).
:param try_first: a custom path to try first before searching.   It is silently ignored if it is empty or not an absolute path.
:param paths: a %NULL terminated list of search paths.   Can be empty or %NULL, in which case only @try_first is checked.
:param file_test_flags: the flags passed to g_file_test() when searching   for @progname. Set it to 0 to skip the g_file_test().
:param predicate: if given, pass the file name to this function   for additional checks. This check is performed after the check for   @file_test_flags. You cannot omit both @file_test_flags and @predicate.
:param user_data: user data for @predicate function.
:return: the full path to the helper, if found, or %NULL if not found.
   The returned string is not owned by the caller, but later
   invocations of the function might overwrite it."""
    pass


def utils_format_variant_attributes(attributes: GLib.HashTable=None,
    attr_separator: str=None, key_value_separator: str=None) -> str:
    """Format attributes to a string.

:param attributes: a #GHashTable mapping attribute names to #GVariant values
:param attr_separator: the attribute separator character
:param key_value_separator: character separating key and values
:return: the string representing attributes, or %NULL
    in case there are no attributes"""
    pass


def utils_get_timestamp_msec() -> int:
    """Gets current time in milliseconds of CLOCK_BOOTTIME.

:return: time in milliseconds"""
    pass


def utils_hexstr2bin(hex: str=None) -> GLib.Bytes:
    """Converts a hexadecimal string @hex into an array of bytes.  The optional
separator ':' may be used between single or pairs of hexadecimal characters,
eg "00:11" or "0:1".  Any "0x" at the beginning of @hex is ignored.  @hex
may not start or end with ':'.

:param hex: a string of hexadecimal characters with optional ':' separators
:return: the converted bytes, or %NULL on error"""
    pass


def utils_hwaddr_atoba(asc: str=None, length: int=None) -> typing.Any:
    """Parses @asc and converts it to binary form in a #GByteArray. See
nm_utils_hwaddr_aton() if you don't want a #GByteArray.

:param asc: the ASCII representation of a hardware address
:param length: the expected length in bytes of the result
:return: a new #GByteArray, or %NULL if @asc couldn't be parsed"""
    pass


def utils_hwaddr_aton(asc: str=None, buffer: typing.Any=None, length: int=None
    ) -> int:
    """Parses @asc and converts it to binary form in @buffer.
Bytes in @asc can be separated by colons (:), or hyphens (-), but not mixed.

:param asc: the ASCII representation of a hardware address
:param buffer: buffer to store the result into
:param length: the expected length in bytes of the result and the size of the buffer in bytes.
:return: @buffer, or %NULL if @asc couldn't be parsed
   or would be shorter or longer than @length."""
    pass


def utils_hwaddr_canonical(asc: str=None, length: gssize=None) -> str:
    """Parses @asc to see if it is a valid hardware address of the given
length, and if so, returns it in canonical form (uppercase, with
leading 0s as needed, and with colons rather than hyphens).

:param asc: the ASCII representation of a hardware address
:param length: the length of address that @asc is expected to convert to   (or -1 to accept any length up to %NM_UTILS_HWADDR_LEN_MAX)
:return: the canonicalized address if @asc appears to
   be a valid hardware address of the indicated length, %NULL if not."""
    pass


def utils_hwaddr_len(type: int=None) -> int:
    """Returns the length in octets of a hardware address of type @type.

Before 1.28, it was an error to call this function with any value other than
<literal>ARPHRD_ETHER</literal> or <literal>ARPHRD_INFINIBAND</literal>.

:param type: the type of address; either <literal>ARPHRD_ETHER</literal> or <literal>ARPHRD_INFINIBAND</literal>
:return: the length or zero if the type is unrecognized."""
    pass


def utils_hwaddr_matches(hwaddr1: typing.Any=None, hwaddr1_len: gssize=None,
    hwaddr2: typing.Any=None, hwaddr2_len: gssize=None) -> bool:
    """Generalized hardware address comparison function. Tests if @hwaddr1 and
@hwaddr2 "equal" (or more precisely, "equivalent"), with several advantages
over a simple memcmp():

  1. If @hwaddr1_len or @hwaddr2_len is -1, then the corresponding address is
     assumed to be ASCII rather than binary, and will be converted to binary
     before being compared.

  2. If @hwaddr1 or @hwaddr2 is %NULL, it is treated instead as though it was
     a zero-filled buffer @hwaddr1_len or @hwaddr2_len bytes long.

  3. If @hwaddr1 and @hwaddr2 are InfiniBand hardware addresses (that is, if
     they are <literal>INFINIBAND_ALEN</literal> bytes long in binary form)
     then only the last 8 bytes are compared, since those are the only bytes
     that actually identify the hardware. (The other 12 bytes will change
     depending on the configuration of the InfiniBand fabric that the device
     is connected to.)

If a passed-in ASCII hardware address cannot be parsed, or would parse to an
address larger than %NM_UTILS_HWADDR_LEN_MAX, then it will silently fail to
match. (This means that externally-provided address strings do not need to be
sanity-checked before comparing them against known good addresses; they are
guaranteed to not match if they are invalid.)

:param hwaddr1: pointer to a binary or ASCII hardware address, or %NULL
:param hwaddr1_len: size of @hwaddr1, or -1 if @hwaddr1 is ASCII
:param hwaddr2: pointer to a binary or ASCII hardware address, or %NULL
:param hwaddr2_len: size of @hwaddr2, or -1 if @hwaddr2 is ASCII
:return: %TRUE if @hwaddr1 and @hwaddr2 are equivalent, %FALSE if they are
   different (or either of them is invalid)."""
    pass


def utils_hwaddr_ntoa(addr: typing.Any=None, length: int=None) -> str:
    """Converts @addr to textual form.

:param addr: a binary hardware address
:param length: the length of @addr
:return: the textual form of @addr"""
    pass


def utils_hwaddr_valid(asc: str=None, length: gssize=None) -> bool:
    """Parses @asc to see if it is a valid hardware address of the given
length.

:param asc: the ASCII representation of a hardware address
:param length: the length of address that @asc is expected to convert to   (or -1 to accept any length up to %NM_UTILS_HWADDR_LEN_MAX)
:return: %TRUE if @asc appears to be a valid hardware address
   of the indicated length, %FALSE if not."""
    pass


def utils_iface_valid_name(name: str=None) -> bool:
    """Validate the network interface name.

:param name: Name of interface
:return: %TRUE if interface name is valid, otherwise %FALSE is returned.  Before 1.20, this function did not accept %NULL as @name argument. If you
   want to run against older versions of libnm, don't pass %NULL."""
    pass


def utils_inet4_ntop(inaddr: int=None, dst: str=None) -> str:
    """Wrapper for inet_ntop.

:param inaddr: the address that should be converted to string.
:param dst: the destination buffer, it must contain at least  <literal>INET_ADDRSTRLEN</literal> or %NM_INET_ADDRSTRLEN  characters. If set to %NULL, it will return a pointer to an internal, static  buffer (shared with nm_utils_inet6_ntop()).  Beware, that the internal  buffer will be overwritten with ever new call of nm_utils_inet4_ntop() or  nm_utils_inet6_ntop() that does not provide its own @dst buffer. Since  1.28, the internal buffer is thread local and thus thread safe. Before  it was not thread safe. When in doubt, pass your own  @dst buffer to avoid these issues.
:return: the input buffer @dst, or a pointer to an  internal, static buffer. This function cannot fail."""
    pass


def utils_inet6_ntop(in6addr: typing.Any=None, dst: str=None) -> str:
    """Wrapper for inet_ntop.

:param in6addr: the address that should be converted to string.
:param dst: the destination buffer, it must contain at least  <literal>INET6_ADDRSTRLEN</literal> or %NM_INET_ADDRSTRLEN  characters. If set to %NULL, it will return a pointer to an internal, static  buffer (shared with nm_utils_inet4_ntop()).  Beware, that the internal  buffer will be overwritten with ever new call of nm_utils_inet4_ntop() or  nm_utils_inet6_ntop() that does not provide its own @dst buffer. Since  1.28, the internal buffer is thread local and thus thread safe. Before  it was not thread safe. When in doubt, pass your own  @dst buffer to avoid these issues.
:return: the input buffer @dst, or a pointer to an  internal, static buffer. %NULL is not allowed as @in6addr,  otherwise, this function cannot fail."""
    pass


def utils_ip4_addresses_from_variant(value: GLib.Variant=None, out_gateway:
    str=None) -> typing.Any:
    """Utility function to convert a #GVariant of type 'aau' representing a list of
NetworkManager IPv4 addresses (which are tuples of address, prefix, and
gateway) into a #GPtrArray of #NMIPAddress objects. The "gateway" field of
the first address (if set) will be returned in @out_gateway; the "gateway" fields
of the other addresses are ignored. Note that invalid addresses are discarded
but the valid addresses are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'aau'
:param out_gateway: on return, will   contain the IP gateway
:return: a newly allocated
   #GPtrArray of #NMIPAddress objects"""
    pass


def utils_ip4_addresses_to_variant(addresses: typing.Any=None, gateway: str
    =None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPAddress objects representing
IPv4 addresses into a #GVariant of type 'aau' representing an array of
NetworkManager IPv4 addresses (which are tuples of address, prefix, and
gateway). The "gateway" field of the first address will get the value of
@gateway (if non-%NULL). In all of the other addresses, that field will be 0.

:param addresses: an array of #NMIPAddress objects
:param gateway: the gateway IP address
:return: a new floating #GVariant representing @addresses."""
    pass


def utils_ip4_dns_from_variant(value: GLib.Variant=None) -> str:
    """Utility function to convert a #GVariant of type 'au' representing a list of
IPv4 addresses into an array of IP address strings.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'au'
:return: a %NULL-terminated array of IP address strings."""
    pass


def utils_ip4_dns_to_variant(dns: str=None) -> GLib.Variant:
    """Utility function to convert an array of IP address strings int a #GVariant of
type 'au' representing an array of IPv4 addresses.

:param dns: an array of IP address strings
:return: a new floating #GVariant representing @dns."""
    pass


def utils_ip4_get_default_prefix(ip: int=None) -> int:
    """When the Internet was originally set up, various ranges of IP addresses were
segmented into three network classes: A, B, and C.  This function will return
a prefix that is associated with the IP address specified defining where it
falls in the predefined classes.

:param ip: an IPv4 address (in network byte order)
:return: the default class prefix for the given IP"""
    pass


def utils_ip4_netmask_to_prefix(netmask: int=None) -> int:
    """

:param netmask: an IPv4 netmask in network byte order.   Usually the netmask has all leading bits up to the prefix   set so that the netmask is identical to having the first   prefix bits of the address set.   If that is not the case and there are "holes" in the   mask, the prefix is determined based on the lowest bit   set.
:return: the CIDR prefix represented by the netmask"""
    pass


def utils_ip4_prefix_to_netmask(prefix: int=None) -> int:
    """

:param prefix: a CIDR prefix, must be not larger than 32.
:return: the netmask represented by the prefix, in network byte order"""
    pass


def utils_ip4_routes_from_variant(value: GLib.Variant=None) -> typing.Any:
    """Utility function to convert a #GVariant of type 'aau' representing an array
of NetworkManager IPv4 routes (which are tuples of route, prefix, next hop,
and metric) into a #GPtrArray of #NMIPRoute objects. Note that invalid routes
are discarded but the valid routes are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: #GVariant of type 'aau'
:return: a newly allocated
   #GPtrArray of #NMIPRoute objects"""
    pass


def utils_ip4_routes_to_variant(routes: typing.Any=None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPRoute objects representing
IPv4 routes into a #GVariant of type 'aau' representing an array of
NetworkManager IPv4 routes (which are tuples of route, prefix, next hop, and
metric).

:param routes: an array of #NMIP4Route objects
:return: a new floating #GVariant representing @routes."""
    pass


def utils_ip6_addresses_from_variant(value: GLib.Variant=None, out_gateway:
    str=None) -> typing.Any:
    """Utility function to convert a #GVariant of type 'a(ayuay)' representing a
list of NetworkManager IPv6 addresses (which are tuples of address, prefix,
and gateway) into a #GPtrArray of #NMIPAddress objects. The "gateway" field
of the first address (if set) will be returned in @out_gateway; the "gateway"
fields of the other addresses are ignored. Note that invalid addresses are
discarded but the valid addresses are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'a(ayuay)'
:param out_gateway: on return, will   contain the IP gateway
:return: a newly allocated
   #GPtrArray of #NMIPAddress objects"""
    pass


def utils_ip6_addresses_to_variant(addresses: typing.Any=None, gateway: str
    =None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPAddress objects representing
IPv6 addresses into a #GVariant of type 'a(ayuay)' representing an array of
NetworkManager IPv6 addresses (which are tuples of address, prefix, and
gateway).  The "gateway" field of the first address will get the value of
@gateway (if non-%NULL). In all of the other addresses, that field will be
all 0s.

:param addresses: an array of #NMIPAddress objects
:param gateway: the gateway IP address
:return: a new floating #GVariant representing @addresses."""
    pass


def utils_ip6_dns_from_variant(value: GLib.Variant=None) -> str:
    """Utility function to convert a #GVariant of type 'aay' representing a list of
IPv6 addresses into an array of IP address strings. Each "ay" entry must be
a IPv6 address in binary form (16 bytes long). Invalid entries are silently
ignored.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'aay'
:return: a %NULL-terminated array of IP address strings."""
    pass


def utils_ip6_dns_to_variant(dns: str=None) -> GLib.Variant:
    """Utility function to convert an array of IP address strings int a #GVariant of
type 'aay' representing an array of IPv6 addresses.

If a string cannot be parsed, it will be silently ignored.

:param dns: an array of IP address strings
:return: a new floating #GVariant representing @dns."""
    pass


def utils_ip6_routes_from_variant(value: GLib.Variant=None) -> typing.Any:
    """Utility function to convert a #GVariant of type 'a(ayuayu)' representing an
array of NetworkManager IPv6 routes (which are tuples of route, prefix, next
hop, and metric) into a #GPtrArray of #NMIPRoute objects. Note that invalid
routes are ignored but the valid ones are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: #GVariant of type 'a(ayuayu)'
:return: a newly allocated
   #GPtrArray of #NMIPRoute objects"""
    pass


def utils_ip6_routes_to_variant(routes: typing.Any=None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPRoute objects representing
IPv6 routes into a #GVariant of type 'a(ayuayu)' representing an array of
NetworkManager IPv6 routes (which are tuples of route, prefix, next hop, and
metric).

:param routes: an array of #NMIPRoute objects
:return: a new floating #GVariant representing @routes."""
    pass


def utils_ip_addresses_from_variant(value: GLib.Variant=None, family: int=None
    ) -> typing.Any:
    """Utility function to convert a #GVariant representing a list of new-style
NetworkManager IPv4 or IPv6 addresses (as described in the documentation for
nm_utils_ip_addresses_to_variant()) into a #GPtrArray of #NMIPAddress
objects. Note that invalid addresses are discarded but the valid addresses
are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'aa{sv}'
:param family: an IP address family
:return: a newly allocated
   #GPtrArray of #NMIPAddress objects"""
    pass


def utils_ip_addresses_to_variant(addresses: typing.Any=None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPAddress objects representing
IPv4 or IPv6 addresses into a #GVariant of type 'aa{sv}' representing an
array of new-style NetworkManager IP addresses. All addresses will include
"address" (an IP address string), and "prefix" (a uint). Some addresses may
include additional attributes.

:param addresses: an array of #NMIPAddress objects
:return: a new floating #GVariant representing @addresses."""
    pass


def utils_ip_routes_from_variant(value: GLib.Variant=None, family: int=None
    ) -> typing.Any:
    """Utility function to convert a #GVariant representing a list of new-style
NetworkManager IPv4 or IPv6 addresses (as described in the documentation for
nm_utils_ip_routes_to_variant()) into a #GPtrArray of #NMIPRoute objects.
Invalid routes are discarded but the valid routes are still returned.

Since 1.46, an empty list is returned if the variant type is not valid
(before it was checked as assertion)

:param value: a #GVariant of type 'aa{sv}'
:param family: an IP address family
:return: a newly allocated
   #GPtrArray of #NMIPRoute objects"""
    pass


def utils_ip_routes_to_variant(routes: typing.Any=None) -> GLib.Variant:
    """Utility function to convert a #GPtrArray of #NMIPRoute objects representing
IPv4 or IPv6 routes into a #GVariant of type 'aa{sv}' representing an array
of new-style NetworkManager IP routes. All routes will include "dest" (an IP
address string), "prefix" (an uint) and optionally "next-hop" (an IP address
string) and "metric" (an uint). Some routes may include additional attributes.
Note that invalid routes are discarded and only a warning is emitted, but the
valid routes are still returned.

:param routes: an array of #NMIPRoute objects
:return: a new floating #GVariant representing @routes."""
    pass


def utils_ipaddr_valid(family: int=None, ip: str=None) -> bool:
    """Checks if @ip contains a valid IP address of the given family.

:param family: <literal>AF_INET</literal> or <literal>AF_INET6</literal>, or   <literal>AF_UNSPEC</literal> to accept either
:param ip: an IP address
:return: %TRUE or %FALSE"""
    pass


def utils_is_empty_ssid(ssid: typing.Any=None, len: int=None) -> bool:
    """Different manufacturers use different mechanisms for not broadcasting the
AP's SSID.  This function attempts to detect blank/empty SSIDs using a
number of known SSID-cloaking methods.

:param ssid: pointer to a buffer containing the SSID data
:param len: length of the SSID data in @ssid
:return: %TRUE if the SSID is "empty", %FALSE if it is not"""
    pass


def utils_is_json_object(str: str=None) -> bool:
    """

:param str: the JSON string to test
:return: whether the passed string is valid JSON.
   If libnm is not compiled with libjansson support, this check will
   also return %TRUE for possibly invalid inputs. If that is a problem
   for you, you must validate the JSON yourself."""
    pass


def utils_is_uuid(str: str=None) -> bool:
    """Checks if @str is a UUID

:param str: a string that might be a UUID
:return: %TRUE if @str is a UUID, %FALSE if not  In older versions, nm_utils_is_uuid() did not accept %NULL as @str argument. Don't pass %NULL if you run against older versions of libnm."""
    pass


def utils_is_valid_iface_name(name: str=None) -> bool:
    """Validate the network interface name.

This function is a 1:1 copy of the kernel's interface validation
function in net/core/dev.c.

:param name: Name of interface
:return: %TRUE if interface name is valid, otherwise %FALSE is returned.  Before 1.20, this function did not accept %NULL as @name argument. If you
   want to run against older versions of libnm, don't pass %NULL."""
    pass


def utils_parse_variant_attributes(string: str=None, attr_separator: str=
    None, key_value_separator: str=None, ignore_unknown: bool=None, spec:
    VariantAttributeSpec=None) -> GLib.HashTable:
    """Parse attributes from a string.

:param string: the input string
:param attr_separator: the attribute separator character
:param key_value_separator: character separating key and values
:param ignore_unknown: whether unknown attributes should be ignored
:param spec: the attribute format specifiers
:return: a #GHashTable mapping attribute names to #GVariant values. Warning: the variant are still floating references, owned by the hash table. If you take a reference, ensure to sink the one of the hash table first."""
    pass


def utils_print(output_mode: int=None, msg: str=None) -> None:
    """The only purpose of this function is to give access to g_print()
or g_printerr() from pygobject. libnm can do debug logging by
setting LIBNM_CLIENT_DEBUG and uses thereby g_printerr() or
g_print(). A plain "print()" function in python is not in sync
with these functions (it implements additional buffering). By
using nm_utils_print(), the same logging mechanisms can be used.

LIBNM_CLIENT_DEBUG is a list of keywords separated by commas. The keyword
"trace" enables printing messages of the lowest up to the highest severity.
Likewise, the severities "debug", "warn" ("warning") and "error" are honored
in similar way. Setting the flags "ERROR" or "WARN" ("WARNING") implies that
respective levels are enabled, but also are ERROR messages printed with
g_critical() and WARN messages with g_warning(). Together with G_DEBUG="fatal-warnings"
or G_DEBUG="fatal-critical" this can be used to abort the program on errors.
Note that all &lt;error&gt; messages imply an unexpected data on the D-Bus API
(due to a bug). &lt;warn&gt; also implies unexepected data, but that can happen
when using different versions of libnm and daemon. For testing, it is
good to turn these into assertions.

By default, messages are printed to stderr, unless LIBNM_CLIENT_DEBUG
contains "stdout" flag. Also, libnm honors LIBNM_CLIENT_DEBUG_FILE
environment. If this is set to a filename pattern (accepting "%%p" for the
process ID), then the debug log is written to that file instead of
stderr/stdout. With @output_mode zero, the same location will be written.

LIBNM_CLIENT_DEBUG_FILE is supported since 1.44. "ERROR", "WARN" and "WARNING"
are supported since 1.46.

:param output_mode: if 1 it uses g_print(). If 2, it uses g_printerr().   If 0, it uses the same output as internal libnm debug logging   does. That is, depending on LIBNM_CLIENT_DEBUG's "stdout" flag   it uses g_print() or g_printerr() and if LIBNM_CLIENT_DEBUG_FILE is   set, it writes the output to file instead
:param msg: the message to print. The function does not append   a trailing newline.
:return: """
    pass


def utils_same_ssid(ssid1: typing.Any=None, len1: int=None, ssid2:
    typing.Any=None, len2: int=None, ignore_trailing_null: bool=None) -> bool:
    """Earlier versions of the Linux kernel added a NULL byte to the end of the
SSID to enable easy printing of the SSID on the console or in a terminal,
but this behavior was problematic (SSIDs are simply byte arrays, not strings)
and thus was changed.  This function compensates for that behavior at the
cost of some compatibility with odd SSIDs that may legitimately have trailing
NULLs, even though that is functionally pointless.

:param ssid1: the first SSID to compare
:param len1: length of the SSID data in @ssid1
:param ssid2: the second SSID to compare
:param len2: length of the SSID data in @ssid2
:param ignore_trailing_null: %TRUE to ignore one trailing NULL byte
:return: %TRUE if the SSIDs are the same, %FALSE if they are not"""
    pass


def utils_security_valid(type: UtilsSecurityType=None, wifi_caps:
    DeviceWifiCapabilities=None, have_ap: bool=None, adhoc: bool=None,
    ap_flags: NM80211ApFlags=None, ap_wpa: NM80211ApSecurityFlags=None, ap_rsn:
    NM80211ApSecurityFlags=None) -> bool:
    """Given a set of device capabilities, and a desired security type to check
against, determines whether the combination of device, desired security
type, and AP capabilities intersect.

NOTE: this function cannot handle checking security for AP/Hotspot mode;
use nm_utils_ap_mode_security_valid() instead.

:param type: the security type to check AP flags and device capabilities against, e.g. #NMU_SEC_STATIC_WEP
:param wifi_caps: bitfield of the capabilities of the specific Wi-Fi device, e.g. #NM_WIFI_DEVICE_CAP_CIPHER_WEP40
:param have_ap: whether the @ap_flags, @ap_wpa, and @ap_rsn arguments are valid
:param adhoc: whether the capabilities being tested are from an Ad-Hoc AP (IBSS)
:param ap_flags: bitfield of AP capabilities, e.g. #NM_802_11_AP_FLAGS_PRIVACY
:param ap_wpa: bitfield of AP capabilities derived from the AP's WPA beacon, e.g. (#NM_802_11_AP_SEC_PAIR_TKIP | #NM_802_11_AP_SEC_KEY_MGMT_PSK)
:param ap_rsn: bitfield of AP capabilities derived from the AP's RSN/WPA2 beacon, e.g. (#NM_802_11_AP_SEC_PAIR_CCMP | #NM_802_11_AP_SEC_PAIR_TKIP)
:return: %TRUE if the device capabilities and AP capabilities intersect and are compatible with the desired @type, %FALSE if they are not"""
    pass


def utils_sriov_vf_from_str(str: str=None) -> SriovVF:
    """Converts a string to a SR-IOV virtual function object.

:param str: the input string
:return: the virtual function object"""
    pass


def utils_sriov_vf_to_str(vf: SriovVF=None, omit_index: bool=None) -> str:
    """Converts a SR-IOV virtual function object to its string representation.

:param vf: the %NMSriovVF
:param omit_index: if %TRUE, the VF index will be omitted from output string
:return: a newly allocated string or %NULL on error"""
    pass


def utils_ssid_to_utf8(ssid: typing.Any=None, len: int=None) -> str:
    """Wi-Fi SSIDs are byte arrays, they are _not_ strings.  Thus, an SSID may
contain embedded NULLs and other unprintable characters.  Often it is
useful to print the SSID out for debugging purposes, but that should be the
_only_ use of this function.  Do not use this function for any persistent
storage of the SSID, since the printable SSID returned from this function
cannot be converted back into the real SSID of the access point.

This function does almost everything humanly possible to convert the input
into a printable UTF-8 string, using roughly the following procedure:

1) if the input data is already UTF-8 safe, no conversion is performed
2) attempts to get the current system language from the LANG environment
   variable, and depending on the language, uses a table of alternative
   encodings to try.  For example, if LANG=hu_HU, the table may first try
   the ISO-8859-2 encoding, and if that fails, try the Windows-1250 encoding.
   If all fallback encodings fail, replaces non-UTF-8 characters with '?'.
3) If the system language was unable to be determined, falls back to the
   ISO-8859-1 encoding, then to the Windows-1251 encoding.
4) If step 3 fails, replaces non-UTF-8 characters with '?'.

Again, this function should be used for debugging and display purposes
_only_.

:param ssid: pointer to a buffer containing the SSID data
:param len: length of the SSID data in @ssid
:return: an allocated string containing a UTF-8 representation of the SSID, which must be freed by the caller using g_free(). Returns %NULL on errors."""
    pass


def utils_tc_action_from_str(str: str=None) -> TCAction:
    """Parses the tc style string action representation of the queueing
discipline to a %NMTCAction instance. Supports a subset of the tc language.

:param str: the string representation of a action
:return: the %NMTCAction or %NULL"""
    pass


def utils_tc_action_to_str(action: TCAction=None) -> str:
    """Turns the %NMTCAction into a tc style string representation of the queueing
discipline.

:param action: the %NMTCAction
:return: formatted string or %NULL"""
    pass


def utils_tc_qdisc_from_str(str: str=None) -> TCQdisc:
    """Parses the tc style string qdisc representation of the queueing
discipline to a %NMTCQdisc instance. Supports a subset of the tc language.

:param str: the string representation of a qdisc
:return: the %NMTCQdisc or %NULL"""
    pass


def utils_tc_qdisc_to_str(qdisc: TCQdisc=None) -> str:
    """Turns the %NMTCQdisc into a tc style string representation of the queueing
discipline.

:param qdisc: the %NMTCQdisc
:return: formatted string or %NULL"""
    pass


def utils_tc_tfilter_from_str(str: str=None) -> TCTfilter:
    """Parses the tc style string tfilter representation of the queueing
discipline to a %NMTCTfilter instance. Supports a subset of the tc language.

:param str: the string representation of a tfilter
:return: the %NMTCTfilter or %NULL"""
    pass


def utils_tc_tfilter_to_str(tfilter: TCTfilter=None) -> str:
    """Turns the %NMTCTfilter into a tc style string representation of the queueing
discipline.

:param tfilter: the %NMTCTfilter
:return: formatted string or %NULL"""
    pass


def utils_uuid_generate() -> str:
    """

:return: a newly allocated UUID suitable for use as the #NMSettingConnection object's #NMSettingConnection:id: property.  Should be freed with g_free()"""
    pass


def utils_version() -> int:
    """

:return: the version ID of the libnm version. That is, the %NM_VERSION
   at runtime."""
    pass


def utils_wep_key_valid(key: str=None, wep_type: WepKeyType=None) -> bool:
    """Checks if @key is a valid WEP key

:param key: a string that might be a WEP key
:param wep_type: the #NMWepKeyType type of the WEP key
:return: %TRUE if @key is a WEP key, %FALSE if not"""
    pass


def utils_wifi_2ghz_freqs() -> int:
    """Utility function to return 2.4 GHz Wi-Fi frequencies (802.11bg band).

:return: zero-terminated array of frequencies numbers (in MHz)"""
    pass


def utils_wifi_5ghz_freqs() -> int:
    """Utility function to return 5 GHz Wi-Fi frequencies (802.11a band).

:return: zero-terminated array of frequencies numbers (in MHz)"""
    pass


def utils_wifi_channel_to_freq(channel: int=None, band: str=None) -> int:
    """Utility function to translate a Wi-Fi channel to its corresponding frequency.

:param channel: channel
:param band: frequency band for wireless ("a" or "bg")
:return: the frequency represented by the channel of the band,
          or -1 when the freq is invalid, or 0 when the band
          is invalid"""
    pass


def utils_wifi_find_next_channel(channel: int=None, direction: int=None,
    band: str=None) -> int:
    """Utility function to find out next/previous Wi-Fi channel for a channel.

:param channel: current channel
:param direction: whether going downward (0 or less) or upward (1 or more)
:param band: frequency band for wireless ("a" or "bg")
:return: the next channel in the specified direction or 0"""
    pass


def utils_wifi_freq_to_channel(freq: int=None) -> int:
    """Utility function to translate a Wi-Fi frequency to its corresponding channel.

:param freq: frequency
:return: the channel represented by the frequency or 0"""
    pass


def utils_wifi_is_channel_valid(channel: int=None, band: str=None) -> bool:
    """Utility function to verify Wi-Fi channel validity.

:param channel: channel
:param band: frequency band for wireless ("a" or "bg")
:return: %TRUE or %FALSE"""
    pass


def utils_wifi_strength_bars(strength: int=None) -> str:
    """Converts @strength into a 4-character-wide graphical representation of
strength suitable for printing to stdout.

Previous versions used to take a guess at the terminal type and possibly
return a wide UTF-8 encoded string. Now it always returns a 7-bit
clean strings of one to 0 to 4 asterisks. Users that actually need
the functionality are encouraged to make their implementations instead.

:param strength: the access point strength, from 0 to 100
:return: the graphical representation of the access point strength"""
    pass


def utils_wpa_psk_valid(psk: str=None) -> bool:
    """Checks if @psk is a valid WPA PSK

:param psk: a string that might be a WPA PSK
:return: %TRUE if @psk is a WPA PSK, %FALSE if not"""
    pass


def vpn_editor_plugin_load(plugin_name: str=None, check_service: str=None
    ) -> VpnEditorPlugin:
    """Load the shared library @plugin_name and create a new
#NMVpnEditorPlugin instance via the #NMVpnEditorPluginFactory
function.

This is similar to nm_vpn_editor_plugin_load_from_file(), but
it does no validation of the plugin name, instead passes it directly
to dlopen(). If you have the full path to a plugin file,
nm_vpn_editor_plugin_load_from_file() is preferred.

:param plugin_name: The name of the shared library to load.  This path will be directly passed to dlopen() without  further checks.
:param check_service: if not-null, check that the loaded plugin advertises  the given service.
:return: a new plugin instance or %NULL on error."""
    pass


def vpn_editor_plugin_load_from_file(plugin_name: str=None, check_service:
    str=None, check_owner: int=None, check_file: UtilsCheckFilePredicate=
    None, user_data: typing.Any=None) -> VpnEditorPlugin:
    """Load the shared library @plugin_name and create a new
#NMVpnEditorPlugin instance via the #NMVpnEditorPluginFactory
function.

If @plugin_name is not an absolute path name, it assumes the file
is in the plugin directory of NetworkManager. In any case, the call
will do certain checks on the file before passing it to dlopen.
A consequence for that is, that you cannot omit the ".so" suffix
as you could for nm_vpn_editor_plugin_load().

:param plugin_name: The path or name of the shared library to load.  The path must either be an absolute filename to an existing file.  Alternatively, it can be the name (without path) of a library in the  plugin directory of NetworkManager.
:param check_service: if not-null, check that the loaded plugin advertises  the given service.
:param check_owner: if non-negative, check whether the file is owned  by UID @check_owner or by root. In this case also check that  the file is not writable by anybody else.
:param check_file: optional callback to validate the file prior to   loading the shared library.
:param user_data: user data for @check_file
:return: a new plugin instance or %NULL on error."""
    pass


def vpn_plugin_error_quark() -> GLib.Quark:
    """

:return: """
    pass


class AccessPointClass:
    """"""


class ActiveConnectionClass:
    """"""


class BridgeVlan:
    """"""

    def __init__(self, vid_start: int=None, vid_end: int=None) -> None:
        """Creates a new #NMBridgeVlan object for the given VLAN id range.
Setting @vid_end to 0 is equivalent to setting it to @vid_start
and creates a single-id VLAN.

Since 1.42, ref-counting of #NMBridgeVlan is thread-safe.

:param self: 
:param vid_start: the start VLAN id, must be between 1 and 4094.
:param vid_end: the end VLAN id, must be 0 or between @vid_start and 4094.
:return: """
        pass

    @staticmethod
    def new(vid_start: int=None, vid_end: int=None) -> BridgeVlan:
        """Creates a new #NMBridgeVlan object for the given VLAN id range.
Setting @vid_end to 0 is equivalent to setting it to @vid_start
and creates a single-id VLAN.

Since 1.42, ref-counting of #NMBridgeVlan is thread-safe.

:param vid_start: the start VLAN id, must be between 1 and 4094.
:param vid_end: the end VLAN id, must be 0 or between @vid_start and 4094.
:return: the new #NMBridgeVlan object."""
        pass

    def cmp(self, b: BridgeVlan=None) -> int:
        """Compare two bridge VLAN objects.

:param self: a #NMBridgeVlan
:param b: another #NMBridgeVlan
:return: zero of the two instances are equivalent or
   a non-zero integer otherwise. This defines a total ordering
   over the VLANs. Whether a VLAN is sealed or not does not
   affect the comparison."""
        pass

    def get_vid_range(self, vid_start: int=None, vid_end: int=None) -> bool:
        """Gets the VLAN id range.

:param self: the #NMBridgeVlan
:param vid_start: location to store the VLAN id range start.
:param vid_end: location to store the VLAN id range end
:return: %TRUE is the VLAN specifies a range, %FALSE if it is a single-id VLAN."""
        pass

    def is_pvid(self) -> bool:
        """Returns whether the VLAN is the PVID for the port.

:param self: the #NMBridgeVlan
:return: %TRUE if the VLAN is the PVID"""
        pass

    def is_sealed(self) -> bool:
        """

:param self: the #NMBridgeVlan instance
:return: whether @self is sealed or not."""
        pass

    def is_untagged(self) -> bool:
        """Returns whether the VLAN is untagged.

:param self: the #NMBridgeVlan
:return: %TRUE if the VLAN is untagged, %FALSE otherwise"""
        pass

    def new_clone(self) -> BridgeVlan:
        """

:param self: the #NMBridgeVlan instance to copy
:return: a clone of @vlan. This instance
   is always unsealed."""
        pass

    def ref(self) -> BridgeVlan:
        """Increases the reference count of the object.

:param self: the #NMBridgeVlan
:return: the input argument @vlan object.  Since 1.42, ref-counting of #NMBridgeVlan is thread-safe."""
        pass

    def seal(self) -> None:
        """Seal the #NMBridgeVlan instance. Afterwards, it is a bug
to call all functions that modify the instance (except ref/unref).
A sealed instance cannot be unsealed again, but you can create
an unsealed copy with nm_bridge_vlan_new_clone().

:param self: the #NMBridgeVlan instance
:return: """
        pass

    def set_pvid(self, value: bool=None) -> None:
        """Change the value of the PVID property of the VLAN. It
is invalid to set the value to %TRUE for non-single-id
VLANs.

:param self: the #NMBridgeVlan
:param value: the new value
:return: """
        pass

    def set_untagged(self, value: bool=None) -> None:
        """Change the value of the untagged property of the VLAN.

:param self: the #NMBridgeVlan
:param value: the new value
:return: """
        pass

    def to_str(self) -> str:
        """Convert a %NMBridgeVlan to a string.

:param self: the %NMBridgeVlan
:return: formatted string or %NULL"""
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero the object will be destroyed.

Since 1.42, ref-counting of #NMBridgeVlan is thread-safe.

:param self: the #NMBridgeVlan
:return: """
        pass

    @staticmethod
    def from_str(str: str=None) -> BridgeVlan:
        """Parses the string representation of the queueing
discipline to a %NMBridgeVlan instance.

:param str: the string representation of a bridge VLAN
:return: the %NMBridgeVlan or %NULL"""
        pass


class CheckpointClass:
    """"""


class Client(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """NMClient contains a cache of the objects of NetworkManager's D-Bus API.
It uses #GMainContext and #GDBusConnection for that and registers to
D-Bus signals. That means, when iterating the associated #GMainContext,
D-Bus signals gets processed and the #NMClient instance updates and
emits #GObject signals."""

    def __init__(self, cancellable: Gio.Cancellable=None) -> None:
        """Creates a new #NMClient synchronously.

Note that this will block until a NMClient instance is fully initialized.
This does nothing beside calling g_initable_new(). You are free to call
g_initable_new() or g_object_new()/g_initable_init() directly for more
control, to set GObject properties or get access to the NMClient instance
while it is still initializing.

Using the synchronous initialization creates an #NMClient instance
that uses an internal #GMainContext. This context is invisible to the
user. This introduces an additional overhead that is payed not
only during object initialization, but for the entire lifetime of
this object.
Also, due to this internal #GMainContext, the events are no longer
in sync with other messages from #GDBusConnection (but all events
of the NMClient will themselves still be ordered).
For a serious program, you should therefore avoid these problems by
using g_async_initable_init_async() or nm_client_new_async() instead.
The sync initialization is still useful for simple scripts or interactive
testing for example via pygobject.

Creating an #NMClient instance can only fail for two reasons. First, if you didn't
provide a %NM_CLIENT_DBUS_CONNECTION and the call to g_bus_get()
fails. You can avoid that by using g_initable_new() directly and
set a D-Bus connection.
Second, if you cancelled the creation. If you do that, then note
that after the failure there might still be idle actions pending
which keep nm_client_get_main_context() alive. That means,
in that case you must continue iterating the context to avoid
leaks. See nm_client_get_context_busy_watcher().

Creating an #NMClient instance when NetworkManager is not running
does not cause a failure.

:param self: 
:param cancellable: a #GCancellable, or %NULL
:return: """
        pass

    @staticmethod
    def new(cancellable: Gio.Cancellable=None) -> Client:
        """Creates a new #NMClient synchronously.

Note that this will block until a NMClient instance is fully initialized.
This does nothing beside calling g_initable_new(). You are free to call
g_initable_new() or g_object_new()/g_initable_init() directly for more
control, to set GObject properties or get access to the NMClient instance
while it is still initializing.

Using the synchronous initialization creates an #NMClient instance
that uses an internal #GMainContext. This context is invisible to the
user. This introduces an additional overhead that is payed not
only during object initialization, but for the entire lifetime of
this object.
Also, due to this internal #GMainContext, the events are no longer
in sync with other messages from #GDBusConnection (but all events
of the NMClient will themselves still be ordered).
For a serious program, you should therefore avoid these problems by
using g_async_initable_init_async() or nm_client_new_async() instead.
The sync initialization is still useful for simple scripts or interactive
testing for example via pygobject.

Creating an #NMClient instance can only fail for two reasons. First, if you didn't
provide a %NM_CLIENT_DBUS_CONNECTION and the call to g_bus_get()
fails. You can avoid that by using g_initable_new() directly and
set a D-Bus connection.
Second, if you cancelled the creation. If you do that, then note
that after the failure there might still be idle actions pending
which keep nm_client_get_main_context() alive. That means,
in that case you must continue iterating the context to avoid
leaks. See nm_client_get_context_busy_watcher().

Creating an #NMClient instance when NetworkManager is not running
does not cause a failure.

:param cancellable: a #GCancellable, or %NULL
:return: a new #NMClient or NULL on an error"""
        pass

    @staticmethod
    def new_finish(result: Gio.AsyncResult=None) -> Client:
        """Gets the result of an nm_client_new_async() call.

:param result: a #GAsyncResult
:return: a new #NMClient, or %NULL on error"""
        pass

    @staticmethod
    def new_async(cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Creates a new #NMClient asynchronously.
@callback will be called when it is done. Use
nm_client_new_finish() to get the result.

This does nothing beside calling g_async_initable_new_async(). You are free to
call g_async_initable_new_async() or g_object_new()/g_async_initable_init_async()
directly for more control, to set GObject properties or get access to the NMClient
instance while it is still initializing.

Creating an #NMClient instance can only fail for two reasons. First, if you didn't
provide a %NM_CLIENT_DBUS_CONNECTION and the call to g_bus_get()
fails. You can avoid that by using g_async_initable_new_async() directly and
set a D-Bus connection.
Second, if you cancelled the creation. If you do that, then note
that after the failure there might still be idle actions pending
which keep nm_client_get_main_context() alive. That means,
in that case you must continue iterating the context to avoid
leaks. See nm_client_get_context_busy_watcher().

Creating an #NMClient instance when NetworkManager is not running
does not cause a failure.

:param cancellable: a #GCancellable, or %NULL
:param callback: callback to call when the client is created
:param user_data: data for @callback
:return: """
        pass

    @staticmethod
    def wait_shutdown_finish(result: Gio.AsyncResult=None) -> bool:
        """

:param result: a #GAsyncResult obtained from the #GAsyncReadyCallback passed to nm_client_wait_shutdown()
:return: %TRUE if waiting is complete successfully. In that case, all resources of the
   nmclient are wrapped up and released. This can only fail by user cancellation."""
        pass

    def activate_connection_async(self, connection: Connection=None, device:
        Device=None, specific_object: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Asynchronously starts a connection to a particular network using the
configuration settings from @connection and the network device @device.
Certain connection types also take a "specific object" which is the object
path of a connection- specific object, like an #NMAccessPoint for Wi-Fi
connections, or an #NMWimaxNsp for WiMAX connections, to which you wish to
connect.  If the specific object is not given, NetworkManager can, in some
cases, automatically determine which network to connect to given the settings
in @connection.

If @connection is not given for a device-based activation, NetworkManager
picks the best available connection for the device and activates it.

Note that the callback is invoked when NetworkManager has started activating
the new connection, not when it finishes. You can use the returned
#NMActiveConnection object (in particular, #NMActiveConnection:state) to
track the activation to its completion.

:param self: a #NMClient
:param connection: an #NMConnection
:param device: the #NMDevice
:param specific_object: the object path of a connection-type-specific   object this activation should use. This parameter is currently ignored for   wired and mobile broadband connections, and the value of %NULL should be used   (ie, no specific object).  For Wi-Fi or WiMAX connections, pass the object   path of a #NMAccessPoint or #NMWimaxNsp owned by @device, which you can   get using nm_object_get_path(), and which will be used to complete the   details of the newly added connection.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the activation has started
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def activate_connection_finish(self, result: Gio.AsyncResult=None
        ) -> ActiveConnection:
        """Gets the result of a call to nm_client_activate_connection_async().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: the new #NMActiveConnection on success, %NULL on
   failure, in which case @error will be set."""
        pass

    def add_and_activate_connection2(self, partial: Connection=None, device:
        Device=None, specific_object: str=None, options: GLib.Variant=None,
        cancellable: Gio.Cancellable=None, callback: Gio.AsyncReadyCallback
        =None, user_data: typing.Any=None) -> None:
        """Adds a new connection using the given details (if any) as a template,
automatically filling in missing settings with the capabilities of the given
device and specific object.  The new connection is then asynchronously
activated as with nm_client_activate_connection_async(). Cannot be used for
VPN connections at this time.

Note that the callback is invoked when NetworkManager has started activating
the new connection, not when it finishes. You can used the returned
#NMActiveConnection object (in particular, #NMActiveConnection:state) to
track the activation to its completion.

This is identical to nm_client_add_and_activate_connection_async() but takes
a further @options parameter. Currently, the following options are supported
by the daemon:
 * "persist": A string describing how the connection should be stored.
              The default is "disk", but it can be modified to "memory" (until
              the daemon quits) or "volatile" (will be deleted on disconnect).
 * "bind-activation": Bind the connection lifetime to something. The default is "none",
           meaning an explicit disconnect is needed. The value "dbus-client"
           means the connection will automatically be deactivated when the calling
           D-Bus client disappears from the system bus.

:param self: a #NMClient
:param partial: an #NMConnection to add; the connection may be   partially filled (or even %NULL) and will be completed by NetworkManager   using the given @device and @specific_object before being added
:param device: the #NMDevice
:param specific_object: the object path of a connection-type-specific   object this activation should use. This parameter is currently ignored for   wired and mobile broadband connections, and the value of %NULL should be used   (i.e., no specific object).  For Wi-Fi or WiMAX connections, pass the object   path of a #NMAccessPoint or #NMWimaxNsp owned by @device, which you can   get using nm_object_get_path(), and which will be used to complete the   details of the newly added connection.
:param options: a #GVariant containing a dictionary with options, or %NULL
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the activation has started
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def add_and_activate_connection2_finish(self, result: Gio.AsyncResult=
        None, out_result: GLib.Variant=None) -> ActiveConnection:
        """Gets the result of a call to nm_client_add_and_activate_connection2().

You can call nm_active_connection_get_connection() on the returned
#NMActiveConnection to find the path of the created #NMConnection.

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:param out_result: the output result   of type "a{sv}" returned by D-Bus' AddAndActivate2 call. Currently, no   output is implemented yet.
:return: the new #NMActiveConnection on success, %NULL on
   failure, in which case @error will be set."""
        pass

    def add_and_activate_connection_async(self, partial: Connection=None,
        device: Device=None, specific_object: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Adds a new connection using the given details (if any) as a template,
automatically filling in missing settings with the capabilities of the given
device and specific object.  The new connection is then asynchronously
activated as with nm_client_activate_connection_async(). Cannot be used for
VPN connections at this time.

Note that the callback is invoked when NetworkManager has started activating
the new connection, not when it finishes. You can used the returned
#NMActiveConnection object (in particular, #NMActiveConnection:state) to
track the activation to its completion.

:param self: a #NMClient
:param partial: an #NMConnection to add; the connection may be   partially filled (or even %NULL) and will be completed by NetworkManager   using the given @device and @specific_object before being added
:param device: the #NMDevice
:param specific_object: the object path of a connection-type-specific   object this activation should use. This parameter is currently ignored for   wired and mobile broadband connections, and the value of %NULL should be used   (ie, no specific object).  For Wi-Fi or WiMAX connections, pass the object   path of a #NMAccessPoint or #NMWimaxNsp owned by @device, which you can   get using nm_object_get_path(), and which will be used to complete the   details of the newly added connection.   If the variant is floating, it will be consumed.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the activation has started
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def add_and_activate_connection_finish(self, result: Gio.AsyncResult=None
        ) -> ActiveConnection:
        """Gets the result of a call to nm_client_add_and_activate_connection_async().

You can call nm_active_connection_get_connection() on the returned
#NMActiveConnection to find the path of the created #NMConnection.

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: the new #NMActiveConnection on success, %NULL on
   failure, in which case @error will be set."""
        pass

    def add_connection2(self, settings: GLib.Variant=None, flags:
        SettingsAddConnection2Flags=None, args: GLib.Variant=None,
        ignore_out_result: bool=None, cancellable: Gio.Cancellable=None,
        callback: Gio.AsyncReadyCallback=None, user_data: typing.Any=None
        ) -> None:
        """Call AddConnection2() D-Bus API asynchronously.

:param self: the %NMClient
:param settings: the "a{sa{sv}}" #GVariant with the content of the setting.
:param flags: the %NMSettingsAddConnection2Flags argument.
:param args: the "a{sv}" #GVariant with extra argument or %NULL   for no extra arguments.
:param ignore_out_result: this function wraps AddConnection2(), which has an   additional result "a{sv}" output parameter. By setting this to %TRUE,   you signal that you are not interested in that output parameter.   This allows the function to fall back to AddConnection() and AddConnectionUnsaved(),   which is interesting if you run against an older server version that does   not yet provide AddConnection2(). By setting this to %FALSE, the function   under the hood always calls AddConnection2().
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def add_connection2_finish(self, result: Gio.AsyncResult=None,
        out_result: GLib.Variant=None) -> RemoteConnection:
        """

:param self: the #NMClient
:param result: the #GAsyncResult
:param out_result: the output   #GVariant from AddConnection2().   If you care about the output result, then the "ignore_out_result"   parameter of nm_client_add_connection2() must not be set to %TRUE.
:return: on success, a pointer to the added
   #NMRemoteConnection."""
        pass

    def add_connection_async(self, connection: Connection=None,
        save_to_disk: bool=None, cancellable: Gio.Cancellable=None,
        callback: Gio.AsyncReadyCallback=None, user_data: typing.Any=None
        ) -> None:
        """Requests that the remote settings service add the given settings to a new
connection.  If @save_to_disk is %TRUE, the connection is immediately written
to disk; otherwise it is initially only stored in memory, but may be saved
later by calling the connection's nm_remote_connection_commit_changes()
method.

@connection is untouched by this function and only serves as a template of
the settings to add.  The #NMRemoteConnection object that represents what
NetworkManager actually added is returned to @callback when the addition
operation is complete.

Note that the #NMRemoteConnection returned in @callback may not contain
identical settings to @connection as NetworkManager may perform automatic
completion and/or normalization of connection properties.

:param self: the %NMClient
:param connection: the connection to add. Note that this object's settings will be   added, not the object itself
:param save_to_disk: whether to immediately save the connection to disk
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def add_connection_finish(self, result: Gio.AsyncResult=None
        ) -> RemoteConnection:
        """Gets the result of a call to nm_client_add_connection_async().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: the new #NMRemoteConnection on success, %NULL on
   failure, in which case @error will be set."""
        pass

    def check_connectivity(self, cancellable: Gio.Cancellable=None
        ) -> ConnectivityState:
        """Updates the network connectivity state and returns the (new)
current state. Contrast nm_client_get_connectivity(), which returns
the most recent known state without re-checking.

This is a blocking call; use nm_client_check_connectivity_async()
if you do not want to block.

:param self: an #NMClient
:param cancellable: a #GCancellable
:return: the (new) current connectivity state"""
        pass

    def check_connectivity_async(self, cancellable: Gio.Cancellable=None,
        callback: Gio.AsyncReadyCallback=None, user_data: typing.Any=None
        ) -> None:
        """Asynchronously updates the network connectivity state and invokes
@callback when complete. Contrast nm_client_get_connectivity(),
which (immediately) returns the most recent known state without
re-checking, and nm_client_check_connectivity(), which blocks.

:param self: an #NMClient
:param cancellable: a #GCancellable
:param callback: callback to call with the result
:param user_data: data for @callback.
:return: """
        pass

    def check_connectivity_finish(self, result: Gio.AsyncResult=None
        ) -> ConnectivityState:
        """Retrieves the result of an nm_client_check_connectivity_async()
call.

:param self: an #NMClient
:param result: the #GAsyncResult
:return: the (new) current connectivity state"""
        pass

    def checkpoint_adjust_rollback_timeout(self, checkpoint_path: str=None,
        add_timeout: int=None, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Resets the timeout for the checkpoint with path @checkpoint_path
to @timeout_add.

:param self: the %NMClient
:param checkpoint_path: a D-Bus path to a checkpoint
:param add_timeout: the timeout in seconds counting from now.   Set to zero, to disable the timeout.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def checkpoint_adjust_rollback_timeout_finish(self, result:
        Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_client_checkpoint_adjust_rollback_timeout().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success or %FALSE on failure."""
        pass

    def checkpoint_create(self, devices: typing.Any=None, rollback_timeout:
        int=None, flags: CheckpointCreateFlags=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Creates a checkpoint of the current networking configuration
for given interfaces. An empty @devices argument means all
devices. If @rollback_timeout is not zero, a rollback is
automatically performed after the given timeout.

:param self: the %NMClient
:param devices: a list of devices for which a   checkpoint should be created.
:param rollback_timeout: the rollback timeout in seconds
:param flags: creation flags
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def checkpoint_create_finish(self, result: Gio.AsyncResult=None
        ) -> Checkpoint:
        """Gets the result of a call to nm_client_checkpoint_create().

:param self: the #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: the new #NMCheckpoint on success, %NULL on
   failure, in which case @error will be set."""
        pass

    def checkpoint_destroy(self, checkpoint_path: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Destroys an existing checkpoint without performing a rollback.

:param self: the %NMClient
:param checkpoint_path: the D-Bus path for the checkpoint
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def checkpoint_destroy_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_client_checkpoint_destroy().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success or %FALSE on failure, in which case
   @error will be set."""
        pass

    def checkpoint_rollback(self, checkpoint_path: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Performs the rollback of a checkpoint before the timeout is reached.

:param self: the %NMClient
:param checkpoint_path: the D-Bus path to the checkpoint
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def checkpoint_rollback_finish(self, result: Gio.AsyncResult=None
        ) -> GLib.HashTable:
        """Gets the result of a call to nm_client_checkpoint_rollback().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: an hash table of
   devices and results. Devices are represented by their original
   D-Bus path; each result is a #NMRollbackResult."""
        pass

    def connectivity_check_get_available(self) -> bool:
        """Determine whether connectivity checking is available.  This
requires that the URI of a connectivity service has been set in the
configuration file.

:param self: a #NMClient
:return: %TRUE if connectivity checking is available."""
        pass

    def connectivity_check_get_enabled(self) -> bool:
        """Determine whether connectivity checking is enabled.

:param self: a #NMClient
:return: %TRUE if connectivity checking is enabled."""
        pass

    def connectivity_check_get_uri(self) -> str:
        """Get the URI that will be queried to determine if there is internet
connectivity.

:param self: a #NMClient
:return: the connectivity URI in use"""
        pass

    def connectivity_check_set_enabled(self, enabled: bool=None) -> None:
        """Enable or disable connectivity checking.  Note that if a
connectivity checking URI has not been configured, this will not
have any effect.

:param self: a #NMClient
:param enabled: %TRUE to enable connectivity checking
:return: """
        pass

    def dbus_call(self, object_path: str=None, interface_name: str=None,
        method_name: str=None, parameters: GLib.Variant=None, reply_type:
        GLib.VariantType=None, timeout_msec: int=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Call g_dbus_connection_call() on the current name owner with the specified
arguments. Most importantly, this invokes g_dbus_connection_call() with the
client's #GMainContext, so that the response is always in order with other
events D-Bus events. Of course, the call uses #GTask and will invoke the
callback on the current g_main_context_get_thread_default().

This API is merely a convenient wrapper for g_dbus_connection_call(). You can
also use g_dbus_connection_call() directly, with the same effect.

:param self: the #NMClient
:param object_path: path of remote object
:param interface_name: D-Bus interface to invoke method on
:param method_name: the name of the method to invoke
:param parameters: a #GVariant tuple with parameters for the method     or %NULL if not passing parameters
:param reply_type: the expected type of the reply (which will be a     tuple), or %NULL
:param timeout_msec: the timeout in milliseconds, -1 to use the default     timeout or %G_MAXINT for no timeout
:param cancellable: a #GCancellable or %NULL
:param callback: a #GAsyncReadyCallback to call when the request     is satisfied or %NULL if you don't care about the result of the     method invocation
:param user_data: the data to pass to @callback
:return: """
        pass

    def dbus_call_finish(self, result: Gio.AsyncResult=None) -> GLib.Variant:
        """Gets the result of a call to nm_client_dbus_call().

:param self: the #NMClient instance
:param result: the result passed to the #GAsyncReadyCallback
:return: the result #GVariant or %NULL on error."""
        pass

    def dbus_set_property(self, object_path: str=None, interface_name: str=
        None, property_name: str=None, value: GLib.Variant=None,
        timeout_msec: int=None, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Like nm_client_dbus_call() but calls "Set" on the standard "org.freedesktop.DBus.Properties"
D-Bus interface.

:param self: the #NMClient
:param object_path: path of remote object
:param interface_name: D-Bus interface for the property to set.
:param property_name: the name of the property to set
:param value: a #GVariant with the value to set.
:param timeout_msec: the timeout in milliseconds, -1 to use the default     timeout or %G_MAXINT for no timeout
:param cancellable: a #GCancellable or %NULL
:param callback: a #GAsyncReadyCallback to call when the request     is satisfied or %NULL if you don't care about the result of the     method invocation
:param user_data: the data to pass to @callback
:return: """
        pass

    def dbus_set_property_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_client_dbus_set_property().

:param self: the #NMClient instance
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success or %FALSE on failure."""
        pass

    def deactivate_connection(self, active: ActiveConnection=None,
        cancellable: Gio.Cancellable=None) -> bool:
        """Deactivates an active #NMActiveConnection.

:param self: a #NMClient
:param active: the #NMActiveConnection to deactivate
:param cancellable: a #GCancellable, or %NULL
:return: success or failure"""
        pass

    def deactivate_connection_async(self, active: ActiveConnection=None,
        cancellable: Gio.Cancellable=None, callback: Gio.AsyncReadyCallback
        =None, user_data: typing.Any=None) -> None:
        """Asynchronously deactivates an active #NMActiveConnection.

:param self: a #NMClient
:param active: the #NMActiveConnection to deactivate
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the deactivation has completed
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def deactivate_connection_finish(self, result: Gio.AsyncResult=None
        ) -> bool:
        """Gets the result of a call to nm_client_deactivate_connection_async().

:param self: a #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: success or failure"""
        pass

    def get_activating_connection(self) -> ActiveConnection:
        """Gets the #NMActiveConnection corresponding to a
currently-activating connection that is expected to become the new
#NMClient:primary-connection upon successful activation.

:param self: an #NMClient
:return: the appropriate #NMActiveConnection, if any."""
        pass

    def get_active_connections(self) -> typing.Any:
        """Gets the active connections.

:param self: a #NMClient
:return: a #GPtrArray  containing all the active #NMActiveConnections. The returned array is owned by the client and should not be modified."""
        pass

    def get_all_devices(self) -> typing.Any:
        """Gets both real devices and device placeholders (eg, software devices which
do not currently exist, but could be created automatically by NetworkManager
if one of their NMDevice::ActivatableConnections was activated).  Use
nm_device_is_real() to determine whether each device is a real device or
a placeholder.

Use nm_device_get_type() or the NM_IS_DEVICE_XXXX() functions to determine
what kind of device each member of the returned array is, and then you may
use device-specific methods such as nm_device_ethernet_get_hw_address().

:param self: a #NMClient
:return: a #GPtrArray containing all the #NMDevices.  The returned array is owned by the #NMClient object and should not be modified."""
        pass

    def get_capabilities(self, length: int=None) -> typing.Any:
        """

:param self: the #NMClient instance
:param length: the number of returned capabilities.
:return: the
   list of capabilities reported by the server or %NULL
   if the capabilities are unknown.
   The numeric values correspond to #NMCapability enum.
   The array is terminated by a numeric zero sentinel
   at position @length."""
        pass

    def get_checkpoints(self) -> typing.Any:
        """Gets all the active checkpoints.

:param self: a #NMClient
:return: a #GPtrArray containing all the #NMCheckpoint.  The returned array is owned by the #NMClient object and should not be modified."""
        pass

    def get_connection_by_id(self, id: str=None) -> RemoteConnection:
        """Returns the first matching %NMRemoteConnection matching a given @id.

:param self: the %NMClient
:param id: the id of the remote connection
:return: the remote connection object on success, or %NULL if no  matching object was found.  The connection is as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_connection_by_path(self, path: str=None) -> RemoteConnection:
        """Returns the %NMRemoteConnection representing the connection at @path.

:param self: the %NMClient
:param path: the D-Bus object path of the remote connection
:return: the remote connection object on success, or %NULL if the object was  not known  The connection is as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_connection_by_uuid(self, uuid: str=None) -> RemoteConnection:
        """Returns the %NMRemoteConnection identified by @uuid.

:param self: the %NMClient
:param uuid: the UUID of the remote connection
:return: the remote connection object on success, or %NULL if the object was  not known  The connection is as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_connections(self) -> typing.Any:
        """

:param self: the %NMClient
:return: an array containing all connections provided by the remote settings service.  The returned array is owned by the #NMClient object and should not be modified.  The connections are as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_connectivity(self) -> ConnectivityState:
        """Gets the current network connectivity state. Contrast
nm_client_check_connectivity() and
nm_client_check_connectivity_async(), which re-check the
connectivity state first before returning any information.

:param self: an #NMClient
:return: the current connectivity state"""
        pass

    def get_context_busy_watcher(self) -> GObject.Object:
        """

:param self: the NMClient instance.
:return: a GObject that stays alive as long as there are pending
   D-Bus operations.  NMClient will schedule asynchronous D-Bus requests which will complete on the GMainContext associated with the instance. When destroying the NMClient instance, those requests are cancelled right away, however their pending requests are still outstanding and queued in the GMainContext. These outstanding callbacks keep the GMainContext alive. In order to fully release all resources, the user must keep iterating the main context until all these callbacks are handled. Of course, at this point no more actual callbacks will be invoked for the user, those are all cancelled internally.  This just leaves one problem: how long does the user need to keep the GMainContext running to ensure everything is cleaned up? The answer is this GObject. Subscribe a weak reference to the returned object and keep iterating the main context until the object got unreferenced.  Note that after the NMClient instance gets destroyed, all outstanding operations will be cancelled right away. That means, the user needs to iterate the #GMainContext a bit longer, but it is guaranteed that the cleanup happens soon after.  The way of using the context-busy-watch, is by registering a weak pointer to see when it gets destroyed. That means, user code should not take additional references on this object to not keep it alive longer.  If you plan to exit the program after releasing the NMClient instance you may not need to worry about these "leaks". Also, if you anyway plan to continue iterating the #GMainContext afterwards, then you don't need to care when exactly NMClient is gone completely."""
        pass

    def get_dbus_connection(self) -> Gio.DBusConnection:
        """Gets the %GDBusConnection of the instance. This can be either passed when
constructing the instance (as "dbus-connection" property), or it will be
automatically initialized during async/sync init.

:param self: a #NMClient
:return: the D-Bus connection of the client, or %NULL if none is set."""
        pass

    def get_dbus_name_owner(self) -> str:
        """

:param self: a #NMClient
:return: the current name owner of the D-Bus service of NetworkManager."""
        pass

    def get_device_by_iface(self, iface: str=None) -> Device:
        """Gets a #NMDevice from a #NMClient.

:param self: a #NMClient
:param iface: the interface name to search for
:return: the #NMDevice for the given @iface or %NULL if none is found."""
        pass

    def get_device_by_path(self, object_path: str=None) -> Device:
        """Gets a #NMDevice from a #NMClient.

:param self: a #NMClient
:param object_path: the object path to search for
:return: the #NMDevice for the given @object_path or %NULL if none is found."""
        pass

    def get_devices(self) -> typing.Any:
        """Gets all the known network devices.  Use nm_device_get_type() or the
<literal>NM_IS_DEVICE_XXXX</literal> functions to determine what kind of
device member of the returned array is, and then you may use device-specific
methods such as nm_device_ethernet_get_hw_address().

:param self: a #NMClient
:return: a #GPtrArray containing all the #NMDevices.  The returned array is owned by the #NMClient object and should not be modified."""
        pass

    def get_dns_configuration(self) -> typing.Any:
        """Gets the current DNS configuration

:param self: a #NMClient
:return: a #GPtrArray containing #NMDnsEntry elements or %NULL in case the value is not available.  The returned array is owned by the #NMClient object and should not be modified."""
        pass

    def get_dns_mode(self) -> str:
        """Gets the current DNS processing mode.

:param self: the #NMClient
:return: the DNS processing mode, or %NULL in case the
   value is not available."""
        pass

    def get_dns_rc_manager(self) -> str:
        """Gets the current DNS resolv.conf manager.

:param self: the #NMClient
:return: the resolv.conf manager or %NULL in case the
   value is not available."""
        pass

    def get_instance_flags(self) -> ClientInstanceFlags:
        """

:param self: the #NMClient instance.
:return: the #NMClientInstanceFlags flags."""
        pass

    def get_logging(self, level: str=None, domains: str=None) -> bool:
        """Gets NetworkManager current logging level and domains.

:param self: a #NMClient
:param level: return location for logging level string
:param domains: return location for log domains string. The string is   a list of domains separated by ","
:return: %TRUE on success, %FALSE otherwise"""
        pass

    def get_main_context(self) -> GLib.MainContext:
        """The #NMClient instance is permanently associated with the current
thread default #GMainContext, referenced the time when the instance
was created. To receive events, the user must iterate this context
and can use it to synchronize access to the client.

Note that even after #NMClient instance got destroyed, there might
still be pending sources registered in the context. That means, to fully
clean up, the user must continue iterating the context as long as
the nm_client_get_context_busy_watcher() object is alive.

:param self: the #NMClient instance
:return: the #GMainContext of the client."""
        pass

    def get_metered(self) -> Metered:
        """

:param self: a #NMClient
:return: whether the default route is metered."""
        pass

    def get_nm_running(self) -> bool:
        """Determines whether the daemon is running.

:param self: a #NMClient
:return: %TRUE if the daemon is running"""
        pass

    def get_object_by_path(self, dbus_path: str=None) -> Object:
        """

:param self: the #NMClient instance
:param dbus_path: the D-Bus path of the object to look up
:return: the #NMObject instance that is
   cached under @dbus_path, or %NULL if no such object exists."""
        pass

    def get_permission_result(self, permission: ClientPermission=None
        ) -> ClientPermissionResult:
        """Requests the result of a specific permission, which indicates whether the
client can or cannot perform the action the permission represents

:param self: a #NMClient
:param permission: the permission for which to return the result, one of #NMClientPermission
:return: the permission's result, one of #NMClientPermissionResult"""
        pass

    def get_permissions_state(self) -> Ternary:
        """

:param self: the #NMClient instance
:return: the state of the cached permissions. %NM_TERNARY_DEFAULT
   means that no permissions result was yet received. All permissions
   are unknown. %NM_TERNARY_TRUE means that the permissions got received
   and are cached. %%NM_TERNARY_FALSE means that permissions are cached,
   but they are invalided as "CheckPermissions" signal was received
   in the meantime."""
        pass

    def get_primary_connection(self) -> ActiveConnection:
        """Gets the #NMActiveConnection corresponding to the primary active
network device.

In particular, when there is no VPN active, or the VPN does not
have the default route, this returns the active connection that has
the default route. If there is a VPN active with the default route,
then this function returns the active connection that contains the
route to the VPN endpoint.

If there is no default route, or the default route is over a
non-NetworkManager-recognized device, this will return %NULL.

:param self: an #NMClient
:return: the appropriate #NMActiveConnection, if any"""
        pass

    def get_radio_flags(self) -> RadioFlags:
        """Get radio flags.

:param self: a #NMClient
:return: the #NMRadioFlags."""
        pass

    def get_startup(self) -> bool:
        """Tests whether the daemon is still in the process of activating
connections at startup.

:param self: a #NMClient
:return: whether the daemon is still starting up"""
        pass

    def get_state(self) -> State:
        """Gets the current daemon state.

:param self: a #NMClient
:return: the current %NMState"""
        pass

    def get_version(self) -> str:
        """Gets NetworkManager version.

:param self: a #NMClient
:return: string with the version (or %NULL if NetworkManager is not running)"""
        pass

    def get_version_info(self, length: int=None) -> typing.Any:
        """If available, the first element in the array is NM_VERSION which
encodes the daemon version as "(major << 16 | minor << 8 | micro)".
The following elements are a bitfield of %NMVersionInfoCapability
that indicate that the daemon supports a certain capability.

:param self: the #NMClient instance
:param length: the number of returned capabilities.
:return: the
   list of capabilities reported by the server or %NULL
   if the capabilities are unknown."""
        pass

    def load_connections(self, filenames: typing.Any=None, failures: str=
        None, cancellable: Gio.Cancellable=None) -> bool:
        """Requests that the remote settings service load or reload the given files,
adding or updating the connections described within.

The changes to the indicated files will not yet be reflected in
@client's connections array when the function returns.

If all of the indicated files were successfully loaded, the
function will return %TRUE, and @failures will be set to %NULL. If
NetworkManager tried to load the files, but some (or all) failed,
then @failures will be set to a %NULL-terminated array of the
filenames that failed to load.

:param self: the %NMClient
:param filenames: %NULL-terminated array of filenames to load
:param failures: on return, a %NULL-terminated array of   filenames that failed to load
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success.  Warning: before libnm 1.22, the boolean return value was inconsistent.
   That is made worse, because when running against certain server versions
   before 1.20, the server would return wrong values for success/failure.
   This means, if you use this function in libnm before 1.22, you are advised
   to ignore the boolean return value and only look at @failures and @error.
   With libnm >= 1.22, the boolean return value corresponds to whether @error was
   set. Note that even in the success case, you might have individual @failures.
   With 1.22, the return value is consistent with nm_client_load_connections_finish()."""
        pass

    def load_connections_async(self, filenames: typing.Any=None,
        cancellable: Gio.Cancellable=None, callback: Gio.AsyncReadyCallback
        =None, user_data: typing.Any=None) -> None:
        """Requests that the remote settings service asynchronously load or reload the
given files, adding or updating the connections described within.

See nm_client_load_connections() for more details.

:param self: the %NMClient
:param filenames: %NULL-terminated array of filenames to load
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def load_connections_finish(self, failures: typing.Any=None, result:
        Gio.AsyncResult=None) -> bool:
        """Gets the result of an nm_client_load_connections_async() call.

See nm_client_load_connections() for more details.

:param self: the %NMClient
:param failures: on return, a    %NULL-terminated array of filenames that failed to load
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success.
   Note that even in the success case, you might have individual @failures."""
        pass

    def networking_get_enabled(self) -> bool:
        """Whether networking is enabled or disabled.

:param self: a #NMClient
:return: %TRUE if networking is enabled, %FALSE if networking is disabled"""
        pass

    def networking_set_enabled(self, enabled: bool=None) -> bool:
        """Enables or disables networking.  When networking is disabled, all controlled
interfaces are disconnected and deactivated.  When networking is enabled,
all controlled interfaces are available for activation.

:param self: a #NMClient
:param enabled: %TRUE to set networking enabled, %FALSE to set networking disabled
:return: %TRUE on success, %FALSE otherwise"""
        pass

    def reload(self, flags: ManagerReloadFlags=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Reload NetworkManager's configuration and perform certain updates, like
flushing caches or rewriting external state to disk. This is similar to
sending SIGHUP to NetworkManager but it allows for more fine-grained control
over what to reload (see @flags). It also allows non-root access via
PolicyKit and contrary to signals it is synchronous.

:param self: the %NMClient
:param flags: flags indicating what to reload.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the add operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def reload_connections(self, cancellable: Gio.Cancellable=None) -> bool:
        """Requests that the remote settings service reload all connection
files from disk, adding, updating, and removing connections until
the in-memory state matches the on-disk state.

:param self: the #NMClient
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on failure"""
        pass

    def reload_connections_async(self, cancellable: Gio.Cancellable=None,
        callback: Gio.AsyncReadyCallback=None, user_data: typing.Any=None
        ) -> None:
        """Requests that the remote settings service begin reloading all connection
files from disk, adding, updating, and removing connections until the
in-memory state matches the on-disk state.

:param self: the #NMClient
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the reload operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def reload_connections_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of an nm_client_reload_connections_async() call.

:param self: the #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on failure"""
        pass

    def reload_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_client_reload().

:param self: an #NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success or %FALSE on failure."""
        pass

    def save_hostname(self, hostname: str=None, cancellable:
        Gio.Cancellable=None) -> bool:
        """Requests that the machine's persistent hostname be set to the specified value
or cleared.

:param self: the %NMClient
:param hostname: the new persistent hostname to set, or %NULL to   clear any existing persistent hostname
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE if the request was successful, %FALSE if it failed"""
        pass

    def save_hostname_async(self, hostname: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Requests that the machine's persistent hostname be set to the specified value
or cleared.

:param self: the %NMClient
:param hostname: the new persistent hostname to set, or %NULL to   clear any existing persistent hostname
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def save_hostname_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of an nm_client_save_hostname_async() call.

:param self: the %NMClient
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE if the request was successful, %FALSE if it failed"""
        pass

    def set_logging(self, level: str=None, domains: str=None) -> bool:
        """Sets NetworkManager logging level and/or domains.

:param self: a #NMClient
:param level: logging level to set (%NULL or an empty string for no change)
:param domains: logging domains to set. The string should be a list of log   domains separated by ",". (%NULL or an empty string for no change)
:return: %TRUE on success, %FALSE otherwise"""
        pass

    def wait_shutdown(self, integrate_maincontext: bool=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """The way to stop #NMClient is by unrefing it. That will cancel all
internally pending async operations. However, as async operations in
NMClient use GTask, hence they cannot complete right away. Instead,
their (internal) result callback still needs to be dispatched by iterating
the client's main context.

You thus cannot stop iterating the client's main context until
everything is wrapped up. nm_client_get_context_busy_watcher()
helps to watch how long that will be.

This function automates that waiting. Like all glib async operations
this honors the current g_main_context_get_thread_default().

In any case, to complete the shutdown, nm_client_get_main_context()
must be iterated. If the current g_main_context_get_thread_default() is
the same as nm_client_get_main_context(), then @integrate_maincontext
is ignored. In that case, the caller is required to iterate the context
for shutdown to complete. Otherwise, if g_main_context_get_thread_default()
differs from nm_client_get_main_context() and @integrate_maincontext
is %FALSE, the caller must make sure that both contexts are iterated
until completion. Otherwise, if @integrate_maincontext is %TRUE, then
nm_client_get_main_context() will be integrated in g_main_context_get_thread_default().
This means, the caller gives nm_client_get_main_context() up until the waiting
completes, the function will acquire the context and hook it into
g_main_context_get_thread_default().
It is a bug to request @integrate_maincontext while having nm_client_get_main_context()
acquired or iterated otherwise because a context can only be acquired once
at a time.

Shutdown can only complete after all references to @client were released.

It is possible to call this function multiple times for the same client.
But note that with @integrate_maincontext the client's context is acquired,
which can only be done once at a time.

It is permissible to start waiting before the objects is fully initialized.

The function really allows two separate things. To get a notification (callback) when
shutdown is complete, and to integrate the client's context in another context.
The latter case is useful if the client has a separate context and you hand it
over to another GMainContext to wrap up.

The main use is to have a NMClient and a separate GMainContext on a worker
thread. When being done, you can hand over the cleanup of the context
to g_main_context_default(), assuming that the main thread iterates
the default context. In that case, you don't need to care about passing
a callback to know when shutdown completed.

:param self: the #NMClient to shutdown.
:param integrate_maincontext: whether to hook the client's maincontext   in the current thread default. Otherwise, you must ensure   that the client's maincontext gets iterated so that it can complete.   By integrating the maincontext in the current thread default, you   may instead only iterate the latter.
:param cancellable: the #GCancellable to abort the shutdown.
:param callback: a #GAsyncReadyCallback to call when the request   is satisfied or %NULL if you don't care about the result of the   method invocation.
:param user_data: the data to pass to @callback
:return: """
        pass

    def wimax_get_enabled(self) -> bool:
        """Determines whether WiMAX is enabled.

:param self: a #NMClient
:return: %TRUE if WiMAX is enabled"""
        pass

    def wimax_hardware_get_enabled(self) -> bool:
        """Determines whether the WiMAX hardware is enabled.

:param self: a #NMClient
:return: %TRUE if the WiMAX hardware is enabled"""
        pass

    def wimax_set_enabled(self, enabled: bool=None) -> None:
        """Enables or disables WiMAX devices.

:param self: a #NMClient
:param enabled: %TRUE to enable WiMAX
:return: """
        pass

    def wireless_get_enabled(self) -> bool:
        """Determines whether the wireless is enabled.

:param self: a #NMClient
:return: %TRUE if wireless is enabled"""
        pass

    def wireless_hardware_get_enabled(self) -> bool:
        """Determines whether the wireless hardware is enabled.

:param self: a #NMClient
:return: %TRUE if the wireless hardware is enabled"""
        pass

    def wireless_set_enabled(self, enabled: bool=None) -> None:
        """Enables or disables wireless devices.

:param self: a #NMClient
:param enabled: %TRUE to enable wireless
:return: """
        pass

    def wwan_get_enabled(self) -> bool:
        """Determines whether WWAN is enabled.

:param self: a #NMClient
:return: %TRUE if WWAN is enabled"""
        pass

    def wwan_hardware_get_enabled(self) -> bool:
        """Determines whether the WWAN hardware is enabled.

:param self: a #NMClient
:return: %TRUE if the WWAN hardware is enabled"""
        pass

    def wwan_set_enabled(self, enabled: bool=None) -> None:
        """Enables or disables WWAN devices.

:param self: a #NMClient
:param enabled: %TRUE to enable WWAN
:return: """
        pass


class ClientClass:
    """"""


class Connection:
    """NMConnection is the interface implemented by #NMRemoteConnection on the
client side, and #NMSettingsConnection on the daemon side."""

    def changed(self) -> None:
        """emitted when any change to the connection's settings occurs

:param self: 
:return: """
        pass

    def secrets_cleared(self) -> None:
        """emitted when the connection's secrets are cleared

:param self: 
:return: """
        pass

    def secrets_updated(self, setting: str=None) -> None:
        """emitted when the connection's secrets are updated

:param self: 
:param setting: 
:return: """
        pass

    def add_setting(self, setting: Setting=None) -> None:
        """Adds a #NMSetting to the connection, replacing any previous #NMSetting of the
same name which has previously been added to the #NMConnection.  The
connection takes ownership of the #NMSetting object and does not increase
the setting object's reference count.

:param self: a #NMConnection
:param setting: the #NMSetting to add to the connection object
:return: """
        pass

    def clear_secrets(self) -> None:
        """Clears and frees any secrets that may be stored in the connection, to avoid
keeping secret data in memory when not needed.

:param self: the #NMConnection
:return: """
        pass

    def clear_secrets_with_flags(self, func: SettingClearSecretsWithFlagsFn
        =None, user_data: typing.Any=None) -> None:
        """Clears and frees secrets determined by @func.

:param self: the #NMConnection
:param func: function to be called to determine whether a     specific secret should be cleared or not. If %NULL, all secrets are cleared.
:param user_data: caller-supplied data passed to @func
:return: """
        pass

    def clear_settings(self) -> None:
        """Deletes all of @connection's settings.

:param self: a #NMConnection
:return: """
        pass

    def compare(self, b: Connection=None, flags: SettingCompareFlags=None
        ) -> bool:
        """Compares two #NMConnection objects for similarity, with comparison behavior
modified by a set of flags.  See nm_setting_compare() for a description of
each flag's behavior.

:param self: a #NMConnection
:param b: a second #NMConnection to compare with the first
:param flags: compare flags, e.g. %NM_SETTING_COMPARE_FLAG_EXACT
:return: %TRUE if the comparison succeeds, %FALSE if it does not"""
        pass

    def diff(self, b: Connection=None, flags: SettingCompareFlags=None,
        out_settings: GLib.HashTable=None) -> bool:
        """Compares two #NMConnection objects for similarity, with comparison behavior
modified by a set of flags.  See nm_setting_compare() for a description of
each flag's behavior.  If the connections differ, settings and keys within
each setting that differ are added to the returned @out_settings hash table.
No values are returned, only key names.

:param self: a #NMConnection
:param b: a second #NMConnection to compare with the first
:param flags: compare flags, e.g. %NM_SETTING_COMPARE_FLAG_EXACT
:param out_settings: if the connections differ, on return a hash table mapping setting names to second-level GHashTable (utf8 to guint32), which contains the key names that differ mapped to one or more of %NMSettingDiffResult as a bitfield
:return: %TRUE if the connections contain the same values, %FALSE if they do not"""
        pass

    def dump(self) -> None:
        """Print the connection (including secrets!) to stdout. For debugging
purposes ONLY, should NOT be used for serialization of the setting,
or machine-parsed in any way. The output format is not guaranteed to
be stable and may change at any time.

:param self: the #NMConnection
:return: """
        pass

    def for_each_setting_value(self, func: SettingValueIterFn=None,
        user_data: typing.Any=None) -> None:
        """Iterates over the properties of each #NMSetting object in the #NMConnection,
calling the supplied user function for each property.

:param self: the #NMConnection
:param func: user-supplied function called for each setting's property
:param user_data: user data passed to @func at each invocation
:return: """
        pass

    def get_connection_type(self) -> str:
        """A shortcut to return the type from the connection's #NMSettingConnection.

:param self: the #NMConnection
:return: the type from the connection's 'connection' setting"""
        pass

    def get_id(self) -> str:
        """A shortcut to return the ID from the connection's #NMSettingConnection.

:param self: the #NMConnection
:return: the ID from the connection's 'connection' setting"""
        pass

    def get_interface_name(self) -> str:
        """Returns the interface name as stored in NMSettingConnection:interface_name.
If the connection contains no NMSettingConnection, it will return %NULL.

For hardware devices and software devices created outside of NetworkManager,
this name is used to match the device. for software devices created by
NetworkManager, this is the name of the created interface.

:param self: The #NMConnection
:return: Name of the kernel interface or %NULL"""
        pass

    def get_path(self) -> str:
        """Returns the connection's D-Bus path.

:param self: the #NMConnection
:return: the D-Bus path of the connection, previously set by a call to nm_connection_set_path()."""
        pass

    def get_setting(self, setting_type: GType=None) -> Setting:
        """Gets the #NMSetting with the given #GType, if one has been previously added
to the #NMConnection.

:param self: a #NMConnection
:param setting_type: the #GType of the setting object to return
:return: the #NMSetting, or %NULL if no setting of that type was previously added to the #NMConnection"""
        pass

    def get_setting_802_1x(self) -> Setting8021x:
        """A shortcut to return any #NMSetting8021x the connection might contain.

:param self: the #NMConnection
:return: an #NMSetting8021x if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_adsl(self) -> SettingAdsl:
        """A shortcut to return any #NMSettingAdsl the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingAdsl if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_bluetooth(self) -> SettingBluetooth:
        """A shortcut to return any #NMSettingBluetooth the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingBluetooth if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_bond(self) -> SettingBond:
        """A shortcut to return any #NMSettingBond the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingBond if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_bridge(self) -> SettingBridge:
        """A shortcut to return any #NMSettingBridge the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingBridge if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_bridge_port(self) -> SettingBridgePort:
        """A shortcut to return any #NMSettingBridgePort the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingBridgePort if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_by_name(self, name: str=None) -> Setting:
        """Gets the #NMSetting with the given name, if one has been previously added
the #NMConnection.

:param self: a #NMConnection
:param name: a setting name
:return: the #NMSetting, or %NULL if no setting with that name was previously added to the #NMConnection"""
        pass

    def get_setting_cdma(self) -> SettingCdma:
        """A shortcut to return any #NMSettingCdma the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingCdma if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_connection(self) -> SettingConnection:
        """A shortcut to return any #NMSettingConnection the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingConnection if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_dcb(self) -> SettingDcb:
        """A shortcut to return any #NMSettingDcb the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingDcb if the connection contains one, otherwise NULL"""
        pass

    def get_setting_dummy(self) -> SettingDummy:
        """A shortcut to return any #NMSettingDummy the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingDummy if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_generic(self) -> SettingGeneric:
        """A shortcut to return any #NMSettingGeneric the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingGeneric if the connection contains one, otherwise NULL"""
        pass

    def get_setting_gsm(self) -> SettingGsm:
        """A shortcut to return any #NMSettingGsm the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingGsm if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_infiniband(self) -> SettingInfiniband:
        """A shortcut to return any #NMSettingInfiniband the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingInfiniband if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ip4_config(self) -> SettingIP4Config:
        """A shortcut to return any #NMSettingIP4Config the connection might contain.

Note that it returns the value as type #NMSettingIPConfig, since the vast
majority of IPv4-setting-related methods are on that type, not
#NMSettingIP4Config.

:param self: the #NMConnection
:return: an #NMSettingIP4Config if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ip6_config(self) -> SettingIP6Config:
        """A shortcut to return any #NMSettingIP6Config the connection might contain.

Note that it returns the value as type #NMSettingIPConfig, since the vast
majority of IPv6-setting-related methods are on that type, not
#NMSettingIP6Config.

:param self: the #NMConnection
:return: an #NMSettingIP6Config if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ip_tunnel(self) -> SettingIPTunnel:
        """A shortcut to return any #NMSettingIPTunnel the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingIPTunnel if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_macsec(self) -> SettingMacsec:
        """A shortcut to return any #NMSettingMacsec the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingMacsec if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_macvlan(self) -> SettingMacvlan:
        """A shortcut to return any #NMSettingMacvlan the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingMacvlan if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_olpc_mesh(self) -> SettingOlpcMesh:
        """A shortcut to return any #NMSettingOlpcMesh the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingOlpcMesh if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ovs_bridge(self) -> SettingOvsBridge:
        """A shortcut to return any #NMSettingOvsBridge the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingOvsBridge if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ovs_interface(self) -> SettingOvsInterface:
        """A shortcut to return any #NMSettingOvsInterface the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingOvsInterface if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ovs_patch(self) -> SettingOvsPatch:
        """A shortcut to return any #NMSettingOvsPatch the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingOvsPatch if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ovs_port(self) -> SettingOvsPort:
        """A shortcut to return any #NMSettingOvsPort the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingOvsPort if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_ppp(self) -> SettingPpp:
        """A shortcut to return any #NMSettingPpp the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingPpp if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_pppoe(self) -> SettingPppoe:
        """A shortcut to return any #NMSettingPppoe the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingPppoe if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_proxy(self) -> SettingProxy:
        """A shortcut to return any #NMSettingProxy the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingProxy if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_serial(self) -> SettingSerial:
        """A shortcut to return any #NMSettingSerial the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingSerial if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_tc_config(self) -> SettingTCConfig:
        """A shortcut to return any #NMSettingTCConfig the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingTCConfig if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_team(self) -> SettingTeam:
        """A shortcut to return any #NMSettingTeam the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingTeam if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_team_port(self) -> SettingTeamPort:
        """A shortcut to return any #NMSettingTeamPort the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingTeamPort if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_tun(self) -> SettingTun:
        """A shortcut to return any #NMSettingTun the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingTun if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_vlan(self) -> SettingVlan:
        """A shortcut to return any #NMSettingVlan the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingVlan if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_vpn(self) -> SettingVpn:
        """A shortcut to return any #NMSettingVpn the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingVpn if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_vxlan(self) -> SettingVxlan:
        """A shortcut to return any #NMSettingVxlan the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingVxlan if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_wimax(self) -> SettingWimax:
        """A shortcut to return any #NMSettingWimax the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingWimax if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_wired(self) -> SettingWired:
        """A shortcut to return any #NMSettingWired the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingWired if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_wireless(self) -> SettingWireless:
        """A shortcut to return any #NMSettingWireless the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingWireless if the connection contains one, otherwise %NULL"""
        pass

    def get_setting_wireless_security(self) -> SettingWirelessSecurity:
        """A shortcut to return any #NMSettingWirelessSecurity the connection might contain.

:param self: the #NMConnection
:return: an #NMSettingWirelessSecurity if the connection contains one, otherwise %NULL"""
        pass

    def get_settings(self, out_length: int=None) -> typing.Any:
        """Retrieves the settings in @connection.

The returned array is %NULL-terminated.

:param self: the #NMConnection instance
:param out_length: the length of the returned array
:return: a
   %NULL-terminated array containing every setting of @connection.
   If the connection has no settings, %NULL is returned."""
        pass

    def get_uuid(self) -> str:
        """A shortcut to return the UUID from the connection's #NMSettingConnection.

:param self: the #NMConnection
:return: the UUID from the connection's 'connection' setting"""
        pass

    def get_virtual_device_description(self) -> str:
        """Returns the name that nm_device_disambiguate_names() would
return for the virtual device that would be created for @connection.
Eg, "VLAN (eth1.1)".

:param self: an #NMConnection for a virtual device type
:return: the name of @connection's device,
   or %NULL if @connection is not a virtual connection type"""
        pass

    def is_type(self, type: str=None) -> bool:
        """A convenience function to check if the given @connection is a particular
type (ie wired, Wi-Fi, ppp, etc). Checks the #NMSettingConnection:type
property of the connection and matches that against @type.

:param self: the #NMConnection
:param type: a setting name to check the connection's type against (like %NM_SETTING_WIRELESS_SETTING_NAME or %NM_SETTING_WIRED_SETTING_NAME)
:return: %TRUE if the connection is of the given @type, %FALSE if not"""
        pass

    def is_virtual(self) -> bool:
        """Checks if @connection refers to a virtual device (and thus can potentially be
activated even if the device it refers to doesn't exist).

:param self: an #NMConnection
:return: whether @connection refers to a virtual device"""
        pass

    def need_secrets(self, hints: typing.Any=None) -> str:
        """Returns the name of the first setting object in the connection which would
need secrets to make a successful connection.  The returned hints are only
intended as a guide to what secrets may be required, because in some
circumstances, there is no way to conclusively determine exactly which
secrets are needed.

:param self: the #NMConnection
:param hints: the address of a pointer to a #GPtrArray, initialized to %NULL, which on   return points to an allocated #GPtrArray containing the property names of   secrets of the #NMSetting which may be required; the caller owns the array   and must free the array itself with g_ptr_array_free(), but not free its   elements
:return: the setting name of the #NMSetting object which has
   invalid or missing secrets"""
        pass

    def normalize(self, parameters: GLib.HashTable=None, modified: bool=None
        ) -> bool:
        """Does some basic normalization and fixup of well known inconsistencies
and deprecated fields. If the connection was modified in any way,
the output parameter @modified is set %TRUE.

Finally the connection will be verified and %TRUE returns if the connection
is valid. As this function only performs some specific normalization steps
it cannot repair all connections. If the connection has errors that
cannot be normalized, the connection will not be modified.

:param self: the #NMConnection to normalize
:param parameters: a #GHashTable with normalization parameters to allow customization of the normalization by providing specific arguments. Unknown arguments will be ignored and the default will be used. The keys must be strings compared with g_str_equal() function. The values are opaque and depend on the parameter name.
:param modified: outputs whether any settings were modified.
:return: %TRUE if the connection is valid, %FALSE if it is not"""
        pass

    def remove_setting(self, setting_type: GType=None) -> None:
        """Removes the #NMSetting with the given #GType from the #NMConnection.  This
operation dereferences the #NMSetting object.

:param self: a #NMConnection
:param setting_type: the #GType of the setting object to remove
:return: """
        pass

    def replace_settings(self, new_settings: GLib.Variant=None) -> bool:
        """Replaces @connection's settings with @new_settings (which must be
syntactically valid, and describe a known type of connection, but does not
need to result in a connection that passes nm_connection_verify()).

:param self: a #NMConnection
:param new_settings: a #GVariant of type %NM_VARIANT_TYPE_CONNECTION, with the new settings
:return: %TRUE if connection was updated, %FALSE if @new_settings could not
   be deserialized (in which case @connection will be unchanged)."""
        pass

    def replace_settings_from_connection(self, new_connection: Connection=None
        ) -> None:
        """Deep-copies the settings of @new_connection and replaces the settings of @connection
with the copied settings.

:param self: a #NMConnection
:param new_connection: a #NMConnection to replace the settings of @connection with
:return: """
        pass

    def set_path(self, path: str=None) -> None:
        """Sets the D-Bus path of the connection.  This property is not serialized, and
is only for the reference of the caller.  Sets the #NMConnection:path
property.

:param self: the #NMConnection
:param path: the D-Bus path of the connection as given by the settings service which provides the connection
:return: """
        pass

    def to_dbus(self, flags: ConnectionSerializationFlags=None
        ) -> GLib.Variant:
        """Converts the #NMConnection into a #GVariant of type
%NM_VARIANT_TYPE_CONNECTION describing the connection, suitable for
marshalling over D-Bus or otherwise serializing.

:param self: the #NMConnection
:param flags: serialization flags, e.g. %NM_CONNECTION_SERIALIZE_ALL
:return: a new floating #GVariant describing the connection, its settings, and each setting's properties."""
        pass

    def update_secrets(self, setting_name: str=None, secrets: GLib.Variant=None
        ) -> bool:
        """Update the specified setting's secrets, given a dictionary of secrets
intended for that setting (deserialized from D-Bus for example).  Will also
extract the given setting's secrets hash if given a connection dictionary.
If @setting_name is %NULL, expects a fully serialized #NMConnection as
returned by nm_connection_to_dbus() and will update all secrets from all
settings contained in @secrets.

:param self: the #NMConnection
:param setting_name: the setting object name to which the secrets apply
:param secrets: a #GVariant of secrets, of type %NM_VARIANT_TYPE_CONNECTION   or %NM_VARIANT_TYPE_SETTING
:return: %TRUE if the secrets were successfully updated, %FALSE if the update failed (tried to update secrets for a setting that doesn't exist, etc)"""
        pass

    def verify(self) -> bool:
        """Validates the connection and all its settings.  Each setting's properties
have allowed values, and some values are dependent on other values.  For
example, if a Wi-Fi connection is security enabled, the #NMSettingWireless
setting object's 'security' property must contain the setting name of the
#NMSettingWirelessSecurity object, which must also be present in the
connection for the connection to be valid.  As another example, the
#NMSettingWired object's 'mac-address' property must be a validly formatted
MAC address.  The returned #GError contains information about which
setting and which property failed validation, and how it failed validation.

:param self: the #NMConnection to verify
:return: %TRUE if the connection is valid, %FALSE if it is not"""
        pass

    def verify_secrets(self) -> bool:
        """Verifies the secrets in the connection.

:param self: the #NMConnection to verify in
:return: %TRUE if the secrets are valid, %FALSE if they are not"""
        pass


class ConnectionInterface:
    """"""
    parent: GObject.TypeInterface
    secrets_updated: typing.Any
    secrets_cleared: typing.Any
    changed: typing.Any


class Device6LowpanClass:
    """"""


class DeviceAdslClass:
    """"""


class DeviceBondClass:
    """"""


class DeviceBridgeClass:
    """"""


class DeviceBtClass:
    """"""


class DeviceClass:
    """"""


class DeviceDummyClass:
    """"""


class DeviceEthernetClass:
    """"""


class DeviceGenericClass:
    """"""


class DeviceHsrClass:
    """"""


class DeviceIPTunnelClass:
    """"""


class DeviceInfinibandClass:
    """"""


class DeviceIpvlanClass:
    """"""


class DeviceLoopbackClass:
    """"""


class DeviceMacsecClass:
    """"""


class DeviceMacvlanClass:
    """"""


class DeviceModemClass:
    """"""


class DeviceOlpcMeshClass:
    """"""


class DeviceOvsBridgeClass:
    """"""


class DeviceOvsInterfaceClass:
    """"""


class DeviceOvsPortClass:
    """"""


class DevicePppClass:
    """"""


class DeviceTeamClass:
    """"""


class DeviceTunClass:
    """"""


class DeviceVethClass:
    """"""


class DeviceVlanClass:
    """"""


class DeviceVrfClass:
    """"""


class DeviceVxlanClass:
    """"""


class DeviceWifiClass:
    """"""


class DeviceWifiP2PClass:
    """"""


class DeviceWimaxClass:
    """"""


class DeviceWireGuardClass:
    """"""


class DeviceWpanClass:
    """"""


class DhcpConfigClass:
    """"""


class DnsEntry:
    """"""

    def get_domains(self) -> typing.Any:
        """Gets the list of DNS domains.

:param self: the #NMDnsEntry
:return: the list of DNS domains"""
        pass

    def get_interface(self) -> str:
        """Gets the interface on which name servers are contacted.

:param self: the #NMDnsEntry
:return: the interface name"""
        pass

    def get_nameservers(self) -> typing.Any:
        """Gets the list of name servers for this entry.

:param self: the #NMDnsEntry
:return: the list of name servers"""
        pass

    def get_priority(self) -> int:
        """Gets the priority of the entry

:param self: the #NMDnsEntry
:return: the priority of the entry"""
        pass

    def get_vpn(self) -> bool:
        """Gets whether the entry refers to VPN name servers.

:param self: the #NMDnsEntry
:return: %TRUE if the entry refers to VPN name servers"""
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMDnsEntry
:return: """
        pass


class IPAddress:
    """"""

    def __init__(self, family: int=None, addr: str=None, prefix: int=None
        ) -> None:
        """Creates a new #NMIPAddress object.

:param self: 
:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param addr: the IP address
:param prefix: the address prefix length
:return: """
        pass

    @staticmethod
    def new(family: int=None, addr: str=None, prefix: int=None) -> IPAddress:
        """Creates a new #NMIPAddress object.

:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param addr: the IP address
:param prefix: the address prefix length
:return: the new #NMIPAddress object, or %NULL on error"""
        pass

    @staticmethod
    def new_binary(family: int=None, addr: typing.Any=None, prefix: int=None
        ) -> IPAddress:
        """Creates a new #NMIPAddress object. @addr must point to a buffer of the
correct size for @family.

:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param addr: the IP address
:param prefix: the address prefix length
:return: the new #NMIPAddress object, or %NULL on error"""
        pass

    def cmp_full(self, b: IPAddress=None, cmp_flags: IPAddressCmpFlags=None
        ) -> int:
        """Note that with @cmp_flags #NM_IP_ADDRESS_CMP_FLAGS_WITH_ATTRS, there
is no total order for comparing GVariant. That means, if the two addresses
only differ by their attributes, the sort order is undefined and the return
value only indicates equality.

:param self: the #NMIPAddress
:param b: the #NMIPAddress to compare @address to.
:param cmp_flags: the #NMIPAddressCmpFlags that indicate what to compare.
:return: 0 if the two objects have the same values (according to their flags)
   or a integer indicating the compare order."""
        pass

    def dup(self) -> IPAddress:
        """Creates a copy of @address

:param self: the #NMIPAddress
:return: a copy of @address  This API was part of public headers before 1.32.0 but was erroneously not exported in the ABI. It is thus only usable since 1.32.0."""
        pass

    def equal(self, other: IPAddress=None) -> bool:
        """Determines if two #NMIPAddress objects contain the same address and prefix
(attributes are not compared).

:param self: the #NMIPAddress
:param other: the #NMIPAddress to compare @address to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_address(self) -> str:
        """Gets the IP address property of this address object.

:param self: the #NMIPAddress
:return: the IP address"""
        pass

    def get_address_binary(self, addr: typing.Any=None) -> None:
        """Gets the IP address property of this address object.

@addr must point to a buffer that is the correct size for @address's family.

:param self: the #NMIPAddress
:param addr: a buffer in which to store the address in binary format.
:return: """
        pass

    def get_attribute(self, name: str=None) -> GLib.Variant:
        """Gets the value of the attribute with name @name on @address

:param self: the #NMIPAddress
:param name: the name of an address attribute
:return: the value of the attribute with name @name on
   @address, or %NULL if @address has no such attribute."""
        pass

    def get_attribute_names(self) -> typing.Any:
        """Gets an array of attribute names defined on @address.

:param self: the #NMIPAddress
:return: a %NULL-terminated array of attribute names,"""
        pass

    def get_family(self) -> int:
        """Gets the IP address family (eg, AF_INET) property of this address
object.

:param self: the #NMIPAddress
:return: the IP address family"""
        pass

    def get_prefix(self) -> int:
        """Gets the IP address prefix (ie "24" or "30" etc) property of this address
object.

:param self: the #NMIPAddress
:return: the IP address prefix"""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMIPAddress
:return: """
        pass

    def set_address(self, addr: str=None) -> None:
        """Sets the IP address property of this address object.

@addr must be a valid address of @address's family. If you aren't sure you
have a valid address, use nm_utils_ipaddr_valid() to check it.

:param self: the #NMIPAddress
:param addr: the IP address, as a string
:return: """
        pass

    def set_address_binary(self, addr: typing.Any=None) -> None:
        """Sets the IP address property of this address object.

@addr must point to a buffer that is the correct size for @address's family.

:param self: the #NMIPAddress
:param addr: the address, in binary format
:return: """
        pass

    def set_attribute(self, name: str=None, value: GLib.Variant=None) -> None:
        """Sets or clears the named attribute on @address to the given value.

:param self: the #NMIPAddress
:param name: the name of an address attribute
:param value: the value
:return: """
        pass

    def set_prefix(self, prefix: int=None) -> None:
        """Sets the IP address prefix property of this address object.

:param self: the #NMIPAddress
:param prefix: the IP address prefix
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMIPAddress
:return: """
        pass


class IPConfigClass:
    """"""


class IPRoute:
    """"""

    def __init__(self, family: int=None, dest: str=None, prefix: int=None,
        next_hop: str=None, metric: int=None) -> None:
        """Creates a new #NMIPRoute object.

:param self: 
:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param dest: the IP address of the route's destination
:param prefix: the address prefix length
:param next_hop: the IP address of the next hop (or %NULL)
:param metric: the route metric (or -1 for "default")
:return: """
        pass

    @staticmethod
    def new(family: int=None, dest: str=None, prefix: int=None, next_hop:
        str=None, metric: int=None) -> IPRoute:
        """Creates a new #NMIPRoute object.

:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param dest: the IP address of the route's destination
:param prefix: the address prefix length
:param next_hop: the IP address of the next hop (or %NULL)
:param metric: the route metric (or -1 for "default")
:return: the new #NMIPRoute object, or %NULL on error"""
        pass

    @staticmethod
    def new_binary(family: int=None, dest: typing.Any=None, prefix: int=
        None, next_hop: typing.Any=None, metric: int=None) -> IPRoute:
        """Creates a new #NMIPRoute object. @dest and @next_hop (if non-%NULL) must
point to buffers of the correct size for @family.

:param family: the IP address family (<literal>AF_INET</literal> or   <literal>AF_INET6</literal>)
:param dest: the IP address of the route's destination
:param prefix: the address prefix length
:param next_hop: the IP address of the next hop (or %NULL)
:param metric: the route metric (or -1 for "default")
:return: the new #NMIPRoute object, or %NULL on error"""
        pass

    def dup(self) -> IPRoute:
        """Creates a copy of @route

:param self: the #NMIPRoute
:return: a copy of @route  This API was part of public headers before 1.32.0 but was erroneously not exported in the ABI. It is thus only usable since 1.32.0."""
        pass

    def equal(self, other: IPRoute=None) -> bool:
        """Determines if two #NMIPRoute objects contain the same destination, prefix,
next hop, and metric. (Attributes are not compared.)

:param self: the #NMIPRoute
:param other: the #NMIPRoute to compare @route to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def equal_full(self, other: IPRoute=None, cmp_flags: int=None) -> bool:
        """Determines if two #NMIPRoute objects contain the same destination, prefix,
next hop, and metric.

:param self: the #NMIPRoute
:param other: the #NMIPRoute to compare @route to.
:param cmp_flags: tune how to compare attributes. Currently, only   NM_IP_ROUTE_EQUAL_CMP_FLAGS_NONE (0) and NM_IP_ROUTE_EQUAL_CMP_FLAGS_WITH_ATTRS (1)   is supported.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_attribute(self, name: str=None) -> GLib.Variant:
        """Gets the value of the attribute with name @name on @route

:param self: the #NMIPRoute
:param name: the name of an route attribute
:return: the value of the attribute with name @name on
   @route, or %NULL if @route has no such attribute."""
        pass

    def get_attribute_names(self) -> typing.Any:
        """Gets an array of attribute names defined on @route.

:param self: the #NMIPRoute
:return: a %NULL-terminated array of attribute names"""
        pass

    def get_dest(self) -> str:
        """Gets the IP destination address property of this route object.

:param self: the #NMIPRoute
:return: the IP address of the route's destination"""
        pass

    def get_dest_binary(self, dest: typing.Any=None) -> None:
        """Gets the destination property of this route object.

@dest must point to a buffer that is the correct size for @route's family.

:param self: the #NMIPRoute
:param dest: a buffer in which to store the destination in binary format.
:return: """
        pass

    def get_family(self) -> int:
        """Gets the IP address family (eg, AF_INET) property of this route
object.

:param self: the #NMIPRoute
:return: the IP address family"""
        pass

    def get_metric(self) -> int:
        """Gets the route metric property of this route object; lower values
indicate "better" or more preferred routes; -1 indicates "default"
(meaning NetworkManager will set it appropriately).

:param self: the #NMIPRoute
:return: the route metric"""
        pass

    def get_next_hop(self) -> str:
        """Gets the IP address of the next hop of this route; this will be %NULL if the
route has no next hop.

:param self: the #NMIPRoute
:return: the IP address of the next hop, or %NULL if this is a device route."""
        pass

    def get_next_hop_binary(self, next_hop: typing.Any=None) -> bool:
        """Gets the next hop property of this route object.

@next_hop must point to a buffer that is the correct size for @route's family.

:param self: the #NMIPRoute
:param next_hop: a buffer in which to store the next hop in binary format.
:return: %TRUE if @route has a next hop, %FALSE if not (in which case @next_hop will be zeroed out)"""
        pass

    def get_prefix(self) -> int:
        """Gets the IP prefix (ie "24" or "30" etc) of this route.

:param self: the #NMIPRoute
:return: the IP prefix"""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMIPRoute
:return: """
        pass

    def set_attribute(self, name: str=None, value: GLib.Variant=None) -> None:
        """Sets the named attribute on @route to the given value.

:param self: the #NMIPRoute
:param name: the name of a route attribute
:param value: the value
:return: """
        pass

    def set_dest(self, dest: str=None) -> None:
        """Sets the destination property of this route object.

@dest must be a valid address of @route's family. If you aren't sure you
have a valid address, use nm_inet_is_valid() to check it.

:param self: the #NMIPRoute
:param dest: the route's destination, as a string
:return: """
        pass

    def set_dest_binary(self, dest: typing.Any=None) -> None:
        """Sets the destination property of this route object.

@dest must point to a buffer that is the correct size for @route's family.

:param self: the #NMIPRoute
:param dest: the route's destination, in binary format
:return: """
        pass

    def set_metric(self, metric: int=None) -> None:
        """Sets the metric property of this route object.

:param self: the #NMIPRoute
:param metric: the route metric (or -1 for "default")
:return: """
        pass

    def set_next_hop(self, next_hop: str=None) -> None:
        """Sets the next-hop property of this route object.

@next_hop (if non-%NULL) must be a valid address of @route's family. If you
aren't sure you have a valid address, use nm_utils_ipaddr_valid() to check
it.

:param self: the #NMIPRoute
:param next_hop: the route's next hop, as a string
:return: """
        pass

    def set_next_hop_binary(self, next_hop: typing.Any=None) -> None:
        """Sets the destination property of this route object.

@next_hop (if non-%NULL) must point to a buffer that is the correct size for
@route's family.

:param self: the #NMIPRoute
:param next_hop: the route's next hop, in binary format
:return: """
        pass

    def set_prefix(self, prefix: int=None) -> None:
        """Sets the prefix property of this route object.

:param self: the #NMIPRoute
:param prefix: the route prefix
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMIPRoute
:return: """
        pass

    @staticmethod
    def attribute_validate(name: str=None, value: GLib.Variant=None, family:
        int=None, known: bool=None) -> bool:
        """Validates a route attribute, i.e. checks that the attribute is a known one
and the value is of the correct type and well-formed.

:param name: the attribute name
:param value: the attribute value
:param family: IP address family of the route
:param known: on return, whether the attribute name is a known one
:return: %TRUE if the attribute is valid, %FALSE otherwise"""
        pass

    @staticmethod
    def get_variant_attribute_spec() -> VariantAttributeSpec:
        """

:return: the specifiers for route attributes"""
        pass


class IPRoutingRule:
    """"""

    def __init__(self, addr_family: int=None) -> None:
        """

:param self: 
:param addr_family: the address family of the routing rule. Must be either   %AF_INET (2) or %AF_INET6 (10).
:return: """
        pass

    @staticmethod
    def new(addr_family: int=None) -> IPRoutingRule:
        """

:param addr_family: the address family of the routing rule. Must be either   %AF_INET (2) or %AF_INET6 (10).
:return: a newly created rule instance with the
   provided address family. The instance is unsealed."""
        pass

    def cmp(self, other: IPRoutingRule=None) -> int:
        """

:param self: the #NMIPRoutingRule instance to compare
:param other: the other #NMIPRoutingRule instance to compare
:return: zero, a positive, or a negative integer to indicate
   equality or how the arguments compare."""
        pass

    def get_action(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the set action."""
        pass

    def get_addr_family(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the address family of the rule. Either %AF_INET or %AF_INET6."""
        pass

    def get_destination_port_end(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the destination port end setting."""
        pass

    def get_destination_port_start(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the destination port start setting."""
        pass

    def get_from(self) -> str:
        """

:param self: the #NMIPRoutingRule instance
:return: the set from/src parameter or
   %NULL, if no value is set."""
        pass

    def get_from_len(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the set prefix length for the from/src parameter."""
        pass

    def get_fwmark(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the fwmark setting."""
        pass

    def get_fwmask(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the fwmask setting."""
        pass

    def get_iifname(self) -> str:
        """

:param self: the #NMIPRoutingRule instance.
:return: the set iifname or %NULL if unset."""
        pass

    def get_invert(self) -> bool:
        """

:param self: the #NMIPRoutingRule instance
:return: the "invert" setting of the rule."""
        pass

    def get_ipproto(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the ipproto of the rule."""
        pass

    def get_oifname(self) -> str:
        """

:param self: the #NMIPRoutingRule instance.
:return: the set oifname or %NULL if unset."""
        pass

    def get_priority(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the priority. A valid priority is in the range from
   0 to %G_MAXUINT32. If unset, -1 is returned."""
        pass

    def get_source_port_end(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the source port end setting."""
        pass

    def get_source_port_start(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the source port start setting."""
        pass

    def get_suppress_prefixlength(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the suppress_prefixlength of the rule. -1 means that the value is unset."""
        pass

    def get_table(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the set table."""
        pass

    def get_to(self) -> str:
        """

:param self: the #NMIPRoutingRule instance
:return: the set to/dst parameter or
   %NULL, if no value is set."""
        pass

    def get_to_len(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the set prefix length for the to/dst parameter."""
        pass

    def get_tos(self) -> int:
        """

:param self: the #NMIPRoutingRule instance
:return: the tos of the rule."""
        pass

    def get_uid_range(self, out_range_start: int=None, out_range_end: int=None
        ) -> bool:
        """

:param self: the #NMIPRoutingRule instance
:param out_range_start: returns the start of the range   or 0 if the range is not set.
:param out_range_end: returns the end of the range   or 0 if the range is not set.
:return: %TRUE if a uid range is set.  This API was wrongly introduced in the header files for 1.32, but the symbols were not exported. The API only works since 1.34 and newer."""
        pass

    def is_sealed(self) -> bool:
        """

:param self: the #NMIPRoutingRule instance
:return: whether @self is sealed. Once sealed, an instance
   cannot be modified nor unsealed."""
        pass

    def new_clone(self) -> IPRoutingRule:
        """Since 1.42, ref-counting of #NMIPRoutingRule is thread-safe.

:param self: the #NMIPRoutingRule to clone.
:return: a newly created rule instance with
   the same settings as @rule. Note that the instance will
   always be unsealed."""
        pass

    def ref(self) -> IPRoutingRule:
        """Increases the reference count of the instance.

:param self: the #NMIPRoutingRule instance
:return: the @self argument with incremented  reference count.  Since 1.42, ref-counting of #NMIPRoutingRule is thread-safe."""
        pass

    def seal(self) -> None:
        """Seals the routing rule. Afterwards, the instance can no longer be
modified, and it is a bug to call any of the accessors that would
modify the rule. If @self was already sealed, this has no effect.

:param self: the #NMIPRoutingRule instance
:return: """
        pass

    def set_action(self, action: int=None) -> None:
        """Note that currently only certain actions are allowed. nm_ip_routing_rule_validate()
will reject unsupported actions as invalid.

:param self: the #NMIPRoutingRule instance
:param action: the action to set
:return: """
        pass

    def set_destination_port(self, start: int=None, end: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param start: the start port to set.
:param end: the end port to set.
:return: """
        pass

    def set_from(self, _from: str=None, len: int=None) -> None:
        """Setting invalid values is accepted, but will later fail
during nm_ip_routing_rule_validate().

:param self: the #NMIPRoutingRule instance
:param _from: the from/src address to set.   The address family must match.
:param len: the corresponding prefix length of the address.
:return: """
        pass

    def set_fwmark(self, fwmark: int=None, fwmask: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param fwmark: the fwmark
:param fwmask: the fwmask
:return: """
        pass

    def set_iifname(self, iifname: str=None) -> None:
        """The name supports C backslash escaping for non-UTF-8 characters.
Note that nm_ip_routing_rule_from_string() too uses backslash
escaping when tokenizing the words by whitespace. So, in string
representation you'd get double backslashes.

:param self: the #NMIPRoutingRule instance.
:param iifname: the iifname to set or %NULL to unset.
:return: """
        pass

    def set_invert(self, invert: bool=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param invert: the new value to set
:return: """
        pass

    def set_ipproto(self, ipproto: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param ipproto: the ipproto to set
:return: """
        pass

    def set_oifname(self, oifname: str=None) -> None:
        """The name supports C backslash escaping for non-UTF-8 characters.
Note that nm_ip_routing_rule_from_string() too uses backslash
escaping when tokenizing the words by whitespace. So, in string
representation you'd get double backslashes.

:param self: the #NMIPRoutingRule instance.
:param oifname: the oifname to set or %NULL to unset.
:return: """
        pass

    def set_priority(self, priority: int=None) -> None:
        """A valid priority ranges from 0 to %G_MAXUINT32. "-1" is also allowed
to reset the priority. It is a bug calling this function with any
other value.

:param self: the #NMIPRoutingRule instance
:param priority: the priority to set
:return: """
        pass

    def set_source_port(self, start: int=None, end: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param start: the start port to set.
:param end: the end port to set.
:return: """
        pass

    def set_suppress_prefixlength(self, suppress_prefixlength: int=None
        ) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param suppress_prefixlength: the suppress_prefixlength to set. The value -1 means   unset.
:return: """
        pass

    def set_table(self, table: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param table: the table to set
:return: """
        pass

    def set_to(self, to: str=None, len: int=None) -> None:
        """Setting invalid values is accepted, but will later fail
during nm_ip_routing_rule_validate().

:param self: the #NMIPRoutingRule instance
:param to: the to/dst address to set.   The address family must match.
:param len: the corresponding prefix length of the address.   If @to is %NULL, this valid is ignored.
:return: """
        pass

    def set_tos(self, tos: int=None) -> None:
        """

:param self: the #NMIPRoutingRule instance
:param tos: the tos to set
:return: """
        pass

    def set_uid_range(self, uid_range_start: int=None, uid_range_end: int=None
        ) -> None:
        """For a valid range, start must be less or equal to end.
If set to an invalid range, the range gets unset.

This API was wrongly introduced in the header files for 1.32, but the
symbols were not exported. The API only works since 1.34 and newer.

:param self: the #NMIPRoutingRule instance
:param uid_range_start: the uid_range start to set.
:param uid_range_end: the uid_range start to set.
:return: """
        pass

    def to_string(self, to_string_flags: IPRoutingRuleAsStringFlags=None,
        extra_args: GLib.HashTable=None) -> str:
        """

:param self: the #NMIPRoutingRule instance to convert to string.
:param to_string_flags: #NMIPRoutingRuleAsStringFlags for controlling the   string conversion.
:param extra_args: extra arguments for controlling the string   conversion. Currently, not extra arguments are supported.
:return: the string representation or %NULL on error."""
        pass

    def unref(self) -> None:
        """Decreases the reference count of the instance and destroys
the instance if the reference count reaches zero.

Since 1.42, ref-counting of #NMIPRoutingRule is thread-safe.

:param self: the #NMIPRoutingRule instance
:return: """
        pass

    def validate(self) -> bool:
        """

:param self: the #NMIPRoutingRule instance to validate
:return: %TRUE if the rule validates."""
        pass

    @staticmethod
    def from_string(str: str=None, to_string_flags:
        IPRoutingRuleAsStringFlags=None, extra_args: GLib.HashTable=None
        ) -> IPRoutingRule:
        """

:param str: the string representation to convert to an #NMIPRoutingRule
:param to_string_flags: #NMIPRoutingRuleAsStringFlags for controlling the   string conversion.
:param extra_args: extra arguments for controlling the string   conversion. Currently, not extra arguments are supported.
:return: the new #NMIPRoutingRule or %NULL on error."""
        pass


class KeyfileHandlerData:
    """Opaque type with parameters for the callback. The actual content
depends on the %NMKeyfileHandlerType."""

    def fail_with_error(self, src: GLib.Error=None) -> None:
        """Set the error for the handler. This lets the operation fail
with the provided error. You may only set the error once.

@src must be non-%NULL.

Note that @src is no longer valid after this call. If you want
to keep using the same GError*, you need to set it to %NULL
after calling this function on it.

:param self: the #NMKeyfileHandlerData
:param src: error to move into the return location
:return: """
        pass

    def get_context(self, out_kf_group_name: str=None, out_kf_key_name: str
        =None, out_cur_setting: Setting=None, out_cur_property_name: str=None
        ) -> None:
        """Get context information of the current event. This function can be called
on all events, but the context information may be unset.

:param self: the #NMKeyfileHandlerData for any event.
:param out_kf_group_name: if the event   is in the context of a keyfile group, the group name.
:param out_kf_key_name: if the event   is in the context of a keyfile value, the key name.
:param out_cur_setting: if the event   happens while handling a particular #NMSetting instance.
:param out_cur_property_name: the   property name if applicable.
:return: """
        pass

    def warn_get(self, out_message: str=None, out_severity:
        KeyfileWarnSeverity=None) -> None:
        """

:param self: the #NMKeyfileHandlerData for a %NM_KEYFILE_HANDLER_TYPE_WARN  event.
:param out_message: the warning message.
:param out_severity: the #NMKeyfileWarnSeverity warning severity.
:return: """
        pass


class LldpNeighbor:
    """Supported attributes are:

- #NM_LLDP_ATTR_CHASSIS_ID_TYPE (type: 'u')
- #NM_LLDP_ATTR_CHASSIS_ID (type: 's')
- #NM_LLDP_ATTR_DESTINATION (type: 's')
- #NM_LLDP_ATTR_IEEE_802_1_PPVID (type: 'u'). This attribute only reports the first PPVID
  and therefore it is deprecated in favor of NM_LLDP_ATTR_IEEE_802_1_PPVIDS which reports
  all the PPVID.
- #NM_LLDP_ATTR_IEEE_802_1_PPVID_FLAGS (type: 'u'). This attribute only reports the first PPVID
  and therefore it is deprecated in favor of NM_LLDP_ATTR_IEEE_802_1_PPVIDS which reports
  all the PPVID.
- #NM_LLDP_ATTR_IEEE_802_1_PPVIDS (type: 'aa{sv}')

  An array of dictionaries where each element has keys:
  - flags (type: 'u')
  - ppvid (type: 'u')
- #NM_LLDP_ATTR_IEEE_802_1_PVID (type: 'u')
- #NM_LLDP_ATTR_IEEE_802_1_VID (type: 'u'). This attribute only reports the first VLAN
  and therefore it is deprecated in favor of NM_LLDP_ATTR_IEEE_802_1_VLANS which reports
  all the VLANs.
- #NM_LLDP_ATTR_IEEE_802_1_VLAN_NAME (type: 's'). This attribute only reports the first VLAN
  and therefore it is deprecated in favor of NM_LLDP_ATTR_IEEE_802_1_VLANS which reports
  all the VLANs.
- #NM_LLDP_ATTR_IEEE_802_1_VLANS (type: 'aa{sv}')

  An array of dictionaries where each element has keys:
  - name (type: 's')
  - vid (type: 'u')
- #NM_LLDP_ATTR_IEEE_802_3_MAC_PHY_CONF (type: 'a{sv}')

  Dictionary where each element has keys:
  - autoneg (type: 'u')
  - operational-mau-type (type: 'u')
  - pmd-autoneg-cap (type: 'u')
- #NM_LLDP_ATTR_IEEE_802_3_MAX_FRAME_SIZE (type: 'u')
- #NM_LLDP_ATTR_IEEE_802_3_POWER_VIA_MDI (type: 'a{sv}')

  Dictionary where each element has keys:
  - mdi-power-support (type: 'u')
  - power-class (type: 'u')
  - pse-power-pair (type: 'u')
- #NM_LLDP_ATTR_MANAGEMENT_ADDRESSES (type: 'aa{sv}')

  An array of dictionaries where each element has keys:
  - address (type: 'ay')
  - address-subtype (type: 'u')
  - interface-number (type: 'u')
  - interface-number-subtype (type: 'u')
  - object-id (type: 'ay')
- #NM_LLDP_ATTR_PORT_DESCRIPTION (type: 's')
- #NM_LLDP_ATTR_PORT_ID_TYPE (type: 'u')
- #NM_LLDP_ATTR_PORT_ID (type: 's')
- #NM_LLDP_ATTR_RAW (type: 'ay')
- #NM_LLDP_ATTR_SYSTEM_CAPABILITIES (type: 'u')
- #NM_LLDP_ATTR_SYSTEM_DESCRIPTION (type: 's')
- #NM_LLDP_ATTR_SYSTEM_NAME (type: 's')"""

    def __init__(self) -> None:
        """Creates a new #NMLldpNeighbor object.

Note that #NMLldpNeighbor has no public API for mutating
an instance. Also, libnm will not internally mutate a
once exposed object. They are guaranteed to be immutable.

Since 1.32, ref-counting of #NMLldpNeighbor is thread-safe.

This function is not useful, as there is no public API to
actually modify the (empty) instance.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> LldpNeighbor:
        """Creates a new #NMLldpNeighbor object.

Note that #NMLldpNeighbor has no public API for mutating
an instance. Also, libnm will not internally mutate a
once exposed object. They are guaranteed to be immutable.

Since 1.32, ref-counting of #NMLldpNeighbor is thread-safe.

This function is not useful, as there is no public API to
actually modify the (empty) instance.

:return: the new #NMLldpNeighbor object."""
        pass

    def get_attr_names(self) -> typing.Any:
        """Gets an array of attribute names available for @neighbor.

:param self: the #NMLldpNeighbor
:return: a %NULL-terminated array of attribute names."""
        pass

    def get_attr_string_value(self, name: str=None, out_value: str=None
        ) -> bool:
        """Gets the string value of attribute with name @name on @neighbor

:param self: the #NMLldpNeighbor
:param name: the attribute name
:param out_value: on return, the   attribute value
:return: %TRUE if a string attribute with name @name was found, %FALSE otherwise"""
        pass

    def get_attr_type(self, name: str=None) -> GLib.VariantType:
        """Get the type of an attribute.

:param self: the #NMLldpNeighbor
:param name: the attribute name
:return: the #GVariantType of the attribute with name @name"""
        pass

    def get_attr_uint_value(self, name: str=None, out_value: int=None) -> bool:
        """Gets the uint32 value of attribute with name @name on @neighbor

:param self: the #NMLldpNeighbor
:param name: the attribute name
:param out_value: on return, the attribute value
:return: %TRUE if a uint32 attribute with name @name was found, %FALSE otherwise"""
        pass

    def get_attr_value(self, name: str=None) -> GLib.Variant:
        """Gets the value (as a GVariant) of attribute with name @name on @neighbor

:param self: the #NMLldpNeighbor
:param name: the attribute name
:return: the value or %NULL if the attribute with @name was not found."""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

Since 1.32, ref-counting of #NMLldpNeighbor is thread-safe.

:param self: the #NMLldpNeighbor
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

Since 1.32, ref-counting of #NMLldpNeighbor is thread-safe.

:param self: the #NMLldpNeighbor
:return: """
        pass


class Object(GObject.Object):
    """"""

    def get_client(self) -> typing.Any:
        """Returns the #NMClient instance in which object is cached.
Also, if the object got removed from the client cached,
this returns %NULL. So it can be used to check whether the
object is still alive.

:param self: a #NMObject
:return: the #NMClient cache in which the object can be found, or %NULL if the object is no longer cached."""
        pass

    def get_path(self) -> str:
        """Gets the DBus path of the #NMObject.

:param self: a #NMObject
:return: the object's path. This is the internal string used by the object, and must not be modified.  Note that the D-Bus path of an NMObject never changes, even if the instance gets removed from the cache. To find out whether the object is still alive/cached, check nm_object_get_client()."""
        pass


class ObjectClass:
    """"""


class Range:
    """"""

    def __init__(self, start: int=None, end: int=None) -> None:
        """Creates a new #NMRange object for the given range. Setting @end
equal to @start creates a single-element range.

:param self: 
:param start: the first element of the range
:param end: the last element of the range, must be greater than or equal to @start.
:return: """
        pass

    @staticmethod
    def new(start: int=None, end: int=None) -> Range:
        """Creates a new #NMRange object for the given range. Setting @end
equal to @start creates a single-element range.

:param start: the first element of the range
:param end: the last element of the range, must be greater than or equal to @start.
:return: the new #NMRange object."""
        pass

    def cmp(self, b: Range=None) -> int:
        """Compare two ranges.

:param self: a #NMRange
:param b: another #NMRange
:return: zero if the two instances are equivalent or
   a non-zero integer otherwise. This defines a total ordering
   over the ranges."""
        pass

    def get_range(self, start: int=None, end: int=None) -> bool:
        """Gets the start and end values for the range.

:param self: the #NMRange
:param start: location to store the start value
:param end: location to store the end value
:return: %TRUE if the range contains more than one element, %FALSE otherwise."""
        pass

    def ref(self) -> Range:
        """Increases the reference count of the object.
This is thread-safe.

:param self: the #NMRange
:return: the input argument @range object."""
        pass

    def to_str(self) -> str:
        """Convert a %NMRange to a string.

:param self: the %NMRange
:return: a string representing the range."""
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero the object will be destroyed.
This is thread-safe.

:param self: the #NMRange
:return: """
        pass

    @staticmethod
    def from_str(str: str=None) -> Range:
        """Parses the string representation of the range to create a %NMRange
instance.

:param str: the string representation of a range
:return: the %NMRange or %NULL"""
        pass


class RemoteConnection(Object, Connection):
    """"""

    def commit_changes(self, save_to_disk: bool=None, cancellable:
        Gio.Cancellable=None) -> bool:
        """Send any local changes to the settings and properties of @connection to
NetworkManager. If @save_to_disk is %TRUE, the updated connection will be saved to
disk; if %FALSE, then only the in-memory representation will be changed.

:param self: the #NMRemoteConnection
:param save_to_disk: whether to persist the changes to disk
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def commit_changes_async(self, save_to_disk: bool=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Asynchronously sends any local changes to the settings and properties of
@connection to NetworkManager. If @save is %TRUE, the updated connection will
be saved to disk; if %FALSE, then only the in-memory representation will be
changed.

:param self: the #NMRemoteConnection
:param save_to_disk: whether to save the changes to persistent storage
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the commit operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def commit_changes_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_remote_connection_commit_changes_async().

:param self: the #NMRemoteConnection
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def delete(self, cancellable: Gio.Cancellable=None) -> bool:
        """Deletes the connection.

:param self: the #NMRemoteConnection
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def delete_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously deletes the connection.

:param self: the #NMRemoteConnection
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the delete operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def delete_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_remote_connection_delete_async().

:param self: the #NMRemoteConnection
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def get_filename(self) -> str:
        """

:param self: the #NMRemoteConnection
:return: file that stores the connection in case the connection is file-backed."""
        pass

    def get_flags(self) -> SettingsConnectionFlags:
        """

:param self: the #NMRemoteConnection
:return: the flags of the connection of type #NMSettingsConnectionFlags."""
        pass

    def get_secrets(self, setting_name: str=None, cancellable:
        Gio.Cancellable=None) -> GLib.Variant:
        """Request the connection's secrets. Note that this is a blocking D-Bus call,
not a simple property accessor.

:param self: the #NMRemoteConnection
:param setting_name: the #NMSetting object name to get secrets for
:param cancellable: a #GCancellable, or %NULL
:return: a #GVariant of type %NM_VARIANT_TYPE_CONNECTION containing @connection's secrets, or %NULL on error.  Warning: NMClient contains a cache of objects on D-Bus. This cache gets updated
   with D-Bus signals when iterating the GMainContext. This function performs a
   (pseudo) blocking D-Bus call. Aside blocking, the result will not be in sync
   and not be ordered with the content of the NMClient cache.
   This function used to be deprecated between 1.22 and 1.38 releases."""
        pass

    def get_secrets_async(self, setting_name: str=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Asynchronously requests the connection's secrets.

:param self: the #NMRemoteConnection
:param setting_name: the #NMSetting object name to get secrets for
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the secret request completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def get_secrets_finish(self, result: Gio.AsyncResult=None) -> GLib.Variant:
        """Gets the result of a call to nm_remote_connection_get_secrets_async().

:param self: the #NMRemoteConnection
:param result: the result passed to the #GAsyncReadyCallback
:return: a #GVariant of type %NM_VARIANT_TYPE_CONNECTION
   containing @connection's secrets, or %NULL on error."""
        pass

    def get_unsaved(self) -> bool:
        """

:param self: the #NMRemoteConnection
:return: %TRUE if the remote connection contains changes that have not been saved to disk, %FALSE if the connection is the same as its on-disk representation."""
        pass

    def get_version_id(self) -> int:
        """

:param self: the #NMRemoteConnection
:return: the version-id of the profile. This ID is incremented
   whenever the profile is modified."""
        pass

    def get_visible(self) -> bool:
        """Checks if the connection is visible to the current user.  If the
connection is not visible then it is essentially useless; it will
not contain any settings, and operations such as
nm_remote_connection_save() and nm_remote_connection_delete() will
always fail. (#NMRemoteSettings will not normally return
non-visible connections to callers, but it is possible for a
connection's visibility to change after you already have a
reference to it.)

:param self: the #NMRemoteConnection
:return: %TRUE if the remote connection is visible to the current user, %FALSE if not."""
        pass

    def save(self, cancellable: Gio.Cancellable=None) -> bool:
        """Saves the connection to disk if the connection has changes that have not yet
been written to disk, or if the connection has never been saved.

:param self: the #NMRemoteConnection
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def save_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Saves the connection to disk if the connection has changes that have not yet
been written to disk, or if the connection has never been saved.

:param self: the #NMRemoteConnection
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the save operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def save_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_remote_connection_save_async().

:param self: the #NMRemoteConnection
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def update2(self, settings: GLib.Variant=None, flags:
        SettingsUpdate2Flags=None, args: GLib.Variant=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Asynchronously calls the Update2() D-Bus method.

:param self: the #NMRemoteConnection
:param settings: optional connection to update the settings.
:param flags: update-flags
:param args: optional arguments.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the commit operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def update2_finish(self, result: Gio.AsyncResult=None) -> GLib.Variant:
        """Gets the result of a call to nm_remote_connection_commit_changes_async().

:param self: the #NMRemoteConnection
:param result: the result passed to the #GAsyncReadyCallback
:return: on success, a #GVariant of type "a{sv}" with the result. On failure,
   %NULL."""
        pass


class RemoteConnectionClass:
    """"""


class SecretAgentOld(GObject.Object, Gio.AsyncInitable, Gio.Initable):
    """"""

    def cancel_get_secrets(self, connection_path: str=None, setting_name:
        str=None) -> None:
        """

:param self: 
:param connection_path: 
:param setting_name: 
:return: """
        pass

    def delete_secrets(self, connection: Connection=None, connection_path:
        str=None, callback: SecretAgentOldDeleteSecretsFunc=None, user_data:
        typing.Any=None) -> None:
        """Asynchronously asks the agent to delete all saved secrets belonging to
@connection.

:param self: a #NMSecretAgentOld
:param connection: a #NMConnection
:param connection_path: 
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def get_secrets(self, connection: Connection=None, connection_path: str
        =None, setting_name: str=None, hints: typing.Any=None, flags:
        SecretAgentGetSecretsFlags=None, callback:
        SecretAgentOldGetSecretsFunc=None, user_data: typing.Any=None) -> None:
        """Asynchronously retrieves secrets belonging to @connection for the
setting @setting_name.  @flags indicate specific behavior that the secret
agent should use when performing the request, for example returning only
existing secrets without user interaction, or requesting entirely new
secrets from the user.

:param self: a #NMSecretAgentOld
:param connection: the #NMConnection for which we're asked secrets
:param connection_path: 
:param setting_name: the name of the secret setting
:param hints: hints to the agent
:param flags: flags that modify the behavior of the request
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def save_secrets(self, connection: Connection=None, connection_path:
        str=None, callback: SecretAgentOldSaveSecretsFunc=None, user_data:
        typing.Any=None) -> None:
        """Asynchronously ensures that all secrets inside @connection are stored to
disk.

:param self: a #NMSecretAgentOld
:param connection: a #NMConnection
:param connection_path: 
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def delete_secrets(self, connection: Connection=None, callback:
        SecretAgentOldDeleteSecretsFunc=None, user_data: typing.Any=None
        ) -> None:
        """Asynchronously asks the agent to delete all saved secrets belonging to
@connection.

:param self: a #NMSecretAgentOld
:param connection: a #NMConnection
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def destroy(self) -> None:
        """Since 1.24, the instance will already register a D-Bus object on the
D-Bus connection during initialization. That object will stay registered
until @self gets unrefed (destroyed) or this function is called. This
function performs the necessary cleanup to tear down the instance. Afterwards,
the function can not longer be used. This is optional, but necessary to
ensure unregistering the D-Bus object at a define point, when other users
might still have a reference on @self.

You may call this function any time and repeatedly. However, after destroying
the instance, it is a bug to still use the instance for other purposes. The
instance becomes defunct and cannot re-register.

:param self: the #NMSecretAgentOld instance.
:return: """
        pass

    def enable(self, enable: bool=None) -> None:
        """This has the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER
property.

Unlike most other functions, you may already call this function before
initialization completes.

:param self: the #NMSecretAgentOld instance
:param enable: whether to enable or disable the listener.
:return: """
        pass

    def get_context_busy_watcher(self) -> GObject.Object:
        """Returns a #GObject that stays alive as long as there are pending
requests in the #GDBusConnection. Such requests keep the #GMainContext
alive, and thus you may want to keep iterating the context as long
until a weak reference indicates that this object is gone. This is
useful because even when you destroy the instance right away (and all
the internally pending requests get cancelled), any pending g_dbus_connection_call()
requests will still invoke the result on the #GMainContext. Hence, this
allows you to know how long you must iterate the context to know
that all remains are cleaned up.

:param self: the #NMSecretAgentOld instance
:return: a #GObject that you may register a weak pointer
   to know that the #GMainContext is still kept busy by @self."""
        pass

    def get_dbus_connection(self) -> Gio.DBusConnection:
        """

:param self: the #NMSecretAgentOld instance
:return: the #GDBusConnection used by the secret agent.
   You may either set this as construct property %NM_SECRET_AGENT_OLD_DBUS_CONNECTION,
   or it will automatically set during initialization."""
        pass

    def get_dbus_name_owner(self) -> str:
        """

:param self: the #NMSecretAgentOld instance
:return: the current D-Bus name owner. While this property
   is set while registering, it really only makes sense when
   the nm_secret_agent_old_get_registered() indicates that
   registration is successful."""
        pass

    def get_main_context(self) -> GLib.MainContext:
        """

:param self: the #NMSecretAgentOld instance
:return: the #GMainContext instance associate with the
   instance. This is the g_main_context_get_thread_default() at the time
   when creating the instance."""
        pass

    def get_registered(self) -> bool:
        """Note that the secret agent transparently registers and re-registers
as the D-Bus name owner appears. Hence, this property is not really
useful. Also, to be graceful against races during registration, the
instance will already accept requests while being in the process of
registering.
If you need to avoid races and want to wait until @self is registered,
call nm_secret_agent_old_register_async(). If that function completes
with success, you know the instance is registered.

:param self: a #NMSecretAgentOld
:return: a %TRUE if the agent is registered, %FALSE if it is not."""
        pass

    def get_secrets(self, connection: Connection=None, setting_name: str=
        None, hints: typing.Any=None, flags: SecretAgentGetSecretsFlags=
        None, callback: SecretAgentOldGetSecretsFunc=None, user_data:
        typing.Any=None) -> None:
        """Asynchronously retrieves secrets belonging to @connection for the
setting @setting_name.  @flags indicate specific behavior that the secret
agent should use when performing the request, for example returning only
existing secrets without user interaction, or requesting entirely new
secrets from the user.

:param self: a #NMSecretAgentOld
:param connection: the #NMConnection for which we're asked secrets
:param setting_name: the name of the secret setting
:param hints: hints to the agent
:param flags: flags that modify the behavior of the request
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def register(self, cancellable: Gio.Cancellable=None) -> bool:
        """Registers the #NMSecretAgentOld with the NetworkManager secret manager,
indicating to NetworkManager that the agent is able to provide and save
secrets for connections on behalf of its user.

:param self: a #NMSecretAgentOld
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE if registration was successful, %FALSE on error.  Since 1.24, this can no longer fail unless the @cancellable gets cancelled. Contrary to nm_secret_agent_old_register_async(), this also does not wait for the registration to succeed. You cannot synchronously (without iterating the caller's GMainContext) wait for registration.  Since 1.24, registration is idempotent. It has the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %TRUE or nm_secret_agent_old_enable()."""
        pass

    def register_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously registers the #NMSecretAgentOld with the NetworkManager secret
manager, indicating to NetworkManager that the agent is able to provide and
save secrets for connections on behalf of its user.

Since 1.24, registration cannot fail and is idempotent. It has
the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %TRUE
or nm_secret_agent_old_enable().

Since 1.24, the asynchronous result indicates whether the instance is successfully
registered. In any case, this call enables the agent and it will automatically
try to register and handle secret requests. A failure of this function only indicates
that currently the instance might not be ready (but since it will automatically
try to recover, it might be ready in a moment afterwards). Use this function if
you want to check and ensure that the agent is registered.

:param self: a #NMSecretAgentOld
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to call when the agent is registered
:param user_data: data for @callback
:return: """
        pass

    def register_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_secret_agent_old_register_async().

:param self: a #NMSecretAgentOld
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE if registration was successful, %FALSE on error.  Since 1.24, registration cannot fail and is idempotent. It has the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %TRUE or nm_secret_agent_old_enable()."""
        pass

    def save_secrets(self, connection: Connection=None, callback:
        SecretAgentOldSaveSecretsFunc=None, user_data: typing.Any=None
        ) -> None:
        """Asynchronously ensures that all secrets inside @connection are stored to
disk.

:param self: a #NMSecretAgentOld
:param connection: a #NMConnection
:param callback: a callback, to be invoked when the operation is done
:param user_data: caller-specific data to be passed to @callback
:return: """
        pass

    def unregister(self, cancellable: Gio.Cancellable=None) -> bool:
        """Unregisters the #NMSecretAgentOld with the NetworkManager secret manager,
indicating to NetworkManager that the agent will no longer provide or
store secrets on behalf of this user.

:param self: a #NMSecretAgentOld
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE if unregistration was successful, %FALSE on error  Since 1.24, registration cannot fail and is idempotent. It has the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %FALSE or nm_secret_agent_old_enable()."""
        pass

    def unregister_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously unregisters the #NMSecretAgentOld with the NetworkManager secret
manager, indicating to NetworkManager that the agent will no longer provide
or store secrets on behalf of this user.

Since 1.24, registration cannot fail and is idempotent. It has
the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %FALSE
or nm_secret_agent_old_enable().

:param self: a #NMSecretAgentOld
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to call when the agent is unregistered
:param user_data: data for @callback
:return: """
        pass

    def unregister_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_secret_agent_old_unregister_async().

:param self: a #NMSecretAgentOld
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE if unregistration was successful, %FALSE on error.  Since 1.24, registration cannot fail and is idempotent. It has the same effect as setting %NM_SECRET_AGENT_OLD_AUTO_REGISTER to %FALSE or nm_secret_agent_old_enable()."""
        pass
    parent: GObject.Object


class SecretAgentOldClass:
    """"""
    parent: GObject.ObjectClass
    get_secrets: typing.Any
    cancel_get_secrets: typing.Any
    save_secrets: typing.Any
    delete_secrets: typing.Any
    padding: typing.Any


class Setting(GObject.Object):
    """"""

    @staticmethod
    def get_enum_property_type(setting_type: GType=None, property_name: str
        =None) -> GType:
        """Get the type of the enum that defines the values that the property accepts. It is only
useful for properties configured to accept values from certain enum type, otherwise
it will return %G_TYPE_INVALID. Note that flags (children of G_TYPE_FLAGS) are also
considered enums.

Note that the GObject property might be implemented as an integer, actually, and not
as enum. Find out what underlying type is used, checking the #GParamSpec, before
setting the GObject property.

:param setting_type: the GType of the NMSetting instance
:param property_name: the name of the property
:return: the enum's GType, or %G_TYPE_INVALID if the property is not of enum type"""
        pass

    @staticmethod
    def lookup_type(name: str=None) -> GType:
        """Returns the #GType of the setting's class for a given setting name.

:param name: a setting name
:return: the #GType of the setting's class, or %G_TYPE_INVALID if
   @name is not recognized."""
        pass

    def compare(self, b: Setting=None, flags: SettingCompareFlags=None
        ) -> bool:
        """Compares two #NMSetting objects for similarity, with comparison behavior
modified by a set of flags.  See the documentation for #NMSettingCompareFlags
for a description of each flag's behavior.

:param self: a #NMSetting
:param b: a second #NMSetting to compare with the first
:param flags: compare flags, e.g. %NM_SETTING_COMPARE_FLAG_EXACT
:return: %TRUE if the comparison succeeds, %FALSE if it does not"""
        pass

    def diff(self, b: Setting=None, flags: SettingCompareFlags=None,
        invert_results: bool=None, results: GLib.HashTable=None) -> bool:
        """Compares two #NMSetting objects for similarity, with comparison behavior
modified by a set of flags.  See the documentation for #NMSettingCompareFlags
for a description of each flag's behavior.  If the settings differ, the keys
of each setting that differ from the other are added to @results, mapped to
one or more #NMSettingDiffResult values.

:param self: a #NMSetting
:param b: a second #NMSetting to compare with the first
:param flags: compare flags, e.g. %NM_SETTING_COMPARE_FLAG_EXACT
:param invert_results: this parameter is used internally by libnm and should be set to %FALSE.  If %TRUE inverts the meaning of the #NMSettingDiffResult.
:param results: if the settings differ, on return a hash table mapping the differing keys to one or more %NMSettingDiffResult values OR-ed together.  If the settings do not differ, any hash table passed in is unmodified.  If no hash table is passed in and the settings differ, a new one is created and returned.
:return: %TRUE if the settings contain the same values, %FALSE if they do not"""
        pass

    def duplicate(self) -> Setting:
        """Duplicates a #NMSetting.

:param self: the #NMSetting to duplicate
:return: a new #NMSetting containing the same properties and values as the source #NMSetting"""
        pass

    def enumerate_values(self, func: SettingValueIterFn=None, user_data:
        typing.Any=None) -> None:
        """Iterates over each property of the #NMSetting object, calling the supplied
user function for each property.

:param self: the #NMSetting
:param func: user-supplied function called for each property of the setting
:param user_data: user data passed to @func at each invocation
:return: """
        pass

    def get_dbus_property_type(self, property_name: str=None
        ) -> GLib.VariantType:
        """Gets the D-Bus marshalling type of a property. @property_name is a D-Bus
property name, which may not necessarily be a #GObject property.

:param self: an #NMSetting
:param property_name: the property of @setting to get the type of
:return: the D-Bus marshalling type of @property on @setting."""
        pass

    def get_name(self) -> str:
        """Returns the type name of the #NMSetting object

:param self: the #NMSetting
:return: a string containing the type name of the #NMSetting object, like 'ppp' or 'wireless' or 'wired'."""
        pass

    def get_secret_flags(self, secret_name: str=None, out_flags:
        SettingSecretFlags=None) -> bool:
        """For a given secret, retrieves the #NMSettingSecretFlags describing how to
handle that secret.

:param self: the #NMSetting
:param secret_name: the secret key name to get flags for
:param out_flags: on success, the #NMSettingSecretFlags for the secret
:return: %TRUE on success (if the given secret name was a valid property of this setting, and if that property is secret), %FALSE if not"""
        pass

    def option_clear_by_name(self, predicate: UtilsPredicateStr=None) -> None:
        """

:param self: the #NMSetting
:param predicate: the predicate for which names   should be clear.   If the predicate returns %TRUE for an option name, the option   gets removed. If %NULL, all options will be removed.
:return: """
        pass

    def option_get(self, opt_name: str=None) -> GLib.Variant:
        """

:param self: the #NMSetting
:param opt_name: the option name to request.
:return: the #GVariant or %NULL if the option
   is not set."""
        pass

    def option_get_all_names(self, out_len: int=None) -> typing.Any:
        """Gives the name of all set options.

:param self: the #NMSetting
:param out_len: 
:return: A %NULL terminated array of key names. If no names are present, this returns
   %NULL. The returned array and the names are owned by %NMSetting and might be invalidated
   by the next operation."""
        pass

    def option_get_boolean(self, opt_name: str=None, out_value: bool=None
        ) -> bool:
        """

:param self: the #NMSetting
:param opt_name: the option to get
:param out_value: the optional output value.   If the option is unset, %FALSE will be returned.
:return: %TRUE if @opt_name is set to a boolean variant."""
        pass

    def option_get_uint32(self, opt_name: str=None, out_value: int=None
        ) -> bool:
        """

:param self: the #NMSetting
:param opt_name: the option to get
:param out_value: the optional output value.   If the option is unset, 0 will be returned.
:return: %TRUE if @opt_name is set to a uint32 variant."""
        pass

    def option_set(self, opt_name: str=None, variant: GLib.Variant=None
        ) -> None:
        """If @variant is %NULL, this clears the option if it is set.
Otherwise, @variant is set as the option. If @variant is
a floating reference, it will be consumed.

Note that not all setting types support options. It is a bug
setting a variant to a setting that doesn't support it.
Currently, only #NMSettingEthtool supports it.

:param self: the #NMSetting
:param opt_name: the option name to set
:param variant: the variant to set.
:return: """
        pass

    def option_set_boolean(self, opt_name: str=None, value: bool=None) -> None:
        """Like nm_setting_option_set() to set a boolean GVariant.

:param self: the #NMSetting
:param opt_name: 
:param value: the value to set.
:return: """
        pass

    def option_set_uint32(self, opt_name: str=None, value: int=None) -> None:
        """Like nm_setting_option_set() to set a uint32 GVariant.

:param self: the #NMSetting
:param opt_name: 
:param value: the value to set.
:return: """
        pass

    def set_secret_flags(self, secret_name: str=None, flags:
        SettingSecretFlags=None) -> bool:
        """For a given secret, stores the #NMSettingSecretFlags describing how to
handle that secret.

:param self: the #NMSetting
:param secret_name: the secret key name to set flags for
:param flags: the #NMSettingSecretFlags for the secret
:return: %TRUE on success (if the given secret name was a valid property of this setting, and if that property is secret), %FALSE if not"""
        pass

    def to_string(self) -> str:
        """Convert the setting (including secrets!) into a string. For debugging
purposes ONLY, should NOT be used for serialization of the setting,
or machine-parsed in any way. The output format is not guaranteed to
be stable and may change at any time.

:param self: the #NMSetting
:return: an allocated string containing a textual representation of the setting's properties and values, which the caller should free with g_free()"""
        pass

    def verify(self, connection: Connection=None) -> bool:
        """Validates the setting.  Each setting's properties have allowed values, and
some are dependent on other values (hence the need for @connection).  The
returned #GError contains information about which property of the setting
failed validation, and in what way that property failed validation.

:param self: the #NMSetting to verify
:param connection: the #NMConnection that @setting came from, or   %NULL if @setting is being verified in isolation.
:return: %TRUE if the setting is valid, %FALSE if it is not"""
        pass

    def verify_secrets(self, connection: Connection=None) -> bool:
        """Verifies the secrets in the setting.
The returned #GError contains information about which secret of the setting
failed validation, and in what way that secret failed validation.
The secret validation is done separately from main setting validation, because
in some cases connection failure is not desired just for the secrets.

:param self: the #NMSetting to verify secrets in
:param connection: the #NMConnection that @setting came from, or   %NULL if @setting is being verified in isolation.
:return: %TRUE if the setting secrets are valid, %FALSE if they are not"""
        pass


class Setting6Lowpan(Setting):
    """6LoWPAN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSetting6Lowpan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSetting6Lowpan object with default values.

:return: the new empty #NMSetting6Lowpan object"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSetting6Lowpan
:return: the #NMSetting6Lowpan:parent property of the setting"""
        pass


class Setting6LowpanClass:
    """"""


class Setting8021x(Setting):
    """IEEE 802.1x Authentication Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSetting8021x object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSetting8021x object with default values.

:return: the new empty #NMSetting8021x object"""
        pass

    @staticmethod
    def check_cert_scheme(pdata: typing.Any=None, length: int=None
        ) -> Setting8021xCKScheme:
        """Determines and verifies the blob type.
When setting certificate properties of NMSetting8021x
the blob must be not UNKNOWN (or NULL).

:param pdata: the data pointer
:param length: the length of the data
:return: the scheme of the blob or %NM_SETTING_802_1X_CK_SCHEME_UNKNOWN. For NULL it also returns NM_SETTING_802_1X_CK_SCHEME_UNKNOWN."""
        pass

    def add_altsubject_match(self, altsubject_match: str=None) -> bool:
        """Adds an allowed alternate subject name match.  Until at least one
match is added, the altSubjectName of the remote authentication
server is not verified.

:param self: the #NMSetting8021x
:param altsubject_match: the altSubjectName to allow for this connection
:return: %TRUE if the alternative subject name match was  successfully added, %FALSE if it was already allowed."""
        pass

    def add_eap_method(self, eap: str=None) -> bool:
        """Adds an allowed EAP method.  The setting is not valid until at least one
EAP method has been added.  See #NMSetting8021x:eap property for a list of
allowed EAP methods.

:param self: the #NMSetting8021x
:param eap: the name of the EAP method to allow for this connection
:return: %TRUE if the EAP method was successfully added, %FALSE if it was  not a valid method or if it was already allowed."""
        pass

    def add_phase2_altsubject_match(self, phase2_altsubject_match: str=None
        ) -> bool:
        """Adds an allowed alternate subject name match for "phase 2".  Until
at least one match is added, the altSubjectName of the "phase 2"
remote authentication server is not verified.

:param self: the #NMSetting8021x
:param phase2_altsubject_match: the "phase 2" altSubjectName to allow for this connection
:return: %TRUE if the "phase 2" alternative subject name match was  successfully added, %FALSE if it was already allowed."""
        pass

    def clear_altsubject_matches(self) -> None:
        """Clears all altSubjectName matches.

:param self: the #NMSetting8021x
:return: """
        pass

    def clear_eap_methods(self) -> None:
        """Clears all allowed EAP methods.

:param self: the #NMSetting8021x
:return: """
        pass

    def clear_phase2_altsubject_matches(self) -> None:
        """Clears all "phase 2" altSubjectName matches.

:param self: the #NMSetting8021x
:return: """
        pass

    def get_altsubject_match(self, i: int=None) -> str:
        """Returns the altSubjectName match at index @i.

:param self: the #NMSettingConnection
:param i: the zero-based index of the array of altSubjectName matches
:return: the altSubjectName match at index @i"""
        pass

    def get_anonymous_identity(self) -> str:
        """Returns the anonymous identifier used by some EAP methods (like TTLS) to
authenticate the user in the outer unencrypted "phase 1" authentication.  The
inner "phase 2" authentication will use the #NMSetting8021x:identity in
a secure form, if applicable for that EAP method.

:param self: the #NMSetting8021x
:return: the anonymous identifier"""
        pass

    def get_auth_timeout(self) -> int:
        """Returns the value contained in the #NMSetting8021x:auth-timeout property.

:param self: the #NMSetting8021x
:return: the configured authentication timeout in seconds. Zero means the global default value."""
        pass

    def get_ca_cert_blob(self) -> GLib.Bytes:
        """Returns the CA certificate blob if the CA certificate is stored using the
%NM_SETTING_802_1X_CK_SCHEME_BLOB scheme.  Not all EAP methods use a
CA certificate (LEAP for example), and those that can take advantage of the
CA certificate allow it to be unset.  Note that lack of a CA certificate
reduces security by allowing man-in-the-middle attacks, because the identity
of the network cannot be confirmed by the client.

:param self: the #NMSetting8021x
:return: the CA certificate data"""
        pass

    def get_ca_cert_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the password used to access the CA certificate stored in #NMSetting8021x:ca-cert property. Only makes sense if the certificate is stored on a PKCS#<!-- -->11 token that requires a login."""
        pass

    def get_ca_cert_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:ca-cert-password"""
        pass

    def get_ca_cert_path(self) -> str:
        """Returns the CA certificate path if the CA certificate is stored using the
%NM_SETTING_802_1X_CK_SCHEME_PATH scheme.  Not all EAP methods use a
CA certificate (LEAP for example), and those that can take advantage of the
CA certificate allow it to be unset.  Note that lack of a CA certificate
reduces security by allowing man-in-the-middle attacks, because the identity
of the network cannot be confirmed by the client.

:param self: the #NMSetting8021x
:return: path to the CA certificate file"""
        pass

    def get_ca_cert_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the CA certificate.  If the returned scheme
is %NM_SETTING_802_1X_CK_SCHEME_BLOB, use nm_setting_802_1x_get_ca_cert_blob();
if %NM_SETTING_802_1X_CK_SCHEME_PATH, use nm_setting_802_1x_get_ca_cert_path();
if %NM_SETTING_802_1X_CK_SCHEME_PKCS11, use nm_setting_802_1x_get_ca_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the CA certificate (blob or path)"""
        pass

    def get_ca_cert_uri(self) -> str:
        """Returns the CA certificate URI analogously to
nm_setting_802_1x_get_ca_cert_blob() and
nm_setting_802_1x_get_ca_cert_path().

Currently, it's limited to PKCS#11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_ca_path(self) -> str:
        """Returns the path of the CA certificate directory if previously set.  Systems
will often have a directory that contains multiple individual CA certificates
which the supplicant can then add to the verification chain.  This may be
used in addition to the #NMSetting8021x:ca-cert property to add more CA
certificates for verifying the network to client.

:param self: the #NMSetting8021x
:return: the CA certificate directory path"""
        pass

    def get_client_cert_blob(self) -> GLib.Bytes:
        """Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: the client certificate data"""
        pass

    def get_client_cert_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the password used to access the client certificate stored in #NMSetting8021x:client-cert property. Only makes sense if the certificate is stored on a PKCS#<!-- -->11 token that requires a login."""
        pass

    def get_client_cert_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:client-cert-password"""
        pass

    def get_client_cert_path(self) -> str:
        """Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: path to the client certificate file"""
        pass

    def get_client_cert_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the client certificate.  If the returned scheme
is %NM_SETTING_802_1X_CK_SCHEME_BLOB, use nm_setting_802_1x_get_client_cert_blob();
if %NM_SETTING_802_1X_CK_SCHEME_PATH, use nm_setting_802_1x_get_client_cert_path();
if %NM_SETTING_802_1X_CK_SCHEME_PKCS11, use nm_setting_802_1x_get_client_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the client certificate (blob or path)"""
        pass

    def get_client_cert_uri(self) -> str:
        """Returns the client certificate URI analogously to
nm_setting_802_1x_get_client_cert_blob() and
nm_setting_802_1x_get_client_cert_path().

Currently, it's limited to PKCS#11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_domain_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:domain-match property."""
        pass

    def get_domain_suffix_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:domain-suffix-match property."""
        pass

    def get_eap_method(self, i: int=None) -> str:
        """Returns the name of the allowed EAP method at index @i.

:param self: the #NMSetting8021x
:param i: the index of the EAP method name to return
:return: the name of the allowed EAP method at index @i"""
        pass

    def get_identity(self) -> str:
        """Returns the identifier used by some EAP methods (like TLS) to
authenticate the user.  Often this is a username or login name.

:param self: the #NMSetting8021x
:return: the user identifier"""
        pass

    def get_num_altsubject_matches(self) -> int:
        """Returns the number of entries in the
#NMSetting8021x:altsubject-matches property of this setting.

:param self: the #NMSetting8021x
:return: the number of altsubject-matches entries."""
        pass

    def get_num_eap_methods(self) -> int:
        """Returns the number of eap methods allowed for use when connecting to the
network.  Generally only one EAP method is used.  Use the functions
nm_setting_802_1x_get_eap_method(), nm_setting_802_1x_add_eap_method(),
and nm_setting_802_1x_remove_eap_method() for adding, removing, and retrieving
allowed EAP methods.

:param self: the #NMSetting8021x
:return: the number of allowed EAP methods"""
        pass

    def get_num_phase2_altsubject_matches(self) -> int:
        """Returns the number of entries in the
#NMSetting8021x:phase2-altsubject-matches property of this setting.

:param self: the #NMSetting8021x
:return: the number of phase2-altsubject-matches entries."""
        pass

    def get_openssl_ciphers(self) -> str:
        """Returns the openssl_ciphers configuration for wpa_supplicant.

:param self: the #NMSetting8021x
:return: cipher string for tls setup in wpa_supplicant."""
        pass

    def get_optional(self) -> bool:
        """Returns the value contained in the #NMSetting8021x:optional property.

:param self: the #NMSetting8021x
:return: %TRUE if the activation should proceed even when the 802.1X
     authentication fails; %FALSE otherwise"""
        pass

    def get_pac_file(self) -> str:
        """Returns the file containing PAC credentials used by EAP-FAST method.

:param self: the #NMSetting8021x
:return: the PAC file"""
        pass

    def get_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the password used by the authentication method, if any, as specified
   by the #NMSetting8021x:password property"""
        pass

    def get_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:password"""
        pass

    def get_password_raw(self) -> GLib.Bytes:
        """

:param self: the #NMSetting8021x
:return: the password used by the authentication method as a UTF-8-encoded array of bytes, as specified by the #NMSetting8021x:password-raw property"""
        pass

    def get_password_raw_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the
   #NMSetting8021x:password-raw"""
        pass

    def get_phase1_auth_flags(self) -> Setting8021xAuthFlags:
        """

:param self: the #NMSetting8021x
:return: the authentication flags for "phase 1"."""
        pass

    def get_phase1_fast_provisioning(self) -> str:
        """

:param self: the #NMSetting8021x
:return: whether "phase 1" PEAP fast provisioning should be used, as specified  by the #NMSetting8021x:phase1-fast-provisioning property.  See the  wpa_supplicant documentation for more details."""
        pass

    def get_phase1_peaplabel(self) -> str:
        """

:param self: the #NMSetting8021x
:return: whether the "phase 1" PEAP label is new-style or old-style, to be  used when authenticating with EAP-PEAP, as contained in the  #NMSetting8021x:phase1-peaplabel property.  Valid values are %NULL (unset),  "0" (use old-style label), and "1" (use new-style label).  See the  wpa_supplicant documentation for more details."""
        pass

    def get_phase1_peapver(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the "phase 1" PEAP version to be used when authenticating with  EAP-PEAP as contained in the #NMSetting8021x:phase1-peapver property.  Valid  values are %NULL (unset), "0" (PEAP version 0), and "1" (PEAP version 1)."""
        pass

    def get_phase2_altsubject_match(self, i: int=None) -> str:
        """Returns the "phase 2" altSubjectName match at index @i.

:param self: the #NMSettingConnection
:param i: the zero-based index of the array of "phase 2" altSubjectName matches
:return: the "phase 2" altSubjectName match at index @i"""
        pass

    def get_phase2_auth(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the "phase 2" non-EAP (ex MD5) allowed authentication method as
   specified by the #NMSetting8021x:phase2-auth property."""
        pass

    def get_phase2_autheap(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the "phase 2" EAP-based (ex TLS) allowed authentication method as
   specified by the #NMSetting8021x:phase2-autheap property."""
        pass

    def get_phase2_ca_cert_blob(self) -> GLib.Bytes:
        """Returns the "phase 2" CA certificate blob if the CA certificate is stored
using the %NM_SETTING_802_1X_CK_SCHEME_BLOB scheme.  Not all EAP methods use
a CA certificate (LEAP for example), and those that can take advantage of the
CA certificate allow it to be unset.  Note that lack of a CA certificate
reduces security by allowing man-in-the-middle attacks, because the identity
of the network cannot be confirmed by the client.

:param self: the #NMSetting8021x
:return: the "phase 2" CA certificate data"""
        pass

    def get_phase2_ca_cert_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the password used to access the "phase2" CA certificate stored in #NMSetting8021x:phase2-ca-cert property. Only makes sense if the certificate is stored on a PKCS#<!-- -->11 token that requires a login."""
        pass

    def get_phase2_ca_cert_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:phase2-private-key-password"""
        pass

    def get_phase2_ca_cert_path(self) -> str:
        """Returns the "phase 2" CA certificate path if the CA certificate is stored
using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.  Not all EAP methods use
a CA certificate (LEAP for example), and those that can take advantage of the
CA certificate allow it to be unset.  Note that lack of a CA certificate
reduces security by allowing man-in-the-middle attacks, because the identity
of the network cannot be confirmed by the client.

:param self: the #NMSetting8021x
:return: path to the "phase 2" CA certificate file"""
        pass

    def get_phase2_ca_cert_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the "phase 2" CA certificate.  If the
returned scheme is %NM_SETTING_802_1X_CK_SCHEME_BLOB, use
nm_setting_802_1x_get_ca_cert_blob(); if %NM_SETTING_802_1X_CK_SCHEME_PATH,
use nm_setting_802_1x_get_ca_cert_path(); if %NM_SETTING_802_1X_CK_SCHEME_PKCS11,
use nm_setting_802_1x_get_ca_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the "phase 2" CA certificate (blob or path)"""
        pass

    def get_phase2_ca_cert_uri(self) -> str:
        """Returns the "phase 2" CA certificate URI analogously to
nm_setting_802_1x_get_phase2_ca_cert_blob() and
nm_setting_802_1x_get_phase2_ca_cert_path().

Currently, it's limited to PKCS#<!-- -->11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_phase2_ca_path(self) -> str:
        """Returns the path of the "phase 2" CA certificate directory if previously set.
Systems will often have a directory that contains multiple individual CA
certificates which the supplicant can then add to the verification chain.
This may be used in addition to the #NMSetting8021x:phase2-ca-cert property
to add more CA certificates for verifying the network to client.

:param self: the #NMSetting8021x
:return: the "phase 2" CA certificate directory path"""
        pass

    def get_phase2_client_cert_blob(self) -> GLib.Bytes:
        """Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: the "phase 2" client certificate data"""
        pass

    def get_phase2_client_cert_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the password used to access the "phase2" client certificate stored in #NMSetting8021x:phase2-client-cert property. Only makes sense if the certificate is stored on a PKCS#<!-- -->11 token that requires a login."""
        pass

    def get_phase2_client_cert_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:phase2-client-cert-password"""
        pass

    def get_phase2_client_cert_path(self) -> str:
        """Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: path to the "phase 2" client certificate file"""
        pass

    def get_phase2_client_cert_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the "phase 2" client certificate.  If the
returned scheme is %NM_SETTING_802_1X_CK_SCHEME_BLOB, use
nm_setting_802_1x_get_client_cert_blob(); if
%NM_SETTING_802_1X_CK_SCHEME_PATH, use
nm_setting_802_1x_get_client_cert_path(); if
%NM_SETTING_802_1X_CK_SCHEME_PKCS11, use
nm_setting_802_1x_get_client_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the "phase 2" client certificate (blob or path)"""
        pass

    def get_phase2_client_cert_uri(self) -> str:
        """Returns the "phase 2" client certificate URI analogously to
nm_setting_802_1x_get_phase2_ca_cert_blob() and
nm_setting_802_1x_get_phase2_ca_cert_path().

Currently, it's limited to PKCS#<!-- -->11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_phase2_domain_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:phase2-domain-match property."""
        pass

    def get_phase2_domain_suffix_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:phase2-domain-suffix-match property."""
        pass

    def get_phase2_private_key_blob(self) -> GLib.Bytes:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

WARNING: the phase2 private key property is not a "secret" property, and thus
unencrypted private key data may be readable by unprivileged users.  Private
keys should always be encrypted with a private key password.

:param self: the #NMSetting8021x
:return: the "phase 2" private key data"""
        pass

    def get_phase2_private_key_format(self) -> Setting8021xCKFormat:
        """

:param self: the #NMSetting8021x
:return: the data format of the "phase 2" private key data stored in the
   #NMSetting8021x:phase2-private-key property"""
        pass

    def get_phase2_private_key_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the private key password used to decrypt the private key if  previously set with nm_setting_802_1x_set_phase2_private_key() or the  #NMSetting8021x:phase2-private-key-password property."""
        pass

    def get_phase2_private_key_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:phase2-private-key-password"""
        pass

    def get_phase2_private_key_path(self) -> str:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: path to the "phase 2" private key file"""
        pass

    def get_phase2_private_key_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the "phase 2" private key.  If the returned
scheme is %NM_SETTING_802_1X_CK_SCHEME_BLOB, use
nm_setting_802_1x_get_client_cert_blob(); if
%NM_SETTING_802_1X_CK_SCHEME_PATH, use
nm_setting_802_1x_get_client_cert_path(); if
%NM_SETTING_802_1X_CK_SCHEME_PKCS11, use
nm_setting_802_1x_get_client_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the "phase 2" private key (blob or path)"""
        pass

    def get_phase2_private_key_uri(self) -> str:
        """Returns the "phase 2" private key URI analogously to
nm_setting_802_1x_get_phase2_private_key_blob() and
nm_setting_802_1x_get_phase2_private_key_path().

Currently, it's limited to PKCS#<!-- -->11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_phase2_subject_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:phase2-subject-match property. This is the substring to be matched against the subject of the "phase 2" authentication server certificate, or %NULL no subject verification is to be performed."""
        pass

    def get_pin(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the PIN used by the authentication method, if any, as specified
   by the #NMSetting8021x:pin property"""
        pass

    def get_pin_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:pin"""
        pass

    def get_private_key_blob(self) -> GLib.Bytes:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

WARNING: the private key property is not a "secret" property, and thus
unencrypted private key data may be readable by unprivileged users.  Private
keys should always be encrypted with a private key password.

:param self: the #NMSetting8021x
:return: the private key data"""
        pass

    def get_private_key_format(self) -> Setting8021xCKFormat:
        """

:param self: the #NMSetting8021x
:return: the data format of the private key data stored in the
   #NMSetting8021x:private-key property"""
        pass

    def get_private_key_password(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the private key password used to decrypt the private key if  previously set with nm_setting_802_1x_set_private_key(), or the  #NMSetting8021x:private-key-password property."""
        pass

    def get_private_key_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSetting8021x
:return: the #NMSettingSecretFlags pertaining to the #NMSetting8021x:private-key-password"""
        pass

    def get_private_key_path(self) -> str:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:return: path to the private key file"""
        pass

    def get_private_key_scheme(self) -> Setting8021xCKScheme:
        """Returns the scheme used to store the private key.  If the returned scheme is
%NM_SETTING_802_1X_CK_SCHEME_BLOB, use
nm_setting_802_1x_get_client_cert_blob(); if
%NM_SETTING_802_1X_CK_SCHEME_PATH, use
nm_setting_802_1x_get_client_cert_path(); if
%NM_SETTING_802_1X_CK_SCHEME_PKCS11, use
nm_setting_802_1x_get_client_cert_uri().

:param self: the #NMSetting8021x
:return: scheme used to store the private key (blob or path)"""
        pass

    def get_private_key_uri(self) -> str:
        """Returns the private key URI analogously to
nm_setting_802_1x_get_private_key_blob() and
nm_setting_802_1x_get_private_key_path().

Currently, it's limited to PKCS#<!-- -->11 URIs ('pkcs11' scheme as defined by RFC
7512), but may be extended to other schemes in future (such as 'file' URIs
for local files and 'data' URIs for inline certificate data).

:param self: the #NMSetting8021x
:return: the URI string"""
        pass

    def get_subject_match(self) -> str:
        """

:param self: the #NMSetting8021x
:return: the #NMSetting8021x:subject-match property. This is the substring to be matched against the subject of the authentication server certificate, or %NULL no subject verification is to be performed."""
        pass

    def get_system_ca_certs(self) -> bool:
        """Sets the #NMSetting8021x:system-ca-certs property. The
#NMSetting8021x:ca-path and #NMSetting8021x:phase2-ca-path
properties are ignored if the #NMSetting8021x:system-ca-certs property is
%TRUE, in which case a system-wide CA certificate directory specified at
compile time (using the --system-ca-path configure option) is used in place
of these properties.

:param self: the #NMSetting8021x
:return: %TRUE if a system CA certificate path should be used, %FALSE if not"""
        pass

    def remove_altsubject_match(self, i: int=None) -> None:
        """Removes the allowed altSubjectName at the specified index.

:param self: the #NMSetting8021x
:param i: the index of the altSubjectName match to remove
:return: """
        pass

    def remove_altsubject_match_by_value(self, altsubject_match: str=None
        ) -> bool:
        """Removes the allowed altSubjectName @altsubject_match.

:param self: the #NMSetting8021x
:param altsubject_match: the altSubjectName to remove
:return: %TRUE if the alternative subject name match was found and removed,
          %FALSE if it was not."""
        pass

    def remove_eap_method(self, i: int=None) -> None:
        """Removes the allowed EAP method at the specified index.

:param self: the #NMSetting8021x
:param i: the index of the EAP method to remove
:return: """
        pass

    def remove_eap_method_by_value(self, eap: str=None) -> bool:
        """Removes the allowed EAP method @method.

:param self: the #NMSetting8021x
:param eap: the name of the EAP method to remove
:return: %TRUE if the EAP method was founs and removed, %FALSE if it was not."""
        pass

    def remove_phase2_altsubject_match(self, i: int=None) -> None:
        """Removes the allowed "phase 2" altSubjectName at the specified index.

:param self: the #NMSetting8021x
:param i: the index of the "phase 2" altSubjectName match to remove
:return: """
        pass

    def remove_phase2_altsubject_match_by_value(self,
        phase2_altsubject_match: str=None) -> bool:
        """Removes the allowed "phase 2" altSubjectName @phase2_altsubject_match.

:param self: the #NMSetting8021x
:param phase2_altsubject_match: the "phase 2" altSubjectName to remove
:return: %TRUE if the alternative subject name match for "phase 2" was found and removed,
          %FALSE if it was not."""
        pass

    def set_ca_cert(self, value: str=None, scheme: Setting8021xCKScheme=
        None, out_format: Setting8021xCKFormat=None) -> bool:
        """Reads a certificate from disk and sets the #NMSetting8021x:ca-cert property
with the raw certificate data if using the %NM_SETTING_802_1X_CK_SCHEME_BLOB
scheme, or with the path to the certificate file if using the
%NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH   or %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the CA certificate   file (PEM or DER format).  The path must be UTF-8 encoded; use   g_filename_to_utf8() to convert if needed.  Passing %NULL with any @scheme   clears the CA certificate.
:param scheme: desired storage scheme for the certificate
:param out_format: on successful return, the type of the certificate added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass

    def set_client_cert(self, value: str=None, scheme: Setting8021xCKScheme
        =None, out_format: Setting8021xCKFormat=None) -> bool:
        """Reads a certificate from disk and sets the #NMSetting8021x:client-cert
property with the raw certificate data if using the
%NM_SETTING_802_1X_CK_SCHEME_BLOB scheme, or with the path to the certificate
file if using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH   or %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the client   certificate file (PEM, DER, or PKCS#<!-- -->12 format).  The path must be UTF-8   encoded; use g_filename_to_utf8() to convert if needed.  Passing %NULL with   any @scheme clears the client certificate.
:param scheme: desired storage scheme for the certificate
:param out_format: on successful return, the type of the certificate added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass

    def set_phase2_ca_cert(self, value: str=None, scheme:
        Setting8021xCKScheme=None, out_format: Setting8021xCKFormat=None
        ) -> bool:
        """Reads a certificate from disk and sets the #NMSetting8021x:phase2-ca-cert
property with the raw certificate data if using the
%NM_SETTING_802_1X_CK_SCHEME_BLOB scheme, or with the path to the certificate
file if using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH   or %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the "phase2" CA   certificate file (PEM or DER format).  The path must be UTF-8 encoded; use   g_filename_to_utf8() to convert if needed.  Passing %NULL with any @scheme   clears the "phase2" CA certificate.
:param scheme: desired storage scheme for the certificate
:param out_format: on successful return, the type of the certificate added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass

    def set_phase2_client_cert(self, value: str=None, scheme:
        Setting8021xCKScheme=None, out_format: Setting8021xCKFormat=None
        ) -> bool:
        """Reads a certificate from disk and sets the #NMSetting8021x:phase2-client-cert
property with the raw certificate data if using the
%NM_SETTING_802_1X_CK_SCHEME_BLOB scheme, or with the path to the certificate
file if using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

Client certificates are used to identify the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH   or %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the "phase2" client   certificate file (PEM, DER, or PKCS#<!-- -->12 format).  The path must be UTF-8   encoded; use g_filename_to_utf8() to convert if needed.  Passing %NULL with   any @scheme clears the "phase2" client certificate.
:param scheme: desired storage scheme for the certificate
:param out_format: on successful return, the type of the certificate added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass

    def set_phase2_private_key(self, value: str=None, password: str=None,
        scheme: Setting8021xCKScheme=None, out_format: Setting8021xCKFormat
        =None) -> bool:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

This function reads a private key from disk and sets the
#NMSetting8021x:phase2-private-key property with the private key file data if
using the %NM_SETTING_802_1X_CK_SCHEME_BLOB scheme, or with the path to the
private key file if using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

If @password is given, this function attempts to decrypt the private key to
verify that @password is correct, and if it is, updates the
#NMSetting8021x:phase2-private-key-password property with the given
@password.  If the decryption is unsuccessful, %FALSE is returned, @error is
set, and no internal data is changed.  If no @password is given, the private
key is assumed to be valid, no decryption is performed, and the password may
be set at a later time.

WARNING: the "phase2" private key property is not a "secret" property, and
thus unencrypted private key data using the BLOB scheme may be readable by
unprivileged users.  Private keys should always be encrypted with a private
key password to prevent unauthorized access to unencrypted private key data.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH or   %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the "phase2" private   key file (PEM, DER, or PKCS#<!-- -->12 format).  The path must be UTF-8 encoded;   use g_filename_to_utf8() to convert if needed.  Passing %NULL with any   @scheme clears the private key.
:param password: password used to decrypt the private key, or %NULL if the password   is unknown.  If the password is given but fails to decrypt the private key,   an error is returned.
:param scheme: desired storage scheme for the private key
:param out_format: on successful return, the type of the private key added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass

    def set_private_key(self, value: str=None, password: str=None, scheme:
        Setting8021xCKScheme=None, out_format: Setting8021xCKFormat=None
        ) -> bool:
        """Private keys are used to authenticate the connecting client to the network
when EAP-TLS is used as either the "phase 1" or "phase 2" 802.1x
authentication method.

This function reads a private key from disk and sets the
#NMSetting8021x:private-key property with the private key file data if using
the %NM_SETTING_802_1X_CK_SCHEME_BLOB scheme, or with the path to the private
key file if using the %NM_SETTING_802_1X_CK_SCHEME_PATH scheme.

If @password is given, this function attempts to decrypt the private key to
verify that @password is correct, and if it is, updates the
#NMSetting8021x:private-key-password property with the given @password.  If
the decryption is unsuccessful, %FALSE is returned, @error is set, and no
internal data is changed.  If no @password is given, the private key is
assumed to be valid, no decryption is performed, and the password may be set
at a later time.

WARNING: the private key property is not a "secret" property, and thus
unencrypted private key data using the BLOB scheme may be readable by
unprivileged users.  Private keys should always be encrypted with a private
key password to prevent unauthorized access to unencrypted private key data.

:param self: the #NMSetting8021x
:param value: when @scheme is set to either %NM_SETTING_802_1X_CK_SCHEME_PATH or   %NM_SETTING_802_1X_CK_SCHEME_BLOB, pass the path of the private key file   (PEM, DER, or PKCS#<!-- -->12 format).  The path must be UTF-8 encoded; use   g_filename_to_utf8() to convert if needed.  Passing %NULL with any @scheme   clears the private key.
:param password: password used to decrypt the private key, or %NULL if the password   is unknown.  If the password is given but fails to decrypt the private key,   an error is returned.
:param scheme: desired storage scheme for the private key
:param out_format: on successful return, the type of the private key added
:return: %TRUE if the operation succeeded, %FALSE if it was unsuccessful"""
        pass


class Setting8021xClass:
    """"""


class SettingAdsl(Setting):
    """ADSL Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingAdsl object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingAdsl object with default values.

:return: the new empty #NMSettingAdsl object"""
        pass

    def get_encapsulation(self) -> str:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:encapsulation property of the setting"""
        pass

    def get_password(self) -> str:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:password property of the setting"""
        pass

    def get_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingSecretFlags pertaining to the #NMSettingAdsl:password"""
        pass

    def get_protocol(self) -> str:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:protocol property of the setting"""
        pass

    def get_username(self) -> str:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:username property of the setting"""
        pass

    def get_vci(self) -> int:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:vci property of the setting"""
        pass

    def get_vpi(self) -> int:
        """

:param self: the #NMSettingAdsl
:return: the #NMSettingAdsl:vpi property of the setting"""
        pass


class SettingAdslClass:
    """"""


class SettingBluetooth(Setting):
    """Bluetooth Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingBluetooth object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingBluetooth object with default values.

:return: the new empty #NMSettingBluetooth object"""
        pass

    def get_bdaddr(self) -> str:
        """Gets the Bluetooth address of the remote device which this setting
describes a connection to.

:param self: the #NMSettingBluetooth
:return: the Bluetooth address"""
        pass

    def get_connection_type(self) -> str:
        """Returns the connection method for communicating with the remote device (i.e.
either DUN to a DUN-capable device or PANU to a NAP-capable device).

:param self: the #NMSettingBluetooth
:return: the type, either %NM_SETTING_BLUETOOTH_TYPE_PANU, %NM_SETTING_BLUETOOTH_TYPE_NAP or %NM_SETTING_BLUETOOTH_TYPE_DUN"""
        pass


class SettingBluetoothClass:
    """"""


class SettingBond(Setting):
    """Bonding Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingBond object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingBond object with default values.

:return: the new empty #NMSettingBond object"""
        pass

    @staticmethod
    def validate_option(name: str=None, value: str=None) -> bool:
        """Checks whether @name is a valid bond option and @value is a valid value for
the @name. If @value is %NULL, the function only validates the option name.

:param name: the name of the option to validate
:param value: the value of the option to validate.
:return: %TRUE, if the @value is valid for the given name. If the @name is not a valid option, %FALSE will be returned."""
        pass

    def add_option(self, name: str=None, value: str=None) -> bool:
        """Add an option to the table. Adding a new name replaces any existing name/value pair
that may already exist.

:param self: the #NMSettingBond
:param name: name for the option
:param value: value for the option
:return: returns %FALSE if either @name or @value is %NULL, in that case the option is not set. Otherwise, the function does not fail and does not validate the arguments. All validation happens via nm_connection_verify() or do basic validation yourself with nm_setting_bond_validate_option().  Note: Before 1.30, libnm would perform basic validation of the name and the value via nm_setting_bond_validate_option() and reject the request by returning FALSE. Since 1.30, libnm no longer rejects any values as the setter is not supposed to perform validation."""
        pass

    def get_num_options(self) -> int:
        """Returns the number of options that should be set for this bond when it
is activated. This can be used to retrieve each option individually
using nm_setting_bond_get_option().

:param self: the #NMSettingBond
:return: the number of bonding options"""
        pass

    def get_option(self, idx: int=None, out_name: str=None, out_value: str=None
        ) -> bool:
        """Given an index, return the value of the bonding option at that index.  Indexes
are *not* guaranteed to be static across modifications to options done by
nm_setting_bond_add_option() and nm_setting_bond_remove_option(),
and should not be used to refer to options except for short periods of time
such as during option iteration.

:param self: the #NMSettingBond
:param idx: index of the desired option, from 0 to nm_setting_bond_get_num_options() - 1
:param out_name: on return, the name of the bonding option;   this value is owned by the setting and should not be modified
:param out_value: on return, the value of the name of the   bonding option; this value is owned by the setting and should not be   modified
:return: %TRUE on success if the index was valid and an option was found, %FALSE if the index was invalid (ie, greater than the number of options currently held by the setting)"""
        pass

    def get_option_by_name(self, name: str=None) -> str:
        """Returns the value associated with the bonding option specified by
@name, if it exists.

:param self: the #NMSettingBond
:param name: the option name for which to retrieve the value
:return: the value, or %NULL if the key/value pair was never added to the setting; the value is owned by the setting and must not be modified"""
        pass

    def get_option_default(self, name: str=None) -> str:
        """

:param self: the #NMSettingBond
:param name: the name of the option
:return: the value of the bond option if not overridden by an entry in
   the #NMSettingBond:options property."""
        pass

    def get_option_normalized(self, name: str=None) -> str:
        """

:param self: the #NMSettingBond
:param name: the name of the option
:return: the value of the bond option after normalization, which is what NetworkManager
   will actually apply when activating the connection. %NULL if the option won't be applied
   to the connection."""
        pass

    def get_valid_options(self) -> typing.Any:
        """Returns a list of valid bond options.

The @setting argument is unused and may be passed as %NULL.

:param self: the #NMSettingBond
:return: a %NULL-terminated array of strings of valid bond options."""
        pass

    def remove_option(self, name: str=None) -> bool:
        """Remove the bonding option referenced by @name from the internal option
list.

:param self: the #NMSettingBond
:param name: name of the option to remove
:return: %TRUE if the option was found and removed from the internal option list, %FALSE if it was not."""
        pass


class SettingBondClass:
    """"""


class SettingBondPort(Setting):
    """Bond Port Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingBondPort object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingBondPort object with default values.

:return: the new empty #NMSettingBondPort object"""
        pass

    def get_prio(self) -> int:
        """

:param self: the #NMSettingBondPort
:return: the #NMSettingBondPort:prio property of the setting"""
        pass

    def get_queue_id(self) -> int:
        """

:param self: the #NMSettingBondPort
:return: the #NMSettingBondPort:queue_id property of the setting"""
        pass


class SettingBondPortClass:
    """"""


class SettingBridge(Setting):
    """Bridging Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingBridge object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingBridge object with default values.

:return: the new empty #NMSettingBridge object"""
        pass

    def add_vlan(self, vlan: BridgeVlan=None) -> None:
        """Appends a new vlan and associated information to the setting.  The
given vlan gets sealed and a reference to it is added.

:param self: the #NMSettingBridge
:param vlan: the vlan to add
:return: """
        pass

    def clear_vlans(self) -> None:
        """Removes all configured VLANs.

:param self: the #NMSettingBridge
:return: """
        pass

    def get_ageing_time(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:ageing-time property of the setting"""
        pass

    def get_forward_delay(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:forward-delay property of the setting"""
        pass

    def get_group_address(self) -> str:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:group-address property of the setting"""
        pass

    def get_group_forward_mask(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:group-forward-mask property of the setting"""
        pass

    def get_hello_time(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:hello-time property of the setting"""
        pass

    def get_mac_address(self) -> str:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:mac-address property of the setting"""
        pass

    def get_max_age(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:max-age property of the setting"""
        pass

    def get_multicast_hash_max(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-hash-max property of the setting"""
        pass

    def get_multicast_last_member_count(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-last-member-count property of the setting"""
        pass

    def get_multicast_last_member_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-last-member-interval property of the setting"""
        pass

    def get_multicast_membership_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-membership-interval property of the setting"""
        pass

    def get_multicast_querier(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-querier property of the setting"""
        pass

    def get_multicast_querier_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-querier-interval property of the setting"""
        pass

    def get_multicast_query_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-query-interval property of the setting"""
        pass

    def get_multicast_query_response_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-query-response-interval property of the setting"""
        pass

    def get_multicast_query_use_ifaddr(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-query-use-ifaddr property of the setting"""
        pass

    def get_multicast_router(self) -> str:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-router property of the setting"""
        pass

    def get_multicast_snooping(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-snooping property of the setting"""
        pass

    def get_multicast_startup_query_count(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-query-response-interval property of the setting"""
        pass

    def get_multicast_startup_query_interval(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:multicast-startup-query-interval property of the setting"""
        pass

    def get_num_vlans(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the number of VLANs"""
        pass

    def get_priority(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:priority property of the setting"""
        pass

    def get_stp(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:stp property of the setting"""
        pass

    def get_vlan(self, idx: int=None) -> BridgeVlan:
        """

:param self: the #NMSettingBridge
:param idx: index number of the VLAN to return
:return: the VLAN at index @idx"""
        pass

    def get_vlan_default_pvid(self) -> int:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:vlan-default-pvid property of the setting"""
        pass

    def get_vlan_filtering(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:vlan-filtering property of the setting"""
        pass

    def get_vlan_protocol(self) -> str:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:vlan-protocol property of the setting"""
        pass

    def get_vlan_stats_enabled(self) -> bool:
        """

:param self: the #NMSettingBridge
:return: the #NMSettingBridge:vlan-stats-enabled property of the setting"""
        pass

    def remove_vlan(self, idx: int=None) -> None:
        """Removes the vlan at index @idx.

:param self: the #NMSettingBridge
:param idx: index number of the VLAN.
:return: """
        pass

    def remove_vlan_by_vid(self, vid_start: int=None, vid_end: int=None
        ) -> bool:
        """Remove the VLAN with range @vid_start to @vid_end.
If @vid_end is zero, it is assumed to be equal to @vid_start
and so the single-id VLAN with id @vid_start is removed.

:param self: the #NMSettingBridge
:param vid_start: the vlan start index
:param vid_end: the vlan end index
:return: %TRUE if the vlan was found and removed; %FALSE otherwise"""
        pass


class SettingBridgeClass:
    """"""


class SettingBridgePort(Setting):
    """Bridge Port Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingBridgePort object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingBridgePort object with default values.

:return: the new empty #NMSettingBridgePort object"""
        pass

    def add_vlan(self, vlan: BridgeVlan=None) -> None:
        """Appends a new vlan and associated information to the setting.  The
given vlan gets sealed and a reference to it is added.

:param self: the #NMSettingBridgePort
:param vlan: the vlan to add
:return: """
        pass

    def clear_vlans(self) -> None:
        """Removes all configured VLANs.

:param self: the #NMSettingBridgePort
:return: """
        pass

    def get_hairpin_mode(self) -> bool:
        """

:param self: the #NMSettingBridgePort
:return: the #NMSettingBridgePort:hairpin-mode property of the setting"""
        pass

    def get_num_vlans(self) -> int:
        """

:param self: the #NMSettingBridgePort
:return: the number of VLANs"""
        pass

    def get_path_cost(self) -> int:
        """

:param self: the #NMSettingBridgePort
:return: the #NMSettingBridgePort:path-cost property of the setting"""
        pass

    def get_priority(self) -> int:
        """

:param self: the #NMSettingBridgePort
:return: the #NMSettingBridgePort:priority property of the setting"""
        pass

    def get_vlan(self, idx: int=None) -> BridgeVlan:
        """

:param self: the #NMSettingBridgePort
:param idx: index number of the VLAN to return
:return: the VLAN at index @idx"""
        pass

    def remove_vlan(self, idx: int=None) -> None:
        """Removes the vlan at index @idx.

:param self: the #NMSettingBridgePort
:param idx: index number of the VLAN.
:return: """
        pass

    def remove_vlan_by_vid(self, vid_start: int=None, vid_end: int=None
        ) -> bool:
        """Remove the VLAN with range @vid_start to @vid_end.
If @vid_end is zero, it is assumed to be equal to @vid_start
and so the single-id VLAN with id @vid_start is removed.

:param self: the #NMSettingBridgePort
:param vid_start: the vlan start index
:param vid_end: the vlan end index
:return: %TRUE if the vlan was found and removed; %FALSE otherwise"""
        pass


class SettingBridgePortClass:
    """"""


class SettingCdma(Setting):
    """CDMA-based Mobile Broadband Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingCdma object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingCdma object with default values.

:return: the new empty #NMSettingCdma object"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingCdma
:return: the #NMSettingCdma:mtu property of the setting"""
        pass

    def get_number(self) -> str:
        """

:param self: the #NMSettingCdma
:return: the #NMSettingCdma:number property of the setting"""
        pass

    def get_password(self) -> str:
        """

:param self: the #NMSettingCdma
:return: the #NMSettingCdma:password property of the setting"""
        pass

    def get_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingCdma
:return: the #NMSettingSecretFlags pertaining to the #NMSettingCdma:password"""
        pass

    def get_username(self) -> str:
        """

:param self: the #NMSettingCdma
:return: the #NMSettingCdma:username property of the setting"""
        pass


class SettingCdmaClass:
    """"""


class SettingClass:
    """"""


class SettingConnection(Setting):
    """General Connection Profile Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingConnection object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingConnection object with default values.

:return: the new empty #NMSettingConnection object"""
        pass

    def add_ip_ping_address(self, address: str=None) -> bool:
        """Adds a new IP address string to the ip-ping-addresses.

:param self: the #NMSettingConnection
:param address: the IP address string to add
:return: %TRUE if the new IP address was added; %FALSE if the IP address was already present"""
        pass

    def add_permission(self, ptype: str=None, pitem: str=None, detail: str=None
        ) -> bool:
        """Adds a permission to the connection's permission list.  At this time, only
the "user" permission type is supported, and @pitem must be a username. See
#NMSettingConnection:permissions: for more details.

:param self: the #NMSettingConnection
:param ptype: the permission type; at this time only "user" is supported
:param pitem: the permission item formatted as required for @ptype
:param detail: unused at this time; must be %NULL
:return: %TRUE if the permission was unique and was successfully added to the list, %FALSE if @ptype or @pitem was invalid. If the permission was already present in the list, it will not be added a second time but %TRUE will be returned. Note that before 1.28, in this case %FALSE would be returned."""
        pass

    def add_secondary(self, sec_uuid: str=None) -> bool:
        """Adds a new secondary connection UUID to the setting.

:param self: the #NMSettingConnection
:param sec_uuid: the secondary connection UUID to add
:return: %TRUE if the secondary connection UUID was added; %FALSE if the UUID was already present"""
        pass

    def clear_ip_ping_addresses(self) -> None:
        """Removes all configured ip-ping-addresses.

:param self: the #NMSettingConnection
:return: """
        pass

    def get_auth_retries(self) -> int:
        """Returns the value contained in the #NMSettingConnection:auth-retries property.

:param self: the #NMSettingConnection
:return: the configured authentication retries. Zero means infinity and -1 means a global default value."""
        pass

    def get_autoconnect(self) -> bool:
        """Returns the #NMSettingConnection:autoconnect property of the connection.

:param self: the #NMSettingConnection
:return: the connection's autoconnect behavior"""
        pass

    def get_autoconnect_ports(self) -> Ternary:
        """Returns the #NMSettingConnection:autoconnect-ports property of the connection.

:param self: the #NMSettingConnection
:return: whether ports of the connection should be activated together
          with the connection."""
        pass

    def get_autoconnect_priority(self) -> int:
        """Returns the #NMSettingConnection:autoconnect-priority property of the connection.
The higher number, the higher priority.

:param self: the #NMSettingConnection
:return: the connection's autoconnect priority"""
        pass

    def get_autoconnect_retries(self) -> int:
        """Returns the #NMSettingConnection:autoconnect-retries property of the connection.
Zero means infinite, -1 means the global default value.

:param self: the #NMSettingConnection
:return: the connection's autoconnect retries"""
        pass

    def get_autoconnect_slaves(self) -> SettingConnectionAutoconnectSlaves:
        """Returns the #NMSettingConnection:autoconnect-slaves property of the connection.

:param self: the #NMSettingConnection
:return: whether ports of the connection should be activated together
          with the connection."""
        pass

    def get_connection_type(self) -> str:
        """Returns the #NMSettingConnection:type property of the connection.

:param self: the #NMSettingConnection
:return: the connection type"""
        pass

    def get_controller(self) -> str:
        """Returns the #NMSettingConnection:controller property of the connection.

:param self: the #NMSettingConnection
:return: interface name of the controller device or UUID of the controller connection."""
        pass

    def get_dns_over_tls(self) -> SettingConnectionDnsOverTls:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:dns-over-tls property of the setting."""
        pass

    def get_dnssec(self) -> SettingConnectionDnssec:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:dnssec property of the setting."""
        pass

    def get_down_on_poweroff(self) -> SettingConnectionDownOnPoweroff:
        """Returns the %NM_SETTING_CONNECTION_DOWN_ON_POWEROFF property.

:param self: the #NMSettingConnection
:return: whether the connection will be brought down before the system is powered off."""
        pass

    def get_gateway_ping_timeout(self) -> int:
        """

:param self: the #NMSettingConnection
:return: the value contained in the #NMSettingConnection:gateway-ping-timeout property."""
        pass

    def get_id(self) -> str:
        """Returns the #NMSettingConnection:id property of the connection.

:param self: the #NMSettingConnection
:return: the connection ID"""
        pass

    def get_interface_name(self) -> str:
        """Returns the #NMSettingConnection:interface-name property of the connection.

:param self: the #NMSettingConnection
:return: the connection's interface name"""
        pass

    def get_ip_ping_address(self, idx: int=None) -> str:
        """

:param self: the #NMSettingConnection
:param idx: the zero-based index of the ip-ping-addresses entry.
:return: the ip address string at index @idx or
   %NULL if @idx is the number of ip-ping-addresses."""
        pass

    def get_ip_ping_addresses_require_all(self) -> Ternary:
        """Returns the #NMSettingConnection:ip-ping-addresses-require-all property of the connection.

:param self: the #NMSettingConnection
:return: whether all the ip ping addresses pass the connectivity check."""
        pass

    def get_ip_ping_timeout(self) -> int:
        """

:param self: the #NMSettingConnection
:return: the value contained in the #NMSettingConnection:ip-ping-timeout property."""
        pass

    def get_lldp(self) -> SettingConnectionLldp:
        """Returns the #NMSettingConnection:lldp property of the connection.

:param self: the #NMSettingConnection
:return: a %NMSettingConnectionLldp which indicates whether LLDP must be enabled for the connection."""
        pass

    def get_llmnr(self) -> SettingConnectionLlmnr:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:llmnr property of the setting."""
        pass

    def get_master(self) -> str:
        """Returns the #NMSettingConnection:master property of the connection.

:param self: the #NMSettingConnection
:return: interface name of the controller device or UUID of the controller connection."""
        pass

    def get_mdns(self) -> SettingConnectionMdns:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:mdns property of the setting."""
        pass

    def get_metered(self) -> Metered:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:metered property of the setting."""
        pass

    def get_mptcp_flags(self) -> MptcpFlags:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:mptcp-flags property of the setting."""
        pass

    def get_mud_url(self) -> str:
        """Returns the value contained in the #NMSettingConnection:mud-url
property.

:param self: the #NMSettingConnection
:return: """
        pass

    def get_multi_connect(self) -> ConnectionMultiConnect:
        """

:param self: the #NMSettingConnection
:return: the #NMSettingConnection:multi-connect property of the connection."""
        pass

    def get_num_permissions(self) -> int:
        """Returns the number of entries in the #NMSettingConnection:permissions
property of this setting.

:param self: the #NMSettingConnection
:return: the number of permissions entries"""
        pass

    def get_num_secondaries(self) -> int:
        """

:param self: the #NMSettingConnection
:return: the number of configured secondary connection UUIDs"""
        pass

    def get_permission(self, idx: int=None, out_ptype: str=None, out_pitem:
        str=None, out_detail: str=None) -> bool:
        """Retrieve one of the entries of the #NMSettingConnection:permissions property
of this setting.

:param self: the #NMSettingConnection
:param idx: the zero-based index of the permissions entry
:param out_ptype: on return, the permission type. This is currently always "user",   unless the entry is invalid, in which case it returns "invalid".
:param out_pitem: on return, the permission item (formatted according to @ptype, see #NMSettingConnection:permissions for more detail
:param out_detail: on return, the permission detail (at this time, always %NULL)
:return: %TRUE if a permission was returned, %FALSE if @idx was invalid"""
        pass

    def get_port_type(self) -> str:
        """Returns the #NMSettingConnection:port-type property of the connection.

:param self: the #NMSettingConnection
:return: the type of port this connection is, if any."""
        pass

    def get_read_only(self) -> bool:
        """Returns the #NMSettingConnection:read-only property of the connection.

:param self: the #NMSettingConnection
:return: %TRUE if the connection is read-only, %FALSE if it is not"""
        pass

    def get_secondary(self, idx: int=None) -> str:
        """

:param self: the #NMSettingConnection
:param idx: the zero-based index of the secondary connection UUID entry.   Access one past the length of secondaries is ok and will return   %NULL. Otherwise, it is a user error.
:return: the secondary connection UUID at index @idx or
   %NULL if @idx is the number of secondaries."""
        pass

    def get_slave_type(self) -> str:
        """Returns the #NMSettingConnection:slave-type property of the connection.

:param self: the #NMSettingConnection
:return: the type of port this connection is, if any"""
        pass

    def get_stable_id(self) -> str:
        """Returns the #NMSettingConnection:stable_id property of the connection.

:param self: the #NMSettingConnection
:return: the stable-id for the connection"""
        pass

    def get_timestamp(self) -> int:
        """Returns the #NMSettingConnection:timestamp property of the connection.

:param self: the #NMSettingConnection
:return: the connection's timestamp"""
        pass

    def get_uuid(self) -> str:
        """Returns the #NMSettingConnection:uuid property of the connection.

:param self: the #NMSettingConnection
:return: the connection UUID"""
        pass

    def get_wait_activation_delay(self) -> int:
        """

:param self: the #NMSettingConnection
:return: the %NM_SETTING_CONNECTION_WAIT_ACTIVATION_DELAY property with
   the delay in milliseconds. -1 is the default."""
        pass

    def get_wait_device_timeout(self) -> int:
        """

:param self: the #NMSettingConnection
:return: the %NM_SETTING_CONNECTION_WAIT_DEVICE_TIMEOUT property with
   the timeout in milliseconds. -1 is the default."""
        pass

    def get_zone(self) -> str:
        """Returns the #NMSettingConnection:zone property of the connection.

:param self: the #NMSettingConnection
:return: the trust level of a connection"""
        pass

    def is_slave_type(self, type: str=None) -> bool:
        """

:param self: the #NMSettingConnection
:param type: the setting name (ie #NM_SETTING_BOND_SETTING_NAME) to be matched against @setting's port type
:return: %TRUE if connection is of the given port @type"""
        pass

    def permissions_user_allowed(self, uname: str=None) -> bool:
        """Checks whether the given username is allowed to view/access this connection.

:param self: the #NMSettingConnection
:param uname: the user name to check permissions for
:return: %TRUE if the requested user is allowed to view this connection, %FALSE if the given user is not allowed to view this connection"""
        pass

    def remove_ip_ping_address(self, idx: int=None) -> None:
        """Removes the IP address at index @idx.

:param self: the #NMSettingConnection
:param idx: index number of the IP address
:return: """
        pass

    def remove_ip_ping_address_by_value(self, address: str=None) -> bool:
        """Removes the IP address @address from ip-ping-addresses.

:param self: the #NMSettingConnection
:param address: the IP address to remove
:return: %TRUE if the IP address was found and removed; %FALSE if it was not."""
        pass

    def remove_permission(self, idx: int=None) -> None:
        """Removes the permission at index @idx from the connection.

:param self: the #NMSettingConnection
:param idx: the zero-based index of the permission to remove
:return: """
        pass

    def remove_permission_by_value(self, ptype: str=None, pitem: str=None,
        detail: str=None) -> bool:
        """Removes the permission from the connection.
At this time, only the "user" permission type is supported, and @pitem must
be a username. See #NMSettingConnection:permissions: for more details.

:param self: the #NMSettingConnection
:param ptype: the permission type; at this time only "user" is supported
:param pitem: the permission item formatted as required for @ptype
:param detail: unused at this time; must be %NULL
:return: %TRUE if the permission was found and removed; %FALSE if it was not."""
        pass

    def remove_secondary(self, idx: int=None) -> None:
        """Removes the secondary connection UUID at index @idx.

:param self: the #NMSettingConnection
:param idx: index number of the secondary connection UUID
:return: """
        pass

    def remove_secondary_by_value(self, sec_uuid: str=None) -> bool:
        """Removes the secondary connection UUID @sec_uuid.

:param self: the #NMSettingConnection
:param sec_uuid: the secondary connection UUID to remove
:return: %TRUE if the secondary connection UUID was found and removed; %FALSE if it was not."""
        pass


class SettingConnectionClass:
    """"""


class SettingDcb(Setting):
    """Data Center Bridging Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingDcb object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingDcb object with default values.

:return: the new empty #NMSettingDcb object"""
        pass

    def get_app_fcoe_flags(self) -> SettingDcbFlags:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-fcoe-flags property of the setting"""
        pass

    def get_app_fcoe_mode(self) -> str:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-fcoe-mode property of the setting"""
        pass

    def get_app_fcoe_priority(self) -> int:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-fcoe-priority property of the setting"""
        pass

    def get_app_fip_flags(self) -> SettingDcbFlags:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-fip-flags property of the setting"""
        pass

    def get_app_fip_priority(self) -> int:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-fip-priority property of the setting"""
        pass

    def get_app_iscsi_flags(self) -> SettingDcbFlags:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-iscsi-flags property of the setting"""
        pass

    def get_app_iscsi_priority(self) -> int:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:app-iscsi-priority property of the setting"""
        pass

    def get_priority_bandwidth(self, user_priority: int=None) -> int:
        """

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to retrieve the group bandwidth percentage for
:return: the allowed bandwidth percentage of @user_priority in its priority group. These values are only valid when #NMSettingDcb:priority-group-flags includes the %NM_SETTING_DCB_FLAG_ENABLE flag."""
        pass

    def get_priority_flow_control(self, user_priority: int=None) -> bool:
        """

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to retrieve flow control for
:return: %TRUE if flow control is enabled for the given @user_priority, %FALSE if not enabled"""
        pass

    def get_priority_flow_control_flags(self) -> SettingDcbFlags:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:priority-flow-control-flags property of the setting"""
        pass

    def get_priority_group_bandwidth(self, group_id: int=None) -> int:
        """

:param self: the #NMSettingDcb
:param group_id: the priority group (0 - 7) to retrieve the bandwidth percentage for
:return: the bandwidth percentage assigned to @group_id.  These values are only valid when #NMSettingDcb:priority-group-flags includes the %NM_SETTING_DCB_FLAG_ENABLE flag."""
        pass

    def get_priority_group_flags(self) -> SettingDcbFlags:
        """

:param self: the #NMSettingDcb
:return: the #NMSettingDcb:priority-group-flags property of the setting"""
        pass

    def get_priority_group_id(self, user_priority: int=None) -> int:
        """

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to retrieve the group ID for
:return: the group number @user_priority is assigned to.  These values are only valid when #NMSettingDcb:priority-group-flags includes the %NM_SETTING_DCB_FLAG_ENABLE flag."""
        pass

    def get_priority_strict_bandwidth(self, user_priority: int=None) -> bool:
        """

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to retrieve strict bandwidth for
:return: %TRUE if @user_priority may use all of the bandwidth allocated to its assigned group, or %FALSE if not. These values are only valid when #NMSettingDcb:priority-group-flags includes the %NM_SETTING_DCB_FLAG_ENABLE flag."""
        pass

    def get_priority_traffic_class(self, user_priority: int=None) -> int:
        """

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to retrieve the traffic class for
:return: the traffic class assigned to @user_priority. These values are only valid when #NMSettingDcb:priority-group-flags includes the %NM_SETTING_DCB_FLAG_ENABLE flag."""
        pass

    def set_priority_bandwidth(self, user_priority: int=None,
        bandwidth_percent: int=None) -> None:
        """These values are only valid when #NMSettingDcb:priority-group-flags includes
the %NM_SETTING_DCB_FLAG_ENABLE flag.

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to set the bandwidth percentage for
:param bandwidth_percent: the bandwidth percentage (0 - 100) that @user_priority is allowed to use within its priority group
:return: """
        pass

    def set_priority_flow_control(self, user_priority: int=None, enabled:
        bool=None) -> None:
        """These values are only valid when #NMSettingDcb:priority-flow-control includes
the %NM_SETTING_DCB_FLAG_ENABLE flag.

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to set flow control for
:param enabled: %TRUE to enable flow control for this priority, %FALSE to disable it
:return: """
        pass

    def set_priority_group_bandwidth(self, group_id: int=None,
        bandwidth_percent: int=None) -> None:
        """These values are only valid when #NMSettingDcb:priority-group-flags includes
the %NM_SETTING_DCB_FLAG_ENABLE flag.

:param self: the #NMSettingDcb
:param group_id: the priority group (0 - 7) to set the bandwidth percentage for
:param bandwidth_percent: the bandwidth percentage (0 - 100) to assign to @group_id to
:return: """
        pass

    def set_priority_group_id(self, user_priority: int=None, group_id: int=None
        ) -> None:
        """These values are only valid when #NMSettingDcb:priority-group-flags includes
the %NM_SETTING_DCB_FLAG_ENABLE flag.

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to set flow control for
:param group_id: the group (0 - 7) to assign @user_priority to, or 15 for the unrestricted group.
:return: """
        pass

    def set_priority_strict_bandwidth(self, user_priority: int=None, strict:
        bool=None) -> None:
        """These values are only valid when #NMSettingDcb:priority-group-flags includes
the %NM_SETTING_DCB_FLAG_ENABLE flag.

:param self: the #NMSettingDcb
:param user_priority: the User Priority (0 - 7) to set strict bandwidth for
:param strict: %TRUE to allow @user_priority to use all the bandwidth allocated to its priority group, or %FALSE if not
:return: """
        pass

    def set_priority_traffic_class(self, user_priority: int=None,
        traffic_class: int=None) -> None:
        """

:param self: 
:param user_priority: 
:param traffic_class: 
:return: """
        pass


class SettingDcbClass:
    """"""


class SettingDummy(Setting):
    """Dummy Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingDummy object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingDummy object with default values.

:return: the new empty #NMSettingDummy object"""
        pass


class SettingDummyClass:
    """"""


class SettingEthtool(Setting):
    """Ethtool Ethernet Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingEthtool object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingEthtool object with default values.

:return: the new empty #NMSettingEthtool object"""
        pass

    def clear_features(self) -> None:
        """Clears all offload features settings

:param self: the #NMSettingEthtool
:return: """
        pass

    def get_feature(self, optname: str=None) -> Ternary:
        """Gets and offload feature setting. Returns %NM_TERNARY_DEFAULT if the
feature is not set.

Note that @optname must be a valid name for a feature, according to
nm_ethtool_optname_is_feature().

:param self: the #NMSettingEthtool
:param optname: option name of the offload feature to get
:return: a #NMTernary value indicating whether the offload feature
   is enabled, disabled, or left untouched."""
        pass

    def get_optnames(self, out_length: int=None) -> typing.Any:
        """This returns all options names that are set. This includes the feature names
like %NM_ETHTOOL_OPTNAME_FEATURE_GRO. See nm_ethtool_optname_is_feature() to
check whether the option name is valid for offload features.

:param self: the #NMSettingEthtool instance.
:param out_length: return location for the number of keys returned, or %NULL
:return: list of set option
   names or %NULL if no options are set. The option names are still owned by
   @setting and may get invalidated when @setting gets modified."""
        pass

    def set_feature(self, optname: str=None, value: Ternary=None) -> None:
        """Sets and offload feature setting.

Note that @optname must be a valid name for a feature, according to
nm_ethtool_optname_is_feature().

:param self: the #NMSettingEthtool
:param optname: option name of the offload feature to get
:param value: the new value to set. The special value %NM_TERNARY_DEFAULT   means to clear the offload feature setting.
:return: """
        pass


class SettingEthtoolClass:
    """"""


class SettingGeneric(Setting):
    """Generic Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingGeneric object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingGeneric object with default values.

:return: the new empty #NMSettingGeneric object"""
        pass

    def get_device_handler(self) -> str:
        """Returns the #NMSettingGeneric:device-handler property of the connection.

:param self: the #NMSettingGeneric
:return: the device handler name, or %NULL if no device handler is set"""
        pass


class SettingGenericClass:
    """"""


class SettingGsm(Setting):
    """GSM-based Mobile Broadband Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingGsm object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingGsm object with default values.

:return: the new empty #NMSettingGsm object"""
        pass

    def get_apn(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:apn property of the setting"""
        pass

    def get_auto_config(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:auto-config property of the setting"""
        pass

    def get_device_id(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:device-id property of the setting"""
        pass

    def get_device_uid(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:device-uid property of the setting"""
        pass

    def get_home_only(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:home-only property of the setting"""
        pass

    def get_initial_eps_apn(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:initial-eps-bearer-apn property of the setting"""
        pass

    def get_initial_eps_config(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:initial-eps-bearer-configure property of the setting"""
        pass

    def get_initial_eps_noauth(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-noauth property of the setting"""
        pass

    def get_initial_eps_password(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:initial-eps-bearer-password property of the setting"""
        pass

    def get_initial_eps_refuse_chap(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-refuse-chap property of the setting"""
        pass

    def get_initial_eps_refuse_eap(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-refuse-eap property of the setting"""
        pass

    def get_initial_eps_refuse_mschap(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-refuse-mschap property of the setting"""
        pass

    def get_initial_eps_refuse_mschapv2(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-refuse-mschapv2 property of the setting"""
        pass

    def get_initial_eps_refuse_pap(self) -> bool:
        """

:param self: the #NMSettingGsm
:return: For LTE modems, the #NMSettingGsm:initial-eps-refuse-pap property of the setting"""
        pass

    def get_initial_eps_username(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:initial-eps-bearer-username property of the setting"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:mtu property of the setting"""
        pass

    def get_network_id(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:network-id property of the setting"""
        pass

    def get_number(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:number property of the setting"""
        pass

    def get_password(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:password property of the setting"""
        pass

    def get_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingSecretFlags pertaining to the #NMSettingGsm:password"""
        pass

    def get_pin(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:pin property of the setting"""
        pass

    def get_pin_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingSecretFlags pertaining to the #NMSettingGsm:pin"""
        pass

    def get_sim_id(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:sim-id property of the setting"""
        pass

    def get_sim_operator_id(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:sim-operator-id property of the setting"""
        pass

    def get_username(self) -> str:
        """

:param self: the #NMSettingGsm
:return: the #NMSettingGsm:username property of the setting"""
        pass


class SettingGsmClass:
    """"""


class SettingHostname(Setting):
    """Hostname settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingHostname object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingHostname object with default values.

:return: the new empty #NMSettingHostname object"""
        pass

    def get_from_dhcp(self) -> Ternary:
        """Returns the value contained in the #NMSettingHostname:from-dhcp
property.

:param self: the #NMSettingHostname
:return: the 'from-dhcp' property value"""
        pass

    def get_from_dns_lookup(self) -> Ternary:
        """Returns the value contained in the #NMSettingHostname:from-dns-lookup
property.

:param self: the #NMSettingHostname
:return: the 'from-dns-lookup' property value"""
        pass

    def get_only_from_default(self) -> Ternary:
        """Returns the value contained in the #NMSettingHostname:only-from-default
property.

:param self: the #NMSettingHostname
:return: the 'only-from-default' property value"""
        pass

    def get_priority(self) -> int:
        """Returns the value contained in the #NMSettingHostname:priority
property.

:param self: the #NMSettingHostname
:return: the 'priority' property value"""
        pass


class SettingHostnameClass:
    """"""


class SettingHsr(Setting):
    """HSR/PRP Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingHsr object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingHsr object with default values.

:return: the new empty #NMSettingHsr object"""
        pass

    def get_interlink(self) -> str:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:interlink property of the setting"""
        pass

    def get_multicast_spec(self) -> int:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:multicast_spec property of the setting"""
        pass

    def get_port1(self) -> str:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:port1 property of the setting"""
        pass

    def get_port2(self) -> str:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:port2 property of the setting"""
        pass

    def get_protocol_version(self) -> SettingHsrProtocolVersion:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:protocol-version property of the setting"""
        pass

    def get_prp(self) -> bool:
        """

:param self: the #NMSettingHsr
:return: the #NMSettingHsr:prp property of the setting"""
        pass


class SettingHsrClass:
    """"""


class SettingIP4ConfigClass:
    """"""


class SettingIP6ConfigClass:
    """"""


class SettingIPConfig(Setting):
    """"""

    def add_address(self, address: IPAddress=None) -> bool:
        """Adds a new IP address and associated information to the setting.  The
given address is duplicated internally and is not changed by this function.

:param self: the #NMSettingIPConfig
:param address: the new address to add
:return: %TRUE if the address was added; %FALSE if the address was already known."""
        pass

    def add_dhcp_reject_server(self, server: str=None) -> None:
        """Adds a new DHCP reject server to the setting.

:param self: the #NMSettingIPConfig
:param server: the DHCP reject server to add
:return: """
        pass

    def add_dns(self, dns: str=None) -> bool:
        """Adds a new DNS server to the setting.

:param self: the #NMSettingIPConfig
:param dns: the IP address of the DNS server to add
:return: %TRUE if the DNS server was added; %FALSE if the server was already known  Before 1.42, setting @dns to an invalid string was treated as user-error. Now, also invalid DNS values can be set, but will be rejected later during nm_connection_verify()."""
        pass

    def add_dns_option(self, dns_option: str=None) -> bool:
        """Adds a new DNS option to the setting.

:param self: the #NMSettingIPConfig
:param dns_option: the DNS option to add
:return: %TRUE if the DNS option was added; %FALSE otherwise"""
        pass

    def add_dns_search(self, dns_search: str=None) -> bool:
        """Adds a new DNS search domain to the setting.

:param self: the #NMSettingIPConfig
:param dns_search: the search domain to add
:return: %TRUE if the DNS search domain was added; %FALSE if the search domain was already known"""
        pass

    def add_route(self, route: IPRoute=None) -> bool:
        """Appends a new route and associated information to the setting.  The
given route is duplicated internally and is not changed by this function.
If an identical route (considering attributes as well) already exists, the
route is not added and the function returns %FALSE.

Note that before 1.10, this function would not consider route attributes
and not add a route that has an existing route with same dest/prefix,next_hop,metric
parameters.

:param self: the #NMSettingIPConfig
:param route: the route to add
:return: %TRUE if the route was added; %FALSE if the route was already known."""
        pass

    def add_routing_rule(self, routing_rule: IPRoutingRule=None) -> None:
        """Appends a new routing-rule and associated information to the setting. The
given routing rules gets sealed and the reference count is incremented.
The function does not check whether an identical rule already exists
and always appends the rule to the end of the list.

:param self: the #NMSettingIPConfig
:param routing_rule: the #NMIPRoutingRule to add. The address family   of the added rule must be compatible with the setting.
:return: """
        pass

    def clear_addresses(self) -> None:
        """Removes all configured addresses.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def clear_dhcp_reject_servers(self) -> None:
        """Removes all configured DHCP reject servers.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def clear_dns(self) -> None:
        """Removes all configured DNS servers.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def clear_dns_options(self, is_set: bool=None) -> None:
        """Removes all configured DNS options.

:param self: the #NMSettingIPConfig
:param is_set: the dns-options can be either empty or unset (default).   Specify how to clear the options.
:return: """
        pass

    def clear_dns_searches(self) -> None:
        """Removes all configured DNS search domains.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def clear_routes(self) -> None:
        """Removes all configured routes.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def clear_routing_rules(self) -> None:
        """Removes all configured routing rules.

:param self: the #NMSettingIPConfig
:return: """
        pass

    def get_address(self, idx: int=None) -> IPAddress:
        """

:param self: the #NMSettingIPConfig
:param idx: index number of the address to return
:return: the address at index @idx"""
        pass

    def get_auto_route_ext_gw(self) -> Ternary:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:auto-route-ext-gw property of the setting"""
        pass

    def get_dad_timeout(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:dad-timeout property."""
        pass

    def get_dhcp_dscp(self) -> str:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-dscp
property.

:param self: the #NMSettingIPConfig
:return: the value for the DSCP field for DHCP"""
        pass

    def get_dhcp_hostname(self) -> str:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-hostname
property.

:param self: the #NMSettingIPConfig
:return: the configured hostname to send to the DHCP server"""
        pass

    def get_dhcp_hostname_flags(self) -> DhcpHostnameFlags:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-hostname-flags
property.

:param self: the #NMSettingIPConfig
:return: flags for the DHCP hostname and FQDN"""
        pass

    def get_dhcp_iaid(self) -> str:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-iaid
property.

:param self: the #NMSettingIPConfig
:return: the configured DHCP IAID (Identity Association Identifier)"""
        pass

    def get_dhcp_reject_servers(self, out_len: int=None) -> typing.Any:
        """

:param self: the #NMSettingIPConfig
:param out_len: the number of returned elements
:return: A %NULL terminated array of DHCP reject servers. Even if no reject
   servers are configured, this always returns a non %NULL value."""
        pass

    def get_dhcp_send_hostname(self) -> bool:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-send-hostname
property.

:param self: the #NMSettingIPConfig
:return: %TRUE if NetworkManager should send the machine hostname to the DHCP server when requesting addresses to allow the server to automatically update DNS information for this machine."""
        pass

    def get_dhcp_send_hostname_v2(self) -> Ternary:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-send-hostname-v2
property.

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:dhcp-send-hostname-v2 property of the setting"""
        pass

    def get_dhcp_send_release(self) -> Ternary:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:dhcp-send-release property of the setting"""
        pass

    def get_dhcp_timeout(self) -> int:
        """Returns the value contained in the #NMSettingIPConfig:dhcp-timeout
property.

:param self: the #NMSettingIPConfig
:return: the configured DHCP timeout in seconds. 0 = default for the particular kind of device."""
        pass

    def get_dns(self, idx: int=None) -> str:
        """

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS server to return
:return: the IP address of the DNS server at index @idx"""
        pass

    def get_dns_option(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS option
:return: the DNS option at index @idx"""
        pass

    def get_dns_priority(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the priority of DNS servers"""
        pass

    def get_dns_search(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS search domain to return
:return: the DNS search domain at index @idx"""
        pass

    def get_forwarding(self) -> SettingIPConfigForwarding:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:forwarding property of the setting"""
        pass

    def get_gateway(self) -> str:
        """

:param self: the #NMSettingIPConfig
:return: the IP address of the gateway associated with this configuration, or %NULL."""
        pass

    def get_ignore_auto_dns(self) -> bool:
        """Returns the value contained in the #NMSettingIPConfig:ignore-auto-dns
property.

:param self: the #NMSettingIPConfig
:return: %TRUE if automatically configured (ie via DHCP) DNS information should be ignored."""
        pass

    def get_ignore_auto_routes(self) -> bool:
        """Returns the value contained in the #NMSettingIPConfig:ignore-auto-routes
property.

:param self: the #NMSettingIPConfig
:return: %TRUE if automatically configured (ie via DHCP) routes should be ignored."""
        pass

    def get_may_fail(self) -> bool:
        """Returns the value contained in the #NMSettingIPConfig:may-fail
property.

:param self: the #NMSettingIPConfig
:return: %TRUE if this connection doesn't require this type of IP addressing to complete for the connection to succeed."""
        pass

    def get_method(self) -> str:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:method property of the setting; see #NMSettingIP4Config and #NMSettingIP6Config for details of the methods available with each type."""
        pass

    def get_never_default(self) -> bool:
        """Returns the value contained in the #NMSettingIPConfig:never-default
property.

:param self: the #NMSettingIPConfig
:return: %TRUE if this connection should never be the default
   connection"""
        pass

    def get_num_addresses(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured addresses"""
        pass

    def get_num_dns(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured DNS servers"""
        pass

    def get_num_dns_options(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured DNS options"""
        pass

    def get_num_dns_searches(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured DNS search domains"""
        pass

    def get_num_routes(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured routes"""
        pass

    def get_num_routing_rules(self) -> int:
        """

:param self: the #NMSettingIPConfig
:return: the number of configured routing rules"""
        pass

    def get_replace_local_rule(self) -> Ternary:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:replace-local-rule property of the setting"""
        pass

    def get_required_timeout(self) -> int:
        """Returns the value contained in the #NMSettingIPConfig:required-timeout
property.

:param self: the #NMSettingIPConfig
:return: the required timeout for the address family"""
        pass

    def get_route(self, idx: int=None) -> IPRoute:
        """

:param self: the #NMSettingIPConfig
:param idx: index number of the route to return
:return: the route at index @idx"""
        pass

    def get_route_metric(self) -> int:
        """Returns the value contained in the #NMSettingIPConfig:route-metric
property.

:param self: the #NMSettingIPConfig
:return: the route metric that is used for routes that don't explicitly specify a metric. See #NMSettingIPConfig:route-metric for more details."""
        pass

    def get_route_table(self) -> int:
        """Returns the value contained in the #NMSettingIPConfig:route-table
property.

:param self: the #NMSettingIPConfig
:return: the configured route-table."""
        pass

    def get_routed_dns(self) -> SettingIPConfigRoutedDns:
        """

:param self: the #NMSettingIPConfig
:return: the #NMSettingIPConfig:routed-dns property of the setting"""
        pass

    def get_routing_rule(self, idx: int=None) -> IPRoutingRule:
        """

:param self: the #NMSettingIPConfig
:param idx: index number of the routing_rule to return
:return: the routing rule at index @idx"""
        pass

    def get_shared_dhcp_lease_time(self) -> int:
        """Returns the value contained in the #NMSettingIPConfig:shared-dhcp-lease-time
property.

:param self: the #NMSettingIPConfig
:return: the configured DHCP server lease time"""
        pass

    def get_shared_dhcp_range(self) -> str:
        """Returns the value contained in the #NMSettingIPConfig:shared-dhcp-range
property.

:param self: the #NMSettingIPConfig
:return: the configured DHCP server range"""
        pass

    def has_dns_options(self) -> bool:
        """NMSettingIPConfig can have a list of dns-options. If the list
is empty, there are two similar (but differentiated) states.
Either the options are explicitly set to have no values,
or the options are left undefined. The latter means to use
a default configuration, while the former explicitly means "no-options".

:param self: the #NMSettingIPConfig
:return: whether DNS options are initialized or left unset (the default)."""
        pass

    def remove_address(self, idx: int=None) -> None:
        """Removes the address at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the address to remove
:return: """
        pass

    def remove_address_by_value(self, address: IPAddress=None) -> bool:
        """Removes the address @address.

:param self: the #NMSettingIPConfig
:param address: the IP address to remove
:return: %TRUE if the address was found and removed; %FALSE if it was not."""
        pass

    def remove_dhcp_reject_server(self, idx: int=None) -> None:
        """Removes the DHCP reject server at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the DHCP reject server
:return: """
        pass

    def remove_dns(self, idx: int=None) -> None:
        """Removes the DNS server at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS server to remove
:return: """
        pass

    def remove_dns_by_value(self, dns: str=None) -> bool:
        """Removes the DNS server @dns.

:param self: the #NMSettingIPConfig
:param dns: the DNS server to remove
:return: %TRUE if the DNS server was found and removed; %FALSE if it was not.  Before 1.42, setting @dns to an invalid string was treated as user-error."""
        pass

    def remove_dns_option(self, idx: int=None) -> None:
        """Removes the DNS option at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS option
:return: """
        pass

    def remove_dns_option_by_value(self, dns_option: str=None) -> bool:
        """Removes the DNS option @dns_option.

:param self: the #NMSettingIPConfig
:param dns_option: the DNS option to remove
:return: %TRUE if the DNS option was found and removed; %FALSE if it was not."""
        pass

    def remove_dns_search(self, idx: int=None) -> None:
        """Removes the DNS search domain at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the DNS search domain
:return: """
        pass

    def remove_dns_search_by_value(self, dns_search: str=None) -> bool:
        """Removes the DNS search domain @dns_search.

:param self: the #NMSettingIPConfig
:param dns_search: the search domain to remove
:return: %TRUE if the DNS search domain was found and removed; %FALSE if it was not."""
        pass

    def remove_route(self, idx: int=None) -> None:
        """Removes the route at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the route
:return: """
        pass

    def remove_route_by_value(self, route: IPRoute=None) -> bool:
        """Removes the first matching route that matches @route.
Note that before 1.10, this function would only compare dest/prefix,next_hop,metric
and ignore route attributes. Now, @route must match exactly.

:param self: the #NMSettingIPConfig
:param route: the route to remove
:return: %TRUE if the route was found and removed; %FALSE if it was not."""
        pass

    def remove_routing_rule(self, idx: int=None) -> None:
        """Removes the routing_rule at index @idx.

:param self: the #NMSettingIPConfig
:param idx: index number of the routing_rule
:return: """
        pass


class SettingIPConfigClass:
    """"""


class SettingIPTunnel(Setting):
    """IP Tunneling Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingIPTunnel object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingIPTunnel object with default values.

:return: the new empty #NMSettingIPTunnel object"""
        pass

    def get_encapsulation_limit(self) -> int:
        """Returns the #NMSettingIPTunnel:encapsulation-limit property of the setting.

:param self: the #NMSettingIPTunnel
:return: the encapsulation limit value"""
        pass

    def get_flags(self) -> IPTunnelFlags:
        """Returns the #NMSettingIPTunnel:flags property of the setting.

:param self: the #NMSettingIPTunnel
:return: the tunnel flags"""
        pass

    def get_flow_label(self) -> int:
        """Returns the #NMSettingIPTunnel:flow-label property of the setting.

:param self: the #NMSettingIPTunnel
:return: the flow label value"""
        pass

    def get_fwmark(self) -> int:
        """Returns the #NMSettingIPTunnel:fwmark property of the setting.

:param self: the #NMSettingIPTunnel
:return: the fwmark value"""
        pass

    def get_input_key(self) -> str:
        """Returns the #NMSettingIPTunnel:input-key property of the setting.

:param self: the #NMSettingIPTunnel
:return: the input key"""
        pass

    def get_local(self) -> str:
        """Returns the #NMSettingIPTunnel:local property of the setting.

:param self: the #NMSettingIPTunnel
:return: the local endpoint"""
        pass

    def get_mode(self) -> IPTunnelMode:
        """Returns the #NMSettingIPTunnel:mode property of the setting.

:param self: the #NMSettingIPTunnel
:return: the tunnel mode"""
        pass

    def get_mtu(self) -> int:
        """Returns the #NMSettingIPTunnel:mtu property of the setting.

:param self: the #NMSettingIPTunnel
:return: the MTU"""
        pass

    def get_output_key(self) -> str:
        """Returns the #NMSettingIPTunnel:output-key property of the setting.

:param self: the #NMSettingIPTunnel
:return: the output key"""
        pass

    def get_parent(self) -> str:
        """Returns the #NMSettingIPTunnel:parent property of the setting

:param self: the #NMSettingIPTunnel
:return: the parent device"""
        pass

    def get_path_mtu_discovery(self) -> bool:
        """Returns the #NMSettingIPTunnel:path-mtu-discovery property of the setting.

:param self: the #NMSettingIPTunnel
:return: whether path MTU discovery is enabled"""
        pass

    def get_remote(self) -> str:
        """Returns the #NMSettingIPTunnel:remote property of the setting.

:param self: the #NMSettingIPTunnel
:return: the remote endpoint"""
        pass

    def get_tos(self) -> int:
        """Returns the #NMSettingIPTunnel:tos property of the setting.

:param self: the #NMSettingIPTunnel
:return: the TOS value"""
        pass

    def get_ttl(self) -> int:
        """Returns the #NMSettingIPTunnel:ttl property of the setting.

:param self: the #NMSettingIPTunnel
:return: the Time-to-live value"""
        pass


class SettingIPTunnelClass:
    """"""


class SettingInfiniband(Setting):
    """Infiniband Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingInfiniband object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingInfiniband object with default values.

:return: the new empty #NMSettingInfiniband object"""
        pass

    def get_mac_address(self) -> str:
        """

:param self: the #NMSettingInfiniband
:return: the #NMSettingInfiniband:mac-address property of the setting"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingInfiniband
:return: the #NMSettingInfiniband:mtu property of the setting"""
        pass

    def get_p_key(self) -> int:
        """Returns the P_Key to use for this device. A value of -1 means to
use the default P_Key (aka "the P_Key at index 0"). Otherwise, it is
a 16-bit unsigned integer.

:param self: the #NMSettingInfiniband
:return: the IPoIB P_Key"""
        pass

    def get_parent(self) -> str:
        """Returns the parent interface name for this device, if set.

:param self: the #NMSettingInfiniband
:return: the parent interface name"""
        pass

    def get_transport_mode(self) -> str:
        """Returns the transport mode for this device. Either 'datagram' or
'connected'.

:param self: the #NMSettingInfiniband
:return: the IPoIB transport mode"""
        pass

    def get_virtual_interface_name(self) -> str:
        """Returns the interface name created by combining #NMSettingInfiniband:parent
and #NMSettingInfiniband:p-key. (If either property is unset, this will
return %NULL.)

:param self: the #NMSettingInfiniband
:return: the interface name, or %NULL"""
        pass


class SettingInfinibandClass:
    """"""


class SettingIpvlan(Setting):
    """IPVLAN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingIpvlan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingIpvlan object with default values.

:return: the new empty #NMSettingIpvlan object"""
        pass

    def get_mode(self) -> SettingIpvlanMode:
        """

:param self: the #NMSettingIpvlan
:return: the #NMSettingIpvlan:mode property of the setting"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingIpvlan
:return: the #NMSettingIpvlan:parent property of the setting"""
        pass

    def get_private(self) -> bool:
        """

:param self: the #NMSettingIpvlan
:return: the #NMSettingIpvlan:private property of the setting"""
        pass

    def get_vepa(self) -> bool:
        """

:param self: the #NMSettingIpvlan
:return: the #NMSettingIpvlan:vepa property of the setting"""
        pass


class SettingIpvlanClass:
    """"""


class SettingLink(Setting):
    """Link settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingLink object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingLink object with default values.

:return: the new empty #NMSettingLink object"""
        pass

    def get_gro_max_size(self) -> int:
        """Returns the value contained in the #NMSettingLink:gro-max-size
property.

:param self: the #NMSettingLink
:return: the 'gro-max-size' property value"""
        pass

    def get_gso_max_segments(self) -> int:
        """Returns the value contained in the #NMSettingLink:gso-max-segments
property.

:param self: the #NMSettingLink
:return: the 'gso-max-segments' property value"""
        pass

    def get_gso_max_size(self) -> int:
        """Returns the value contained in the #NMSettingLink:gso-max-size
property.

:param self: the #NMSettingLink
:return: the 'gso-max-size' property value"""
        pass

    def get_tx_queue_length(self) -> int:
        """Returns the value contained in the #NMSettingLink:tx-queue-length
property.

:param self: the #NMSettingLink
:return: the 'tx-queue-length' property value"""
        pass


class SettingLinkClass:
    """"""


class SettingLoopback(Setting):
    """Loopback Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingLoopback object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingLoopback object with default values.

:return: the new empty #NMSettingLoopback object"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingLoopback
:return: the #NMSettingLoopback:mtu property of the setting"""
        pass


class SettingLoopbackClass:
    """"""


class SettingMacsec(Setting):
    """MACSec Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingMacsec object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingMacsec object with default values.

:return: the new empty #NMSettingMacsec object"""
        pass

    def get_encrypt(self) -> bool:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:encrypt property of the setting"""
        pass

    def get_mka_cak(self) -> str:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:mka-cak property of the setting"""
        pass

    def get_mka_cak_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingSecretFlags pertaining to the #NMSettingMacsec:mka-cak"""
        pass

    def get_mka_ckn(self) -> str:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:mka-ckn property of the setting"""
        pass

    def get_mode(self) -> SettingMacsecMode:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:mode property of the setting"""
        pass

    def get_offload(self) -> SettingMacsecOffload:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:offload property of the setting"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:parent property of the setting"""
        pass

    def get_port(self) -> int:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:port property of the setting"""
        pass

    def get_send_sci(self) -> bool:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:send-sci property of the setting"""
        pass

    def get_validation(self) -> SettingMacsecValidation:
        """

:param self: the #NMSettingMacsec
:return: the #NMSettingMacsec:validation property of the setting"""
        pass


class SettingMacsecClass:
    """"""


class SettingMacvlan(Setting):
    """MAC VLAN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingMacvlan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingMacvlan object with default values.

:return: the new empty #NMSettingMacvlan object"""
        pass

    def get_mode(self) -> SettingMacvlanMode:
        """

:param self: the #NMSettingMacvlan
:return: the #NMSettingMacvlan:mode property of the setting"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingMacvlan
:return: the #NMSettingMacvlan:parent property of the setting"""
        pass

    def get_promiscuous(self) -> bool:
        """

:param self: the #NMSettingMacvlan
:return: the #NMSettingMacvlan:promiscuous property of the setting"""
        pass

    def get_tap(self) -> bool:
        """

:param self: the #NMSettingMacvlan
:return: the #NMSettingMacvlan:tap property of the setting"""
        pass


class SettingMacvlanClass:
    """"""


class SettingMatch(Setting):
    """Match settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingMatch object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingMatch object with default values.

:return: the new empty #NMSettingMatch object  Note that this function was present in header files since version 1.14. But due to a bug the symbol is only exposed and usable since version 1.32. As workaround, use g_object_new(NM_TYPE_SETTING_MATCH) which works with all versions since 1.14."""
        pass

    def add_driver(self, driver: str=None) -> None:
        """Adds a new driver to the setting.

:param self: the #NMSettingMatch
:param driver: the driver to add
:return: """
        pass

    def add_interface_name(self, interface_name: str=None) -> None:
        """Adds a new interface name to the setting.

:param self: the #NMSettingMatch
:param interface_name: the interface name to add
:return: """
        pass

    def add_kernel_command_line(self, kernel_command_line: str=None) -> None:
        """Adds a new kernel command line argument to the setting.

:param self: the #NMSettingMatch
:param kernel_command_line: the kernel command line argument to add
:return: """
        pass

    def add_path(self, path: str=None) -> None:
        """Adds a new path to the setting.

:param self: the #NMSettingMatch
:param path: the path to add
:return: """
        pass

    def clear_drivers(self) -> None:
        """Removes all configured drivers.

:param self: the #NMSettingMatch
:return: """
        pass

    def clear_interface_names(self) -> None:
        """Removes all configured interface names.

:param self: the #NMSettingMatch
:return: """
        pass

    def clear_kernel_command_lines(self) -> None:
        """Removes all configured kernel command line arguments.

:param self: the #NMSettingMatch
:return: """
        pass

    def clear_paths(self) -> None:
        """Removes all configured paths.

:param self: the #NMSettingMatch
:return: """
        pass

    def get_driver(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingMatch
:param idx: index number of the driver to return
:return: the driver at index @idx"""
        pass

    def get_drivers(self, length: int=None) -> typing.Any:
        """Returns all the drivers.

:param self: the #NMSettingMatch
:param length: the length of the returned drivers array.
:return: the configured drivers."""
        pass

    def get_interface_name(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingMatch
:param idx: index number of the DNS search domain to return
:return: the interface name at index @idx"""
        pass

    def get_interface_names(self, length: int=None) -> typing.Any:
        """Returns all the interface names.

:param self: the #NMSettingMatch
:param length: the length of the returned interface names array.
:return: the NULL terminated list of
   configured interface names.  Before 1.26, the returned array was not %NULL terminated and you MUST provide a length."""
        pass

    def get_kernel_command_line(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingMatch
:param idx: index number of the kernel command line argument to return
:return: the kernel command line argument at index @idx"""
        pass

    def get_kernel_command_lines(self, length: int=None) -> typing.Any:
        """Returns all the kernel command line arguments.

:param self: the #NMSettingMatch
:param length: the length of the returned interface names array.
:return: the configured kernel command
    line arguments."""
        pass

    def get_num_drivers(self) -> int:
        """

:param self: the #NMSettingMatch
:return: the number of configured drivers"""
        pass

    def get_num_interface_names(self) -> int:
        """

:param self: the #NMSettingMatch
:return: the number of configured interface names"""
        pass

    def get_num_kernel_command_lines(self) -> int:
        """

:param self: the #NMSettingMatch
:return: the number of configured kernel command line arguments"""
        pass

    def get_num_paths(self) -> int:
        """

:param self: the #NMSettingMatch
:return: the number of configured paths"""
        pass

    def get_path(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingMatch
:param idx: index number of the path to return
:return: the path at index @idx"""
        pass

    def get_paths(self, length: int=None) -> typing.Any:
        """Returns all the paths.

:param self: the #NMSettingMatch
:param length: the length of the returned paths array.
:return: the configured paths."""
        pass

    def remove_driver(self, idx: int=None) -> None:
        """Removes the driver at index @idx.

:param self: the #NMSettingMatch
:param idx: index number of the driver
:return: """
        pass

    def remove_driver_by_value(self, driver: str=None) -> bool:
        """Removes @driver.

:param self: the #NMSettingMatch
:param driver: the driver to remove
:return: %TRUE if the driver was found and removed; %FALSE if it was not."""
        pass

    def remove_interface_name(self, idx: int=None) -> None:
        """Removes the interface name at index @idx.

:param self: the #NMSettingMatch
:param idx: index number of the interface name
:return: """
        pass

    def remove_interface_name_by_value(self, interface_name: str=None) -> bool:
        """Removes @interface_name.

:param self: the #NMSettingMatch
:param interface_name: the interface name to remove
:return: %TRUE if the interface name was found and removed; %FALSE if it was not."""
        pass

    def remove_kernel_command_line(self, idx: int=None) -> None:
        """Removes the kernel command line argument at index @idx.

:param self: the #NMSettingMatch
:param idx: index number of the kernel command line argument
:return: """
        pass

    def remove_kernel_command_line_by_value(self, kernel_command_line: str=None
        ) -> bool:
        """Removes @kernel_command_line.

:param self: the #NMSettingMatch
:param kernel_command_line: the kernel command line argument name to remove
:return: %TRUE if the kernel command line argument was found and removed; %FALSE if it was not."""
        pass

    def remove_path(self, idx: int=None) -> None:
        """Removes the path at index @idx.

:param self: the #NMSettingMatch
:param idx: index number of the path
:return: """
        pass

    def remove_path_by_value(self, path: str=None) -> bool:
        """Removes @path.

:param self: the #NMSettingMatch
:param path: the path to remove
:return: %TRUE if the path was found and removed; %FALSE if it was not."""
        pass


class SettingMatchClass:
    """"""


class SettingOlpcMesh(Setting):
    """OLPC Wireless Mesh Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOlpcMesh object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOlpcMesh object with default values.

:return: the new empty #NMSettingOlpcMesh object"""
        pass

    def get_channel(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_dhcp_anycast_address(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_ssid(self) -> GLib.Bytes:
        """

:param self: the #NMSettingOlpcMesh
:return: """
        pass


class SettingOlpcMeshClass:
    """"""


class SettingOvsBridge(Setting):
    """OvsBridge Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsBridge object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOvsBridge object with default values.

:return: the new empty #NMSettingOvsBridge object"""
        pass

    def get_datapath_type(self) -> str:
        """

:param self: the #NMSettingOvsBridge
:return: the #NMSettingOvsBridge:datapath_type property of the setting"""
        pass

    def get_fail_mode(self) -> str:
        """

:param self: the #NMSettingOvsBridge
:return: the #NMSettingOvsBridge:fail_mode property of the setting"""
        pass

    def get_mcast_snooping_enable(self) -> bool:
        """

:param self: the #NMSettingOvsBridge
:return: the #NMSettingOvsBridge:mcast_snooping_enable property of the setting"""
        pass

    def get_rstp_enable(self) -> bool:
        """

:param self: the #NMSettingOvsBridge
:return: the #NMSettingOvsBridge:rstp_enable property of the setting"""
        pass

    def get_stp_enable(self) -> bool:
        """

:param self: the #NMSettingOvsBridge
:return: the #NMSettingOvsBridge:stp_enable property of the setting"""
        pass


class SettingOvsBridgeClass:
    """"""


class SettingOvsDpdk(Setting):
    """OvsDpdk Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsDpdk object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOvsDpdk object with default values.

:return: the new empty #NMSettingOvsDpdk object"""
        pass

    def get_devargs(self) -> str:
        """

:param self: the #NMSettingOvsDpdk
:return: the #NMSettingOvsDpdk:devargs property of the setting"""
        pass

    def get_lsc_interrupt(self) -> SettingOvsDpdkLscInterrupt:
        """

:param self: the #NMSettingOvsDpdk
:return: the #NMSettingOvsDpdk:lsc-interrupt property of the setting"""
        pass

    def get_n_rxq(self) -> int:
        """

:param self: the #NMSettingOvsDpdk
:return: the #NMSettingOvsDpdk:n-rxq property of the setting"""
        pass

    def get_n_rxq_desc(self) -> int:
        """

:param self: the #NMSettingOvsDpdk
:return: the #NMSettingOvsDpdk:n-rxq-desc property of the setting"""
        pass

    def get_n_txq_desc(self) -> int:
        """

:param self: the #NMSettingOvsDpdk
:return: the #NMSettingOvsDpdk:n-txq-desc property of the setting"""
        pass


class SettingOvsDpdkClass:
    """"""


class SettingOvsExternalIDs(Setting):
    """OVS External IDs Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsExternalIDs object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> SettingOvsExternalIDs:
        """Creates a new #NMSettingOvsExternalIDs object with default values.

:return: the new empty #NMSettingOvsExternalIDs object"""
        pass

    @staticmethod
    def check_key(key: str=None) -> bool:
        """Checks whether @key is a valid key for OVS' external-ids.
This means, the key cannot be %NULL, not too large and valid ASCII.
Also, only digits and numbers are allowed with a few special
characters. They key must also not start with "NM.".

:param key: the key to check
:return: %TRUE if @key is a valid user data key."""
        pass

    @staticmethod
    def check_val(val: str=None) -> bool:
        """Checks whether @val is a valid user data value. This means,
value is not %NULL, not too large and valid UTF-8.

:param val: the value to check
:return: %TRUE if @val is a valid user data value."""
        pass

    def get_data(self, key: str=None) -> str:
        """

:param self: the #NMSettingOvsExternalIDs instance
:param key: the external-id to lookup
:return: the value associated with @key or %NULL if no such
   value exists."""
        pass

    def get_data_keys(self, out_len: int=None) -> typing.Any:
        """

:param self: the #NMSettingOvsExternalIDs
:param out_len: the length of the returned array
:return: a
   %NULL-terminated array containing each key from the table."""
        pass

    def set_data(self, key: str=None, val: str=None) -> None:
        """

:param self: the #NMSettingOvsExternalIDs instance
:param key: the key to set
:param val: the value to set or %NULL to clear a key.
:return: """
        pass


class SettingOvsExternalIDsClass:
    """"""


class SettingOvsInterface(Setting):
    """Open vSwitch Interface Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsInterface object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOvsInterface object with default values.

:return: the new empty #NMSettingOvsInterface object"""
        pass

    def get_interface_type(self) -> str:
        """

:param self: the #NMSettingOvsInterface
:return: the #NMSettingOvsInterface:type property of the setting"""
        pass

    def get_ofport_request(self) -> int:
        """

:param self: the #NMSettingOvsInterface
:return: id of the preassigned ovs port"""
        pass


class SettingOvsInterfaceClass:
    """"""


class SettingOvsOtherConfig(Setting):
    """OVS Other Config Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsOtherConfig object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> SettingOvsOtherConfig:
        """Creates a new #NMSettingOvsOtherConfig object with default values.

:return: the new empty #NMSettingOvsOtherConfig object"""
        pass

    def get_data(self, key: str=None) -> str:
        """

:param self: the #NMSettingOvsOtherConfig instance
:param key: the other-config to lookup
:return: the value associated with @key or %NULL if no such
   value exists."""
        pass

    def get_data_keys(self, out_len: int=None) -> typing.Any:
        """

:param self: the #NMSettingOvsOtherConfig
:param out_len: the length of the returned array
:return: a
   %NULL-terminated array containing each key from the table."""
        pass

    def set_data(self, key: str=None, val: str=None) -> None:
        """

:param self: the #NMSettingOvsOtherConfig instance
:param key: the key to set
:param val: the value to set or %NULL to clear a key.
:return: """
        pass


class SettingOvsOtherConfigClass:
    """"""


class SettingOvsPatch(Setting):
    """OvsPatch Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsPatch object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOvsPatch object with default values.

:return: the new empty #NMSettingOvsPatch object"""
        pass

    def get_peer(self) -> str:
        """

:param self: the #NMSettingOvsPatch
:return: the #NMSettingOvsPatch:peer property of the setting"""
        pass


class SettingOvsPatchClass:
    """"""


class SettingOvsPort(Setting):
    """OvsPort Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingOvsPort object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingOvsPort object with default values.

:return: the new empty #NMSettingOvsPort object"""
        pass

    def add_trunk(self, trunk: Range=None) -> None:
        """Appends a new trunk range to the setting.
This takes a reference to @trunk.

:param self: the #NMSettingOvsPort
:param trunk: the trunk to add
:return: """
        pass

    def clear_trunks(self) -> None:
        """Removes all configured trunk ranges.

:param self: the #NMSettingOvsPort
:return: """
        pass

    def get_bond_downdelay(self) -> int:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:bond-downdelay property of the setting"""
        pass

    def get_bond_mode(self) -> str:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:bond-mode property of the setting"""
        pass

    def get_bond_updelay(self) -> int:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:bond-updelay property of the setting"""
        pass

    def get_lacp(self) -> str:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:lacp property of the setting"""
        pass

    def get_num_trunks(self) -> int:
        """

:param self: the #NMSettingOvsPort
:return: the number of trunk ranges"""
        pass

    def get_tag(self) -> int:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:tag property of the setting"""
        pass

    def get_trunk(self, idx: int=None) -> Range:
        """

:param self: the #NMSettingOvsPort
:param idx: index number of the trunk range to return
:return: the trunk range at index @idx"""
        pass

    def get_vlan_mode(self) -> str:
        """

:param self: the #NMSettingOvsPort
:return: the #NMSettingOvsPort:vlan-mode property of the setting"""
        pass

    def remove_trunk(self, idx: int=None) -> None:
        """Removes the trunk range at index @idx.

:param self: the #NMSettingOvsPort
:param idx: index number of the trunk range.
:return: """
        pass

    def remove_trunk_by_value(self, start: int=None, end: int=None) -> bool:
        """Remove the trunk range with range @start to @end.

:param self: the #NMSettingOvsPort
:param start: the trunk range start index
:param end: the trunk range end index
:return: %TRUE if the trunk range was found and removed; %FALSE otherwise"""
        pass


class SettingOvsPortClass:
    """"""


class SettingPpp(Setting):
    """Point-to-Point Protocol Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingPpp object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingPpp object with default values.

:return: the new empty #NMSettingPpp object"""
        pass

    def get_baud(self) -> int:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:baud property of the setting"""
        pass

    def get_crtscts(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:crtscts property of the setting"""
        pass

    def get_lcp_echo_failure(self) -> int:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:lcp-echo-failure property of the setting"""
        pass

    def get_lcp_echo_interval(self) -> int:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:lcp-echo-interval property of the setting"""
        pass

    def get_mppe_stateful(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:mppe-stateful property of the setting"""
        pass

    def get_mru(self) -> int:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:mru property of the setting"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:mtu property of the setting"""
        pass

    def get_no_vj_comp(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:no-vj-comp property of the setting"""
        pass

    def get_noauth(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:noauth property of the setting"""
        pass

    def get_nobsdcomp(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:nobsdcomp property of the setting"""
        pass

    def get_nodeflate(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:nodeflate property of the setting"""
        pass

    def get_refuse_chap(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:refuse-chap property of the setting"""
        pass

    def get_refuse_eap(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:refuse-eap property of the setting"""
        pass

    def get_refuse_mschap(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:refuse-mschap property of the setting"""
        pass

    def get_refuse_mschapv2(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:refuse-mschapv2 property of the setting"""
        pass

    def get_refuse_pap(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:refuse-pap property of the setting"""
        pass

    def get_require_mppe(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:require-mppe property of the setting"""
        pass

    def get_require_mppe_128(self) -> bool:
        """

:param self: the #NMSettingPpp
:return: the #NMSettingPpp:require-mppe-128 property of the setting"""
        pass


class SettingPppClass:
    """"""


class SettingPppoe(Setting):
    """PPP-over-Ethernet Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingPppoe object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingPppoe object with default values.

:return: the new empty #NMSettingPppoe object"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingPppoe
:return: the #NMSettingPppoe:parent property of the setting"""
        pass

    def get_password(self) -> str:
        """

:param self: the #NMSettingPppoe
:return: the #NMSettingPppoe:password property of the setting"""
        pass

    def get_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingPppoe
:return: the #NMSettingSecretFlags pertaining to the #NMSettingPppoe:password"""
        pass

    def get_service(self) -> str:
        """

:param self: the #NMSettingPppoe
:return: the #NMSettingPppoe:service property of the setting"""
        pass

    def get_username(self) -> str:
        """

:param self: the #NMSettingPppoe
:return: the #NMSettingPppoe:username property of the setting"""
        pass


class SettingPppoeClass:
    """"""


class SettingPrefixDelegation(Setting):
    """IPv6 prefix delegation settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingPrefixDelegation object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingPrefixDelegation object with default values.

:return: the new empty #NMSettingPrefixDelegation object"""
        pass

    def get_subnet_id(self) -> int:
        """

:param self: the #NMSettingPrefixDelegation
:return: the subnet ID for prefix delegation"""
        pass


class SettingPrefixDelegationClass:
    """"""


class SettingProxy(Setting):
    """WWW Proxy Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingProxy object.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingProxy object.

:return: the new empty #NMSettingProxy object"""
        pass

    def get_browser_only(self) -> bool:
        """

:param self: the #NMSettingProxy
:return: %TRUE if this proxy configuration is only for browser clients/schemes, %FALSE otherwise."""
        pass

    def get_method(self) -> SettingProxyMethod:
        """Returns the proxy configuration method. By default the value is %NM_SETTING_PROXY_METHOD_NONE.
%NM_SETTING_PROXY_METHOD_NONE should be selected for a connection intended for direct network
access.

:param self: the #NMSettingProxy
:return: the proxy configuration method"""
        pass

    def get_pac_script(self) -> str:
        """

:param self: the #NMSettingProxy
:return: the PAC script."""
        pass

    def get_pac_url(self) -> str:
        """

:param self: the #NMSettingProxy
:return: the PAC URL for obtaining PAC file"""
        pass


class SettingProxyClass:
    """"""


class SettingSerial(Setting):
    """Serial Link Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingSerial object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingSerial object with default values.

:return: the new empty #NMSettingSerial object"""
        pass

    def get_baud(self) -> int:
        """

:param self: the #NMSettingSerial
:return: the #NMSettingSerial:baud property of the setting"""
        pass

    def get_bits(self) -> int:
        """

:param self: the #NMSettingSerial
:return: the #NMSettingSerial:bits property of the setting"""
        pass

    def get_parity(self) -> SettingSerialParity:
        """

:param self: the #NMSettingSerial
:return: the #NMSettingSerial:parity property of the setting"""
        pass

    def get_send_delay(self) -> int:
        """

:param self: the #NMSettingSerial
:return: the #NMSettingSerial:send-delay property of the setting"""
        pass

    def get_stopbits(self) -> int:
        """

:param self: the #NMSettingSerial
:return: the #NMSettingSerial:stopbits property of the setting"""
        pass


class SettingSerialClass:
    """"""


class SettingSriov(Setting):
    """SR-IOV settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingSriov object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingSriov object with default values.

:return: the new empty #NMSettingSriov object"""
        pass

    def add_vf(self, vf: SriovVF=None) -> None:
        """Appends a new VF and associated information to the setting.  The
given VF is duplicated internally and is not changed by this function.

:param self: the #NMSettingSriov
:param vf: the VF to add
:return: """
        pass

    def clear_vfs(self) -> None:
        """Removes all configured VFs.

:param self: the #NMSettingSriov
:return: """
        pass

    def get_autoprobe_drivers(self) -> Ternary:
        """Returns the value contained in the #NMSettingSriov:autoprobe-drivers
property.

:param self: the #NMSettingSriov
:return: the autoprobe-drivers property value"""
        pass

    def get_eswitch_encap_mode(self) -> SriovEswitchEncapMode:
        """

:param self: the #NMSettingSriov
:return: the value contained in the #NMSettingSriov:eswitch-encap-mode property."""
        pass

    def get_eswitch_inline_mode(self) -> SriovEswitchInlineMode:
        """

:param self: the #NMSettingSriov
:return: the value contained in the #NMSettingSriov:eswitch-inline-mode property."""
        pass

    def get_eswitch_mode(self) -> SriovEswitchMode:
        """

:param self: the #NMSettingSriov
:return: the value contained in the #NMSettingSriov:eswitch-mode property."""
        pass

    def get_num_vfs(self) -> int:
        """

:param self: the #NMSettingSriov
:return: the number of configured VFs"""
        pass

    def get_preserve_on_down(self) -> SriovPreserveOnDown:
        """

:param self: the #NMSettingSriov
:return: the value contained in the #NMSettingSriov:preserve-on-down property."""
        pass

    def get_total_vfs(self) -> int:
        """Returns the value contained in the #NMSettingSriov:total-vfs
property.

:param self: the #NMSettingSriov
:return: the total number of SR-IOV virtual functions to create"""
        pass

    def get_vf(self, idx: int=None) -> SriovVF:
        """

:param self: the #NMSettingSriov
:param idx: index number of the VF to return
:return: the VF at index @idx"""
        pass

    def remove_vf(self, idx: int=None) -> None:
        """Removes the VF at index @idx.

:param self: the #NMSettingSriov
:param idx: index number of the VF
:return: """
        pass

    def remove_vf_by_index(self, index: int=None) -> bool:
        """Removes the VF with VF index @index.

:param self: the #NMSettingSriov
:param index: the VF index of the VF to remove
:return: %TRUE if the VF was found and removed; %FALSE if it was not"""
        pass


class SettingSriovClass:
    """"""


class SettingTCConfig(Setting):
    """Linux Traffic Control Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingTCConfig object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingTCConfig object with default values.

:return: the new empty #NMSettingTCConfig object"""
        pass

    def add_qdisc(self, qdisc: TCQdisc=None) -> bool:
        """Appends a new qdisc and associated information to the setting.  The
given qdisc is duplicated internally and is not changed by this function.
If an identical qdisc (considering attributes as well) already exists, the
qdisc is not added and the function returns %FALSE.

:param self: the #NMSettingTCConfig
:param qdisc: the qdisc to add
:return: %TRUE if the qdisc was added; %FALSE if the qdisc was already known."""
        pass

    def add_tfilter(self, tfilter: TCTfilter=None) -> bool:
        """Appends a new tfilter and associated information to the setting.  The
given tfilter is duplicated internally and is not changed by this function.
If an identical tfilter (considering attributes as well) already exists, the
tfilter is not added and the function returns %FALSE.

:param self: the #NMSettingTCConfig
:param tfilter: the tfilter to add
:return: %TRUE if the tfilter was added; %FALSE if the tfilter was already known."""
        pass

    def clear_qdiscs(self) -> None:
        """Removes all configured queueing disciplines.

:param self: the #NMSettingTCConfig
:return: """
        pass

    def clear_tfilters(self) -> None:
        """Removes all configured queueing disciplines.

:param self: the #NMSettingTCConfig
:return: """
        pass

    def get_num_qdiscs(self) -> int:
        """

:param self: the #NMSettingTCConfig
:return: the number of configured queueing disciplines"""
        pass

    def get_num_tfilters(self) -> int:
        """

:param self: the #NMSettingTCConfig
:return: the number of configured queueing disciplines"""
        pass

    def get_qdisc(self, idx: int=None) -> TCQdisc:
        """

:param self: the #NMSettingTCConfig
:param idx: index number of the qdisc to return
:return: the qdisc at index @idx"""
        pass

    def get_tfilter(self, idx: int=None) -> TCTfilter:
        """

:param self: the #NMSettingTCConfig
:param idx: index number of the tfilter to return
:return: the tfilter at index @idx"""
        pass

    def remove_qdisc(self, idx: int=None) -> None:
        """Removes the qdisc at index @idx.

:param self: the #NMSettingTCConfig
:param idx: index number of the qdisc
:return: """
        pass

    def remove_qdisc_by_value(self, qdisc: TCQdisc=None) -> bool:
        """Removes the first matching qdisc that matches @qdisc.

:param self: the #NMSettingTCConfig
:param qdisc: the qdisc to remove
:return: %TRUE if the qdisc was found and removed; %FALSE if it was not."""
        pass

    def remove_tfilter(self, idx: int=None) -> None:
        """Removes the tfilter at index @idx.

:param self: the #NMSettingTCConfig
:param idx: index number of the tfilter
:return: """
        pass

    def remove_tfilter_by_value(self, tfilter: TCTfilter=None) -> bool:
        """Removes the first matching tfilter that matches @tfilter.

:param self: the #NMSettingTCConfig
:param tfilter: the tfilter to remove
:return: %TRUE if the tfilter was found and removed; %FALSE if it was not."""
        pass


class SettingTCConfigClass:
    """"""


class SettingTeam(Setting):
    """Teaming Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingTeam object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingTeam object with default values.

:return: the new empty #NMSettingTeam object"""
        pass

    def add_link_watcher(self, link_watcher: TeamLinkWatcher=None) -> bool:
        """Appends a new link watcher to the setting.

:param self: the #NMSettingTeam
:param link_watcher: the link watcher to add
:return: %TRUE if the link watcher is added; %FALSE if an identical link watcher was already there."""
        pass

    def add_runner_tx_hash(self, txhash: str=None) -> bool:
        """Adds a new txhash element to the setting.

:param self: the #NMSettingTeam
:param txhash: the element to add to txhash
:return: %TRUE if the txhash element was added; %FALSE if the element was already knnown."""
        pass

    def clear_link_watchers(self) -> None:
        """Removes all configured link watchers.

:param self: the #NMSettingTeam
:return: """
        pass

    def get_config(self) -> str:
        """

:param self: the #NMSettingTeam
:return: the #NMSettingTeam:config property of the setting"""
        pass

    def get_link_watcher(self, idx: int=None) -> TeamLinkWatcher:
        """

:param self: the #NMSettingTeam
:param idx: index number of the link watcher to return
:return: the link watcher at index @idx."""
        pass

    def get_mcast_rejoin_count(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:mcast-rejoin-count property of the setting"""
        pass

    def get_mcast_rejoin_interval(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:mcast-rejoin-interval property of the setting"""
        pass

    def get_notify_peers_count(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:notify-peers-count property of the setting"""
        pass

    def get_notify_peers_interval(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:notify-peers-interval property of the setting"""
        pass

    def get_num_link_watchers(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the number of configured link watchers"""
        pass

    def get_num_runner_tx_hash(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the number of elements in txhash"""
        pass

    def get_runner(self) -> str:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner property of the setting"""
        pass

    def get_runner_active(self) -> bool:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner_active property of the setting"""
        pass

    def get_runner_agg_select_policy(self) -> str:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-agg-select-policy property of the setting"""
        pass

    def get_runner_fast_rate(self) -> bool:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-fast-rate property of the setting"""
        pass

    def get_runner_hwaddr_policy(self) -> str:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-hwaddr-policy property of the setting"""
        pass

    def get_runner_min_ports(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-min-ports property of the setting"""
        pass

    def get_runner_sys_prio(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-sys-prio property of the setting"""
        pass

    def get_runner_tx_balancer(self) -> str:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-tx-balancer property of the setting"""
        pass

    def get_runner_tx_balancer_interval(self) -> int:
        """

:param self: the #NMSettingTeam
:return: the ##NMSettingTeam:runner-tx-balancer_interval property of the setting"""
        pass

    def get_runner_tx_hash(self, idx: int=None) -> str:
        """

:param self: the #NMSettingTeam
:param idx: index number of the txhash element to return
:return: the txhash element at index @idx"""
        pass

    def remove_link_watcher(self, idx: int=None) -> None:
        """Removes the link watcher at index #idx.

:param self: the #NMSettingTeam
:param idx: index number of the link watcher to remove
:return: """
        pass

    def remove_link_watcher_by_value(self, link_watcher: TeamLinkWatcher=None
        ) -> bool:
        """Removes the link watcher entry matching link_watcher.

:param self: the #NMSettingTeam
:param link_watcher: the link watcher to remove
:return: %TRUE if the link watcher was found and removed, %FALSE otherwise."""
        pass

    def remove_runner_tx_hash(self, idx: int=None) -> None:
        """Removes the txhash element at index @idx.

:param self: the #NMSettingTeam
:param idx: index number of the element to remove from txhash
:return: """
        pass

    def remove_runner_tx_hash_by_value(self, txhash: str=None) -> bool:
        """Removes the txhash element #txhash

:param self: the #NMSetetingTeam
:param txhash: the txhash element to remove
:return: %TRUE if the txhash element was found and removed; %FALSE if it was not."""
        pass


class SettingTeamClass:
    """"""


class SettingTeamPort(Setting):
    """Team Port Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingTeamPort object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingTeamPort object with default values.

:return: the new empty #NMSettingTeamPort object"""
        pass

    def add_link_watcher(self, link_watcher: TeamLinkWatcher=None) -> bool:
        """Appends a new link watcher to the setting.

:param self: the #NMSettingTeamPort
:param link_watcher: the link watcher to add
:return: %TRUE if the link watcher is added; %FALSE if an identical link watcher was already there."""
        pass

    def clear_link_watchers(self) -> None:
        """Removes all configured link watchers.

:param self: the #NMSettingTeamPort
:return: """
        pass

    def get_config(self) -> str:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:config property of the setting"""
        pass

    def get_lacp_key(self) -> int:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:lacp-key property of the setting"""
        pass

    def get_lacp_prio(self) -> int:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:lacp-prio property of the setting"""
        pass

    def get_link_watcher(self, idx: int=None) -> TeamLinkWatcher:
        """

:param self: the #NMSettingTeamPort
:param idx: index number of the link watcher to return
:return: the link watcher at index @idx."""
        pass

    def get_num_link_watchers(self) -> int:
        """

:param self: the #NMSettingTeamPort
:return: the number of configured link watchers"""
        pass

    def get_prio(self) -> int:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:prio property of the setting"""
        pass

    def get_queue_id(self) -> int:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:queue_id property of the setting"""
        pass

    def get_sticky(self) -> bool:
        """

:param self: the #NMSettingTeamPort
:return: the #NMSettingTeamPort:sticky property of the setting"""
        pass

    def remove_link_watcher(self, idx: int=None) -> None:
        """Removes the link watcher at index #idx.

:param self: the #NMSettingTeamPort
:param idx: index number of the link watcher to remove
:return: """
        pass

    def remove_link_watcher_by_value(self, link_watcher: TeamLinkWatcher=None
        ) -> bool:
        """Removes the link watcher entry matching link_watcher.

:param self: the #NMSettingTeamPort
:param link_watcher: the link watcher to remove
:return: %TRUE if the link watcher was found and removed, %FALSE otherwise."""
        pass


class SettingTeamPortClass:
    """"""


class SettingTun(Setting):
    """Tunnel Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingTun object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingTun object with default values.

:return: the new empty #NMSettingTun object"""
        pass

    def get_group(self) -> str:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:group property of the setting"""
        pass

    def get_mode(self) -> SettingTunMode:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:mode property of the setting"""
        pass

    def get_multi_queue(self) -> bool:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:multi-queue property of the setting"""
        pass

    def get_owner(self) -> str:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:owner property of the setting"""
        pass

    def get_pi(self) -> bool:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:pi property of the setting"""
        pass

    def get_vnet_hdr(self) -> bool:
        """

:param self: the #NMSettingTun
:return: the #NMSettingTun:vnet_hdr property of the setting"""
        pass


class SettingTunClass:
    """"""


class SettingUser(Setting):
    """General User Profile Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingUser object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingUser object with default values.

:return: the new empty #NMSettingUser object"""
        pass

    @staticmethod
    def check_key(key: str=None) -> bool:
        """Checks whether @key is a valid user data key. This means,
key is not %NULL, not too large and valid ASCII. Also,
only digits and numbers are allowed with a few special
characters. The key must contain at least one '.' and
look like a fully qualified DNS name.

:param key: the key to check
:return: %TRUE if @key is a valid user data key."""
        pass

    @staticmethod
    def check_val(val: str=None) -> bool:
        """Checks whether @val is a valid user data value. This means,
value is not %NULL, not too large and valid UTF-8.

:param val: the value to check
:return: %TRUE if @val is a valid user data value."""
        pass

    def get_data(self, key: str=None) -> str:
        """

:param self: the #NMSettingUser instance
:param key: the key to lookup
:return: the value associated with @key or %NULL if no such
   value exists."""
        pass

    def get_keys(self, out_len: int=None) -> typing.Any:
        """

:param self: the #NMSettingUser
:param out_len: the length of the returned array
:return: a
   %NULL-terminated array containing each key from the table."""
        pass

    def set_data(self, key: str=None, val: str=None) -> bool:
        """

:param self: the #NMSettingUser instance
:param key: the key to set
:param val: the value to set or %NULL to clear a key.
:return: %TRUE if the operation was successful. The operation
   can fail if @key or @val are not valid strings according
   to nm_setting_user_check_key() and nm_setting_user_check_val()."""
        pass


class SettingUserClass:
    """"""


class SettingVeth(Setting):
    """Veth Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingVeth object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingVeth object with default values.

:return: the new empty #NMSettingVeth object"""
        pass

    def get_peer(self) -> str:
        """

:param self: the #NMSettingVeth
:return: the #NMSettingVeth:peer property of the setting"""
        pass


class SettingVethClass:
    """"""


class SettingVlan(Setting):
    """VLAN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingVlan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingVlan object with default values.

:return: the new empty #NMSettingVlan object"""
        pass

    def add_priority(self, map: VlanPriorityMap=None, _from: int=None, to:
        int=None) -> bool:
        """Adds a priority mapping to the #NMSettingVlan:ingress_priority_map or
#NMSettingVlan:egress_priority_map properties of the setting. If @from is
already in the given priority map, this function will overwrite the
existing entry with the new @to.

If @map is #NM_VLAN_INGRESS_MAP then @from is the incoming 802.1q VLAN
Priority Code Point (PCP) value, and @to is the Linux SKB priority value.

If @map is #NM_VLAN_EGRESS_MAP then @from is the Linux SKB priority value and
@to is the outgoing 802.1q VLAN Priority Code Point (PCP) value.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param _from: the priority to map to @to
:param to: the priority to map @from to
:return: %TRUE."""
        pass

    def add_priority_str(self, map: VlanPriorityMap=None, str: str=None
        ) -> bool:
        """Adds a priority map entry into either the #NMSettingVlan:ingress_priority_map
or the #NMSettingVlan:egress_priority_map properties.  The priority map maps
the Linux SKB priorities to 802.1p priorities.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param str: the string which contains a priority map, like "3:7"
:return: %TRUE if the entry was successfully added to the list, or it overwrote the old value, %FALSE if @str is not a valid mapping."""
        pass

    def clear_priorities(self, map: VlanPriorityMap=None) -> None:
        """Clear all the entries from #NMSettingVlan:ingress_priority_map or
#NMSettingVlan:egress_priority_map properties.

:param self: the #NMSettingVlan
:param map: the type of priority map
:return: """
        pass

    def get_flags(self) -> int:
        """

:param self: the #NMSettingVlan
:return: the #NMSettingVlan:flags property of the setting"""
        pass

    def get_id(self) -> int:
        """

:param self: the #NMSettingVlan
:return: the #NMSettingVlan:id property of the setting"""
        pass

    def get_num_priorities(self, map: VlanPriorityMap=None) -> int:
        """Returns the number of entries in the
#NMSettingVlan:ingress_priority_map or #NMSettingVlan:egress_priority_map
properties of this setting.

:param self: the #NMSettingVlan
:param map: the type of priority map
:return: return the number of ingress/egress priority entries."""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingVlan
:return: the #NMSettingVlan:parent property of the setting"""
        pass

    def get_priority(self, map: VlanPriorityMap=None, idx: int=None,
        out_from: int=None, out_to: int=None) -> bool:
        """Retrieve one of the entries of the #NMSettingVlan:ingress_priority_map
or #NMSettingVlan:egress_priority_map properties of this setting.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param idx: the zero-based index of the ingress/egress priority map entry
:param out_from: on return the value of the priority map's 'from' item
:param out_to: on return the value of priority map's 'to' item
:return: returns %TRUE if @idx is in range. Otherwise, %FALSE."""
        pass

    def get_protocol(self) -> str:
        """

:param self: the #NMSettingVlan
:return: the #NMSettingVlan:protocol property of the setting"""
        pass

    def remove_priority(self, map: VlanPriorityMap=None, idx: int=None
        ) -> None:
        """Removes the priority map at index @idx from the
#NMSettingVlan:ingress_priority_map or #NMSettingVlan:egress_priority_map
properties.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param idx: the zero-based index of the priority map to remove
:return: """
        pass

    def remove_priority_by_value(self, map: VlanPriorityMap=None, _from:
        int=None, to: int=None) -> bool:
        """Removes the priority map @form:@to from the #NMSettingVlan:ingress_priority_map
or #NMSettingVlan:egress_priority_map (according to @map argument)
properties.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param _from: the priority to map to @to
:param to: the priority to map @from to
:return: %TRUE if the priority mapping was found and removed; %FALSE if it was not."""
        pass

    def remove_priority_str_by_value(self, map: VlanPriorityMap=None, str:
        str=None) -> bool:
        """Removes the priority map @str from the #NMSettingVlan:ingress_priority_map
or #NMSettingVlan:egress_priority_map (according to @map argument)
properties.

:param self: the #NMSettingVlan
:param map: the type of priority map
:param str: the string which contains a priority map, like "3:7"
:return: %TRUE if the priority mapping was found and removed; %FALSE if it was not."""
        pass


class SettingVlanClass:
    """"""


class SettingVpn(Setting):
    """VPN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingVpn object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingVpn object with default values.

:return: the new empty #NMSettingVpn object"""
        pass

    def add_data_item(self, key: str=None, item: str=None) -> None:
        """Establishes a relationship between @key and @item internally in the
setting which may be retrieved later.  Should not be used to store passwords
or other secrets, which is what nm_setting_vpn_add_secret() is for.

Before 1.24, @item must not be %NULL and not an empty string. Since 1.24,
@item can be set to an empty string. It can also be set to %NULL to unset
the key. In that case, the behavior is as if calling nm_setting_vpn_remove_data_item().

:param self: the #NMSettingVpn
:param key: a name that uniquely identifies the given value @item
:param item: the value to be referenced by @key
:return: """
        pass

    def add_secret(self, key: str=None, secret: str=None) -> None:
        """Establishes a relationship between @key and @secret internally in the
setting which may be retrieved later.

Before 1.24, @secret must not be %NULL and not an empty string. Since 1.24,
@secret can be set to an empty string. It can also be set to %NULL to unset
the key. In that case, the behavior is as if calling nm_setting_vpn_remove_secret().

:param self: the #NMSettingVpn
:param key: a name that uniquely identifies the given secret @secret
:param secret: the secret to be referenced by @key
:return: """
        pass

    def foreach_data_item(self, func: VpnIterFunc=None, user_data:
        typing.Any=None) -> None:
        """Iterates all data items stored in this setting.  It is safe to add, remove,
and modify data items inside @func, though any additions or removals made
during iteration will not be part of the iteration.

:param self: a #NMSettingVpn
:param func: an user provided function
:param user_data: data to be passed to @func
:return: """
        pass

    def foreach_secret(self, func: VpnIterFunc=None, user_data: typing.Any=None
        ) -> None:
        """Iterates all secrets stored in this setting.  It is safe to add, remove,
and modify secrets inside @func, though any additions or removals made during
iteration will not be part of the iteration.

:param self: a #NMSettingVpn
:param func: an user provided function
:param user_data: data to be passed to @func
:return: """
        pass

    def get_data_item(self, key: str=None) -> str:
        """Retrieves the data item of a key/value relationship previously established
by nm_setting_vpn_add_data_item().

:param self: the #NMSettingVpn
:param key: the name of the data item to retrieve
:return: the data item, if any"""
        pass

    def get_data_keys(self, out_length: int=None) -> typing.Any:
        """Retrieves every data key inside @setting, as an array.

:param self: the #NMSettingVpn
:param out_length: the length of the returned array
:return: a
   %NULL-terminated array containing each data key or %NULL if
   there are no data items."""
        pass

    def get_num_data_items(self) -> int:
        """Gets number of key/value pairs of VPN configuration data.

:param self: the #NMSettingVpn
:return: the number of VPN plugin specific configuration data items"""
        pass

    def get_num_secrets(self) -> int:
        """Gets number of VPN plugin specific secrets in the setting.

:param self: the #NMSettingVpn
:return: the number of VPN plugin specific secrets"""
        pass

    def get_persistent(self) -> bool:
        """

:param self: the #NMSettingVpn
:return: the #NMSettingVpn:persistent property of the setting"""
        pass

    def get_secret(self, key: str=None) -> str:
        """Retrieves the secret of a key/value relationship previously established
by nm_setting_vpn_add_secret().

:param self: the #NMSettingVpn
:param key: the name of the secret to retrieve
:return: the secret, if any"""
        pass

    def get_secret_keys(self, out_length: int=None) -> typing.Any:
        """Retrieves every secret key inside @setting, as an array.

:param self: the #NMSettingVpn
:param out_length: the length of the returned array
:return: a
   %NULL-terminated array containing each secret key or %NULL if
   there are no secrets."""
        pass

    def get_service_type(self) -> str:
        """Returns the service name of the VPN, which identifies the specific VPN
plugin that should be used to connect to this VPN.

:param self: the #NMSettingVpn
:return: the VPN plugin's service name"""
        pass

    def get_timeout(self) -> int:
        """

:param self: the #NMSettingVpn
:return: the #NMSettingVpn:timeout property of the setting"""
        pass

    def get_user_name(self) -> str:
        """

:param self: the #NMSettingVpn
:return: the #NMSettingVpn:user-name property of the setting"""
        pass

    def remove_data_item(self, key: str=None) -> bool:
        """Deletes a key/value relationship previously established by
nm_setting_vpn_add_data_item().

:param self: the #NMSettingVpn
:param key: the name of the data item to remove
:return: %TRUE if the data item was found and removed from the internal list, %FALSE if it was not."""
        pass

    def remove_secret(self, key: str=None) -> bool:
        """Deletes a key/value relationship previously established by
nm_setting_vpn_add_secret().

:param self: the #NMSettingVpn
:param key: the name of the secret to remove
:return: %TRUE if the secret was found and removed from the internal list, %FALSE if it was not."""
        pass


class SettingVpnClass:
    """"""


class SettingVrf(Setting):
    """VRF settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingVrf object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingVrf object with default values.

:return: the new empty #NMSettingVrf object"""
        pass

    def get_table(self) -> int:
        """

:param self: the #NMSettingVrf
:return: the routing table for the VRF"""
        pass


class SettingVrfClass:
    """"""


class SettingVxlan(Setting):
    """VXLAN Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingVxlan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingVxlan object with default values.

:return: the new empty #NMSettingVxlan object"""
        pass

    def get_ageing(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:ageing property of the setting"""
        pass

    def get_destination_port(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:destination-port property of the setting"""
        pass

    def get_id(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:id property of the setting"""
        pass

    def get_l2_miss(self) -> bool:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:l2_miss property of the setting"""
        pass

    def get_l3_miss(self) -> bool:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:l3_miss property of the setting"""
        pass

    def get_learning(self) -> bool:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:learning property of the setting"""
        pass

    def get_limit(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:limit property of the setting"""
        pass

    def get_local(self) -> str:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:local property of the setting"""
        pass

    def get_parent(self) -> str:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:parent property of the setting"""
        pass

    def get_proxy(self) -> bool:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:proxy property of the setting"""
        pass

    def get_remote(self) -> str:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:remote property of the setting"""
        pass

    def get_rsc(self) -> bool:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:rsc property of the setting"""
        pass

    def get_source_port_max(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:source-port-max property of the setting"""
        pass

    def get_source_port_min(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:source-port-min property of the setting"""
        pass

    def get_tos(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:tos property of the setting"""
        pass

    def get_ttl(self) -> int:
        """

:param self: the #NMSettingVxlan
:return: the #NMSettingVxlan:ttl property of the setting"""
        pass


class SettingVxlanClass:
    """"""


class SettingWifiP2P(Setting):
    """Wi-Fi P2P Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWifiP2P object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWifiP2P object with default values.

:return: the new empty #NMSettingWifiP2P object"""
        pass

    def get_peer(self) -> str:
        """

:param self: the #NMSettingWifiP2P
:return: the #NMSettingWifiP2P:peer property of the setting"""
        pass

    def get_wfd_ies(self) -> GLib.Bytes:
        """

:param self: the #NMSettingWiFiP2P
:return: the #NMSettingWiFiP2P:wfd-ies property of the setting"""
        pass

    def get_wps_method(self) -> SettingWirelessSecurityWpsMethod:
        """

:param self: the #NMSettingWifiP2P
:return: the #NMSettingWifiP2P:wps-method property of the setting"""
        pass


class SettingWifiP2PClass:
    """"""


class SettingWimax(Setting):
    """WiMax Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWimax object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWimax object with default values.

:return: the new empty #NMSettingWimax object"""
        pass

    def get_mac_address(self) -> str:
        """Returns the MAC address of a WiMAX device which this connection is locked
to.

:param self: the #NMSettingWimax
:return: the MAC address"""
        pass

    def get_network_name(self) -> str:
        """Returns the WiMAX NSP name (ex "Sprint" or "CLEAR") which identifies the
specific WiMAX network this setting describes a connection to.

:param self: the #NMSettingWimax
:return: the WiMAX NSP name"""
        pass


class SettingWimaxClass:
    """"""


class SettingWireGuard(Setting):
    """WireGuard Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWireGuard object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWireGuard object with default values.

:return: the new empty #NMSettingWireGuard object"""
        pass

    def append_peer(self, peer: WireGuardPeer=None) -> None:
        """If a peer with the same public-key already exists, that
one is replaced by @peer. The new @peer is always appended
(or moved to) the end, so in case a peer is replaced, the
indexes are shifted and the number of peers stays unchanged.

:param self: the #NMSettingWireGuard instance
:param peer: the #NMWireGuardPeer instance to append.   This seals @peer and keeps a reference on the   instance.
:return: """
        pass

    def clear_peers(self) -> int:
        """

:param self: the #NMSettingWireGuard instance
:return: the number of cleared peers."""
        pass

    def get_fwmark(self) -> int:
        """

:param self: the #NMSettingWireGuard instance
:return: the set firewall mark."""
        pass

    def get_ip4_auto_default_route(self) -> Ternary:
        """

:param self: the #NMSettingWireGuard setting.
:return: the "ip4-auto-default-route" property of the setting."""
        pass

    def get_ip6_auto_default_route(self) -> Ternary:
        """

:param self: the #NMSettingWireGuard setting.
:return: the "ip6-auto-default-route" property of the setting."""
        pass

    def get_listen_port(self) -> int:
        """

:param self: the #NMSettingWireGuard instance
:return: the set UDP listen port."""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingWireGuard instance
:return: the MTU of the setting."""
        pass

    def get_peer(self, idx: int=None) -> WireGuardPeer:
        """

:param self: the #NMSettingWireGuard instance
:param idx: the index to lookup.
:return: the #NMWireGuardPeer entry at
   index @idx. If the index is out of range, %NULL is returned."""
        pass

    def get_peer_by_public_key(self, public_key: str=None, out_idx: int=None
        ) -> WireGuardPeer:
        """

:param self: the #NMSettingWireGuard instance
:param public_key: the public key for looking up the   peer.
:param out_idx: optional output argument   for the index of the found peer. If no index is found,   this is set to the nm_setting_wireguard_get_peers_len().
:return: the #NMWireGuardPeer instance with a
   matching public key. If no such peer exists, %NULL is returned."""
        pass

    def get_peer_routes(self) -> bool:
        """

:param self: the #NMSettingWireGuard instance
:return: whether automatically add peer routes."""
        pass

    def get_peers_len(self) -> int:
        """

:param self: the #NMSettingWireGuard instance
:return: the number of registered peers."""
        pass

    def get_private_key(self) -> str:
        """

:param self: the #NMSettingWireGuard instance
:return: the set private-key or %NULL."""
        pass

    def get_private_key_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingWireGuard instance
:return: the secret-flags for #NMSettingWireGuard:private-key."""
        pass

    def remove_peer(self, idx: int=None) -> bool:
        """

:param self: the #NMSettingWireGuard instance
:param idx: the index to remove.
:return: %TRUE if @idx was in range and a peer
   was removed. Otherwise, @self is unchanged."""
        pass

    def set_peer(self, peer: WireGuardPeer=None, idx: int=None) -> None:
        """If @idx is one past the last peer, the behavior is the same
as nm_setting_wireguard_append_peer().
Otherwise, the peer will be at @idx and replace the peer
instance at that index. Note that if a peer with the same
public-key exists on another index, then that peer will also
be replaced. In that case, the number of peers will shrink
by one (because the one at @idx got replace and then one
with the same public-key got removed). This also means,
that the resulting index afterwards may be one less than
@idx (if another peer with a lower index was dropped).

:param self: the #NMSettingWireGuard instance
:param peer: the #NMWireGuardPeer instance to set.   This seals @peer and keeps a reference on the   instance.
:param idx: the index, in the range of 0 to the number of   peers (including). That means, if @idx is one past   the end of the number of peers, this is the same as   nm_setting_wireguard_append_peer(). Otherwise, the   peer at this index is replaced.
:return: """
        pass


class SettingWireGuardClass:
    """"""


class SettingWired(Setting):
    """Wired Ethernet Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWired object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWired object with default values.

:return: the new empty #NMSettingWired object"""
        pass

    def add_mac_blacklist_item(self, mac: str=None) -> bool:
        """Adds a new MAC address to the #NMSettingWired:mac-address-blacklist property.

:param self: the #NMSettingWired
:param mac: the MAC address string (hex-digits-and-colons notation) to blacklist
:return: %TRUE if the MAC address was added; %FALSE if the MAC address is invalid or was already present"""
        pass

    def add_mac_denylist_item(self, mac: str=None) -> bool:
        """Adds a new MAC address to the #NMSettingWired:mac-address-denylist property.

:param self: the #NMSettingWired
:param mac: the MAC address string (hex-digits-and-colons notation) to denylist
:return: %TRUE if the MAC address was added; %FALSE if the MAC address is invalid or was already present"""
        pass

    def add_s390_option(self, key: str=None, value: str=None) -> bool:
        """Add an option to the table. If the key already exists, the value gets
replaced.

Before 1.32, the function would assert that the key is valid. Since then,
an invalid key gets silently added but renders the profile as invalid.

:param self: the #NMSettingWired
:param key: key name for the option
:param value: value for the option
:return: since 1.32 this always returns %TRUE."""
        pass

    def clear_mac_blacklist_items(self) -> None:
        """Removes all blacklisted MAC addresses.

:param self: the #NMSettingWired
:return: """
        pass

    def clear_mac_denylist_items(self) -> None:
        """Removes all denylisted MAC addresses.

:param self: the #NMSettingWired
:return: """
        pass

    def get_accept_all_mac_addresses(self) -> Ternary:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:accept-all-mac-addresses property of the setting"""
        pass

    def get_auto_negotiate(self) -> bool:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:auto-negotiate property of the setting"""
        pass

    def get_cloned_mac_address(self) -> str:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:cloned-mac-address property of the setting"""
        pass

    def get_duplex(self) -> str:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:duplex property of the setting"""
        pass

    def get_generate_mac_address_mask(self) -> str:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:generate-mac-address-mask property of the setting"""
        pass

    def get_mac_address(self) -> str:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:mac-address property of the setting"""
        pass

    def get_mac_address_blacklist(self) -> typing.Any:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:mac-address-blacklist property of the setting"""
        pass

    def get_mac_address_denylist(self) -> typing.Any:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:mac-address-denylist property of the setting"""
        pass

    def get_mac_blacklist_item(self, idx: int=None) -> str:
        """Since 1.48, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingWired
:param idx: the zero-based index of the MAC address entry
:return: the blacklisted MAC address string (hex-digits-and-colons notation) at index @idx"""
        pass

    def get_mac_denylist_item(self, idx: int=None) -> str:
        """

:param self: the #NMSettingWired
:param idx: the zero-based index of the MAC address entry
:return: the denylisted MAC address string (hex-digits-and-colons notation) at index @idx"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:mtu property of the setting"""
        pass

    def get_num_mac_blacklist_items(self) -> int:
        """

:param self: the #NMSettingWired
:return: the number of blacklisted MAC addresses"""
        pass

    def get_num_mac_denylist_items(self) -> int:
        """

:param self: the #NMSettingWired
:return: the number of denylisted MAC addresses"""
        pass

    def get_num_s390_options(self) -> int:
        """Returns the number of s390-specific options that should be set for this
device when it is activated.  This can be used to retrieve each s390
option individually using nm_setting_wired_get_s390_option().

:param self: the #NMSettingWired
:return: the number of s390-specific device options"""
        pass

    def get_port(self) -> str:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:port property of the setting"""
        pass

    def get_s390_nettype(self) -> str:
        """Returns the s390 device type this connection should apply to.  Will be one
of 'qeth', 'lcs', or 'ctc'.

:param self: the #NMSettingWired
:return: the s390 device type"""
        pass

    def get_s390_option(self, idx: int=None, out_key: str=None, out_value:
        str=None) -> bool:
        """Given an index, return the value of the s390 option at that index.  indexes
are *not* guaranteed to be static across modifications to options done by
nm_setting_wired_add_s390_option() and nm_setting_wired_remove_s390_option(),
and should not be used to refer to options except for short periods of time
such as during option iteration.

:param self: the #NMSettingWired
:param idx: index of the desired option, from 0 to nm_setting_wired_get_num_s390_options() - 1
:param out_key: on return, the key   name of the s390 specific option; this value is owned by the setting and   should not be modified
:param out_value: on return, the value   of the key of the s390 specific option; this value is owned by the setting   and should not be modified
:return: %TRUE on success if the index was valid and an option was found, %FALSE if the index was invalid (ie, greater than the number of options currently held by the setting)"""
        pass

    def get_s390_option_by_key(self, key: str=None) -> str:
        """Returns the value associated with the s390-specific option specified by
@key, if it exists.

:param self: the #NMSettingWired
:param key: the key for which to retrieve the value
:return: the value, or %NULL if the key/value pair was never added to the setting; the value is owned by the setting and must not be modified"""
        pass

    def get_s390_subchannels(self) -> typing.Any:
        """Return the list of s390 subchannels that identify the device that this
connection is applicable to.  The connection should only be used in
conjunction with that device.

:param self: the #NMSettingWired
:return: array of strings, each specifying
   one subchannel the s390 device uses to communicate to the host."""
        pass

    def get_speed(self) -> int:
        """

:param self: the #NMSettingWired
:return: the #NMSettingWired:speed property of the setting"""
        pass

    def get_valid_s390_options(self) -> typing.Any:
        """Returns a list of valid s390 options.

The @setting argument is unused and %NULL may be passed instead.

:param self: the #NMSettingWired. This argument is unused   and you may pass %NULL.
:return: a %NULL-terminated array of strings of valid s390 options."""
        pass

    def get_wake_on_lan(self) -> SettingWiredWakeOnLan:
        """Returns the Wake-on-LAN options enabled for the connection

:param self: the #NMSettingWired
:return: the Wake-on-LAN options"""
        pass

    def get_wake_on_lan_password(self) -> str:
        """Returns the Wake-on-LAN password. This only applies to
%NM_SETTING_WIRED_WAKE_ON_LAN_MAGIC.

:param self: the #NMSettingWired
:return: the Wake-on-LAN setting password, or %NULL if there is no password."""
        pass

    def remove_mac_blacklist_item(self, idx: int=None) -> None:
        """Removes the MAC address at index @idx from the blacklist.

:param self: the #NMSettingWired
:param idx: index number of the MAC address
:return: """
        pass

    def remove_mac_blacklist_item_by_value(self, mac: str=None) -> bool:
        """Removes the MAC address @mac from the blacklist.

:param self: the #NMSettingWired
:param mac: the MAC address string (hex-digits-and-colons notation) to remove from the blacklist
:return: %TRUE if the MAC address was found and removed; %FALSE if it was not."""
        pass

    def remove_mac_denylist_item(self, idx: int=None) -> None:
        """Removes the MAC address at index @idx from the denylist.

:param self: the #NMSettingWired
:param idx: index number of the MAC address
:return: """
        pass

    def remove_mac_denylist_item_by_value(self, mac: str=None) -> bool:
        """Removes the MAC address @mac from the denylist.

:param self: the #NMSettingWired
:param mac: the MAC address string (hex-digits-and-colons notation) to remove from the denylist
:return: %TRUE if the MAC address was found and removed; %FALSE if it was not."""
        pass

    def remove_s390_option(self, key: str=None) -> bool:
        """Remove the s390-specific option referenced by @key from the internal option
list.

:param self: the #NMSettingWired
:param key: key name for the option to remove
:return: %TRUE if the option was found and removed from the internal option list, %FALSE if it was not."""
        pass


class SettingWiredClass:
    """"""


class SettingWireless(Setting):
    """Wi-Fi Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWireless object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWireless object with default values.

:return: the new empty #NMSettingWireless object"""
        pass

    def add_mac_blacklist_item(self, mac: str=None) -> bool:
        """Adds a new MAC address to the #NMSettingWireless:mac-address-denylist property.

:param self: the #NMSettingWireless
:param mac: the MAC address string (hex-digits-and-colons notation) to denylist
:return: %TRUE if the MAC address was added; %FALSE if the MAC address is invalid or was already present"""
        pass

    def add_mac_denylist_item(self, mac: str=None) -> bool:
        """Adds a new MAC address to the #NMSettingWireless:mac-address-denylist property.

:param self: the #NMSettingWireless
:param mac: the MAC address string (hex-digits-and-colons notation) to denylist
:return: %TRUE if the MAC address was added; %FALSE if the MAC address is invalid or was already present"""
        pass

    def add_seen_bssid(self, bssid: str=None) -> bool:
        """Adds a new Wi-Fi AP's BSSID to the previously seen BSSID list of the setting.
NetworkManager now tracks previously seen BSSIDs internally so this function
no longer has much use. Actually, changes you make using this function will
not be preserved.

:param self: the #NMSettingWireless
:param bssid: the new BSSID to add to the list
:return: %TRUE if @bssid was already known, %FALSE if not"""
        pass

    def ap_security_compatible(self, s_wireless_sec:
        SettingWirelessSecurity=None, ap_flags: NM80211ApFlags=None, ap_wpa:
        NM80211ApSecurityFlags=None, ap_rsn: NM80211ApSecurityFlags=None,
        ap_mode: NM80211Mode=None) -> bool:
        """Given a #NMSettingWireless and an optional #NMSettingWirelessSecurity,
determine if the configuration given by the settings is compatible with
the security of an access point using that access point's capability flags
and mode.  Useful for clients that wish to filter a set of connections
against a set of access points and determine which connections are
compatible with which access points.

:param self: a #NMSettingWireless
:param s_wireless_sec: a #NMSettingWirelessSecurity or %NULL
:param ap_flags: the %NM80211ApFlags of the given access point
:param ap_wpa: the %NM80211ApSecurityFlags of the given access point's WPA capabilities
:param ap_rsn: the %NM80211ApSecurityFlags of the given access point's WPA2/RSN capabilities
:param ap_mode: the 802.11 mode of the AP, either Ad-Hoc or Infrastructure
:return: %TRUE if the given settings are compatible with the access point's security flags and mode, %FALSE if they are not."""
        pass

    def clear_mac_blacklist_items(self) -> None:
        """Removes all denylisted MAC addresses.

:param self: the #NMSettingWireless
:return: """
        pass

    def clear_mac_denylist_items(self) -> None:
        """Removes all denylisted MAC addresses.

:param self: the #NMSettingWireless
:return: """
        pass

    def get_ap_isolation(self) -> Ternary:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:ap-isolation property of the setting"""
        pass

    def get_band(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:band property of the setting"""
        pass

    def get_bssid(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:bssid property of the setting"""
        pass

    def get_channel(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:channel property of the setting"""
        pass

    def get_channel_width(self) -> SettingWirelessChannelWidth:
        """Returns the #NMSettingWireless:channel-width property.

:param self: the #NMSettingWireless
:return: the channel width"""
        pass

    def get_cloned_mac_address(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:cloned-mac-address property of the setting"""
        pass

    def get_generate_mac_address_mask(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:generate-mac-address-mask property of the setting"""
        pass

    def get_hidden(self) -> bool:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:hidden property of the setting"""
        pass

    def get_mac_address(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mac-address property of the setting"""
        pass

    def get_mac_address_blacklist(self) -> typing.Any:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mac-address-blacklist property of the setting"""
        pass

    def get_mac_address_denylist(self) -> typing.Any:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mac-address-denylist property of the setting"""
        pass

    def get_mac_address_randomization(self) -> SettingMacRandomization:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mac-address-randomization property of the setting"""
        pass

    def get_mac_blacklist_item(self, idx: int=None) -> str:
        """Since 1.46, access at index "len" is allowed and returns NULL.

:param self: the #NMSettingWireless
:param idx: the zero-based index of the MAC address entry
:return: the denylisted MAC address string (hex-digits-and-colons notation) at index @idx"""
        pass

    def get_mac_denylist_item(self, idx: int=None) -> str:
        """

:param self: the #NMSettingWireless
:param idx: the zero-based index of the MAC address entry
:return: the denylisted MAC address string (hex-digits-and-colons notation) at index @idx"""
        pass

    def get_mode(self) -> str:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mode property of the setting"""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:mtu property of the setting"""
        pass

    def get_num_mac_blacklist_items(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the number of blacklist MAC addresses"""
        pass

    def get_num_mac_denylist_items(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the number of denylisted MAC addresses"""
        pass

    def get_num_seen_bssids(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the number of BSSIDs in the previously seen BSSID list"""
        pass

    def get_powersave(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:powersave property of the setting"""
        pass

    def get_rate(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:rate property of the setting"""
        pass

    def get_seen_bssid(self, i: int=None) -> str:
        """

:param self: the #NMSettingWireless
:param i: index of a BSSID in the previously seen BSSID list
:return: the BSSID at index @i"""
        pass

    def get_ssid(self) -> GLib.Bytes:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:ssid property of the setting"""
        pass

    def get_tx_power(self) -> int:
        """

:param self: the #NMSettingWireless
:return: the #NMSettingWireless:tx-power property of the setting"""
        pass

    def get_wake_on_wlan(self) -> SettingWirelessWakeOnWLan:
        """Returns the Wake-on-WLAN options enabled for the connection

:param self: the #NMSettingWireless
:return: the Wake-on-WLAN options"""
        pass

    def remove_mac_blacklist_item(self, idx: int=None) -> None:
        """Removes the MAC address at index @idx from the denylist.

:param self: the #NMSettingWireless
:param idx: index number of the MAC address
:return: """
        pass

    def remove_mac_blacklist_item_by_value(self, mac: str=None) -> bool:
        """Removes the MAC address @mac from the denylist.

:param self: the #NMSettingWireless
:param mac: the MAC address string (hex-digits-and-colons notation) to remove from the denylist
:return: %TRUE if the MAC address was found and removed; %FALSE if it was not."""
        pass

    def remove_mac_denylist_item(self, idx: int=None) -> None:
        """Removes the MAC address at index @idx from the denylist.

:param self: the #NMSettingWireless
:param idx: index number of the MAC address
:return: """
        pass

    def remove_mac_denylist_item_by_value(self, mac: str=None) -> bool:
        """Removes the MAC address @mac from the denylist.

:param self: the #NMSettingWireless
:param mac: the MAC address string (hex-digits-and-colons notation) to remove from the denylist
:return: %TRUE if the MAC address was found and removed; %FALSE if it was not."""
        pass


class SettingWirelessClass:
    """"""


class SettingWirelessSecurity(Setting):
    """Wi-Fi Security Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWirelessSecurity object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWirelessSecurity object with default values.

:return: the new empty #NMSettingWirelessSecurity object"""
        pass

    def add_group(self, group: str=None) -> bool:
        """Adds an encryption algorithm to the list of allowed groupwise encryption
algorithms.  If the list is not empty, then only access points that support
one or more of the encryption algorithms in the list will be considered
compatible with this connection.

:param self: the #NMSettingWirelessSecurity
:param group: the encryption algorithm to add, one of "wep40", "wep104", "tkip", or "ccmp"
:return: %TRUE if the algorithm was added to the list, %FALSE if it was already in the list"""
        pass

    def add_pairwise(self, pairwise: str=None) -> bool:
        """Adds an encryption algorithm to the list of allowed pairwise encryption
algorithms.  If the list is not empty, then only access points that support
one or more of the encryption algorithms in the list will be considered
compatible with this connection.

:param self: the #NMSettingWirelessSecurity
:param pairwise: the encryption algorithm to add, one of "tkip" or "ccmp"
:return: %TRUE if the algorithm was added to the list, %FALSE if it was already in the list"""
        pass

    def add_proto(self, proto: str=None) -> bool:
        """Adds a Wi-Fi security protocol (one of "wpa" or "rsn") to the allowed list;
only protocols in this list will be used when finding and connecting to
the Wi-Fi network specified by this connection.  For example, if the
protocol list contains only "wpa" but the access point for the SSID specified
by this connection only supports WPA2/RSN, the connection cannot be used
with the access point.

:param self: the #NMSettingWirelessSecurity
:param proto: the protocol to add, one of "wpa" or "rsn"
:return: %TRUE if the protocol was new and was added to the allowed protocol list, or %FALSE if it was already in the list"""
        pass

    def clear_groups(self) -> None:
        """Removes all algorithms from the allowed list.  If there are no algorithms
specified then all groupwise encryption algorithms are allowed.

:param self: the #NMSettingWirelessSecurity
:return: """
        pass

    def clear_pairwise(self) -> None:
        """Removes all algorithms from the allowed list.  If there are no algorithms
specified then all pairwise encryption algorithms are allowed.

:param self: the #NMSettingWirelessSecurity
:return: """
        pass

    def clear_protos(self) -> None:
        """Removes all protocols from the allowed list.  If there are no protocols
specified then all protocols are allowed.

:param self: the #NMSettingWirelessSecurity
:return: """
        pass

    def get_auth_alg(self) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:auth-alg property of the setting"""
        pass

    def get_fils(self) -> SettingWirelessSecurityFils:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:fils property of the setting"""
        pass

    def get_group(self, i: int=None) -> str:
        """Returns the allowed groupwise encryption algorithm from allowed algorithm
list.

:param self: the #NMSettingWirelessSecurity
:param i: index of an item in the allowed groupwise encryption algorithm list
:return: the groupwise encryption algorithm at index @i"""
        pass

    def get_key_mgmt(self) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:key-mgmt property of the setting"""
        pass

    def get_leap_password(self) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:leap-password property of the setting"""
        pass

    def get_leap_password_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingSecretFlags pertaining to the #NMSettingWirelessSecurity:leap-password"""
        pass

    def get_leap_username(self) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:leap-username property of the setting"""
        pass

    def get_num_groups(self) -> int:
        """

:param self: the #NMSettingWirelessSecurity
:return: the number of groupwise encryption algorithms in the allowed list"""
        pass

    def get_num_pairwise(self) -> int:
        """

:param self: the #NMSettingWirelessSecurity
:return: the number of pairwise encryption algorithms in the allowed list"""
        pass

    def get_num_protos(self) -> int:
        """

:param self: the #NMSettingWirelessSecurity
:return: the number of security protocols this connection allows when connecting to secure Wi-Fi networks"""
        pass

    def get_pairwise(self, i: int=None) -> str:
        """Returns the allowed pairwise encryption algorithm from allowed algorithm
list.

:param self: the #NMSettingWirelessSecurity
:param i: index of an item in the allowed pairwise encryption algorithm list
:return: the pairwise encryption algorithm at index @i"""
        pass

    def get_pmf(self) -> SettingWirelessSecurityPmf:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:pmf property of the setting"""
        pass

    def get_proto(self, i: int=None) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:param i: an index into the protocol list
:return: the protocol at index @i"""
        pass

    def get_psk(self) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:psk property of the setting"""
        pass

    def get_psk_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingSecretFlags pertaining to the #NMSettingWirelessSecurity:psk"""
        pass

    def get_wep_key(self, idx: int=None) -> str:
        """

:param self: the #NMSettingWirelessSecurity
:param idx: the WEP key index (0..3 inclusive)
:return: the WEP key at the given index"""
        pass

    def get_wep_key_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingSecretFlags pertaining to the all WEP keys"""
        pass

    def get_wep_key_type(self) -> WepKeyType:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:wep-key-type property of the setting"""
        pass

    def get_wep_tx_keyidx(self) -> int:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:wep-tx-keyidx property of the setting"""
        pass

    def get_wps_method(self) -> SettingWirelessSecurityWpsMethod:
        """

:param self: the #NMSettingWirelessSecurity
:return: the #NMSettingWirelessSecurity:wps-method property of the setting"""
        pass

    def remove_group(self, i: int=None) -> None:
        """Removes an encryption algorithm from the allowed groupwise encryption
algorithm list.

:param self: the #NMSettingWirelessSecurity
:param i: the index of an item in the allowed groupwise encryption algorithm list
:return: """
        pass

    def remove_group_by_value(self, group: str=None) -> bool:
        """Removes an encryption algorithm from the allowed groupwise encryption
algorithm list.

:param self: the #NMSettingWirelessSecurity
:param group: the encryption algorithm to remove, one of "wep40", "wep104", "tkip", or "ccmp"
:return: %TRUE if the algorithm was found and removed; %FALSE if it was not."""
        pass

    def remove_pairwise(self, i: int=None) -> None:
        """Removes an encryption algorithm from the allowed pairwise encryption
algorithm list.

:param self: the #NMSettingWirelessSecurity
:param i: the index of an item in the allowed pairwise encryption algorithm list
:return: """
        pass

    def remove_pairwise_by_value(self, pairwise: str=None) -> bool:
        """Removes an encryption algorithm from the allowed pairwise encryption
algorithm list.

:param self: the #NMSettingWirelessSecurity
:param pairwise: the encryption algorithm to remove, one of "tkip" or "ccmp"
:return: %TRUE if the encryption algorithm was found and removed; %FALSE if it was not."""
        pass

    def remove_proto(self, i: int=None) -> None:
        """Removes a protocol from the allowed protocol list.

:param self: the #NMSettingWirelessSecurity
:param i: index of the protocol to remove
:return: """
        pass

    def remove_proto_by_value(self, proto: str=None) -> bool:
        """Removes a protocol from the allowed protocol list.

:param self: the #NMSettingWirelessSecurity
:param proto: the protocol to remove, one of "wpa" or "rsn"
:return: %TRUE if the protocol was found and removed; %FALSE if it was not."""
        pass

    def set_wep_key(self, idx: int=None, key: str=None) -> None:
        """Sets a WEP key in the given index.

:param self: the #NMSettingWirelessSecurity
:param idx: the index of the key (0..3 inclusive)
:param key: the WEP key as a string, in either hexadecimal, ASCII, or passphrase form as determined by the value of the #NMSettingWirelessSecurity:wep-key-type property.
:return: """
        pass


class SettingWirelessSecurityClass:
    """"""


class SettingWpan(Setting):
    """IEEE 802.15.4 (WPAN) MAC Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingWpan object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingWpan object with default values.

:return: the new empty #NMSettingWpan object"""
        pass

    def get_channel(self) -> int:
        """

:param self: the #NMSettingWpan
:return: the #NMSettingWpan:channel property of the setting"""
        pass

    def get_mac_address(self) -> str:
        """

:param self: the #NMSettingWpan
:return: the #NMSettingWpan:mac-address property of the setting"""
        pass

    def get_page(self) -> int:
        """

:param self: the #NMSettingWpan
:return: the #NMSettingWpan:page property of the setting"""
        pass

    def get_pan_id(self) -> int:
        """

:param self: the #NMSettingWpan
:return: the #NMSettingWpan:pan-id property of the setting"""
        pass

    def get_short_address(self) -> int:
        """

:param self: the #NMSettingWpan
:return: the #NMSettingWpan:short-address property of the setting"""
        pass


class SettingWpanClass:
    """"""


class SimpleConnection(GObject.Object, Connection):
    """"""

    @staticmethod
    def new() -> Connection:
        """Creates a new #NMSimpleConnection object with no #NMSetting objects.

:return: the new empty #NMConnection object"""
        pass

    @staticmethod
    def new_clone(connection: Connection=None) -> Connection:
        """Clones an #NMConnection as an #NMSimpleConnection.

:param connection: the #NMConnection to clone
:return: a new #NMConnection containing the same settings and properties as the source #NMConnection"""
        pass

    @staticmethod
    def new_from_dbus(dict: GLib.Variant=None) -> Connection:
        """Creates a new #NMSimpleConnection from a hash table describing the
connection and normalize the connection.  See nm_connection_to_dbus() for a
description of the expected hash table.

:param dict: a #GVariant of type %NM_VARIANT_TYPE_CONNECTION describing the connection
:return: the new #NMSimpleConnection object, populated with settings created from the values in the hash table, or %NULL if the connection failed to normalize."""
        pass


class SimpleConnectionClass:
    """"""


class SriovVF:
    """"""

    def __init__(self, index: int=None) -> None:
        """Creates a new #NMSriovVF object.

:param self: 
:param index: the VF index
:return: """
        pass

    @staticmethod
    def new(index: int=None) -> SriovVF:
        """Creates a new #NMSriovVF object.

:param index: the VF index
:return: the new #NMSriovVF object."""
        pass

    def add_vlan(self, vlan_id: int=None) -> bool:
        """Adds a VLAN to the VF. Currently kernel only supports one VLAN per VF.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:return: %TRUE if the VLAN was added; %FALSE if it already existed"""
        pass

    def dup(self) -> SriovVF:
        """Creates a copy of @vf.

:param self: the #NMSriovVF
:return: a copy of @vf"""
        pass

    def equal(self, other: SriovVF=None) -> bool:
        """Determines if two #NMSriovVF objects have the same index,
attributes and VLANs.

:param self: the #NMSriovVF
:param other: the #NMSriovVF to compare @vf to.
:return: %TRUE if the objects contain the same values, %FALSE
    if they do not."""
        pass

    def get_attribute(self, name: str=None) -> GLib.Variant:
        """Gets the value of the attribute with name @name on @vf

:param self: the #NMSriovVF
:param name: the name of a VF attribute
:return: the value of the attribute with name @name on
   @vf, or %NULL if @vf has no such attribute."""
        pass

    def get_attribute_names(self) -> typing.Any:
        """Gets an array of attribute names defined on @vf.

:param self: the #NMSriovVF
:return: a %NULL-terminated array of attribute names"""
        pass

    def get_index(self) -> int:
        """Gets the index property of this VF object.

:param self: the #NMSriovVF
:return: the VF index"""
        pass

    def get_vlan_ids(self, length: int=None) -> typing.Any:
        """Returns the VLANs currently configured on the VF. Currently kernel only
supports one VLAN per VF.

:param self: the #NMSriovVF
:param length: on return, the number of VLANs configured
:return: a list of VLAN ids configured on the VF."""
        pass

    def get_vlan_protocol(self, vlan_id: int=None) -> SriovVFVlanProtocol:
        """Returns the configured protocol for the given VLAN.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:return: the configured protocol"""
        pass

    def get_vlan_qos(self, vlan_id: int=None) -> int:
        """Returns the QoS value for the given VLAN.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:return: the QoS value"""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMSriovVF
:return: """
        pass

    def remove_vlan(self, vlan_id: int=None) -> bool:
        """Removes a VLAN from a VF.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:return: %TRUE if the VLAN was removed, %FALSE if the VLAN @vlan_id
     did not belong to the VF."""
        pass

    def set_attribute(self, name: str=None, value: GLib.Variant=None) -> None:
        """Sets the named attribute on @vf to the given value.

:param self: the #NMSriovVF
:param name: the name of a route attribute
:param value: the value
:return: """
        pass

    def set_vlan_protocol(self, vlan_id: int=None, protocol:
        SriovVFVlanProtocol=None) -> None:
        """Sets the protocol for the given VLAN.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:param protocol: the VLAN protocol
:return: """
        pass

    def set_vlan_qos(self, vlan_id: int=None, qos: int=None) -> None:
        """Sets a QoS value for the given VLAN.

:param self: the #NMSriovVF
:param vlan_id: the VLAN id
:param qos: a QoS (priority) value
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMSriovVF
:return: """
        pass

    @staticmethod
    def attribute_validate(name: str=None, value: GLib.Variant=None, known:
        bool=None) -> bool:
        """Validates a VF attribute, i.e. checks that the attribute is a known one,
the value is of the correct type and well-formed.

:param name: the attribute name
:param value: the attribute value
:param known: on return, whether the attribute name is a known one
:return: %TRUE if the attribute is valid, %FALSE otherwise"""
        pass


class TCAction:
    """"""

    def __init__(self, kind: str=None) -> None:
        """Creates a new #NMTCAction object.

:param self: 
:param kind: name of the queueing discipline
:return: """
        pass

    @staticmethod
    def new(kind: str=None) -> TCAction:
        """Creates a new #NMTCAction object.

:param kind: name of the queueing discipline
:return: the new #NMTCAction object, or %NULL on error"""
        pass

    def dup(self) -> TCAction:
        """Creates a copy of @action

:param self: the #NMTCAction
:return: a copy of @action"""
        pass

    def equal(self, other: TCAction=None) -> bool:
        """Determines if two #NMTCAction objects contain the same kind, family,
handle, parent and info.

:param self: the #NMTCAction
:param other: the #NMTCAction to compare @action to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_attribute(self, name: str=None) -> GLib.Variant:
        """Gets the value of the attribute with name @name on @action

:param self: the #NMTCAction
:param name: the name of an action attribute
:return: the value of the attribute with name @name on
   @action, or %NULL if @action has no such attribute."""
        pass

    def get_attribute_names(self) -> typing.Any:
        """Gets an array of attribute names defined on @action.

:param self: the #NMTCAction
:return: a %NULL-terminated array of attribute names,"""
        pass

    def get_kind(self) -> str:
        """

:param self: the #NMTCAction
:return: """
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMTCAction
:return: """
        pass

    def set_attribute(self, name: str=None, value: GLib.Variant=None) -> None:
        """Sets or clears the named attribute on @action to the given value.

:param self: the #NMTCAction
:param name: the name of an action attribute
:param value: the value
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMTCAction
:return: """
        pass


class TCQdisc:
    """"""

    def __init__(self, kind: str=None, parent: int=None) -> None:
        """Creates a new #NMTCQdisc object.

:param self: 
:param kind: name of the queueing discipline
:param parent: the parent queueing discipline
:return: """
        pass

    @staticmethod
    def new(kind: str=None, parent: int=None) -> TCQdisc:
        """Creates a new #NMTCQdisc object.

:param kind: name of the queueing discipline
:param parent: the parent queueing discipline
:return: the new #NMTCQdisc object, or %NULL on error"""
        pass

    def dup(self) -> TCQdisc:
        """Creates a copy of @qdisc

:param self: the #NMTCQdisc
:return: a copy of @qdisc"""
        pass

    def equal(self, other: TCQdisc=None) -> bool:
        """Determines if two #NMTCQdisc objects contain the same kind, * handle
and parent.

:param self: the #NMTCQdisc
:param other: the #NMTCQdisc to compare @qdisc to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_attribute(self, name: str=None) -> GLib.Variant:
        """Gets the value of the attribute with name @name on @qdisc

:param self: the #NMTCQdisc
:param name: the name of an qdisc attribute
:return: the value of the attribute with name @name on
   @qdisc, or %NULL if @qdisc has no such attribute."""
        pass

    def get_attribute_names(self) -> typing.Any:
        """Gets an array of attribute names defined on @qdisc.

:param self: the #NMTCQdisc
:return: a %NULL-terminated array of attribute names
   or %NULL if no attributes are set."""
        pass

    def get_handle(self) -> int:
        """

:param self: the #NMTCQdisc
:return: the queueing discipline handle"""
        pass

    def get_kind(self) -> str:
        """

:param self: the #NMTCQdisc
:return: """
        pass

    def get_parent(self) -> int:
        """

:param self: the #NMTCQdisc
:return: the parent class"""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMTCQdisc
:return: """
        pass

    def set_attribute(self, name: str=None, value: GLib.Variant=None) -> None:
        """Sets or clears the named attribute on @qdisc to the given value.

:param self: the #NMTCQdisc
:param name: the name of an qdisc attribute
:param value: the value
:return: """
        pass

    def set_handle(self, handle: int=None) -> None:
        """Sets the queueing discipline handle.

:param self: the #NMTCQdisc
:param handle: the queueing discipline handle
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMTCQdisc
:return: """
        pass


class TCTfilter:
    """"""

    def __init__(self, kind: str=None, parent: int=None) -> None:
        """Creates a new #NMTCTfilter object.

:param self: 
:param kind: name of the queueing discipline
:param parent: the parent queueing discipline
:return: """
        pass

    @staticmethod
    def new(kind: str=None, parent: int=None) -> TCTfilter:
        """Creates a new #NMTCTfilter object.

:param kind: name of the queueing discipline
:param parent: the parent queueing discipline
:return: the new #NMTCTfilter object, or %NULL on error"""
        pass

    def dup(self) -> TCTfilter:
        """Creates a copy of @tfilter

:param self: the #NMTCTfilter
:return: a copy of @tfilter"""
        pass

    def equal(self, other: TCTfilter=None) -> bool:
        """Determines if two #NMTCTfilter objects contain the same kind, family,
handle, parent and info.

:param self: the #NMTCTfilter
:param other: the #NMTCTfilter to compare @tfilter to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_action(self) -> TCAction:
        """

:param self: the #NMTCTfilter
:return: the action associated with a traffic filter."""
        pass

    def get_handle(self) -> int:
        """

:param self: the #NMTCTfilter
:return: the queueing discipline handle"""
        pass

    def get_kind(self) -> str:
        """

:param self: the #NMTCTfilter
:return: """
        pass

    def get_parent(self) -> int:
        """

:param self: the #NMTCTfilter
:return: the parent class"""
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

:param self: the #NMTCTfilter
:return: """
        pass

    def set_action(self, action: TCAction=None) -> None:
        """Sets the action associated with a traffic filter.

:param self: the #NMTCTfilter
:param action: the action object
:return: """
        pass

    def set_handle(self, handle: int=None) -> None:
        """Sets the queueing discipline handle.

:param self: the #NMTCTfilter
:param handle: the queueing discipline handle
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

:param self: the #NMTCTfilter
:return: """
        pass


class TeamLinkWatcher:
    """"""

    @staticmethod
    def new_arp_ping(init_wait: int=None, interval: int=None, missed_max:
        int=None, target_host: str=None, source_host: str=None, flags:
        TeamLinkWatcherArpPingFlags=None) -> TeamLinkWatcher:
        """Creates a new arp_ping #NMTeamLinkWatcher object

:param init_wait: init_wait value
:param interval: interval value
:param missed_max: missed_max value
:param target_host: the host name or the ip address that will be used as destination   address in the arp request
:param source_host: the host name or the ip address that will be used as source   address in the arp request
:param flags: the watcher #NMTeamLinkWatcherArpPingFlags
:return: the new #NMTeamLinkWatcher object, or %NULL on error"""
        pass

    @staticmethod
    def new_arp_ping2(init_wait: int=None, interval: int=None, missed_max:
        int=None, vlanid: int=None, target_host: str=None, source_host: str
        =None, flags: TeamLinkWatcherArpPingFlags=None) -> TeamLinkWatcher:
        """Creates a new arp_ping #NMTeamLinkWatcher object

:param init_wait: init_wait value
:param interval: interval value
:param missed_max: missed_max value
:param vlanid: vlanid value
:param target_host: the host name or the ip address that will be used as destination   address in the arp request
:param source_host: the host name or the ip address that will be used as source   address in the arp request
:param flags: the watcher #NMTeamLinkWatcherArpPingFlags
:return: the new #NMTeamLinkWatcher object, or %NULL on error"""
        pass

    @staticmethod
    def new_ethtool(delay_up: int=None, delay_down: int=None
        ) -> TeamLinkWatcher:
        """Creates a new ethtool #NMTeamLinkWatcher object

:param delay_up: delay_up value
:param delay_down: delay_down value
:return: the new #NMTeamLinkWatcher object"""
        pass

    @staticmethod
    def new_nsna_ping(init_wait: int=None, interval: int=None, missed_max:
        int=None, target_host: str=None) -> TeamLinkWatcher:
        """Creates a new nsna_ping #NMTeamLinkWatcher object

:param init_wait: init_wait value
:param interval: interval value
:param missed_max: missed_max value
:param target_host: the host name or the ipv6 address that will be used as   target address in the NS packet
:return: the new #NMTeamLinkWatcher object, or %NULL on error"""
        pass

    def dup(self) -> TeamLinkWatcher:
        """Creates a copy of @watcher

:param self: the #NMTeamLinkWatcher
:return: a copy of @watcher"""
        pass

    def equal(self, other: TeamLinkWatcher=None) -> bool:
        """Determines if two #NMTeamLinkWatcher objects contain the same values
in all the properties.

:param self: the #NMTeamLinkWatcher
:param other: the #NMTeamLinkWatcher to compare @watcher to.
:return: %TRUE if the objects contain the same values, %FALSE if they do not."""
        pass

    def get_delay_down(self) -> int:
        """Gets the delay_down interval (in milliseconds) that elapses between the link
going down and the runner being notified about it.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_delay_up(self) -> int:
        """Gets the delay_up interval (in milliseconds) that elapses between the link
coming up and the runner being notified about it.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_flags(self) -> TeamLinkWatcherArpPingFlags:
        """Gets the arp ping watcher flags.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_init_wait(self) -> int:
        """Gets the init_wait interval (in milliseconds) that the team port should
wait before sending the first packet to the target host.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_interval(self) -> int:
        """Gets the interval (in milliseconds) that the team port should wait between
sending two check packets to the target host.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_missed_max(self) -> int:
        """Gets the number of missed replies after which the link is considered down.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_name(self) -> str:
        """Gets the name of the link watcher to be used.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_source_host(self) -> str:
        """Gets the ip address to be used as source for the link probing packets.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_target_host(self) -> str:
        """Gets the host name/ip address to be used as destination for the link probing
packets.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def get_vlanid(self) -> int:
        """Gets the VLAN tag ID to be used to outgoing link probes

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def ref(self) -> None:
        """Increases the reference count of the object.

Since 1.20, ref-counting of #NMTeamLinkWatcher is thread-safe.

:param self: the #NMTeamLinkWatcher
:return: """
        pass

    def unref(self) -> None:
        """Decreases the reference count of the object.  If the reference count
reaches zero, the object will be destroyed.

Since 1.20, ref-counting of #NMTeamLinkWatcher is thread-safe.

:param self: the #NMTeamLinkWatcher
:return: """
        pass


class VariantAttributeSpec:
    """"""


class VpnConnectionClass:
    """"""


class VpnEditor:
    """"""

    def changed(self) -> None:
        """emitted when the value of a UI widget changes.  May trigger a
  validity check via @update_connection to write values to the connection.

:param self: 
:return: """
        pass

    def get_widget(self) -> GObject.Object:
        """return the #GtkWidget for the VPN editor's UI

:param self: the #NMVpnEditor
:return: """
        pass

    def update_connection(self, connection: Connection=None) -> bool:
        """called to save the user-entered options to the connection
  object.  Should return %FALSE and set @error if the current options are
  invalid.  @error should contain enough information for the plugin to
  determine which UI widget is invalid at a later point in time.  For
  example, creating unique error codes for what error occurred and populating
  the message field of @error with the name of the invalid property.

:param self: 
:param connection: 
:return: """
        pass

    def get_widget(self) -> GObject.Object:
        """

:param self: the #NMVpnEditor
:return: """
        pass

    def update_connection(self, connection: Connection=None) -> bool:
        """

:param self: 
:param connection: 
:return: """
        pass


class VpnEditorInterface:
    """Interface for editing a specific #NMConnection"""
    g_iface: GObject.TypeInterface
    get_widget: typing.Any
    placeholder: typing.Any
    update_connection: typing.Any
    changed: typing.Any


class VpnEditorPlugin:
    """"""

    @staticmethod
    def load(plugin_name: str=None, check_service: str=None
        ) -> VpnEditorPlugin:
        """Load the shared library @plugin_name and create a new
#NMVpnEditorPlugin instance via the #NMVpnEditorPluginFactory
function.

This is similar to nm_vpn_editor_plugin_load_from_file(), but
it does no validation of the plugin name, instead passes it directly
to dlopen(). If you have the full path to a plugin file,
nm_vpn_editor_plugin_load_from_file() is preferred.

:param plugin_name: The name of the shared library to load.  This path will be directly passed to dlopen() without  further checks.
:param check_service: if not-null, check that the loaded plugin advertises  the given service.
:return: a new plugin instance or %NULL on error."""
        pass

    @staticmethod
    def load_from_file(plugin_name: str=None, check_service: str=None,
        check_owner: int=None, check_file: UtilsCheckFilePredicate=None,
        user_data: typing.Any=None) -> VpnEditorPlugin:
        """Load the shared library @plugin_name and create a new
#NMVpnEditorPlugin instance via the #NMVpnEditorPluginFactory
function.

If @plugin_name is not an absolute path name, it assumes the file
is in the plugin directory of NetworkManager. In any case, the call
will do certain checks on the file before passing it to dlopen.
A consequence for that is, that you cannot omit the ".so" suffix
as you could for nm_vpn_editor_plugin_load().

:param plugin_name: The path or name of the shared library to load.  The path must either be an absolute filename to an existing file.  Alternatively, it can be the name (without path) of a library in the  plugin directory of NetworkManager.
:param check_service: if not-null, check that the loaded plugin advertises  the given service.
:param check_owner: if non-negative, check whether the file is owned  by UID @check_owner or by root. In this case also check that  the file is not writable by anybody else.
:param check_file: optional callback to validate the file prior to   loading the shared library.
:param user_data: user data for @check_file
:return: a new plugin instance or %NULL on error."""
        pass

    def export_to_file(self, path: str=None, connection: Connection=None
        ) -> bool:
        """Export the given connection to the specified path.  Return
  %TRUE on success.  On error, return %FALSE and set @error with additional
  error information.  Note that @error can be %NULL, in which case no
  additional error information should be provided.

:param self: 
:param path: 
:param connection: 
:return: """
        pass

    def get_capabilities(self) -> VpnEditorPluginCapability:
        """returns a bitmask of capabilities.

:param self: 
:return: """
        pass

    def get_editor(self, connection: Connection=None) -> VpnEditor:
        """returns an #NMVpnEditor, pre-filled with values from @connection
  if non-%NULL.

:param self: the #NMVpnEditorPlugin
:param connection: the #NMConnection to be edited
:return: a new #NMVpnEditor or %NULL on error"""
        pass

    def get_suggested_filename(self, connection: Connection=None) -> str:
        """For a given connection, return a suggested file
  name.  Returned value will be %NULL or a suggested file name to be freed by
  the caller.

:param self: 
:param connection: 
:return: """
        pass

    def get_vt(self, out_vt_size: int=None) -> VpnEditorPluginVT:
        """return a virtual function table to implement further functions in
  the plugin, without requiring to update libnm. Used by nm_vpn_editor_plugin_get_vt().

:param self: 
:param out_vt_size: 
:return: """
        pass

    def import_from_file(self, path: str=None) -> Connection:
        """Try to import a connection from the specified path.  On
  success, return a partial #NMConnection object.  On error, return %NULL and
  set @error with additional information.  Note that @error can be %NULL, in
  which case no additional error information should be provided.

:param self: 
:param path: 
:return: """
        pass

    def notify_plugin_info_set(self, plugin_info: VpnPluginInfo=None) -> None:
        """A callback to be called when the plugin info is set.

:param self: 
:param plugin_info: 
:return: """
        pass

    def export(self, path: str=None, connection: Connection=None) -> bool:
        """

:param self: 
:param path: 
:param connection: 
:return: """
        pass

    def get_capabilities(self) -> VpnEditorPluginCapability:
        """

:param self: 
:return: """
        pass

    def get_editor(self, connection: Connection=None) -> VpnEditor:
        """

:param self: the #NMVpnEditorPlugin
:param connection: the #NMConnection to be edited
:return: a new #NMVpnEditor or %NULL on error"""
        pass

    def get_plugin_info(self) -> VpnPluginInfo:
        """

:param self: the #NMVpnEditorPlugin instance
:return: if set, return the #NMVpnPluginInfo instance."""
        pass

    def get_suggested_filename(self, connection: Connection=None) -> str:
        """

:param self: 
:param connection: 
:return: """
        pass

    def get_vt(self, vt: VpnEditorPluginVT=None, vt_size: int=None) -> int:
        """Returns an opaque VT function table for the plugin to extend
functionality. The actual meaning of NMVpnEditorPluginVT is not
defined in public API of libnm, instead it must be agreed by
both the plugin and the caller. See the header-only file
'nm-vpn-editor-plugin-call.h' which defines the meaning.

:param self: the #NMVpnEditorPlugin
:param vt: buffer to be filled with the VT table of the plugin
:param vt_size: the size of the buffer. Can be 0 to only query the   size of plugin's VT.
:return: the actual size of the @plugin's virtual function table."""
        pass

    def _import(self, path: str=None) -> Connection:
        """

:param self: the #NMVpnEditorPlugin
:param path: full path to the file to attempt to read into a new #NMConnection
:return: a new #NMConnection imported from @path, or %NULL on error or if the file at @path was not recognized by this plugin"""
        pass

    def set_plugin_info(self, plugin_info: VpnPluginInfo=None) -> None:
        """Set or clear the plugin-info instance.
This takes a weak reference on @plugin_info, to avoid circular
reference as the plugin-info might also reference the editor-plugin.

:param self: the #NMVpnEditorPlugin instance
:param plugin_info: a #NMVpnPluginInfo instance or %NULL
:return: """
        pass


class VpnEditorPluginInterface:
    """Interface for VPN editor plugins."""
    g_iface: GObject.TypeInterface
    get_editor: typing.Any
    get_capabilities: typing.Any
    import_from_file: typing.Any
    export_to_file: typing.Any
    get_suggested_filename: typing.Any
    notify_plugin_info_set: typing.Any
    get_vt: typing.Any


class VpnEditorPluginVT:
    """"""


class VpnPluginInfo(GObject.Object, Gio.Initable):
    """"""

    @staticmethod
    def new_from_file(filename: str=None) -> VpnPluginInfo:
        """Read the plugin info from file @filename. Does not do
any further verification on the file. You might want to check
file permissions and ownership of the file.

:param filename: filename to read.
:return: %NULL if there is any error or a newly created #NMVpnPluginInfo instance."""
        pass

    @staticmethod
    def new_search_file(name: str=None, service: str=None) -> VpnPluginInfo:
        """This has the same effect as doing a full nm_vpn_plugin_info_list_load()
followed by a search for the first matching VPN plugin info that has the
given @name and/or @service.

:param name: the name to search for. Either @name or @service   must be present.
:param service: the service to search for. Either @name  or   @service must be present.
:return: a newly created instance of plugin info
   or %NULL if no matching value was found."""
        pass

    @staticmethod
    def new_with_data(filename: str=None, keyfile: GLib.KeyFile=None
        ) -> VpnPluginInfo:
        """This constructor does not read any data from file but
takes instead a @keyfile argument.

:param filename: optional filename.
:param keyfile: inject data for the plugin info instance.
:return: new plugin info instance."""
        pass

    @staticmethod
    def list_add(list: GLib.SList=None, plugin_info: VpnPluginInfo=None
        ) -> bool:
        """

:param list: list of plugins
:param plugin_info: instance to add
:return: %TRUE if the plugin was added to @list. This will fail to add duplicate plugins."""
        pass

    @staticmethod
    def list_find_by_filename(list: GLib.SList=None, filename: str=None
        ) -> VpnPluginInfo:
        """

:param list: list of plugins
:param filename: filename to search
:return: the first plugin with a matching @filename (or %NULL)."""
        pass

    @staticmethod
    def list_find_by_name(list: GLib.SList=None, name: str=None
        ) -> VpnPluginInfo:
        """

:param list: list of plugins
:param name: name to search
:return: the first plugin with a matching @name (or %NULL)."""
        pass

    @staticmethod
    def list_find_by_service(list: GLib.SList=None, service: str=None
        ) -> VpnPluginInfo:
        """

:param list: list of plugins
:param service: service to search. This can be the main service-type   or one of the provided aliases.
:return: the first plugin with a matching @service (or %NULL)."""
        pass

    @staticmethod
    def list_find_service_type(list: GLib.SList=None, name: str=None) -> str:
        """A VPN plugin provides one or several service-types, like org.freedesktop.NetworkManager.libreswan
Certain plugins provide more then one service type, via aliases (org.freedesktop.NetworkManager.openswan).
This function looks up a service-type (or an alias) based on a name.

Preferably, the name can be a full service-type/alias of an installed
plugin. Otherwise, it can be the name of a VPN plugin (in which case, the
primary, non-aliased service-type is returned). Otherwise, it can be
one of several well known short-names (which is a hard-coded list of
types in libnm). On success, this returns a full qualified service-type
(or an alias). It doesn't say, that such an plugin is actually available,
but it could be retrieved via nm_vpn_plugin_info_list_find_by_service().

:param list: a possibly empty #GSList of #NMVpnPluginInfo instances
:param name: a name to lookup the service-type.
:return: the resolved service-type or %NULL on failure."""
        pass

    @staticmethod
    def list_get_service_types(list: GLib.SList=None, only_existing: bool=
        None, with_abbreviations: bool=None) -> typing.Any:
        """

:param list: a possibly empty #GSList of #NMVpnPluginInfo
:param only_existing: only include results that are actually in @list.   Otherwise, the result is extended with a hard-code list or   well-known plugins
:param with_abbreviations: if %FALSE, only full service types are returned.   Otherwise, this also includes abbreviated names that can be used   with nm_vpn_plugin_info_list_find_service_type().
:return: a %NULL terminated strv list of strings.
   The list itself and the values must be freed with g_strfreev()."""
        pass

    @staticmethod
    def list_load() -> GLib.SList:
        """

:return: list of plugins loaded from the default directories rejecting duplicates."""
        pass

    @staticmethod
    def list_remove(list: GLib.SList=None, plugin_info: VpnPluginInfo=None
        ) -> bool:
        """Remove @plugin_info from @list.

:param list: list of plugins
:param plugin_info: instance
:return: %TRUE if @plugin_info was in @list and successfully removed."""
        pass

    @staticmethod
    def validate_filename(filename: str=None) -> bool:
        """Regular name files have a certain pattern. That basically means
they have the file extension "name". Check if @filename
is valid according to that pattern.

:param filename: the filename to check
:return: """
        pass

    def get_aliases(self) -> typing.Any:
        """

:param self: plugin info instance
:return: the aliases from the name-file."""
        pass

    def get_auth_dialog(self) -> str:
        """

:param self: plugin info instance
:return: the absolute path to the auth-dialog helper or %NULL."""
        pass

    def get_editor_plugin(self) -> VpnEditorPlugin:
        """

:param self: plugin info instance
:return: the cached #NMVpnEditorPlugin instance."""
        pass

    def get_filename(self) -> str:
        """

:param self: plugin info instance
:return: the filename. Can be %NULL."""
        pass

    def get_name(self) -> str:
        """

:param self: plugin info instance
:return: the name. Cannot be %NULL."""
        pass

    def get_plugin(self) -> str:
        """

:param self: plugin info instance
:return: the plugin. Can be %NULL."""
        pass

    def get_program(self) -> str:
        """

:param self: plugin info instance
:return: the program. Can be %NULL."""
        pass

    def get_service(self) -> str:
        """

:param self: plugin info instance
:return: the service. Cannot be %NULL."""
        pass

    def load_editor_plugin(self) -> VpnEditorPlugin:
        """

:param self: plugin info instance
:return: loads the plugin and returns the newly created
   instance. The plugin is owned by @self and can be later retrieved again
   via nm_vpn_plugin_info_get_editor_plugin(). You can load the
   plugin only once, unless you reset the state via
   nm_vpn_plugin_info_set_editor_plugin()."""
        pass

    def lookup_property(self, group: str=None, key: str=None) -> str:
        """

:param self: plugin info instance
:param group: group name
:param key: name of the property
:return: #NMVpnPluginInfo is internally a #GKeyFile. Returns the matching property."""
        pass

    def set_editor_plugin(self, plugin: VpnEditorPlugin=None) -> None:
        """Set the internal plugin instance. If %NULL, only clear the previous instance.

:param self: plugin info instance
:param plugin: plugin instance
:return: """
        pass

    def supports_hints(self) -> bool:
        """

:param self: plugin info instance
:return: %TRUE if the supports hints for secret requests, otherwise %FALSE"""
        pass

    def supports_multiple(self) -> bool:
        """

:param self: plugin info instance
:return: %TRUE if the service supports multiple instances with different bus names, otherwise %FALSE"""
        pass

    def supports_safe_private_file_access(self) -> bool:
        """

:param self: plugin info instance
:return: %TRUE if the service supports reading files (certificates, keys) of
     private connections in a safe way (i.e. checking user permissions), or
        if the service doesn't need to read any file from disk."""
        pass


class VpnPluginInfoClass:
    """"""


class VpnPluginOld(GObject.Object, Gio.Initable):
    """"""

    @staticmethod
    def get_secret_flags(data: GLib.HashTable=None, secret_name: str=None,
        out_flags: SettingSecretFlags=None) -> bool:
        """Given a VPN secret key name, attempts to find the corresponding flags data
item in @data.  If found, converts the flags data item to
#NMSettingSecretFlags and returns it.

:param data: hash table containing VPN key/value pair data items
:param secret_name: VPN secret key name for which to retrieve flags for
:param out_flags: on success, the flags associated with @secret_name
:return: %TRUE if the flag data item was found and successfully converted to flags, %FALSE if not"""
        pass

    @staticmethod
    def read_vpn_details(fd: int=None, out_data: GLib.HashTable=None,
        out_secrets: GLib.HashTable=None) -> bool:
        """Parses key/value pairs from a file descriptor (normally stdin) passed by
an applet when the applet calls the authentication dialog of the VPN plugin.

:param fd: file descriptor to read from, usually stdin (0)
:param out_data: on successful return, a hash table (mapping char*:char*) containing the key/value pairs of VPN data items
:param out_secrets: on successful return, a hash table (mapping char*:char*) containing the key/value pairsof VPN secrets
:return: %TRUE if reading values was successful, %FALSE if not"""
        pass

    def config(self, config: GLib.Variant=None) -> None:
        """

:param self: 
:param config: 
:return: """
        pass

    def connect(self, connection: Connection=None) -> bool:
        """

:param self: 
:param connection: 
:return: """
        pass

    def connect_interactive(self, connection: Connection=None, details:
        GLib.Variant=None) -> bool:
        """

:param self: 
:param connection: 
:param details: 
:return: """
        pass

    def disconnect(self) -> bool:
        """

:param self: 
:return: """
        pass

    def failure(self, reason: VpnPluginFailure=None) -> None:
        """

:param self: 
:param reason: 
:return: """
        pass

    def ip4_config(self, ip4_config: GLib.Variant=None) -> None:
        """

:param self: 
:param ip4_config: 
:return: """
        pass

    def ip6_config(self, config: GLib.Variant=None) -> None:
        """

:param self: 
:param config: 
:return: """
        pass

    def login_banner(self, banner: str=None) -> None:
        """

:param self: 
:param banner: 
:return: """
        pass

    def need_secrets(self, connection: Connection=None, setting_name: str=None
        ) -> bool:
        """

:param self: 
:param connection: 
:param setting_name: 
:return: """
        pass

    def new_secrets(self, connection: Connection=None) -> bool:
        """

:param self: 
:param connection: 
:return: """
        pass

    def quit(self) -> None:
        """

:param self: 
:return: """
        pass

    def state_changed(self, state: VpnServiceState=None) -> None:
        """

:param self: 
:param state: 
:return: """
        pass

    def disconnect(self) -> bool:
        """

:param self: 
:return: """
        pass

    def failure(self, reason: VpnPluginFailure=None) -> None:
        """

:param self: 
:param reason: 
:return: """
        pass

    def get_connection(self) -> Gio.DBusConnection:
        """

:param self: 
:return: """
        pass

    def get_state(self) -> VpnServiceState:
        """

:param self: 
:return: """
        pass

    def secrets_required(self, message: str=None, hints: str=None) -> None:
        """Called by VPN plugin implementations to signal to NetworkManager that secrets
are required during the connection process.  This signal may be used to
request new secrets when the secrets originally provided by NetworkManager
are insufficient, or the VPN process indicates that it needs additional
information to complete the request.

:param self: the #NMVpnPluginOld
:param message: an information message about why secrets are required, if any
:param hints: VPN specific secret names for required new secrets
:return: """
        pass

    def set_ip4_config(self, ip4_config: GLib.Variant=None) -> None:
        """

:param self: 
:param ip4_config: 
:return: """
        pass

    def set_login_banner(self, banner: str=None) -> None:
        """

:param self: 
:param banner: 
:return: """
        pass

    def set_state(self, state: VpnServiceState=None) -> None:
        """

:param self: 
:param state: 
:return: """
        pass
    parent: GObject.Object


class VpnPluginOldClass:
    """"""
    parent: GObject.ObjectClass
    state_changed: typing.Any
    ip4_config: typing.Any
    login_banner: typing.Any
    failure: typing.Any
    quit: typing.Any
    config: typing.Any
    ip6_config: typing.Any
    connect: typing.Any
    need_secrets: typing.Any
    disconnect: typing.Any
    new_secrets: typing.Any
    connect_interactive: typing.Any
    padding: typing.Any


class VpnServicePlugin(GObject.Object, Gio.Initable):
    """"""

    @staticmethod
    def get_secret_flags(data: GLib.HashTable=None, secret_name: str=None,
        out_flags: SettingSecretFlags=None) -> bool:
        """Given a VPN secret key name, attempts to find the corresponding flags data
item in @data.  If found, converts the flags data item to
#NMSettingSecretFlags and returns it.

:param data: hash table containing VPN key/value pair data items
:param secret_name: VPN secret key name for which to retrieve flags for
:param out_flags: on success, the flags associated with @secret_name
:return: %TRUE if the flag data item was found and successfully converted to flags, %FALSE if not"""
        pass

    @staticmethod
    def read_vpn_details(fd: int=None, out_data: GLib.HashTable=None,
        out_secrets: GLib.HashTable=None) -> bool:
        """Parses key/value pairs from a file descriptor (normally stdin) passed by
an applet when the applet calls the authentication dialog of the VPN plugin.

:param fd: file descriptor to read from, usually stdin (0)
:param out_data: on successful return, a hash table (mapping char*:char*) containing the key/value pairs of VPN data items
:param out_secrets: on successful return, a hash table (mapping char*:char*) containing the key/value pairsof VPN secrets
:return: %TRUE if reading values was successful, %FALSE if not"""
        pass

    def config(self, config: GLib.Variant=None) -> None:
        """

:param self: 
:param config: 
:return: """
        pass

    def connect(self, connection: Connection=None) -> bool:
        """

:param self: 
:param connection: 
:return: """
        pass

    def connect_interactive(self, connection: Connection=None, details:
        GLib.Variant=None) -> bool:
        """

:param self: 
:param connection: 
:param details: 
:return: """
        pass

    def disconnect(self) -> bool:
        """

:param self: 
:return: """
        pass

    def failure(self, reason: VpnPluginFailure=None) -> None:
        """

:param self: 
:param reason: 
:return: """
        pass

    def ip4_config(self, ip4_config: GLib.Variant=None) -> None:
        """

:param self: 
:param ip4_config: 
:return: """
        pass

    def ip6_config(self, config: GLib.Variant=None) -> None:
        """

:param self: 
:param config: 
:return: """
        pass

    def login_banner(self, banner: str=None) -> None:
        """

:param self: 
:param banner: 
:return: """
        pass

    def need_secrets(self, connection: Connection=None, setting_name: str=None
        ) -> bool:
        """

:param self: 
:param connection: 
:param setting_name: 
:return: """
        pass

    def new_secrets(self, connection: Connection=None) -> bool:
        """

:param self: 
:param connection: 
:return: """
        pass

    def quit(self) -> None:
        """

:param self: 
:return: """
        pass

    def state_changed(self, state: VpnServiceState=None) -> None:
        """

:param self: 
:param state: 
:return: """
        pass

    def disconnect(self) -> bool:
        """

:param self: 
:return: """
        pass

    def failure(self, reason: VpnPluginFailure=None) -> None:
        """

:param self: 
:param reason: 
:return: """
        pass

    def get_connection(self) -> Gio.DBusConnection:
        """

:param self: 
:return: """
        pass

    def secrets_required(self, message: str=None, hints: str=None) -> None:
        """Called by VPN plugin implementations to signal to NetworkManager that secrets
are required during the connection process.  This signal may be used to
request new secrets when the secrets originally provided by NetworkManager
are insufficient, or the VPN process indicates that it needs additional
information to complete the request.

:param self: the #NMVpnServicePlugin
:param message: an information message about why secrets are required, if any
:param hints: VPN specific secret names for required new secrets
:return: """
        pass

    def set_config(self, config: GLib.Variant=None) -> None:
        """

:param self: 
:param config: 
:return: """
        pass

    def set_ip4_config(self, ip4_config: GLib.Variant=None) -> None:
        """

:param self: 
:param ip4_config: 
:return: """
        pass

    def set_ip6_config(self, ip6_config: GLib.Variant=None) -> None:
        """

:param self: 
:param ip6_config: 
:return: """
        pass

    def set_login_banner(self, banner: str=None) -> None:
        """

:param self: 
:param banner: 
:return: """
        pass

    def shutdown(self) -> None:
        """Shutdown the @plugin and disconnect from D-Bus. After this,
the plugin instance is dead and should no longer be used.
It ensures to get no more requests from D-Bus. In principle,
you don't need to shutdown the plugin, disposing the instance
has the same effect. However, this gives a way to deactivate
the plugin before giving up the last reference.

:param self: the #NMVpnServicePlugin instance
:return: """
        pass
    parent: GObject.Object


class VpnServicePluginClass:
    """"""
    parent: GObject.ObjectClass
    state_changed: typing.Any
    ip4_config: typing.Any
    login_banner: typing.Any
    failure: typing.Any
    quit: typing.Any
    config: typing.Any
    ip6_config: typing.Any
    connect: typing.Any
    need_secrets: typing.Any
    disconnect: typing.Any
    new_secrets: typing.Any
    connect_interactive: typing.Any
    padding: typing.Any


class WifiP2PPeer(Object):
    """"""

    def connection_valid(self, connection: Connection=None) -> bool:
        """Validates a given connection against a given Wi-Fi P2P peer to ensure that
the connection may be activated with that peer. The connection must match the
@peer's address and in the future possibly other attributes.

:param self: an #NMWifiP2PPeer to validate @connection against
:param connection: an #NMConnection to validate against @peer
:return: %TRUE if the connection may be activated with this Wi-Fi P2P Peer, %FALSE if it cannot be."""
        pass

    def filter_connections(self, connections: typing.Any=None) -> typing.Any:
        """Filters a given array of connections for a given #NMWifiP2PPeer object and
returns connections which may be activated with the P2P peer.  Any
returned connections will match the @peers's HW address and in the future
possibly other attributes.

To obtain the list of connections that are compatible with this P2P peer,
use nm_client_get_connections() and then filter the returned list for a given
#NMDevice using nm_device_filter_connections() and finally filter that list
with this function.

:param self: an #NMWifiP2PPeer to filter connections for
:param connections: an array of #NMConnections to filter
:return: an array of #NMConnections that could be activated with the given @peer. The array should be freed with g_ptr_array_unref() when it is no longer required."""
        pass

    def get_flags(self) -> NM80211ApFlags:
        """Gets the flags of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the flags"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware address of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the hardware address"""
        pass

    def get_last_seen(self) -> int:
        """Returns the timestamp (in CLOCK_BOOTTIME seconds) for the last time the
P2P peer was seen.  A value of -1 means the P2P peer has never been seen.

:param self: a #NMWifiP2PPeer
:return: the last seen time in seconds"""
        pass

    def get_manufacturer(self) -> str:
        """Gets the manufacturer of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the manufacturer"""
        pass

    def get_model(self) -> str:
        """Gets the model of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the model"""
        pass

    def get_model_number(self) -> str:
        """Gets the model number of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the model number"""
        pass

    def get_name(self) -> str:
        """Gets the name of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the name"""
        pass

    def get_serial(self) -> str:
        """Gets the serial number of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the serial number"""
        pass

    def get_strength(self) -> int:
        """Gets the current signal strength of the P2P peer as a percentage.

:param self: a #NMWifiP2PPeer
:return: the signal strength (0 to 100)"""
        pass

    def get_wfd_ies(self) -> GLib.Bytes:
        """Gets the WFD information elements of the P2P peer.

:param self: a #NMWifiP2PPeer
:return: the #GBytes containing the WFD IEs, or %NULL."""
        pass


class WifiP2PPeerClass:
    """"""


class WimaxNsp(Object):
    """"""

    def connection_valid(self, connection: Connection=None) -> bool:
        """Validates a given connection against a given WiMAX NSP to ensure that the
connection may be activated with that NSP.  The connection must match the
@nsp's network name and other attributes.

:param self: an #NMWimaxNsp to validate @connection against
:param connection: an #NMConnection to validate against @nsp
:return: %TRUE if the connection may be activated with this WiMAX NSP, %FALSE if it cannot be."""
        pass

    def filter_connections(self, connections: typing.Any=None) -> typing.Any:
        """Filters a given array of connections for a given #NMWimaxNsp object and
return connections which may be activated with the NSP.  Any returned
connections will match the @nsp's network name and other attributes.

:param self: an #NMWimaxNsp to filter connections for
:param connections: an array of #NMConnections to filter
:return: an array of #NMConnections that could be activated with the given @nsp.  The array should be freed with g_ptr_array_unref() when it is no longer required."""
        pass

    def get_name(self) -> str:
        """Gets the name of the wimax NSP

:param self: a #NMWimaxNsp
:return: the name"""
        pass

    def get_network_type(self) -> WimaxNspNetworkType:
        """Gets the network type of the wimax NSP.

:param self: a #NMWimaxNsp
:return: the network type"""
        pass

    def get_signal_quality(self) -> int:
        """Gets the WPA signal quality of the wimax NSP.

:param self: a #NMWimaxNsp
:return: the signal quality"""
        pass


class WimaxNspClass:
    """"""


class WireGuardPeer:
    """The settings of one WireGuard peer."""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> WireGuardPeer:
        """

:return: a new, default, unsealed #NMWireGuardPeer instance."""
        pass

    def append_allowed_ip(self, allowed_ip: str=None, accept_invalid: bool=None
        ) -> bool:
        """Appends @allowed_ip setting to the list. This does not check
for duplicates and always appends @allowed_ip to the end of the
list. If @allowed_ip is valid, it will be normalized and a modified
for might be appended. If @allowed_ip is invalid, it will still be
appended, but later verification will fail.

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param allowed_ip: the allowed-ip entry to set.
:param accept_invalid: if %TRUE, also invalid @allowed_ip value   will be appended. Otherwise, the function does nothing   in face of invalid values and returns %FALSE.
:return: %TRUE if the value is a valid allowed-ips value, %FALSE otherwise.
   Depending on @accept_invalid, also invalid values are added."""
        pass

    def clear_allowed_ips(self) -> None:
        """Removes all allowed-ip entries.

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:return: """
        pass

    def cmp(self, b: WireGuardPeer=None, compare_flags: SettingCompareFlags
        =None) -> int:
        """

:param self: the #NMWireGuardPeer to compare.
:param b: the other #NMWireGuardPeer to compare.
:param compare_flags: #NMSettingCompareFlags to affect the comparison.
:return: zero of the two instances are equivalent or
   a non-zero integer otherwise. This defines a total ordering
   over the peers. Whether a peer is sealed or not, does not
   affect the comparison."""
        pass

    def get_allowed_ip(self, idx: int=None, out_is_valid: bool=None) -> str:
        """

:param self: the #NMWireGuardPeer instance
:param idx: the index from zero to (allowed-ips-len - 1) to   retrieve.
:param out_is_valid: %TRUE if the returned value is a valid allowed-ip   setting.   This parameter is wrongly not marked as (out) argument, it is   thus not accessible via introspection. This cannot be fixed without   breaking API for introspection users.
:return: the allowed-ip setting at index @idx.
   If @idx is out of range, %NULL will be returned."""
        pass

    def get_allowed_ips_len(self) -> int:
        """

:param self: the #NMWireGuardPeer instance
:return: the number of allowed-ips entries."""
        pass

    def get_endpoint(self) -> str:
        """

:param self: the #NMWireGuardPeer instance
:return: the endpoint or %NULL if none was set."""
        pass

    def get_persistent_keepalive(self) -> int:
        """

:param self: the #NMWireGuardPeer instance
:return: get the persistent-keepalive setting in seconds. Set to zero to disable
   keep-alive."""
        pass

    def get_preshared_key(self) -> str:
        """

:param self: the #NMWireGuardPeer instance
:return: the preshared key or %NULL if unset."""
        pass

    def get_preshared_key_flags(self) -> SettingSecretFlags:
        """

:param self: the #NMWireGuardPeer instance
:return: get the secret flags for the preshared-key."""
        pass

    def get_public_key(self) -> str:
        """

:param self: the #NMWireGuardPeer instance
:return: the public key or %NULL if unset."""
        pass

    def is_sealed(self) -> bool:
        """

:param self: the #NMWireGuardPeer instance
:return: whether @self is sealed or not."""
        pass

    def is_valid(self, check_non_secrets: bool=None, check_secrets: bool=None
        ) -> bool:
        """

:param self: the #NMWireGuardPeer instance
:param check_non_secrets: if %TRUE, secret properties are validated.   Otherwise, they are ignored for this purpose.
:param check_secrets: if %TRUE, non-secret properties are validated.   Otherwise, they are ignored for this purpose.
:return: %TRUE if the peer is valid or fails with an error
   reason."""
        pass

    def new_clone(self, with_secrets: bool=None) -> WireGuardPeer:
        """

:param self: the #NMWireGuardPeer instance to copy.
:param with_secrets: if %TRUE, the preshared-key secrets are copied  as well. Otherwise, they will be removed.
:return: a clone of @self. This instance
   is always unsealed."""
        pass

    def ref(self) -> WireGuardPeer:
        """

:param self: the #NMWireGuardPeer instance
:return: returns the input argument @self after incrementing
   the reference count.  Since 1.42, ref-counting of #NMWireGuardPeer is thread-safe."""
        pass

    def remove_allowed_ip(self, idx: int=None) -> bool:
        """Removes the allowed-ip at the given @idx. This shifts all
following entries one index down.

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param idx: the index from zero to (allowed-ips-len - 1) to   retrieve. If the index is out of range, %FALSE is returned   and nothing is done.
:return: %TRUE if @idx was valid and the allowed-ip was removed.
   %FALSE otherwise, and the peer will not be changed."""
        pass

    def seal(self) -> None:
        """Seal the #NMWireGuardPeer instance. Afterwards, it is a bug
to call all functions that modify the instance (except ref/unref).
A sealed instance cannot be unsealed again, but you can create
an unsealed copy with nm_wireguard_peer_new_clone().

:param self: the #NMWireGuardPeer instance
:return: """
        pass

    def set_endpoint(self, endpoint: str=None, allow_invalid: bool=None
        ) -> bool:
        """Sets or clears the endpoint of @self.

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param endpoint: the socket address endpoint to set or %NULL.
:param allow_invalid: if %TRUE, also invalid values are set.   If %FALSE, the function does nothing for invalid @endpoint   arguments.
:return: %TRUE if the endpoint is %NULL or valid. For an
   invalid @endpoint argument, %FALSE is returned. Depending
   on @allow_invalid, the instance will be modified."""
        pass

    def set_persistent_keepalive(self, persistent_keepalive: int=None) -> None:
        """It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param persistent_keepalive: the keep-alive value to set.
:return: """
        pass

    def set_preshared_key(self, preshared_key: str=None, accept_invalid:
        bool=None) -> bool:
        """Reset the preshared key. Note that if the preshared key is valid, it
will be normalized (which may or may not modify the set value).

Note that the preshared-key is a secret and consequently has corresponding
preshared-key-flags property. This is so that secrets can be optional
and requested on demand from a secret-agent. Also, an invalid  preshared-key
may optionally cause nm_wireguard_peer_is_valid() to fail or it may
be accepted.

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param preshared_key: the new preshared   key or %NULL to clear the preshared key.
:param accept_invalid: whether to allow setting the key to an invalid   value. If %FALSE, @self is unchanged if the key is invalid   and if %FALSE is returned.
:return: %TRUE if the preshared-key is valid, otherwise %FALSE.
   %NULL is considered a valid value.
   If the key is invalid, it depends on @accept_invalid whether the
   previous value was reset."""
        pass

    def set_preshared_key_flags(self, preshared_key_flags:
        SettingSecretFlags=None) -> None:
        """It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param preshared_key_flags: the secret flags to set.
:return: """
        pass

    def set_public_key(self, public_key: str=None, accept_invalid: bool=None
        ) -> bool:
        """Reset the public key. Note that if the public key is valid, it
will be normalized (which may or may not modify the set value).

It is a bug trying to modify a sealed #NMWireGuardPeer instance.

:param self: the unsealed #NMWireGuardPeer instance
:param public_key: the new public   key or %NULL to clear the public key.
:param accept_invalid: if %TRUE and @public_key is not %NULL and   invalid, then do not modify the instance.
:return: %TRUE if the key was valid or %NULL. Returns
   %FALSE for invalid keys. Depending on @accept_invalid
   will an invalid key be set or not."""
        pass

    def unref(self) -> None:
        """Drop a reference to @self. If the last reference is dropped,
the instance is freed and all associate data released.

Since 1.42, ref-counting of #NMWireGuardPeer is thread-safe.

:param self: the #NMWireGuardPeer instance
:return: """
        pass


class AccessPoint(Object):
    """"""

    def connection_valid(self, connection: Connection=None) -> bool:
        """Validates a given connection against a given Wi-Fi access point to ensure that
the connection may be activated with that AP.  The connection must match the
@ap's SSID, (if given) BSSID, and other attributes like security settings,
channel, band, etc.

:param self: an #NMAccessPoint to validate @connection against
:param connection: an #NMConnection to validate against @ap
:return: %TRUE if the connection may be activated with this Wi-Fi AP, %FALSE if it cannot be."""
        pass

    def filter_connections(self, connections: typing.Any=None) -> typing.Any:
        """Filters a given array of connections for a given #NMAccessPoint object and
returns connections which may be activated with the access point.  Any
returned connections will match the @ap's SSID and (if given) BSSID and
other attributes like security settings, channel, etc.

To obtain the list of connections that are compatible with this access point,
use nm_client_get_connections() and then filter the returned list for a given
#NMDevice using nm_device_filter_connections() and finally filter that list
with this function.

:param self: an #NMAccessPoint to filter connections for
:param connections: an array of #NMConnections to filter
:return: an array of #NMConnections that could be activated with the given @ap.  The array should be freed with g_ptr_array_unref() when it is no longer required.  WARNING: the transfer annotation for this function may not work correctly
   with bindings. See https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/305.
   You can filter the list yourself with nm_access_point_connection_valid()."""
        pass

    def get_bandwidth(self) -> int:
        """Gets the bandwidth advertised by the access point in MHz.

:param self: a #NMAccessPoint
:return: the advertised bandwidth (MHz)"""
        pass

    def get_bssid(self) -> str:
        """Gets the Basic Service Set ID (BSSID) of the Wi-Fi access point.

:param self: a #NMAccessPoint
:return: the BSSID of the access point. This is an internal string and must not be modified or freed."""
        pass

    def get_flags(self) -> NM80211ApFlags:
        """Gets the flags of the access point.

:param self: a #NMAccessPoint
:return: the flags"""
        pass

    def get_frequency(self) -> int:
        """Gets the frequency of the access point in MHz.

:param self: a #NMAccessPoint
:return: the frequency in MHz"""
        pass

    def get_last_seen(self) -> int:
        """Returns the timestamp (in CLOCK_BOOTTIME seconds) for the last time the
access point was found in scan results.  A value of -1 means the access
point has not been found in a scan.

:param self: a #NMAccessPoint
:return: the last seen time in seconds"""
        pass

    def get_max_bitrate(self) -> int:
        """Gets the maximum bit rate of the access point in kbit/s.

:param self: a #NMAccessPoint
:return: the maximum bit rate (kbit/s)"""
        pass

    def get_mode(self) -> NM80211Mode:
        """Gets the mode of the access point.

:param self: a #NMAccessPoint
:return: the mode"""
        pass

    def get_rsn_flags(self) -> NM80211ApSecurityFlags:
        """Gets the RSN (Robust Secure Network, ie WPA version 2) flags of the access
point.

:param self: a #NMAccessPoint
:return: the RSN flags"""
        pass

    def get_ssid(self) -> GLib.Bytes:
        """Gets the SSID of the access point.

:param self: a #NMAccessPoint
:return: the #GBytes containing the SSID, or %NULL if the
   SSID is unknown."""
        pass

    def get_strength(self) -> int:
        """Gets the current signal strength of the access point as a percentage.

:param self: a #NMAccessPoint
:return: the signal strength (0 to 100)"""
        pass

    def get_wpa_flags(self) -> NM80211ApSecurityFlags:
        """Gets the WPA (version 1) flags of the access point.

:param self: a #NMAccessPoint
:return: the WPA flags"""
        pass


class ActiveConnection(Object):
    """"""

    def get_connection(self) -> RemoteConnection:
        """Gets the #NMRemoteConnection associated with @connection.

:param self: a #NMActiveConnection
:return: the #NMRemoteConnection which this #NMActiveConnection is an active instance of."""
        pass

    def get_connection_type(self) -> str:
        """Gets the #NMConnection's type.

:param self: a #NMActiveConnection
:return: the type of the #NMConnection that backs the #NMActiveConnection. This is the internal string used by the connection, and must not be modified."""
        pass

    def get_controller(self) -> typing.Any:
        """Gets the controller #NMDevice of the connection. This replaces the
deprecated nm_active_connection_get_master() method.

:param self: a #NMActiveConnection
:return: the controller #NMDevice of the #NMActiveConnection."""
        pass

    def get_default(self) -> bool:
        """Whether the active connection is the default IPv4 one (that is, is used for
the default IPv4 route and DNS information).

:param self: a #NMActiveConnection
:return: %TRUE if the active connection is the default IPv4 connection"""
        pass

    def get_default6(self) -> bool:
        """Whether the active connection is the default IPv6 one (that is, is used for
the default IPv6 route and DNS information).

:param self: a #NMActiveConnection
:return: %TRUE if the active connection is the default IPv6 connection"""
        pass

    def get_devices(self) -> typing.Any:
        """Gets the #NMDevices used for the active connections.

:param self: a #NMActiveConnection
:return: the #GPtrArray containing #NMDevices. This is the internal copy used by the connection, and must not be modified."""
        pass

    def get_dhcp4_config(self) -> DhcpConfig:
        """Gets the current IPv4 #NMDhcpConfig (if any) associated with the
#NMActiveConnection.

:param self: an #NMActiveConnection
:return: the IPv4 #NMDhcpConfig, or %NULL if the connection
   does not use DHCP, or is not in the %NM_ACTIVE_CONNECTION_STATE_ACTIVATED
   state."""
        pass

    def get_dhcp6_config(self) -> DhcpConfig:
        """Gets the current IPv6 #NMDhcpConfig (if any) associated with the
#NMActiveConnection.

:param self: an #NMActiveConnection
:return: the IPv6 #NMDhcpConfig, or %NULL if the connection
   does not use DHCPv6, or is not in the %NM_ACTIVE_CONNECTION_STATE_ACTIVATED
   state."""
        pass

    def get_id(self) -> str:
        """Gets the #NMConnection's ID.

:param self: a #NMActiveConnection
:return: the ID of the #NMConnection that backs the #NMActiveConnection. This is the internal string used by the connection, and must not be modified."""
        pass

    def get_ip4_config(self) -> IPConfig:
        """Gets the current IPv4 #NMIPConfig associated with the #NMActiveConnection.

:param self: an #NMActiveConnection
:return: the IPv4 #NMIPConfig, or %NULL if the connection is
   not in the %NM_ACTIVE_CONNECTION_STATE_ACTIVATED state."""
        pass

    def get_ip6_config(self) -> IPConfig:
        """Gets the current IPv6 #NMIPConfig associated with the #NMActiveConnection.

:param self: an #NMActiveConnection
:return: the IPv6 #NMIPConfig, or %NULL if the connection is
   not in the %NM_ACTIVE_CONNECTION_STATE_ACTIVATED state."""
        pass

    def get_master(self) -> typing.Any:
        """Gets the controller #NMDevice of the connection.

:param self: a #NMActiveConnection
:return: the controller #NMDevice of the #NMActiveConnection."""
        pass

    def get_specific_object_path(self) -> str:
        """Gets the path of the "specific object" used at activation.

Currently, there is no single method that will allow you to automatically turn
this into an appropriate #NMObject; you need to know what kind of object it
is based on other information. (Eg, if @connection corresponds to a Wi-Fi
connection, then the specific object will be an #NMAccessPoint, and you can
resolve it with nm_device_wifi_get_access_point_by_path().)

:param self: a #NMActiveConnection
:return: the specific object's D-Bus path. This is the internal string used by the connection, and must not be modified."""
        pass

    def get_state(self) -> ActiveConnectionState:
        """Gets the active connection's state.

:param self: a #NMActiveConnection
:return: the state"""
        pass

    def get_state_flags(self) -> ActivationStateFlags:
        """Gets the active connection's state flags.

:param self: a #NMActiveConnection
:return: the state flags"""
        pass

    def get_state_reason(self) -> ActiveConnectionStateReason:
        """Gets the reason for active connection's state.

:param self: a #NMActiveConnection
:return: the reason"""
        pass

    def get_uuid(self) -> str:
        """Gets the #NMConnection's UUID.

:param self: a #NMActiveConnection
:return: the UUID of the #NMConnection that backs the #NMActiveConnection. This is the internal string used by the connection, and must not be modified."""
        pass

    def get_vpn(self) -> bool:
        """Whether the active connection is a VPN connection.

:param self: a #NMActiveConnection
:return: %TRUE if the active connection is a VPN connection"""
        pass


class Checkpoint(Object):
    """"""

    def get_created(self) -> int:
        """Gets the timestamp (in CLOCK_BOOTTIME milliseconds) of checkpoint creation.

Use nm_utils_get_timestamp_msec() to obtain current time value suitable for
comparing to this value.

:param self: a #NMCheckpoint
:return: the timestamp of checkpoint creation."""
        pass

    def get_devices(self) -> typing.Any:
        """The devices that are part of this checkpoint.

:param self: a #NMCheckpoint
:return: the devices list."""
        pass

    def get_rollback_timeout(self) -> int:
        """Gets the timeout in seconds for automatic rollback.

:param self: a #NMCheckpoint
:return: the rollback timeout."""
        pass


class Device(Object):
    """"""

    @staticmethod
    def disambiguate_names(devices: typing.Any=None, num_devices: int=None
        ) -> typing.Any:
        """Generates a list of short-ish unique presentation names for the
devices in @devices.

:param devices: an array of #NMDevice
:param num_devices: length of @devices
:return: the device names"""
        pass

    def connection_compatible(self, connection: Connection=None) -> bool:
        """Validates a given connection for a given #NMDevice object and returns
whether the connection may be activated with the device. For example if
@device is a Wi-Fi device that supports only WEP encryption, the connection
will only be valid if it is a Wi-Fi connection which describes a WEP or open
network, and will not be valid if it describes a WPA network, or if it is
an Ethernet, Bluetooth, WWAN, etc connection that is incompatible with the
device.

This function does the same as nm_device_connection_valid(), i.e. checking
compatibility of the given device and connection. But, in addition, it sets
GError when FALSE is returned.

:param self: an #NMDevice to validate @connection against
:param connection: an #NMConnection to validate against @device
:return: %TRUE if the connection may be activated with this device, %FALSE if is incompatible with the device's capabilities and characteristics."""
        pass

    def connection_valid(self, connection: Connection=None) -> bool:
        """Validates a given connection for a given #NMDevice object and returns
whether the connection may be activated with the device. For example if
@device is a Wi-Fi device that supports only WEP encryption, the connection
will only be valid if it is a Wi-Fi connection which describes a WEP or open
network, and will not be valid if it describes a WPA network, or if it is
an Ethernet, Bluetooth, WWAN, etc connection that is incompatible with the
device.

:param self: an #NMDevice to validate @connection against
:param connection: an #NMConnection to validate against @device
:return: %TRUE if the connection may be activated with this device, %FALSE if is incompatible with the device's capabilities and characteristics."""
        pass

    def delete(self, cancellable: Gio.Cancellable=None) -> bool:
        """Deletes the software device. Hardware devices can't be deleted.

:param self: a #NMDevice
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def delete_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously begins deleting the software device. Hardware devices can't
be deleted.

:param self: a #NMDevice
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when delete operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def delete_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_device_delete_async().

:param self: a #NMDevice
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def disconnect(self, cancellable: Gio.Cancellable=None) -> bool:
        """Disconnects the device if currently connected, and prevents the device from
automatically connecting to networks until the next manual network connection
request.

:param self: a #NMDevice
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def disconnect_async(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously begins disconnecting the device if currently connected, and
prevents the device from automatically connecting to networks until the next
manual network connection request.

:param self: a #NMDevice
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the disconnect operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def disconnect_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_device_disconnect_async().

:param self: a #NMDevice
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def filter_connections(self, connections: typing.Any=None) -> typing.Any:
        """Filters a given array of connections for a given #NMDevice object and returns
connections which may be activated with the device. For example if @device
is a Wi-Fi device that supports only WEP encryption, the returned array will
contain any Wi-Fi connections in @connections that allow connection to
unencrypted or WEP-enabled SSIDs.  The returned array will not contain
Ethernet, Bluetooth, Wi-Fi WPA connections, or any other connection that is
incompatible with the device. To get the full list of connections see
nm_client_get_connections().

:param self: an #NMDevice to filter connections for
:param connections: an array of #NMConnections to filter
:return: an array of #NMConnections that could be activated with the given @device.  The array should be freed with g_ptr_array_unref() when it is no longer required.  WARNING: the transfer annotation for this function may not work correctly
   with bindings. See https://gitlab.gnome.org/GNOME/gobject-introspection/-/issues/305.
   You can filter the list yourself with nm_device_connection_valid()."""
        pass

    def get_active_connection(self) -> ActiveConnection:
        """Gets the #NMActiveConnection object which owns this device during activation.

:param self: a #NMDevice
:return: the #NMActiveConnection or %NULL if the device is not part of an active connection"""
        pass

    def get_applied_connection(self, flags: int=None, version_id: int=None,
        cancellable: Gio.Cancellable=None) -> Connection:
        """Fetch the currently applied connection on the device.

:param self: a #NMDevice
:param flags: the flags argument. See #NMDeviceReapplyFlags.
:param version_id: returns the current version id of   the applied connection
:param cancellable: a #GCancellable, or %NULL
:return: a %NMConnection with the currently applied settings
   or %NULL on error.  The connection is as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_applied_connection_async(self, flags: int=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Asynchronously begins and gets the currently applied connection.

:param self: a #NMDevice
:param flags: the flags argument. See #NMDeviceReapplyFlags.
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the reapply operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def get_applied_connection_finish(self, result: Gio.AsyncResult=None,
        version_id: int=None) -> Connection:
        """Gets the result of a call to nm_device_get_applied_connection_async().

:param self: a #NMDevice
:param result: the result passed to the #GAsyncReadyCallback
:param version_id: the current version id of the applied   connection.
:return: a currently applied %NMConnection or %NULL in case
   of error.  The connection is as received from D-Bus and might not validate according to nm_connection_verify()."""
        pass

    def get_autoconnect(self) -> bool:
        """Whether the #NMDevice can be autoconnected.

:param self: a #NMDevice
:return: %TRUE if the device is allowed to be autoconnected"""
        pass

    def get_available_connections(self) -> typing.Any:
        """Gets the #NMRemoteConnections currently known to the daemon that could
be activated on @device.

:param self: a #NMDevice
:return: the #GPtrArray containing #NMRemoteConnections. This is the internal copy used by the connection, and must not be modified."""
        pass

    def get_capabilities(self) -> DeviceCapabilities:
        """Gets the device' capabilities.

:param self: a #NMDevice
:return: the capabilities"""
        pass

    def get_connectivity(self, addr_family: int=None) -> ConnectivityState:
        """The connectivity state of the device for given address family.
Supported address families are %AF_INET for IPv4, %AF_INET6
for IPv6 or %AF_UNSPEC for any.

:param self: a #NMDevice
:param addr_family: network address family
:return: the current connectivity state"""
        pass

    def get_description(self) -> str:
        """Gets a description of @device, based on its vendor and product names.

:param self: an #NMDevice
:return: a description of @device. If either the vendor or the
   product name is unknown, this returns the interface name."""
        pass

    def get_device_type(self) -> DeviceType:
        """Returns the numeric type of the #NMDevice, ie Ethernet, Wi-Fi, etc.

:param self: a #NMDevice
:return: the device type"""
        pass

    def get_dhcp4_config(self) -> DhcpConfig:
        """Gets the current IPv4 #NMDhcpConfig associated with the #NMDevice.

You can alternatively use nm_active_connection_get_dhcp4_config(), which also
works with VPN connections.

:param self: a #NMDevice
:return: the IPv4 #NMDhcpConfig, or %NULL if the device is not activated or not using DHCP."""
        pass

    def get_dhcp6_config(self) -> DhcpConfig:
        """Gets the current IPv6 #NMDhcpConfig associated with the #NMDevice.

You can alternatively use nm_active_connection_get_dhcp6_config(), which also
works with VPN connections.

:param self: a #NMDevice
:return: the IPv6 #NMDhcpConfig, or %NULL if the device is not activated or not using DHCPv6."""
        pass

    def get_driver(self) -> str:
        """Gets the driver of the #NMDevice.

:param self: a #NMDevice
:return: the driver of the device. This is the internal string used by the device, and must not be modified."""
        pass

    def get_driver_version(self) -> str:
        """Gets the driver version of the #NMDevice.

:param self: a #NMDevice
:return: the version of the device driver. This is the internal string used by the device, and must not be modified."""
        pass

    def get_firmware_missing(self) -> bool:
        """Indicates that firmware required for the device's operation is likely
to be missing.

:param self: a #NMDevice
:return: %TRUE if firmware required for the device's operation is likely to be missing."""
        pass

    def get_firmware_version(self) -> str:
        """Gets the firmware version of the #NMDevice.

:param self: a #NMDevice
:return: the firmware version of the device. This is the internal string used by the device, and must not be modified."""
        pass

    def get_hw_address(self) -> str:
        """Gets the current a hardware address (MAC) for the @device.

:param self: a #NMDevice
:return: the current MAC of the device, or %NULL. This is the internal string used by the device, and must not be modified."""
        pass

    def get_iface(self) -> str:
        """Gets the interface name of the #NMDevice.

:param self: a #NMDevice
:return: the interface of the device. This is the internal string used by the device, and must not be modified."""
        pass

    def get_interface_flags(self) -> DeviceInterfaceFlags:
        """Gets the interface flags of the device.

:param self: a #NMDevice
:return: the flags"""
        pass

    def get_ip4_config(self) -> IPConfig:
        """Gets the current IPv4 #NMIPConfig associated with the #NMDevice.

You can alternatively use nm_active_connection_get_ip4_config(), which also
works with VPN connections.

:param self: a #NMDevice
:return: the IPv4 #NMIPConfig, or %NULL if the device is not activated."""
        pass

    def get_ip6_config(self) -> IPConfig:
        """Gets the current IPv6 #NMIPConfig associated with the #NMDevice.

You can alternatively use nm_active_connection_get_ip6_config(), which also
works with VPN connections.

:param self: a #NMDevice
:return: the IPv6 #NMIPConfig or %NULL if the device is not activated."""
        pass

    def get_ip_iface(self) -> str:
        """Gets the IP interface name of the #NMDevice over which IP traffic flows
when the device is in the ACTIVATED state.

:param self: a #NMDevice
:return: the IP traffic interface of the device. This is the internal string used by the device, and must not be modified."""
        pass

    def get_lldp_neighbors(self) -> typing.Any:
        """Gets the list of neighbors discovered through LLDP.

:param self: a #NMDevice
:return: the #GPtrArray containing #NMLldpNeighbor<!-- -->s. This is the internal copy used by the device and must not be modified. The library never modifies the returned array and thus it is safe for callers to reference and keep using it."""
        pass

    def get_managed(self) -> bool:
        """Whether the #NMDevice is managed by NetworkManager.

:param self: a #NMDevice
:return: %TRUE if the device is managed by NetworkManager"""
        pass

    def get_metered(self) -> Metered:
        """Gets the metered setting of a #NMDevice.

:param self: a #NMDevice
:return: the metered setting."""
        pass

    def get_mtu(self) -> int:
        """Gets the  MTU of the #NMDevice.

:param self: a #NMDevice
:return: the MTU of the device in bytes."""
        pass

    def get_nm_plugin_missing(self) -> bool:
        """Indicates that the NetworkManager plugin for the device is not installed.

:param self: a #NMDevice
:return: %TRUE if the device plugin not installed."""
        pass

    def get_path(self) -> str:
        """Gets the path of the #NMDevice as exposed by the udev property ID_PATH.

:param self: a #NMDevice
:return: the path of the device.  The string is backslash escaped (C escaping) for invalid characters. The escaping can be reverted with g_strcompress(), however the result may not be valid UTF-8."""
        pass

    def get_physical_port_id(self) -> str:
        """Gets the physical port ID of the #NMDevice. If non-%NULL, this is
an opaque string that can be used to recognize when
seemingly-unrelated #NMDevices are actually just different virtual
ports on a single physical port. (Eg, NPAR / SR-IOV.)

:param self: a #NMDevice
:return: the physical port ID of the device, or %NULL if the port
   ID is unknown. This is the internal string used by the device and
   must not be modified."""
        pass

    def get_ports(self) -> typing.Any:
        """Gets the devices currently set as port of @device.

:param self: a #NMDevice
:return: the #GPtrArray containing #NMDevices that are ports of @device. This is the internal copy used by the device and must not be modified."""
        pass

    def get_product(self) -> str:
        """Gets the product string of the #NMDevice.

:param self: a #NMDevice
:return: the product name of the device. This is the internal string used by the device, and must not be modified.  The string is backslash escaped (C escaping) for invalid characters. The escaping can be reverted with g_strcompress(), however the result may not be valid UTF-8."""
        pass

    def get_setting_type(self) -> GType:
        """Gets the (primary) #NMSetting subtype associated with connections
that can be used on @device.

:param self: an #NMDevice
:return: @device's associated #NMSetting type"""
        pass

    def get_state(self) -> DeviceState:
        """Gets the current #NMDevice state.

:param self: a #NMDevice
:return: the current device state"""
        pass

    def get_state_reason(self) -> DeviceStateReason:
        """Gets the reason for entering the current #NMDevice state.

:param self: a #NMDevice
:return: the reason for entering the current device state"""
        pass

    def get_type_description(self) -> str:
        """Gets a (non-localized) description of the type of device that
@device is.

:param self: a #NMDevice
:return: the type description of the device. This is the internal string used by the device, and must not be modified."""
        pass

    def get_udi(self) -> str:
        """Gets the Unique Device Identifier of the #NMDevice.

:param self: a #NMDevice
:return: the Unique Device Identifier of the device.  This identifier may be used to gather more information about the device from various operating system services like udev or sysfs."""
        pass

    def get_vendor(self) -> str:
        """Gets the vendor string of the #NMDevice.

:param self: a #NMDevice
:return: the vendor name of the device. This is the internal string used by the device, and must not be modified.  The string is backslash escaped (C escaping) for invalid characters. The escaping can be reverted with g_strcompress(), however the result may not be valid UTF-8."""
        pass

    def is_real(self) -> bool:
        """

:param self: a #NMDevice
:return: %TRUE if the device exists, or %FALSE if it is a placeholder device that could be automatically created by NetworkManager if one of its #NMDevice:available-connections was activated."""
        pass

    def is_software(self) -> bool:
        """Whether the device is a software device.

:param self: a #NMDevice
:return: %TRUE if @device is a software device, %FALSE if it is a hardware device."""
        pass

    def reapply(self, connection: Connection=None, version_id: int=None,
        flags: int=None, cancellable: Gio.Cancellable=None) -> bool:
        """Attempts to update device with changes to the currently active connection
made since it was last applied.

:param self: a #NMDevice
:param connection: the #NMConnection to replace the applied   settings with or %NULL to reuse existing
:param version_id: zero or the expected version id of the applied connection.   If specified and the version id mismatches, the call fails without   modification. This allows one to catch concurrent accesses.
:param flags: always set this to zero
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def reapply_async(self, connection: Connection=None, version_id: int=
        None, flags: int=None, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Asynchronously begins an attempt to update device with changes to the
currently active connection made since it was last applied.

:param self: a #NMDevice
:param connection: the #NMConnection to replace the applied   settings with or %NULL to reuse existing
:param version_id: zero or the expected version id of the applied   connection. If specified and the version id mismatches, the call   fails without modification. This allows one to catch concurrent   accesses.
:param flags: always set this to zero
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the reapply operation completes
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def reapply_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_device_reapply_async().

:param self: a #NMDevice
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def set_autoconnect(self, autoconnect: bool=None) -> None:
        """Enables or disables automatic activation of the #NMDevice.

:param self: a #NMDevice
:param autoconnect: %TRUE to enable autoconnecting
:return: """
        pass

    def set_managed(self, managed: bool=None) -> None:
        """Enables or disables management of  #NMDevice by NetworkManager.

:param self: a #NMDevice
:param managed: %TRUE to make the device managed by NetworkManager.
:return: """
        pass


class Device6Lowpan(Device):
    """"""

    def get_parent(self) -> Device:
        """

:param self: a #NMDevice6Lowpan
:return: the device's parent device"""
        pass


class DeviceAdsl(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceAdsl
:return: %TRUE if the device has carrier"""
        pass


class DeviceBond(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceBond
:return: %TRUE if the device has carrier"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceBond

:param self: a #NMDeviceBond
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_slaves(self) -> typing.Any:
        """Gets the devices currently attached as port to @device.

:param self: a #NMDeviceBond
:return: the #GPtrArray containing #NMDevices that are slaves of @device. This is the internal copy used by the device, and must not be modified."""
        pass


class DeviceBridge(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceBridge
:return: %TRUE if the device has carrier"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceBridge

:param self: a #NMDeviceBridge
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_slaves(self) -> typing.Any:
        """Gets the devices currently attached as port to @device.

:param self: a #NMDeviceBridge
:return: the #GPtrArray containing #NMDevices that are ports of @device. This is the internal copy used by the device, and must not be modified."""
        pass


class DeviceBt(Device):
    """"""

    def get_capabilities(self) -> BluetoothCapabilities:
        """Returns the Bluetooth device's usable capabilities.

:param self: a #NMDeviceBt
:return: a combination of #NMBluetoothCapabilities"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceBt

:param self: a #NMDeviceBt
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_name(self) -> str:
        """Gets the name of the #NMDeviceBt.

:param self: a #NMDeviceBt
:return: the name of the device"""
        pass


class DeviceDummy(Device):
    """"""

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceDummy

:param self: a #NMDeviceDummy
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass


class DeviceEthernet(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceEthernet
:return: %TRUE if the device has carrier"""
        pass

    def get_hw_address(self) -> str:
        """Gets the active hardware (MAC) address of the #NMDeviceEthernet

:param self: a #NMDeviceEthernet
:return: the active hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_permanent_hw_address(self) -> str:
        """Gets the permanent hardware (MAC) address of the #NMDeviceEthernet

:param self: a #NMDeviceEthernet
:return: the permanent hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_s390_subchannels(self) -> typing.Any:
        """Return the list of s390 subchannels if the device supports them.

:param self: a #NMDeviceEthernet
:return: array of strings, each specifying
   one subchannel the s390 device uses to communicate to the host."""
        pass

    def get_speed(self) -> int:
        """Gets the speed of the #NMDeviceEthernet in Mbit/s.

:param self: a #NMDeviceEthernet
:return: the speed of the device in Mbit/s"""
        pass


class DeviceGeneric(Device):
    """"""

    def get_hw_address(self) -> str:
        """Gets the hardware address of the #NMDeviceGeneric

:param self: a #NMDeviceGeneric
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass


class DeviceHsr(Device):
    """"""

    def get_multicast_spec(self) -> int:
        """

:param self: a #NMDeviceHsr
:return: the last byte of the supervision address"""
        pass

    def get_port1(self) -> Device:
        """

:param self: a #NMDeviceHsr
:return: the device's port1 device"""
        pass

    def get_port2(self) -> Device:
        """

:param self: a #NMDeviceHsr
:return: the device's port2 device"""
        pass

    def get_prp(self) -> bool:
        """

:param self: a #NMDeviceHsr
:return: whether PRP protocol is used or not"""
        pass

    def get_supervision_address(self) -> str:
        """

:param self: a #NMDeviceHsr
:return: the supervision MAC adddress"""
        pass


class DeviceIPTunnel(Device):
    """"""

    def get_encapsulation_limit(self) -> int:
        """

:param self: a #NMDeviceIPTunnel
:return: the maximum permitted encapsulation level"""
        pass

    def get_flags(self) -> IPTunnelFlags:
        """

:param self: a #NMDeviceIPTunnel
:return: the tunnel flags"""
        pass

    def get_flow_label(self) -> int:
        """

:param self: a #NMDeviceIPTunnel
:return: the flow label assigned to tunnel packets"""
        pass

    def get_fwmark(self) -> int:
        """

:param self: a #NMDeviceIPTunnel
:return: the fwmark assigned to tunnel packets. This property applies only to VTI tunnels."""
        pass

    def get_input_key(self) -> str:
        """

:param self: a #NMDeviceIPTunnel
:return: the key used for incoming packets"""
        pass

    def get_local(self) -> str:
        """

:param self: a #NMDeviceIPTunnel
:return: the local endpoint of the tunnel"""
        pass

    def get_mode(self) -> IPTunnelMode:
        """

:param self: a #NMDeviceIPTunnel
:return: the tunneling mode"""
        pass

    def get_output_key(self) -> str:
        """

:param self: a #NMDeviceIPTunnel
:return: the key used for outgoing packets"""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceIPTunnel
:return: the device's parent device"""
        pass

    def get_path_mtu_discovery(self) -> bool:
        """

:param self: a #NMDeviceIPTunnel
:return: whether path MTU discovery is enabled"""
        pass

    def get_remote(self) -> str:
        """

:param self: a #NMDeviceIPTunnel
:return: the remote endpoint of the tunnel"""
        pass

    def get_tos(self) -> int:
        """

:param self: a #NMDeviceIPTunnel
:return: type of service (IPv4) or traffic class (IPv6) assigned to tunneled packets."""
        pass

    def get_ttl(self) -> int:
        """

:param self: a #NMDeviceIPTunnel
:return: the TTL assigned to tunneled packets"""
        pass


class DeviceInfiniband(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceInfiniband
:return: %TRUE if the device has carrier"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceInfiniband

:param self: a #NMDeviceInfiniband
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass


class DeviceIpvlan(Device):
    """"""

    def get_mode(self) -> str:
        """Gets the IPVLAN mode of the device.

:param self: a #NMDeviceIpvlan
:return: the IPVLAN mode. This is the internal string used by the device, and must not be modified."""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceIpvlan
:return: the device's parent device"""
        pass

    def get_private(self) -> bool:
        """Gets the private flag of the device.

:param self: a #NMDeviceIpvlan
:return: the private flag of the device."""
        pass

    def get_vepa(self) -> bool:
        """Gets the VEPA flag of the device.

:param self: a #NMDeviceIpvlan
:return: the VEPA flag of the device."""
        pass


class DeviceLoopback(Device):
    """"""


class DeviceMacsec(Device):
    """"""

    def get_cipher_suite(self) -> int:
        """Gets the set of cryptographic algorithms in use

:param self: a #NMDeviceMacsec
:return: the set of cryptographic algorithms in use"""
        pass

    def get_encoding_sa(self) -> int:
        """Gets the value of the Association Number (0..3) for the Security
Association in use.

:param self: a #NMDeviceMacsec
:return: the current Security Association"""
        pass

    def get_encrypt(self) -> bool:
        """Gets whether encryption of transmitted frames is enabled

:param self: a #NMDeviceMacsec
:return: whether encryption is enabled"""
        pass

    def get_es(self) -> bool:
        """Gets whether the ES (End station) bit is enabled in SecTAG for
transmitted frames

:param self: a #NMDeviceMacsec
:return: whether the ES (End station) bit is enabled"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceMacsec

:param self: a #NMDeviceMacsec
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_icv_length(self) -> int:
        """Gets the length of ICV (Integrity Check Value)

:param self: a #NMDeviceMacsec
:return: the length of ICV"""
        pass

    def get_include_sci(self) -> bool:
        """Gets whether the SCI is always included in SecTAG for transmitted
frames

:param self: a #NMDeviceMacsec
:return: whether the SCI is always included"""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceMacsec
:return: the device's parent device"""
        pass

    def get_protect(self) -> bool:
        """Gets whether protection of transmitted frames is enabled

:param self: a #NMDeviceMacsec
:return: whether protection is enabled"""
        pass

    def get_replay_protect(self) -> bool:
        """Gets whether replay protection is enabled

:param self: a #NMDeviceMacsec
:return: whether replay protection is enabled"""
        pass

    def get_scb(self) -> bool:
        """Gets whether the SCB (Single Copy Broadcast) bit is enabled in
SecTAG for transmitted frames

:param self: a #NMDeviceMacsec
:return: whether the SCB (Single Copy Broadcast) bit is enabled"""
        pass

    def get_sci(self) -> int:
        """Gets the Secure Channel Identifier in use

:param self: a #NMDeviceMacsec
:return: the SCI"""
        pass

    def get_validation(self) -> str:
        """Gets the validation mode for incoming packets (strict, check,
disabled)

:param self: a #NMDeviceMacsec
:return: the validation mode"""
        pass

    def get_window(self) -> int:
        """Gets the size of the replay window

:param self: a #NMDeviceMacsec
:return: size of the replay window"""
        pass


class DeviceMacvlan(Device):
    """"""

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceMacvlan

:param self: a #NMDeviceMacvlan
:return: the hardware address. This is the internal string used by the device, and must not be modified.  This property is not implemented yet, and the function always return NULL."""
        pass

    def get_mode(self) -> str:
        """Gets the MACVLAN mode of the device.

:param self: a #NMDeviceMacvlan
:return: the MACVLAN mode. This is the internal string used by the device, and must not be modified."""
        pass

    def get_no_promisc(self) -> bool:
        """Gets the no-promiscuous flag of the device.

:param self: a #NMDeviceMacvlan
:return: the no-promiscuous flag of the device."""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceMacvlan
:return: the device's parent device"""
        pass

    def get_tap(self) -> bool:
        """Gets the device type (MACVLAN or MACVTAP).

:param self: a #NMDeviceMacvlan
:return: %TRUE if the device is a MACVTAP, %FALSE if it is a MACVLAN."""
        pass


class DeviceModem(Device):
    """"""

    def get_apn(self) -> str:
        """The access point name the modem is connected to.

:param self: a #NMDeviceModem
:return: the APN name or %NULL if disconnected"""
        pass

    def get_current_capabilities(self) -> DeviceModemCapabilities:
        """Returns a bitfield of the generic access technology families the modem
supports without a firmware reload or reinitialization.  This value
represents the network types the modem can immediately connect to.

:param self: a #NMDeviceModem
:return: the generic access technology families the modem supports without a firmware reload or other reinitialization"""
        pass

    def get_device_id(self) -> str:
        """An identifier used by the modem backend (ModemManager) that aims to
uniquely identify the a device. Can be used to match a connection to a
particular device.

:param self: a #NMDeviceModem
:return: a device-id string"""
        pass

    def get_modem_capabilities(self) -> DeviceModemCapabilities:
        """Returns a bitfield of the generic access technology families the modem
supports.  Not all capabilities are available concurrently however; some
may require a firmware reload or reinitialization.

:param self: a #NMDeviceModem
:return: the generic access technology families the modem supports"""
        pass

    def get_operator_code(self) -> str:
        """The MCC and MNC (concatenated) of the network the modem is connected to.

:param self: a #NMDeviceModem
:return: the operator code or %NULL if disconnected or not a 3GPP modem."""
        pass


class DeviceOlpcMesh(Device):
    """"""

    def get_active_channel(self) -> int:
        """Returns the active channel of the #NMDeviceOlpcMesh device.

:param self: a #NMDeviceOlpcMesh
:return: active channel of the device"""
        pass

    def get_companion(self) -> DeviceWifi:
        """Gets the companion device of the #NMDeviceOlpcMesh.

:param self: a #NMDeviceOlpcMesh
:return: the companion of the device of %NULL"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceOlpcMesh

:param self: a #NMDeviceOlpcMesh
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass


class DeviceOvsBridge(Device):
    """"""

    def get_slaves(self) -> typing.Any:
        """Gets the ports currently attached as port to @device.

:param self: a #NMDeviceOvsBridge
:return: the #GPtrArray containing #NMDevices that are ports of @device. This is the internal copy used by the device, and must not be modified."""
        pass


class DeviceOvsInterface(Device):
    """"""


class DeviceOvsPort(Device):
    """"""

    def get_slaves(self) -> typing.Any:
        """Gets the interfaces currently attached as port to @device.

:param self: a #NMDeviceOvsPort
:return: the #GPtrArray containing #NMDevices that are ports of @device. This is the internal copy used by the device, and must not be modified."""
        pass


class DevicePpp(Device):
    """"""


class DeviceTeam(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceTeam
:return: %TRUE if the device has carrier"""
        pass

    def get_config(self) -> str:
        """Gets the current JSON configuration of the #NMDeviceTeam

:param self: a #NMDeviceTeam
:return: the current configuration. This is the internal string used by the device, and must not be modified."""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceTeam

:param self: a #NMDeviceTeam
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_slaves(self) -> typing.Any:
        """Gets the devices currently attach as port to @device.

:param self: a #NMDeviceTeam
:return: the #GPtrArray containing #NMDevices that are ports of @device. This is the internal copy used by the device, and must not be modified."""
        pass


class DeviceTun(Device):
    """"""

    def get_group(self) -> int:
        """Gets the tunnel group.

:param self: a #NMDeviceTun
:return: the gid of the tunnel group, or -1 if it has no owner."""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceTun

:param self: a #NMDeviceTun
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_mode(self) -> str:
        """Returns the TUN/TAP mode for the device.

:param self: a #NMDeviceTun
:return: 'tun' or 'tap'"""
        pass

    def get_multi_queue(self) -> bool:
        """Returns whether the #NMDeviceTun has the IFF_MULTI_QUEUE flag.

:param self: a #NMDeviceTun
:return: %TRUE if the device doesn't have the flag, %FALSE otherwise"""
        pass

    def get_no_pi(self) -> bool:
        """Returns whether the #NMDeviceTun has the IFF_NO_PI flag.

:param self: a #NMDeviceTun
:return: %TRUE if the device has the flag, %FALSE otherwise"""
        pass

    def get_owner(self) -> int:
        """Gets the tunnel owner.

:param self: a #NMDeviceTun
:return: the uid of the tunnel owner, or -1 if it has no owner."""
        pass

    def get_vnet_hdr(self) -> bool:
        """Returns whether the #NMDeviceTun has the IFF_VNET_HDR flag.

:param self: a #NMDeviceTun
:return: %TRUE if the device has the flag, %FALSE otherwise"""
        pass


class DeviceVeth(DeviceEthernet):
    """"""

    def get_peer(self) -> Device:
        """

:param self: a #NMDeviceVeth
:return: the device's peer device"""
        pass


class DeviceVlan(Device):
    """"""

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceVlan
:return: %TRUE if the device has carrier"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceVlan

:param self: a #NMDeviceVlan
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceVlan
:return: the device's parent device"""
        pass

    def get_vlan_id(self) -> int:
        """

:param self: a #NMDeviceVlan
:return: the device's VLAN ID"""
        pass


class DeviceVrf(Device):
    """"""

    def get_table(self) -> int:
        """

:param self: a #NMDeviceVrf
:return: the device's VRF routing table."""
        pass


class DeviceVxlan(Device):
    """"""

    def get_ageing(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the lifetime in seconds of FDB entries learnt by the kernel"""
        pass

    def get_carrier(self) -> bool:
        """Whether the device has carrier.

:param self: a #NMDeviceVxlan
:return: %TRUE if the device has carrier.  This property is not implemented yet, and the function always returns FALSE."""
        pass

    def get_dst_port(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the UDP destination port"""
        pass

    def get_group(self) -> str:
        """

:param self: a #NMDeviceVxlan
:return: The unicast destination IP address or the multicast IP address joined"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceVxlan

:param self: a #NMDeviceVxlan
:return: the hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_id(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the device's VXLAN ID."""
        pass

    def get_l2miss(self) -> bool:
        """

:param self: a #NMDeviceVxlan
:return: whether netlink LL ADDR miss notifications are generated"""
        pass

    def get_l3miss(self) -> bool:
        """

:param self: a #NMDeviceVxlan
:return: whether netlink IP ADDR miss notifications are generated"""
        pass

    def get_learning(self) -> bool:
        """

:param self: a #NMDeviceVxlan
:return: whether address learning is enabled"""
        pass

    def get_limit(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the maximum number of entries that can be added to the forwarding table"""
        pass

    def get_local(self) -> str:
        """

:param self: a #NMDeviceVxlan
:return: the source IP address to use in outgoing packets"""
        pass

    def get_parent(self) -> Device:
        """

:param self: a #NMDeviceVxlan
:return: the device's parent device"""
        pass

    def get_proxy(self) -> bool:
        """

:param self: a #NMDeviceVxlan
:return: whether ARP proxy is turned on"""
        pass

    def get_rsc(self) -> bool:
        """

:param self: a #NMDeviceVxlan
:return: whether route short circuit is turned on"""
        pass

    def get_src_port_max(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the maximum UDP source port"""
        pass

    def get_src_port_min(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the minimum UDP source port"""
        pass

    def get_tos(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the TOS value to use in outgoing packets"""
        pass

    def get_ttl(self) -> int:
        """

:param self: a #NMDeviceVxlan
:return: the time-to-live value to use in outgoing packets"""
        pass


class DeviceWifi(Device):
    """"""

    def get_access_point_by_path(self, path: str=None) -> AccessPoint:
        """Gets a #NMAccessPoint by path.

:param self: a #NMDeviceWifi
:param path: the object path of the access point
:return: the access point or %NULL if none is found."""
        pass

    def get_access_points(self) -> typing.Any:
        """Gets all the scanned access points of the #NMDeviceWifi.

:param self: a #NMDeviceWifi
:return: a #GPtrArray containing all the scanned #NMAccessPoints. The returned array is owned by the client and should not be modified."""
        pass

    def get_active_access_point(self) -> AccessPoint:
        """Gets the active #NMAccessPoint.

:param self: a #NMDeviceWifi
:return: the access point or %NULL if none is active"""
        pass

    def get_bitrate(self) -> int:
        """Gets the bit rate of the #NMDeviceWifi in kbit/s.

:param self: a #NMDeviceWifi
:return: the bit rate (kbit/s)"""
        pass

    def get_capabilities(self) -> DeviceWifiCapabilities:
        """Gets the Wi-Fi capabilities of the #NMDeviceWifi.

:param self: a #NMDeviceWifi
:return: the capabilities"""
        pass

    def get_hw_address(self) -> str:
        """Gets the actual hardware (MAC) address of the #NMDeviceWifi

:param self: a #NMDeviceWifi
:return: the actual hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_last_scan(self) -> int:
        """Returns the timestamp (in CLOCK_BOOTTIME milliseconds) for the last finished
network scan. A value of -1 means the device never scanned for access points.

Use nm_utils_get_timestamp_msec() to obtain current time value suitable for
comparing to this value.

:param self: a #NMDeviceWifi
:return: the last scan time in milliseconds (in clock_gettime(CLOCK_BOOTTIME) scale)."""
        pass

    def get_mode(self) -> NM80211Mode:
        """Gets the #NMDeviceWifi mode.

:param self: a #NMDeviceWifi
:return: the mode"""
        pass

    def get_permanent_hw_address(self) -> str:
        """Gets the permanent hardware (MAC) address of the #NMDeviceWifi

:param self: a #NMDeviceWifi
:return: the permanent hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def request_scan(self, cancellable: Gio.Cancellable=None) -> bool:
        """Request NM to scan for access points on @device. Note that the function
returns immediately after requesting the scan, and it may take some time
after that for the scan to complete.

:param self: a #NMDeviceWifi
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def request_scan_async(self, cancellable: Gio.Cancellable=None,
        callback: Gio.AsyncReadyCallback=None, user_data: typing.Any=None
        ) -> None:
        """Request NM to scan for access points on @device. Note that @callback will be
called immediately after requesting the scan, and it may take some time after
that for the scan to complete.

:param self: a #NMDeviceWifi
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the scan has been requested
:param user_data: caller-specific data passed to @callback
:return: """
        pass

    def request_scan_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Gets the result of a call to nm_device_wifi_request_scan_async() and
nm_device_wifi_request_scan_options_async().

:param self: a #NMDeviceWifi
:param result: the result passed to the #GAsyncReadyCallback
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def request_scan_options(self, options: GLib.Variant=None, cancellable:
        Gio.Cancellable=None) -> bool:
        """Request NM to scan for access points on @device. Note that the function
returns immediately after requesting the scan, and it may take some time
after that for the scan to complete.
This is the same as @nm_device_wifi_request_scan except it accepts @options
for the scanning. The argument is the dictionary passed to RequestScan()
D-Bus call. Valid options inside the dictionary are:
'ssids' => array of SSIDs (saay)

:param self: a #NMDeviceWifi
:param options: dictionary with options for RequestScan(), or %NULL
:param cancellable: a #GCancellable, or %NULL
:return: %TRUE on success, %FALSE on error, in which case @error will be set."""
        pass

    def request_scan_options_async(self, options: GLib.Variant=None,
        cancellable: Gio.Cancellable=None, callback: Gio.AsyncReadyCallback
        =None, user_data: typing.Any=None) -> None:
        """Request NM to scan for access points on @device. Note that @callback will be
called immediately after requesting the scan, and it may take some time after
that for the scan to complete.
This is the same as @nm_device_wifi_request_scan_async except it accepts @options
for the scanning. The argument is the dictionary passed to RequestScan()
D-Bus call. Valid options inside the dictionary are:
'ssids' => array of SSIDs (saay)

To complete the request call nm_device_wifi_request_scan_finish().

:param self: a #NMDeviceWifi
:param options: dictionary with options for RequestScan(), or %NULL
:param cancellable: a #GCancellable, or %NULL
:param callback: callback to be called when the scan has been requested
:param user_data: caller-specific data passed to @callback
:return: """
        pass


class DeviceWifiP2P(Device):
    """"""

    def get_hw_address(self) -> str:
        """Gets the actual hardware (MAC) address of the #NMDeviceWifiP2P

:param self: a #NMDeviceWifiP2P
:return: the actual hardware address. This is the internal string used by the device, and must not be modified."""
        pass

    def get_peer_by_path(self, path: str=None) -> WifiP2PPeer:
        """Gets a #NMWifiP2PPeer by path.

:param self: a #NMDeviceWifiP2P
:param path: the object path of the peer
:return: the peer or %NULL if none is found."""
        pass

    def get_peers(self) -> typing.Any:
        """Gets all the found peers of the #NMDeviceWifiP2P.

:param self: a #NMDeviceWifiP2P
:return: a #GPtrArray containing all the
          found #NMWifiP2PPeers. The returned array is owned by the client and should not be modified."""
        pass

    def start_find(self, options: GLib.Variant=None, cancellable:
        Gio.Cancellable=None, callback: Gio.AsyncReadyCallback=None,
        user_data: typing.Any=None) -> None:
        """Request NM to search for Wi-Fi P2P peers on @device. Note that the call
returns immediately after requesting the find, and it may take some time
after that for peers to be found.

The find operation will run for 30s by default. You can stop it earlier
using nm_device_p2p_wifi_stop_find().

:param self: a #NMDeviceWifiP2P
:param options: optional options passed to StartFind.
:param cancellable: a #GCancellable, or %NULL
:param callback: a #GAsyncReadyCallback, or %NULL
:param user_data: user_data for @callback
:return: """
        pass

    def start_find_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Finish an operation started by nm_device_wifi_p2p_start_find().

:param self: a #NMDeviceWifiP2P
:param result: the #GAsyncResult
:return: %TRUE if the call was successful"""
        pass

    def stop_find(self, cancellable: Gio.Cancellable=None, callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> None:
        """Request NM to stop any ongoing find operation for Wi-Fi P2P peers on @device.

:param self: a #NMDeviceWifiP2P
:param cancellable: a #GCancellable, or %NULL
:param callback: a #GAsyncReadyCallback, or %NULL
:param user_data: user_data for @callback
:return: """
        pass

    def stop_find_finish(self, result: Gio.AsyncResult=None) -> bool:
        """Finish an operation started by nm_device_wifi_p2p_stop_find().

:param self: a #NMDeviceWifiP2P
:param result: the #GAsyncResult
:return: %TRUE if the call was successful"""
        pass


class DeviceWimax(Device):
    """"""

    def get_active_nsp(self) -> WimaxNsp:
        """Gets the active #NMWimaxNsp.

:param self: a #NMDeviceWimax
:return: the access point or %NULL if none is active"""
        pass

    def get_bsid(self) -> str:
        """Gets the ID of the serving Base Station when the device is connected.

:param self: a #NMDeviceWimax
:return: the ID of the serving Base Station, or %NULL"""
        pass

    def get_center_frequency(self) -> int:
        """Gets the center frequency (in KHz) of the radio channel the device is using
to communicate with the network when connected.  Has no meaning when the
device is not connected.

:param self: a #NMDeviceWimax
:return: the center frequency in KHz, or 0"""
        pass

    def get_cinr(self) -> int:
        """Gets the CINR (Carrier to Interference + Noise Ratio) of the current radio
link in dB.  CINR is a more accurate measure of radio link quality.  Has no
meaning when the device is not connected.

:param self: a #NMDeviceWimax
:return: the CINR in dB, or 0"""
        pass

    def get_hw_address(self) -> str:
        """Gets the hardware (MAC) address of the #NMDeviceWimax

:param self: a #NMDeviceWimax
:return: the hardware address. This is the internal string used by the
          device, and must not be modified."""
        pass

    def get_nsp_by_path(self, path: str=None) -> WimaxNsp:
        """Gets a #NMWimaxNsp by path.

:param self: a #NMDeviceWimax
:param path: the object path of the NSP
:return: the access point or %NULL if none is found."""
        pass

    def get_nsps(self) -> typing.Any:
        """Gets all the scanned NSPs of the #NMDeviceWimax.

:param self: a #NMDeviceWimax
:return: a #GPtrArray containing
          all the scanned #NMWimaxNsps. The returned array is owned by the client and should not be modified."""
        pass

    def get_rssi(self) -> int:
        """Gets the RSSI of the current radio link in dBm.  This value indicates how
strong the raw received RF signal from the base station is, but does not
indicate the overall quality of the radio link.  Has no meaning when the
device is not connected.

:param self: a #NMDeviceWimax
:return: the RSSI in dBm, or 0"""
        pass

    def get_tx_power(self) -> int:
        """Average power of the last burst transmitted by the device, in units of
0.5 dBm.  i.e. a TxPower of -11 represents an actual device TX power of
-5.5 dBm.  Has no meaning when the device is not connected.

:param self: a #NMDeviceWimax
:return: the TX power in dBm, or 0"""
        pass


class DeviceWireGuard(Device):
    """"""

    def get_fwmark(self) -> int:
        """Gets the fwmark (firewall mark) for this interface.
It can be used to set routing policy for outgoing encrypted packets.
See: ip-rule(8)

:param self: a #NMDeviceWireGuard
:return: 0 if fwmark not in use, 32-bit fwmark value otherwise"""
        pass

    def get_listen_port(self) -> int:
        """Gets the local UDP port this interface listens on

:param self: a #NMDeviceWireGuard
:return: UDP listen port"""
        pass

    def get_public_key(self) -> GLib.Bytes:
        """Gets the public key for this interface

:param self: a #NMDeviceWireGuard
:return: the #GBytes containing the 32-byte public key"""
        pass


class DeviceWpan(Device):
    """"""


class DhcpConfig(Object):
    """"""

    def get_family(self) -> int:
        """Gets the IP address family of the configuration

:param self: a #NMDhcpConfig
:return: the IP address family; either <literal>AF_INET</literal> or
   <literal>AF_INET6</literal>"""
        pass

    def get_one_option(self, option: str=None) -> str:
        """Gets one option by option name.

:param self: a #NMDhcpConfig
:param option: the option to retrieve
:return: the configuration option's value. This is the internal string used by the configuration, and must not be modified."""
        pass

    def get_options(self) -> GLib.HashTable:
        """Gets all the options contained in the configuration.

:param self: a #NMDhcpConfig
:return: the #GHashTable containing strings for keys and values.  This is the internal copy used by the configuration, and must not be modified."""
        pass


class IPConfig(Object):
    """"""

    def get_addresses(self) -> typing.Any:
        """Gets the IP addresses (containing the address, prefix, and gateway).

:param self: a #NMIPConfig
:return: the #GPtrArray containing #NMIPAddress<!-- -->es.  This is the internal copy used by the configuration and must not be modified. The library never modifies the returned array and thus it is safe for callers to reference and keep using it."""
        pass

    def get_domains(self) -> typing.Any:
        """Gets the domain names.

:param self: a #NMIPConfig
:return: the array of domains. (This is never %NULL, though it may be 0-length)."""
        pass

    def get_family(self) -> int:
        """Gets the IP address family

:param self: a #NMIPConfig
:return: the IP address family; either <literal>AF_INET</literal> or <literal>AF_INET6</literal>"""
        pass

    def get_gateway(self) -> str:
        """Gets the IP gateway address.

:param self: a #NMIPConfig
:return: the IP address of the gateway."""
        pass

    def get_nameservers(self) -> typing.Any:
        """Gets the domain name servers (DNS).

:param self: a #NMIPConfig
:return: the array of nameserver IP addresses"""
        pass

    def get_routes(self) -> typing.Any:
        """Gets the routes.

:param self: a #NMIPConfig
:return: the #GPtrArray containing #NMIPRoute<!-- -->s. This is the internal copy used by the configuration, and must not be modified. The library never modifies the returned array and thus it is safe for callers to reference and keep using it."""
        pass

    def get_searches(self) -> typing.Any:
        """Gets the DNS searches.

:param self: a #NMIPConfig
:return: the array of DNS search strings. (This is never %NULL, though it may be 0-length)."""
        pass

    def get_wins_servers(self) -> typing.Any:
        """Gets the Windows Internet Name Service servers (WINS).

:param self: a #NMIPConfig
:return: the arry of WINS server IP address strings. (This is never %NULL, though it may be 0-length.)"""
        pass


class SettingIP4Config(SettingIPConfig):
    """IPv4 Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingIP4Config object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingIP4Config object with default values.

:return: the new empty #NMSettingIP4Config object"""
        pass

    def get_dhcp_client_id(self) -> str:
        """Returns the value contained in the #NMSettingIP4Config:dhcp-client-id
property.

:param self: the #NMSettingIP4Config
:return: the configured Client ID to send to the DHCP server when requesting addresses via DHCP."""
        pass

    def get_dhcp_fqdn(self) -> str:
        """Returns the value contained in the #NMSettingIP4Config:dhcp-fqdn
property.

:param self: the #NMSettingIP4Config
:return: the configured FQDN to send to the DHCP server"""
        pass

    def get_dhcp_ipv6_only_preferred(self) -> SettingIP4DhcpIpv6OnlyPreferred:
        """Returns the value in the #NMSettingIP4Config:dhcp-ipv6-only-preferred
property.

:param self: the #NMSettingIP4Config
:return: the DHCP IPv6-only preferred property value"""
        pass

    def get_dhcp_vendor_class_identifier(self) -> str:
        """Returns the value contained in the #NMSettingIP4Config:dhcp_vendor_class_identifier
property.

:param self: the #NMSettingIP4Config
:return: the vendor class identifier option to send to the DHCP server"""
        pass

    def get_link_local(self) -> SettingIP4LinkLocal:
        """Returns the value contained in the #NMSettingIP4Config:link_local
property.

:param self: the #NMSettingIP4Config
:return: the link-local configuration"""
        pass


class SettingIP6Config(SettingIPConfig):
    """IPv6 Settings"""

    def __init__(self) -> None:
        """Creates a new #NMSettingIP6Config object with default values.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Setting:
        """Creates a new #NMSettingIP6Config object with default values.

:return: the new empty #NMSettingIP6Config object"""
        pass

    def get_addr_gen_mode(self) -> SettingIP6ConfigAddrGenMode:
        """Returns the value contained in the #NMSettingIP6Config:addr-gen-mode
property.

:param self: the #NMSettingIP6Config
:return: IPv6 Address Generation Mode."""
        pass

    def get_dhcp_duid(self) -> str:
        """Returns the value contained in the #NMSettingIP6Config:dhcp-duid
property.

:param self: the #NMSettingIP6Config
:return: The configured DUID value to be included in the DHCPv6 requests sent to the DHCPv6 servers."""
        pass

    def get_dhcp_pd_hint(self) -> str:
        """Returns the value contained in the #NMSettingIP6Config:dhcp-pd-hint
property.

:param self: the #NMSettingIP6Config
:return: a string containing an address and prefix length to be used as hint for DHCPv6 prefix delegation."""
        pass

    def get_ip6_privacy(self) -> SettingIP6ConfigPrivacy:
        """Returns the value contained in the #NMSettingIP6Config:ip6-privacy
property.

:param self: the #NMSettingIP6Config
:return: IPv6 Privacy Extensions configuration value (#NMSettingIP6ConfigPrivacy)."""
        pass

    def get_mtu(self) -> int:
        """

:param self: the #NMSettingIP6Config
:return: The configured %NM_SETTING_IP6_CONFIG_MTU value for the maximum transmission unit."""
        pass

    def get_ra_timeout(self) -> int:
        """

:param self: the #NMSettingIP6Config
:return: The configured %NM_SETTING_IP6_CONFIG_RA_TIMEOUT value with the timeout for router advertisements in seconds."""
        pass

    def get_temp_preferred_lifetime(self) -> int:
        """Returns the value contained in the #NMSettingIP6Config:temp-preferred-lifetime
property.

:param self: the #NMSettingIP6Config
:return: The preferred lifetime of autogenerated temporary addresses."""
        pass

    def get_temp_valid_lifetime(self) -> int:
        """Returns the value contained in the #NMSettingIP6Config:temp-valid-lifetime
property.

:param self: the #NMSettingIP6Config
:return: The valid lifetime of autogenerated temporary addresses."""
        pass

    def get_token(self) -> str:
        """Returns the value contained in the #NMSettingIP6Config:token
property.

:param self: the #NMSettingIP6Config
:return: A string."""
        pass


class VpnConnection(ActiveConnection):
    """"""

    def get_banner(self) -> str:
        """Gets the VPN login banner of the active #NMVpnConnection.

:param self: a #NMVpnConnection
:return: the VPN login banner of the VPN connection. This is the internal string used by the connection, and must not be modified."""
        pass

    def get_vpn_state(self) -> VpnConnectionState:
        """Gets the current #NMVpnConnection state.

:param self: a #NMVpnConnection
:return: the VPN state of the active VPN connection."""
        pass
