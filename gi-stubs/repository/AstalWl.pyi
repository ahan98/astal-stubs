# -*- coding: utf-8 -*-
from gi.repository import GObject
from gi.repository import Wl
from gi.repository import AstalWl
import enum
from gi.repository import GLib


class OutputSubpixel(enum.Enum):
    """This enumeration describes how the physical pixels on an output are laid out."""
    UNKNOWN = 0
    NONE = 1
    HORIZONTAL_RGB = 2
    HORIZONTAL_BGR = 3
    VERTICAL_RGB = 4
    VERTICAL_BGR = 5


class OutputTransform(enum.Enum):
    """This describes transformations that clients and compositors apply to buffer contents. The flipped values correspond to an initial flip around a 
vertical axis followed by rotation."""
    NORMAL = 0
    ROTATE_90 = 1
    ROTATE_180 = 2
    ROTATE_270 = 3
    FLIPPED = 4
    FLIPPED_90 = 5
    FLIPPED_180 = 6
    FLIPPED_270 = 7


class SeatCapabilities(enum.Enum):
    """Bitfield flags describing the input capabilities of this seat."""
    POINTER = 1
    KEYBOARD = 2
    TOUCH = 4


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalWl.Registry:
    """Convenience wrapper for [func@AstalWl.Registry.get_default].
Returns the singleton `Registry` instance that tracks all known globals, outputs, and seats on the connected Wayland display.

:return: """
    pass


class Registry(GObject.Object):
    """Wraps the Wayland `wl_registry` interface and keeps track of all announced globals, outputs and seats.
It exposes high-level collections and lookup helpers and emits signals when globals, outputs or seats are added or removed."""

    @staticmethod
    def get_default() -> AstalWl.Registry:
        """Returns the singleton `Registry` instance.
The first call connects to the Wayland display and sets up the underlying `wl_registry` listener.

:return: """
        pass

    def get_globals(self) -> GLib.List:
        """Returns a list of all known globals.

:param self: 
:return: """
        pass

    def get_outputs(self) -> GLib.List:
        """Returns a list of all known outputs.

:param self: 
:return: """
        pass

    def get_seats(self) -> GLib.List:
        """Returns a list of all known seats.

:param self: 
:return: """
        pass

    def get_registry(self) -> Wl.Registry:
        """Returns the underlying `wl_registry` object.

:param self: 
:return: """
        pass

    def get_display(self) -> Wl.Display:
        """Returns the underlying `wl_display` used by this registry.

:param self: 
:return: """
        pass

    def find_globals(self, interface: str=None) -> GLib.List:
        """Returns a list of globals, optionally filtered by interface name. If `null` is passed, all globals are returned.

:param self: 
:param interface: 
:return: """
        pass

    def get_global_by_id(self, id: int=None) -> AstalWl.Global:
        """Looks up a global by its numeric Iid.

:param self: 
:param id: 
:return: """
        pass

    def get_output_by_id(self, id: int=None) -> AstalWl.Output:
        """Looks up an output by its global id.

:param self: 
:param id: 
:return: """
        pass

    def get_output_by_name(self, name: str=None) -> AstalWl.Output:
        """Looks up an output by its compositor-assigned name.

:param self: 
:param name: 
:return: """
        pass

    def get_output_by_wl_output(self, wl_output: Wl.Output=None
        ) -> AstalWl.Output:
        """Looks up an `Output` by its underlying `wl_output`.

:param self: 
:param wl_output: 
:return: """
        pass

    def get_seat_by_id(self, id: int=None) -> AstalWl.Seat:
        """Looks up a seat by its global id.

:param self: 
:param id: 
:return: """
        pass

    def get_seat_by_name(self, name: str=None) -> AstalWl.Seat:
        """Looks up a seat by its compositor-assigned name.

:param self: 
:param name: 
:return: """
        pass

    def get_seat_by_wl_seat(self, wl_seat: Wl.Seat=None) -> AstalWl.Seat:
        """Looks up a `Seat` by its underlying `wl_seat`.

:param self: 
:param wl_seat: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalWl.Registry:
        """

:return: """
        pass
    parent_instance: GObject.Object
    priv: RegistryPrivate
    globals: GLib.HashTable
    outputs: GLib.HashTable
    seats: GLib.HashTable


class RegistryClass:
    """"""
    parent_class: GObject.ObjectClass


class RegistryPrivate:
    """"""


class Output(GObject.Object):
    """Represents a display output device and tracks properties associated with it.
This class listens to Wayland `wl_output` and optional `zxdg_output_v1` events if supported by the compositor to maintain accurate state 
information."""

    def get_wl_output(self) -> Wl.Output:
        """Returns the underlying `wl_output` proxy pointer.

:param self: 
:return: """
        pass

    def get_id(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_geometry(self) -> AstalWl.Rectangle:
        """

:param self: 
:return: """
        pass

    def get_physical_width(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_physical_height(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_refresh_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_transform(self) -> AstalWl.OutputTransform:
        """

:param self: 
:return: """
        pass

    def get_subpixel(self) -> AstalWl.OutputSubpixel:
        """

:param self: 
:return: """
        pass

    def get_make(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_model(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_scale(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: OutputPrivate


class OutputClass:
    """"""
    parent_class: GObject.ObjectClass


class OutputPrivate:
    """"""


class Seat(GObject.Object):
    """Wraps the Wayland `wl_seat` interface.
A seat represents a user input device group containing one or more keyboards, pointer devices, or touchscreens. It tracks the seats 
capabilities and compositor-assigned name."""

    def get_wl_seat(self) -> Wl.Seat:
        """Returns the underlying `wl_seat` object.

:param self: 
:return: """
        pass

    def get_id(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_capabilities(self) -> AstalWl.SeatCapabilities:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: SeatPrivate


class SeatClass:
    """"""
    parent_class: GObject.ObjectClass


class SeatPrivate:
    """"""


class Global:
    """Describes a single Wayland global announced by `wl_registry`."""
    name: int
    interface: str
    version: int


class Rectangle:
    """A simple 2D axis-aligned rectangle with integer coordinates.
Used throughout the AstalWl library to represent output geometry, window bounds, and other screen regions."""

    def init_zero(self) -> None:
        """Creates a zero-sized rectangle at position (0,0).

:param self: 
:return: """
        pass

    def copy(self, result: AstalWl.Rectangle=None) -> None:
        """Creates an exact copy of this rectangle.

:param self: 
:param result: 
:return: """
        pass

    def normalize(self) -> None:
        """Normalizes the rectangle to ensure positive width and height.
If width or height are negative, adjusts the origin (x,y) so the rectangle always represents a valid region with top-left origin and 
positive extent.

:param self: 
:return: """
        pass

    @staticmethod
    def intersect(a: AstalWl.Rectangle=None, b: AstalWl.Rectangle=None,
        _result_: AstalWl.Rectangle=None) -> bool:
        """Computes the intersection of two rectangles.
If no intersection exists, `result` is set to a zero rectangle and `false` is returned.

:param a: 
:param b: 
:param _result_: 
:return: """
        pass
    x: int
    y: int
    width: int
    height: int
