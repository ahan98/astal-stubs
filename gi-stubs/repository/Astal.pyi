# -*- coding: utf-8 -*-
from gi.repository import GLib
import typing
from gi.repository import Gtk
from gi.repository import Gio
from gi.repository import Gdk
import enum
from gi.repository import AstalIO
from gi.repository import Astal


class WindowAnchor(enum.Enum):
    """"""
    NONE = 1
    TOP = 2
    RIGHT = 4
    LEFT = 8
    BOTTOM = 16


class Exclusivity(enum.Enum):
    """"""
    NORMAL = 0
    EXCLUSIVE = 1
    IGNORE = 2


class Layer(enum.Enum):
    """"""
    BACKGROUND = 0
    BOTTOM = 1
    TOP = 2
    OVERLAY = 3


class Keymode(enum.Enum):
    """"""
    NONE = 0
    EXCLUSIVE = 1
    ON_DEMAND = 2


MAJOR_VERSION = '4'
MINOR_VERSION = '0'
MICRO_VERSION = '0'
VERSION = '4.0.0'


class Bin(Gtk.Widget, Gtk.Buildable):
    """A widget with one child. It is useful for deriving subclasses, since it provides common code needed for handling a single child widget."""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Astal.Bin:
        """

:return: """
        pass

    def get_child(self) -> Gtk.Widget:
        """

:param self: 
:return: """
        pass

    def set_child(self, value: Gtk.Widget=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: Gtk.Widget
    priv: BinPrivate


class BinClass:
    """"""
    parent_class: Gtk.WidgetClass


class BinPrivate:
    """"""


class Box(Gtk.Box):
    """"""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Astal.Box:
        """

:return: """
        pass

    def get_vertical(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_vertical(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_children(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def set_children(self, value: GLib.List=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_child(self) -> Gtk.Widget:
        """

:param self: 
:return: """
        pass

    def set_child(self, value: Gtk.Widget=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: Gtk.Box
    priv: BoxPrivate


class BoxClass:
    """"""
    parent_class: Gtk.BoxClass


class BoxPrivate:
    """"""


class Slider(Gtk.Scale):
    """"""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Astal.Slider:
        """

:return: """
        pass

    def get_value(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_value(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_min(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_min(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_max(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_max(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_step(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_step(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_page(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_page(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: Gtk.Scale
    priv: SliderPrivate


class SliderClass:
    """"""
    parent_class: Gtk.ScaleClass


class SliderPrivate:
    """"""


class Window(Gtk.Window):
    """Subclass of [class@Gtk.Window] which integrates GtkLayerShell as class fields."""

    def get_current_monitor(self) -> Gdk.Monitor:
        """Get the current [class@Gdk.Monitor] this window resides in.

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Astal.Window:
        """

:return: """
        pass

    def get_namespace(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_namespace(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_anchor(self) -> Astal.WindowAnchor:
        """

:param self: 
:return: """
        pass

    def set_anchor(self, value: Astal.WindowAnchor=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_exclusivity(self) -> Astal.Exclusivity:
        """

:param self: 
:return: """
        pass

    def set_exclusivity(self, value: Astal.Exclusivity=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_layer(self) -> Astal.Layer:
        """

:param self: 
:return: """
        pass

    def set_layer(self, value: Astal.Layer=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_keymode(self) -> Astal.Keymode:
        """

:param self: 
:return: """
        pass

    def set_keymode(self, value: Astal.Keymode=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_gdkmonitor(self) -> Gdk.Monitor:
        """

:param self: 
:return: """
        pass

    def set_gdkmonitor(self, value: Gdk.Monitor=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_margin_top(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_margin_top(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_margin_bottom(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_margin_bottom(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_margin_left(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_margin_left(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_margin_right(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_margin_right(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def set_margin(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_monitor(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_monitor(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: Gtk.Window
    priv: WindowPrivate


class WindowClass:
    """"""
    parent_class: Gtk.WindowClass


class WindowPrivate:
    """"""


class Application(Gtk.Application, AstalIO.Application):
    """"""

    def reset_css(self) -> None:
        """Remove all [class@Gtk.StyleContext] providers.

:param self: 
:return: """
        pass

    def get_window(self, name: str=None) -> Gtk.Window:
        """Get a window by its [property@Gtk.Widget:name] that has been added to this app using [method@Gtk.Application.add_window].

:param self: 
:param name: 
:return: """
        pass

    def apply_css(self, style: str=None, reset: bool=None) -> None:
        """Add a new [class@Gtk.StyleContext] provider.

:param self: 
:param style: Css string or a path to a css file.
:param reset: 
:return: """
        pass

    def add_icons(self, path: str=None) -> None:
        """Shortcut for [method@Gtk.IconTheme.add_search_path].

:param self: 
:param path: 
:return: """
        pass

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """Handler for an incoming request.

:param self: 
:param request: Body of the request
:param conn: The connection which expects the response.
:return: """
        pass

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """Handler for an incoming request.

:param self: 
:param request: Body of the request
:param conn: The connection which expects the response.
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> Astal.Application:
        """

:return: """
        pass

    def get_monitors(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_windows(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_gtk_theme(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_gtk_theme(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_icon_theme(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_icon_theme(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_cursor_theme(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_cursor_theme(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: Gtk.Application
    priv: ApplicationPrivate


class ApplicationClass:
    """"""
    parent_class: Gtk.ApplicationClass
    request: typing.Any


class ApplicationPrivate:
    """"""
