# -*- coding: utf-8 -*-
import typing
import enum
from gi.repository import GObject
from gi.repository import GLib


class Available(enum.Enum):
    """"""
    UNKNOWN = 0
    NO = 1
    YES = 2


class DeviceType(enum.Enum):
    """"""
    UNKNOWN = 0
    AUDIO_DEVICE = 1
    VIDEO_DEVICE = 2


class Direction(enum.Enum):
    """"""
    INPUT = 0
    OUTPUT = 1


MAJOR_VERSION = '0'
MICRO_VERSION = '0'
MINOR_VERSION = '1'


class MediaCategory(enum.Enum):
    """"""
    UNKNOWN = 0
    PLAYBACK = 1
    CAPTURE = 2
    DUPLEX = 3
    MONITOR = 4
    MANAGER = 5


class MediaClass(enum.Enum):
    """"""
    UNKNOWN = 0
    AUDIO_SOURCE = 1
    AUDIO_SINK = 2
    STREAM_INPUT_AUDIO = 3
    STREAM_OUTPUT_AUDIO = 4
    VIDEO_SOURCE = 5
    VIDEO_SINK = 6
    STREAM_INPUT_VIDEO = 7
    STREAM_OUTPUT_VIDEO = 8
    AUDIO_SOURCE_VIRTUAL = 9


class MediaRole(enum.Enum):
    """"""
    UNKNOWN = 0
    MOVIE = 1
    MUSIC = 2
    CAMERA = 3
    SCREEN = 4
    COMMUNICATION = 5
    GAME = 6
    NOTIFICATION = 7
    DSP = 8
    PRODUCTION = 9
    ACCESSIBILITY = 10
    TEST = 11


class NodeState(enum.Enum):
    """"""
    ERROR = -1
    CREATING = 0
    SUSPENDED = 1
    IDLE = 2
    RUNNING = 3


class Scale(enum.Enum):
    """"""
    LINEAR = 0
    CUBIC = 1


VERSION = '0.1.0'


def device_type_from_string(string: str=None) -> DeviceType:
    """

:param string: 
:return: """
    pass


def device_type_to_string(device_type: DeviceType=None) -> str:
    """

:param device_type: 
:return: """
    pass


def get_default() -> Wp:
    """gets the default wireplumber object.

:return: gets the default wireplumber object."""
    pass


def media_category_from_string(string: str=None) -> MediaCategory:
    """

:param string: 
:return: """
    pass


def media_category_to_string(category: MediaCategory=None) -> str:
    """

:param category: 
:return: """
    pass


def media_class_from_string(string: str=None) -> MediaClass:
    """

:param string: 
:return: """
    pass


def media_class_to_string(media_class: MediaClass=None) -> str:
    """

:param media_class: 
:return: """
    pass


def media_role_from_string(string: str=None) -> MediaRole:
    """

:param string: 
:return: """
    pass


def media_role_to_string(role: MediaRole=None) -> str:
    """

:param role: 
:return: """
    pass


class Audio(GObject.Object):
    """is instanciated by [class@AstalWp.Wp]. An instance of this class can only be received there.

 This is a convenience class and acts as a filter for [class@AstalWp.Wp] to filter for audio
endpoints and devices."""

    def __init__(self, wp: Wp=None) -> None:
        """creates a new Audio object. You should use [property@AstalWp.Wp:audio] instead

:param self: 
:param wp: 
:return: """
        pass

    @staticmethod
    def new(wp: Wp=None) -> Audio:
        """creates a new Audio object. You should use [property@AstalWp.Wp:audio] instead

:param wp: 
:return: """
        pass

    def get_default_microphone(self) -> Endpoint:
        """gets the default microphone object

:param self: 
:return: """
        pass

    def get_default_speaker(self) -> Endpoint:
        """gets the default speaker object

:param self: 
:return: """
        pass

    def get_device(self, id: int=None) -> Device:
        """gets the device with the given id

:param self: the AstalWpAudio object
:param id: the id of the device
:return: """
        pass

    def get_devices(self) -> GLib.List:
        """a GList containing the devices

:param self: the AstalWpAudio object
:return: """
        pass

    def get_microphone(self, id: int=None) -> Endpoint:
        """gets the microphone with the given id

:param self: the AstalWpAudio object
:param id: the id of the endpoint
:return: """
        pass

    def get_microphones(self) -> GLib.List:
        """a GList containing the microphones

:param self: the AstalWpAudio object
:return: """
        pass

    def get_node(self, id: int=None) -> Node:
        """the node with the given id

:param self: the AstalWpAudio object
:param id: the id of the endpoint
:return: """
        pass

    def get_recorder(self, id: int=None) -> Stream:
        """gets the recorder with the given id

:param self: the AstalWpAudio object
:param id: the id of the endpoint
:return: """
        pass

    def get_recorders(self) -> GLib.List:
        """a GList containing the recorders

:param self: the AstalWpAudio object
:return: """
        pass

    def get_speaker(self, id: int=None) -> Endpoint:
        """gets the speaker with the given id

:param self: the AstalWpAudio object
:param id: the id of the endpoint
:return: """
        pass

    def get_speakers(self) -> GLib.List:
        """a GList containing the speakers

:param self: the AstalWpAudio object
:return: """
        pass

    def get_stream(self, id: int=None) -> Stream:
        """gets the stream with the given id

:param self: the AstalWpAudio object
:param id: the id of the endpoint
:return: """
        pass

    def get_streams(self) -> GLib.List:
        """a GList containing the streams

:param self: the AstalWpAudio object
:return: """
        pass


class AudioClass:
    """"""
    parent_class: GObject.ObjectClass


class Channel(GObject.Object):
    """"""

    def get_name(self) -> str:
        """the name of the channel

:param self: 
:return: """
        pass

    def get_volume(self) -> float:
        """the volume of the channel

:param self: 
:return: """
        pass

    def get_volume_icon(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_volume(self, volume: float=None) -> None:
        """sets the volume for this channel. Note that if [property@AstalWp.Node:lock-channels] is true for
the node this channel is associated with, this method will set the volume for all channels.

:param self: 
:param volume: 
:return: """
        pass


class ChannelClass:
    """"""
    parent_class: GObject.ObjectClass


class Device(GObject.Object):
    """"""

    def get_active_profile_id(self) -> int:
        """gets the currently active profile of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_description(self) -> str:
        """gets the description of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_device_type(self) -> DeviceType:
        """gets the type of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_form_factor(self) -> str:
        """gets the form factor of this device.

:param self: the AstalWpDevice object
:return: """
        pass

    def get_icon(self) -> str:
        """gets the icon of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_id(self) -> int:
        """gets the id of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_input_route_id(self) -> int:
        """gets the currently active input route of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_input_routes(self) -> GLib.List:
        """gets a GList containing the input routes

:param self: the AstalWpDevice object
:return: """
        pass

    def get_output_route_id(self) -> int:
        """gets the currently active output route of this device

:param self: the AstalWpDevice object
:return: """
        pass

    def get_output_routes(self) -> GLib.List:
        """gets a GList containing the output routes

:param self: the AstalWpDevice object
:return: """
        pass

    def get_profile(self, id: int=None) -> Profile:
        """gets the profile with the given id

:param self: the AstalWpDevice object
:param id: the id of the profile
:return: """
        pass

    def get_profiles(self) -> GLib.List:
        """gets a GList containing the profiles

:param self: the AstalWpDevice object
:return: """
        pass

    def get_pw_property(self, key: str=None) -> str:
        """Gets the pipewire property with the give key. You should use the GObject properties of this node
whereever possible, as you can get notified on changes, which is not the case here.

:param self: 
:param key: 
:return: """
        pass

    def get_route(self, id: int=None) -> Route:
        """gets the route with the given id

:param self: the AstalWpDevice object
:param id: the id of the route
:return: """
        pass

    def get_routes(self) -> GLib.List:
        """gets a GList containing the routes

:param self: the AstalWpDevice object
:return: """
        pass

    def set_active_profile_id(self, profile_id: int=None) -> None:
        """sets the profile for this device

:param self: the AstalWpDevice object
:param profile_id: the id of the profile
:return: """
        pass

    def set_route(self, route: Route=None, card_device: int=None) -> None:
        """sets the route for this device. You should use the [method@AstalWp.Endpoint.set_route] instead.

:param self: The AstalWpDevice object
:param route: 
:param card_device: card device index
:return: """
        pass


class DeviceClass:
    """"""
    parent_class: GObject.ObjectClass


class EndpointClass:
    """"""
    parent_class: NodeClass


class Node(GObject.Object):
    """"""

    def metadata_changed(self, key: str=None, type: str=None, value: str=None
        ) -> None:
        """

:param self: 
:param key: 
:param type: 
:param value: 
:return: """
        pass

    def params_changed(self, id: str=None) -> None:
        """

:param self: 
:param id: 
:return: """
        pass

    def get_channels(self) -> GLib.List:
        """gets the list representing the per channel volumes

:param self: the AstalWpNode instance
:return: """
        pass

    def get_description(self) -> str:
        """gets the description of this node

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_icon(self) -> str:
        """gets the icon for this node

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_id(self) -> int:
        """gets the id of the node.

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_lock_channels(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_media_class(self) -> MediaClass:
        """gets the media class of the node.

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_mute(self) -> bool:
        """gets the mute status of the node.

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_name(self) -> str:
        """gets the name of this node

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_path(self) -> str:
        """gets the object path of this node

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_pw_property(self, key: str=None) -> str:
        """Gets the pipewire property with the give key. You should use the GObject properties of this node
whereever possible, as you can get notified on changes, which is not the case here.

:param self: 
:param key: 
:return: """
        pass

    def get_serial(self) -> int:
        """gets the serial number of this node

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_state(self) -> NodeState:
        """gets the current state of this node

:param self: The AstalWpNode instance.
:return: """
        pass

    def get_volume(self) -> float:
        """gets the volume

:param self: the AstalWpNode instance.
:return: """
        pass

    def get_volume_icon(self) -> str:
        """

:param self: 
:return: """
        pass

    def metadata_changed(self, key: str=None, type: str=None, value: str=None
        ) -> None:
        """

:param self: 
:param key: 
:param type: 
:param value: 
:return: """
        pass

    def params_changed(self, id: str=None) -> None:
        """

:param self: 
:param id: 
:return: """
        pass

    def set_lock_channels(self, lock_channels: bool=None) -> None:
        """Lock the channel volumes together. If set, all channels will always have the same volume.

:param self: 
:param lock_channels: 
:return: """
        pass

    def set_mute(self, mute: bool=None) -> None:
        """Sets the mute status for the node.

:param self: the AstalWpNode instance.
:param mute: A boolean indicating whether to mute the node.
:return: """
        pass

    def set_volume(self, volume: float=None) -> None:
        """Sets the volume level for this node. The volume is clamped to be between
0 and 1.5.

:param self: the AstalWpNode object
:param volume: The new volume level to set.
:return: """
        pass
    parent_instance: GObject.Object


class NodeClass:
    """"""
    parent_class: GObject.ObjectClass
    params_changed: typing.Any
    metadata_changed: typing.Any


class Profile(GObject.Object):
    """"""

    def get_available(self) -> Available:
        """

:param self: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_index(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_priority(self) -> int:
        """

:param self: 
:return: """
        pass


class ProfileClass:
    """"""
    parent_class: GObject.ObjectClass


class Route(GObject.Object):
    """"""

    def get_available(self) -> Available:
        """

:param self: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_device(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_direction(self) -> Direction:
        """

:param self: 
:return: """
        pass

    def get_index(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_priority(self) -> int:
        """

:param self: 
:return: """
        pass


class RouteClass:
    """"""
    parent_class: GObject.ObjectClass


class Stream(Node):
    """"""

    def get_media_category(self) -> MediaCategory:
        """

:param self: 
:return: """
        pass

    def get_media_role(self) -> MediaRole:
        """

:param self: 
:return: """
        pass

    def get_target_endpoint(self) -> Endpoint:
        """get the target [class@AstalWp.Endpoint]

:param self: 
:return: """
        pass

    def get_target_serial(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_target_endpoint(self, target: Endpoint=None) -> None:
        """set the target [class@AstalWp.Endpoint]

:param self: 
:param target: 
:return: """
        pass

    def set_target_serial(self, serial: int=None) -> None:
        """

:param self: 
:param serial: 
:return: """
        pass


class StreamClass:
    """"""
    parent_class: NodeClass


class Video(GObject.Object):
    """is instanciated by [class@AstalWp.Wp]. An instance of class can only be received there.

 This is a convinience class and acts as a filter for [class@AstalWp.Wp] to filter for video
endpoints and devices."""

    def __init__(self, wp: Wp=None) -> None:
        """

:param self: 
:param wp: 
:return: """
        pass

    @staticmethod
    def new(wp: Wp=None) -> Video:
        """

:param wp: 
:return: """
        pass

    def get_device(self, id: int=None) -> Device:
        """the device with the given id

:param self: the AstalWpVideo object
:param id: the id of the device
:return: the device with the given id"""
        pass

    def get_devices(self) -> GLib.List:
        """a list containing the devices

:param self: the AstalWpAudio object
:return: a GList containing the devices"""
        pass

    def get_recorder(self, id: int=None) -> Stream:
        """the recorder with the given id

:param self: the AstalWpVideo object
:param id: the id of the endpoint
:return: the recorder with the given id"""
        pass

    def get_recorders(self) -> GLib.List:
        """a list containing the video recorders

:param self: the AstalWpVideo object
:return: a GList containing the video recorders"""
        pass

    def get_sink(self, id: int=None) -> Endpoint:
        """the sink with the given id

:param self: the AstalWpVideo object
:param id: the id of the endpoint
:return: the sink with the given id"""
        pass

    def get_sinks(self) -> GLib.List:
        """a list containing the video sinks

:param self: the AstalWpVideo object
:return: a GList containing the video sinks"""
        pass

    def get_source(self, id: int=None) -> Endpoint:
        """the source with the given id

:param self: the AstalWpVideo object
:param id: the id of the endpoint
:return: the source with the given id"""
        pass

    def get_sources(self) -> GLib.List:
        """a list containing the video sources

:param self: the AstalWpVideo object
:return: a GList containing the video sources"""
        pass

    def get_stream(self, id: int=None) -> Stream:
        """the stream with the given id

:param self: the AstalWpVideo object
:param id: the id of the endpoint
:return: the stream with the given id"""
        pass

    def get_streams(self) -> GLib.List:
        """a list containing the video streams

:param self: the AstalWpVideo object
:return: a GList containing the video streams"""
        pass


class VideoClass:
    """"""
    parent_class: GObject.ObjectClass


class Wp(GObject.Object):
    """manages the connection to wireplumber. Usually you don't want to use this class directly, but use
the [class@AstalWp.Audio] or [class@AstalWp.Video] instead."""

    @staticmethod
    def get_default() -> Wp:
        """gets the default wireplumber object.

:return: gets the default wireplumber object."""
        pass

    def get_audio(self) -> Audio:
        """gets the [class@AstalWp.Audio] object

:param self: 
:return: gets the audio object"""
        pass

    def get_default_microphone(self) -> Endpoint:
        """gets the default microphone object

:param self: 
:return: gets the default microphone object"""
        pass

    def get_default_speaker(self) -> Endpoint:
        """gets the default speaker object

:param self: 
:return: gets the default speaker object"""
        pass

    def get_device(self, id: int=None) -> Device:
        """the device with the given id

:param self: the AstalWpWp object
:param id: the id of the device
:return: the device with the given id"""
        pass

    def get_devices(self) -> GLib.List:
        """the GList containing the devices

:param self: the AstalWpWp object
:return: a GList containing the devices"""
        pass

    def get_node(self, id: int=None) -> Node:
        """the node with the given id

:param self: the AstalWpWp object
:param id: the id of the node
:return: the node with the given id"""
        pass

    def get_node_by_serial(self, serial: int=None) -> Node:
        """finds the AstalWpNode with the give serial.

:param self: 
:param serial: 
:return: """
        pass

    def get_nodes(self) -> GLib.List:
        """a GList containing all nodes

:param self: the AstalWpWp object
:return: a GList containing the nodes"""
        pass

    def get_scale(self) -> Scale:
        """

:param self: 
:return: """
        pass

    def get_video(self) -> Video:
        """gets the video object

:param self: 
:return: gets the video object"""
        pass

    def set_scale(self, scale: Scale=None) -> None:
        """

:param self: 
:param scale: 
:return: """
        pass


class WpClass:
    """"""
    parent_class: GObject.ObjectClass


class Endpoint(Node):
    """"""

    def get_device(self) -> Device:
        """gets the device associated with this endpoint

:param self: 
:return: """
        pass

    def get_device_id(self) -> int:
        """gets the id of the device associated with this endpoint

:param self: 
:return: """
        pass

    def get_is_default(self) -> bool:
        """is this endpoint configured as the default.

:param self: 
:return: """
        pass

    def get_route(self) -> Route:
        """Gets the currently active [class@AstalWp.Route]

:param self: 
:return: """
        pass

    def get_route_id(self) -> int:
        """gets the id of the currently active route

:param self: 
:return: """
        pass

    def get_routes(self) -> GLib.List:
        """Gets a list of available routes.
This list is filtered and contains only routes, that are actually available. You can get a full
list of routes from [property@AstalWp.Device:routes]

:param self: 
:return: """
        pass

    def set_is_default(self, is_default: bool=None) -> None:
        """Sets this endpoint as the default

:param self: 
:param is_default: 
:return: """
        pass

    def set_route(self, route: Route=None) -> None:
        """Sets the currently active [class@AstalWp.Route]

:param self: 
:param route: 
:return: """
        pass

    def set_route_id(self, route_id: int=None) -> None:
        """Sets the currently active route id

:param self: 
:param route_id: 
:return: """
        pass
