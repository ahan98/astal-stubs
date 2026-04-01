from gi.repository import GObject as GObject

class Available:
    UNKNOWN: int
    NO: int
    YES: int

class DeviceType:
    UNKNOWN: int
    AUDIO_DEVICE: int
    VIDEO_DEVICE: int

class Direction:
    INPUT: int
    OUTPUT: int

MAJOR_VERSION: int
MICRO_VERSION: int
MINOR_VERSION: int

class MediaCategory:
    UNKNOWN: int
    PLAYBACK: int
    CAPTURE: int
    DUPLEX: int
    MONITOR: int
    MANAGER: int

class MediaClass:
    UNKNOWN: int
    AUDIO_SOURCE: int
    AUDIO_SINK: int
    STREAM_INPUT_AUDIO: int
    STREAM_OUTPUT_AUDIO: int
    VIDEO_SOURCE: int
    VIDEO_SINK: int
    STREAM_INPUT_VIDEO: int
    STREAM_OUTPUT_VIDEO: int
    AUDIO_SOURCE_VIRTUAL: int

class MediaRole:
    UNKNOWN: int
    MOVIE: int
    MUSIC: int
    CAMERA: int
    SCREEN: int
    COMMUNICATION: int
    GAME: int
    NOTIFICATION: int
    DSP: int
    PRODUCTION: int
    ACCESSIBILITY: int
    TEST: int

class NodeState:
    ERROR: int
    CREATING: int
    SUSPENDED: int
    IDLE: int
    RUNNING: int

class Scale:
    LINEAR: int
    CUBIC: int

VERSION: str

def device_type_from_string(string=None):
    """    
    @type string: str
    @returns: 
    @rtype: DeviceType
    """
def device_type_to_string(device_type=None):
    """    
    @type device_type: DeviceType
    @returns: 
    @rtype: str
    """
def get_default():
    """    gets the default wireplumber object.
    @returns: gets the default wireplumber object.
    @rtype: Wp
    """
def media_category_from_string(string=None):
    """    
    @type string: str
    @returns: 
    @rtype: MediaCategory
    """
def media_category_to_string(category=None):
    """    
    @type category: MediaCategory
    @returns: 
    @rtype: str
    """
def media_class_from_string(string=None):
    """    
    @type string: str
    @returns: 
    @rtype: MediaClass
    """
def media_class_to_string(media_class=None):
    """    
    @type media_class: MediaClass
    @returns: 
    @rtype: str
    """
def media_role_from_string(string=None):
    """    
    @type string: str
    @returns: 
    @rtype: MediaRole
    """
def media_role_to_string(role=None):
    """    
    @type role: MediaRole
    @returns: 
    @rtype: str
    """

class Audio(GObject.Object):
    """is instanciated by [class@AstalWp.Wp]. An instance of this class can only be received there.

 This is a convenience class and acts as a filter for [class@AstalWp.Wp] to filter for audio
endpoints and devices."""
    def __init__(self, wp=None) -> None:
        """        creates a new Audio object. You should use [property@AstalWp.Wp:audio] instead
        @type wp: Wp
        @returns: Newly created Audio
        @rtype: Audio
        """
    @staticmethod
    def new(wp=None):
        """        creates a new Audio object. You should use [property@AstalWp.Wp:audio] instead
        @type wp: Wp
        @returns: Newly created Audio
        @rtype: Audio
        """
    def get_default_microphone(self):
        """        gets the default microphone object
        @returns: 
        @rtype: Endpoint
        """
    def get_default_speaker(self):
        """        gets the default speaker object
        @returns: 
        @rtype: Endpoint
        """
    def get_device(self, id=None):
        """        gets the device with the given id
        @param id: the id of the device
        @type id: int
        @returns: 
        @rtype: Device
        """
    def get_devices(self):
        """        a GList containing the devices
        @returns: 
        @rtype: GLib.List
        """
    def get_microphone(self, id=None):
        """        gets the microphone with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: 
        @rtype: Endpoint
        """
    def get_microphones(self):
        """        a GList containing the microphones
        @returns: 
        @rtype: GLib.List
        """
    def get_node(self, id=None):
        """        the node with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: 
        @rtype: Node
        """
    def get_recorder(self, id=None):
        """        gets the recorder with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: 
        @rtype: Stream
        """
    def get_recorders(self):
        """        a GList containing the recorders
        @returns: 
        @rtype: GLib.List
        """
    def get_speaker(self, id=None):
        """        gets the speaker with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: 
        @rtype: Endpoint
        """
    def get_speakers(self):
        """        a GList containing the speakers
        @returns: 
        @rtype: GLib.List
        """
    def get_stream(self, id=None):
        """        gets the stream with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: 
        @rtype: Stream
        """
    def get_streams(self):
        """        a GList containing the streams
        @returns: 
        @rtype: GLib.List
        """

class AudioClass:
    @property
    def parent_class(self): ...

class Channel(GObject.Object):
    def get_name(self):
        """        the name of the channel
        @returns: 
        @rtype: str
        """
    def get_volume(self):
        """        the volume of the channel
        @returns: 
        @rtype: float
        """
    def get_volume_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_volume(self, volume=None):
        """        sets the volume for this channel. Note that if [property@AstalWp.Node:lock-channels] is true for
        the node this channel is associated with, this method will set the volume for all channels.
        @type volume: float
        @returns: 
        @rtype: None
        """

class ChannelClass:
    @property
    def parent_class(self): ...

class Device(GObject.Object):
    def get_active_profile_id(self):
        """        gets the currently active profile of this device
        @returns: 
        @rtype: int
        """
    def get_description(self):
        """        gets the description of this device
        @returns: 
        @rtype: str
        """
    def get_device_type(self):
        """        gets the type of this device
        @returns: 
        @rtype: DeviceType
        """
    def get_form_factor(self):
        """        gets the form factor of this device.
        @returns: 
        @rtype: str
        """
    def get_icon(self):
        """        gets the icon of this device
        @returns: 
        @rtype: str
        """
    def get_id(self):
        """        gets the id of this device
        @returns: 
        @rtype: int
        """
    def get_input_route_id(self):
        """        gets the currently active input route of this device
        @returns: 
        @rtype: int
        """
    def get_input_routes(self):
        """        gets a GList containing the input routes
        @returns: 
        @rtype: GLib.List
        """
    def get_output_route_id(self):
        """        gets the currently active output route of this device
        @returns: 
        @rtype: int
        """
    def get_output_routes(self):
        """        gets a GList containing the output routes
        @returns: 
        @rtype: GLib.List
        """
    def get_profile(self, id=None):
        """        gets the profile with the given id
        @param id: the id of the profile
        @type id: int
        @returns: 
        @rtype: Profile
        """
    def get_profiles(self):
        """        gets a GList containing the profiles
        @returns: 
        @rtype: GLib.List
        """
    def get_pw_property(self, key=None):
        """        Gets the pipewire property with the give key. You should use the GObject properties of this node
        whereever possible, as you can get notified on changes, which is not the case here.
        @type key: str
        @returns: 
        @rtype: str
        """
    def get_route(self, id=None):
        """        gets the route with the given id
        @param id: the id of the route
        @type id: int
        @returns: 
        @rtype: Route
        """
    def get_routes(self):
        """        gets a GList containing the routes
        @returns: 
        @rtype: GLib.List
        """
    def set_active_profile_id(self, profile_id=None):
        """        sets the profile for this device
        @param profile_id: the id of the profile
        @type profile_id: int
        @returns: 
        @rtype: None
        """
    def set_route(self, route=None, card_device=None):
        """        sets the route for this device. You should use the [method@AstalWp.Endpoint.set_route] instead.
        @param card_device: card device index
        @type route: Route
        @type card_device: int
        @returns: 
        @rtype: None
        """

class DeviceClass:
    @property
    def parent_class(self): ...

class EndpointClass:
    @property
    def parent_class(self): ...

class Node(GObject.Object):
    def metadata_changed(self, key=None, type=None, value=None):
        """        
        @type key: str
        @type type: str
        @type value: str
        @returns: 
        @rtype: None
        """
    def params_changed(self, id=None):
        """        
        @type id: str
        @returns: 
        @rtype: None
        """
    def get_channels(self):
        """        gets the list representing the per channel volumes
        @returns: 
        @rtype: GLib.List
        """
    def get_description(self):
        """        gets the description of this node
        @returns: 
        @rtype: str
        """
    def get_icon(self):
        """        gets the icon for this node
        @returns: 
        @rtype: str
        """
    def get_id(self):
        """        gets the id of the node.
        @returns: 
        @rtype: int
        """
    def get_lock_channels(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_media_class(self):
        """        gets the media class of the node.
        @returns: 
        @rtype: MediaClass
        """
    def get_mute(self):
        """        gets the mute status of the node.
        @returns: 
        @rtype: bool
        """
    def get_name(self):
        """        gets the name of this node
        @returns: 
        @rtype: str
        """
    def get_path(self):
        """        gets the object path of this node
        @returns: 
        @rtype: str
        """
    def get_pw_property(self, key=None):
        """        Gets the pipewire property with the give key. You should use the GObject properties of this node
        whereever possible, as you can get notified on changes, which is not the case here.
        @type key: str
        @returns: 
        @rtype: str
        """
    def get_serial(self):
        """        gets the serial number of this node
        @returns: 
        @rtype: int
        """
    def get_state(self):
        """        gets the current state of this node
        @returns: 
        @rtype: NodeState
        """
    def get_volume(self):
        """        gets the volume
        @returns: 
        @rtype: float
        """
    def get_volume_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    def metadata_changed(self, key=None, type=None, value=None):
        """        
        @type key: str
        @type type: str
        @type value: str
        @returns: 
        @rtype: None
        """
    def params_changed(self, id=None):
        """        
        @type id: str
        @returns: 
        @rtype: None
        """
    def set_lock_channels(self, lock_channels=None):
        """        Lock the channel volumes together. If set, all channels will always have the same volume.
        @type lock_channels: bool
        @returns: 
        @rtype: None
        """
    def set_mute(self, mute=None):
        """        Sets the mute status for the node.
        @param mute: A boolean indicating whether to mute the node.
        @type mute: bool
        @returns: 
        @rtype: None
        """
    def set_volume(self, volume=None):
        """        Sets the volume level for this node. The volume is clamped to be between
        0 and 1.5.
        @param volume: The new volume level to set.
        @type volume: float
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...

class NodeClass:
    @property
    def parent_class(self): ...
    @property
    def params_changed(self): ...
    @property
    def metadata_changed(self): ...

class Profile(GObject.Object):
    def get_available(self):
        """        
        @returns: 
        @rtype: Available
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_index(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_priority(self):
        """        
        @returns: 
        @rtype: int
        """

class ProfileClass:
    @property
    def parent_class(self): ...

class Route(GObject.Object):
    def get_available(self):
        """        
        @returns: 
        @rtype: Available
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_device(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_direction(self):
        """        
        @returns: 
        @rtype: Direction
        """
    def get_index(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_priority(self):
        """        
        @returns: 
        @rtype: int
        """

class RouteClass:
    @property
    def parent_class(self): ...

class Stream(Node):
    def get_media_category(self):
        """        
        @returns: 
        @rtype: MediaCategory
        """
    def get_media_role(self):
        """        
        @returns: 
        @rtype: MediaRole
        """
    def get_target_endpoint(self):
        """        get the target [class@AstalWp.Endpoint]
        @returns: 
        @rtype: Endpoint
        """
    def get_target_serial(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_target_endpoint(self, target=None):
        """        set the target [class@AstalWp.Endpoint]
        @type target: Endpoint
        @returns: 
        @rtype: None
        """
    def set_target_serial(self, serial=None):
        """        
        @type serial: int
        @returns: 
        @rtype: None
        """

class StreamClass:
    @property
    def parent_class(self): ...

class Video(GObject.Object):
    """is instanciated by [class@AstalWp.Wp]. An instance of class can only be received there.

 This is a convinience class and acts as a filter for [class@AstalWp.Wp] to filter for video
endpoints and devices."""
    def __init__(self, wp=None) -> None:
        """        
        @type wp: Wp
        @returns: Newly created Video
        @rtype: Video
        """
    @staticmethod
    def new(wp=None):
        """        
        @type wp: Wp
        @returns: Newly created Video
        @rtype: Video
        """
    def get_device(self, id=None):
        """        the device with the given id
        @param id: the id of the device
        @type id: int
        @returns: the device with the given id
        @rtype: Device
        """
    def get_devices(self):
        """        a list containing the devices
        @returns: a GList containing the devices
        @rtype: GLib.List
        """
    def get_recorder(self, id=None):
        """        the recorder with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: the recorder with the given id
        @rtype: Stream
        """
    def get_recorders(self):
        """        a list containing the video recorders
        @returns: a GList containing the video recorders
        @rtype: GLib.List
        """
    def get_sink(self, id=None):
        """        the sink with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: the sink with the given id
        @rtype: Endpoint
        """
    def get_sinks(self):
        """        a list containing the video sinks
        @returns: a GList containing the video sinks
        @rtype: GLib.List
        """
    def get_source(self, id=None):
        """        the source with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: the source with the given id
        @rtype: Endpoint
        """
    def get_sources(self):
        """        a list containing the video sources
        @returns: a GList containing the video sources
        @rtype: GLib.List
        """
    def get_stream(self, id=None):
        """        the stream with the given id
        @param id: the id of the endpoint
        @type id: int
        @returns: the stream with the given id
        @rtype: Stream
        """
    def get_streams(self):
        """        a list containing the video streams
        @returns: a GList containing the video streams
        @rtype: GLib.List
        """

class VideoClass:
    @property
    def parent_class(self): ...

class Wp(GObject.Object):
    """manages the connection to wireplumber. Usually you don't want to use this class directly, but use
the [class@AstalWp.Audio] or [class@AstalWp.Video] instead."""
    @staticmethod
    def get_default():
        """        gets the default wireplumber object.
        @returns: gets the default wireplumber object.
        @rtype: Wp
        """
    def get_audio(self):
        """        gets the [class@AstalWp.Audio] object
        @returns: gets the audio object
        @rtype: Audio
        """
    def get_default_microphone(self):
        """        gets the default microphone object
        @returns: gets the default microphone object
        @rtype: Endpoint
        """
    def get_default_speaker(self):
        """        gets the default speaker object
        @returns: gets the default speaker object
        @rtype: Endpoint
        """
    def get_device(self, id=None):
        """        the device with the given id
        @param id: the id of the device
        @type id: int
        @returns: the device with the given id
        @rtype: Device
        """
    def get_devices(self):
        """        the GList containing the devices
        @returns: a GList containing the devices
        @rtype: GLib.List
        """
    def get_node(self, id=None):
        """        the node with the given id
        @param id: the id of the node
        @type id: int
        @returns: the node with the given id
        @rtype: Node
        """
    def get_node_by_serial(self, serial=None):
        """        finds the AstalWpNode with the give serial.
        @type serial: int
        @returns: 
        @rtype: Node
        """
    def get_nodes(self):
        """        a GList containing all nodes
        @returns: a GList containing the nodes
        @rtype: GLib.List
        """
    def get_scale(self):
        """        
        @returns: 
        @rtype: Scale
        """
    def get_video(self):
        """        gets the video object
        @returns: gets the video object
        @rtype: Video
        """
    def set_scale(self, scale=None):
        """        
        @type scale: Scale
        @returns: 
        @rtype: None
        """

class WpClass:
    @property
    def parent_class(self): ...

class Endpoint(Node):
    def get_device(self):
        """        gets the device associated with this endpoint
        @returns: 
        @rtype: Device
        """
    def get_device_id(self):
        """        gets the id of the device associated with this endpoint
        @returns: 
        @rtype: int
        """
    def get_is_default(self):
        """        is this endpoint configured as the default.
        @returns: 
        @rtype: bool
        """
    def get_route(self):
        """        Gets the currently active [class@AstalWp.Route]
        @returns: 
        @rtype: Route
        """
    def get_route_id(self):
        """        gets the id of the currently active route
        @returns: 
        @rtype: int
        """
    def get_routes(self):
        """        Gets a list of available routes.
        This list is filtered and contains only routes, that are actually available. You can get a full
        list of routes from [property@AstalWp.Device:routes]
        @returns: 
        @rtype: GLib.List
        """
    def set_is_default(self, is_default=None):
        """        Sets this endpoint as the default
        @type is_default: bool
        @returns: 
        @rtype: None
        """
    def set_route(self, route=None):
        """        Sets the currently active [class@AstalWp.Route]
        @type route: Route
        @returns: 
        @rtype: None
        """
    def set_route_id(self, route_id=None):
        """        Sets the currently active route id
        @type route_id: int
        @returns: 
        @rtype: None
        """
