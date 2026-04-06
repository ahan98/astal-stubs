# -*- coding: utf-8 -*-
import typing
from gi.repository import AstalRiver
from gi.repository import AstalWl
from gi.repository import GLib
from gi.repository import Gio
from gi.repository import Wl
from gi.repository import GObject
MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def is_supported() -> bool:
    """

:return: """
    pass


def get_default() -> AstalRiver.River:
    """Returns the singleton River instance.

:return: """
    pass


class River(GObject.Object):
    """This class creates a connection to the river compositor."""

    @staticmethod
    def get_default() -> AstalRiver.River:
        """Returns the singleton River instance.

:return: """
        pass

    def find_output_by_wl_output(self, wl_output: Wl.Output=None
        ) -> AstalRiver.Output:
        """Looks up an output based on its underlying wl_output object.

:param self: 
:param wl_output: 
:return: """
        pass

    def find_output_by_astal_wl_output(self, wl_output: AstalWl.Output=None
        ) -> AstalRiver.Output:
        """Looks up an output based on its underlying [class@AstalWl.Output] object.

:param self: 
:param wl_output: 
:return: """
        pass

    def find_output_by_name(self, name: str=None) -> AstalRiver.Output:
        """Looks up an output based on its underlying name.

:param self: 
:param name: 
:return: """
        pass

    def find_output_by_id(self, id: int=None) -> AstalRiver.Output:
        """Looks up an output based on its underlying wayland id.

:param self: 
:param id: 
:return: """
        pass

    def run_command(self, cmd: typing.Any=None, cmd_length1: int=None,
        output: str=None) -> bool:
        """executes a given command, similar to riverctl.

:param self: 
:param cmd: 
:param cmd_length1: 
:param output: 
:return: """
        pass

    def run_command_async(self, cmd: typing.Any=None, cmd_length1: int=None,
        _callback_: Gio.AsyncReadyCallback=None, _callback__target:
        typing.Any=None) -> None:
        """executes a given command, similar to riverctl.

:param self: 
:param cmd: 
:param cmd_length1: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def run_command_finish(self, _res_: Gio.AsyncResult=None, output: str=None
        ) -> bool:
        """

:param self: 
:param _res_: 
:param output: 
:return: """
        pass

    def new_layout(self, namespace: str=None) -> AstalRiver.Layout:
        """creates a new Layout object with a given namespace.

:param self: 
:param namespace: 
:return: """
        pass

    def __init__(self) -> None:
        """Creates a new River object. It is recommended to use the [func@AstalRiver.get_default] method instead of this method.

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalRiver.River:
        """Creates a new River object. It is recommended to use the [func@AstalRiver.get_default] method instead of this method.

:return: """
        pass

    def get_outputs(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_focused_output(self) -> AstalRiver.Output:
        """

:param self: 
:return: """
        pass

    def get_focused_output_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_focused_view(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_mode(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: RiverPrivate


class RiverClass:
    """"""
    parent_class: GObject.ObjectClass


class RiverPrivate:
    """"""


class Output(GObject.Object):
    """Represents a display output device."""

    def get_output(self) -> AstalWl.Output:
        """

:param self: 
:return: """
        pass

    def get_focused_tags(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_focused_tags(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_occupied_tags(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_urgent_tags(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_focused_view(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_layout_name(self) -> str:
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


class LayoutDemandResult(GObject.Object):
    """"""

    def __init__(self, layout_name: str=None, rectangles: GLib.List=None
        ) -> None:
        """

:param self: 
:param layout_name: 
:param rectangles: 
:return: """
        pass

    @staticmethod
    def new(layout_name: str=None, rectangles: GLib.List=None
        ) -> AstalRiver.LayoutDemandResult:
        """

:param layout_name: 
:param rectangles: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: LayoutDemandResultPrivate
    layout_name: str
    rectangles: GLib.List


class LayoutDemandResultClass:
    """"""
    parent_class: GObject.ObjectClass


class LayoutDemandResultPrivate:
    """"""


class Layout(GObject.Object):
    """Allows implementing a custom windows Layout generator."""

    def set_layout_demand_closure(self, closure: GObject.Closure=None) -> None:
        """Sets the Closure to be called when a new layout is requested. The Closure is of type [callback@AstalRiver.LayoutDemandCallback].
The Closure must return a [class@AstalRiver.LayoutDemandResult] containing exactly as many [struct@AstalWl.Rectangle] objects as 
requested. Each rectangle represents the position and size of each window. Before the result is applied, each rectangle is croped to ensure it lies 
entirely within the usable area.

:param self: 
:param closure: 
:return: """
        pass

    def get_namespace(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: LayoutPrivate
    layout_demand_closure: GObject.Closure


class LayoutClass:
    """"""
    parent_class: GObject.ObjectClass


class LayoutPrivate:
    """"""
