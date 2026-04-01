from gi.repository import GObject as GObject

class OutputSubpixel:
    """This enumeration describes how the physical pixels on an output are laid out."""
    UNKNOWN: int
    NONE: int
    HORIZONTAL_RGB: int
    HORIZONTAL_BGR: int
    VERTICAL_RGB: int
    VERTICAL_BGR: int

class OutputTransform:
    """This describes transformations that clients and compositors apply to buffer contents. The flipped values correspond to an initial flip around a 
vertical axis followed by rotation."""
    NORMAL: int
    ROTATE_90: int
    ROTATE_180: int
    ROTATE_270: int
    FLIPPED: int
    FLIPPED_90: int
    FLIPPED_180: int
    FLIPPED_270: int

class SeatCapabilities:
    """Bitfield flags describing the input capabilities of this seat."""
    POINTER: int
    KEYBOARD: int
    TOUCH: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Convenience wrapper for [func@AstalWl.Registry.get_default].
    Returns the singleton `Registry` instance that tracks all known globals, outputs, and seats on the connected Wayland display.
    @returns: 
    @rtype: AstalWl.Registry
    """

class Registry(GObject.Object):
    """Wraps the Wayland `wl_registry` interface and keeps track of all announced globals, outputs and seats.
It exposes high-level collections and lookup helpers and emits signals when globals, outputs or seats are added or removed."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Registry
        @rtype: Registry
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Registry
        @rtype: Registry
        """
    @staticmethod
    def get_default():
        """        Returns the singleton `Registry` instance.
        The first call connects to the Wayland display and sets up the underlying `wl_registry` listener.
        @returns: 
        @rtype: AstalWl.Registry
        """
    def get_globals(self):
        """        Returns a list of all known globals.
        @returns: 
        @rtype: GLib.List
        """
    def get_outputs(self):
        """        Returns a list of all known outputs.
        @returns: 
        @rtype: GLib.List
        """
    def get_seats(self):
        """        Returns a list of all known seats.
        @returns: 
        @rtype: GLib.List
        """
    def get_registry(self):
        """        Returns the underlying `wl_registry` object.
        @returns: 
        @rtype: Wl.Registry
        """
    def get_display(self):
        """        Returns the underlying `wl_display` used by this registry.
        @returns: 
        @rtype: Wl.Display
        """
    def find_globals(self, interface=None):
        """        Returns a list of globals, optionally filtered by interface name. If `null` is passed, all globals are returned.
        @type interface: str
        @returns: 
        @rtype: GLib.List
        """
    def get_global_by_id(self, id=None):
        """        Looks up a global by its numeric Iid.
        @type id: int
        @returns: 
        @rtype: AstalWl.Global
        """
    def get_output_by_id(self, id=None):
        """        Looks up an output by its global id.
        @type id: int
        @returns: 
        @rtype: AstalWl.Output
        """
    def get_output_by_name(self, name=None):
        """        Looks up an output by its compositor-assigned name.
        @type name: str
        @returns: 
        @rtype: AstalWl.Output
        """
    def get_output_by_wl_output(self, wl_output=None):
        """        Looks up an `Output` by its underlying `wl_output`.
        @type wl_output: Wl.Output
        @returns: 
        @rtype: AstalWl.Output
        """
    def get_seat_by_id(self, id=None):
        """        Looks up a seat by its global id.
        @type id: int
        @returns: 
        @rtype: AstalWl.Seat
        """
    def get_seat_by_name(self, name=None):
        """        Looks up a seat by its compositor-assigned name.
        @type name: str
        @returns: 
        @rtype: AstalWl.Seat
        """
    def get_seat_by_wl_seat(self, wl_seat=None):
        """        Looks up a `Seat` by its underlying `wl_seat`.
        @type wl_seat: Wl.Seat
        @returns: 
        @rtype: AstalWl.Seat
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...
    @property
    def globals(self): ...
    @property
    def outputs(self): ...
    @property
    def seats(self): ...

class RegistryClass:
    @property
    def parent_class(self): ...

class RegistryPrivate: ...

class Output(GObject.Object):
    """Represents a display output device and tracks properties associated with it.
This class listens to Wayland `wl_output` and optional `zxdg_output_v1` events if supported by the compositor to maintain accurate state 
information."""
    def get_wl_output(self):
        """        Returns the underlying `wl_output` proxy pointer.
        @returns: 
        @rtype: Wl.Output
        """
    def get_id(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_geometry(self):
        """        
        @returns: 
        @rtype: AstalWl.Rectangle
        """
    def get_physical_width(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_physical_height(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_refresh_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_transform(self):
        """        
        @returns: 
        @rtype: AstalWl.OutputTransform
        """
    def get_subpixel(self):
        """        
        @returns: 
        @rtype: AstalWl.OutputSubpixel
        """
    def get_make(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_model(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_scale(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class OutputClass:
    @property
    def parent_class(self): ...

class OutputPrivate: ...

class Seat(GObject.Object):
    """Wraps the Wayland `wl_seat` interface.
A seat represents a user input device group containing one or more keyboards, pointer devices, or touchscreens. It tracks the seats 
capabilities and compositor-assigned name."""
    def get_wl_seat(self):
        """        Returns the underlying `wl_seat` object.
        @returns: 
        @rtype: Wl.Seat
        """
    def get_id(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_capabilities(self):
        """        
        @returns: 
        @rtype: AstalWl.SeatCapabilities
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class SeatClass:
    @property
    def parent_class(self): ...

class SeatPrivate: ...

class Global:
    """Describes a single Wayland global announced by `wl_registry`."""
    @property
    def name(self): ...
    @property
    def interface(self): ...
    @property
    def version(self): ...

class Rectangle:
    """A simple 2D axis-aligned rectangle with integer coordinates.
Used throughout the AstalWl library to represent output geometry, window bounds, and other screen regions."""
    def init_zero(self):
        """        Creates a zero-sized rectangle at position (0,0).
        @returns: 
        @rtype: None
        """
    def copy(self, result=None):
        """        Creates an exact copy of this rectangle.
        @type result: AstalWl.Rectangle
        @returns: 
        @rtype: None
        """
    def normalize(self):
        """        Normalizes the rectangle to ensure positive width and height.
        If width or height are negative, adjusts the origin (x,y) so the rectangle always represents a valid region with top-left origin and 
        positive extent.
        @returns: 
        @rtype: None
        """
    @staticmethod
    def intersect(a=None, b=None, _result_=None):
        """        Computes the intersection of two rectangles.
        If no intersection exists, `result` is set to a zero rectangle and `false` is returned.
        @type a: AstalWl.Rectangle
        @type b: AstalWl.Rectangle
        @type _result_: AstalWl.Rectangle
        @returns: 
        @rtype: bool
        """
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def width(self): ...
    @property
    def height(self): ...
