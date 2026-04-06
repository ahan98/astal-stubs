# -*- coding: utf-8 -*-
from gi.repository import Gio
from gi.repository import GLib
from gi.repository import GObject
import typing
import enum
from gi.repository import AstalHyprland


class Fullscreen(enum.Enum):
    """"""
    CURRENT = -1
    NONE = 0
    MAXIMIZED = 1
    FULLSCREEN = 2


class MonitorTransform(enum.Enum):
    """"""
    NORMAL = 0
    ROTATE_90_DEG = 1
    ROTATE_180_DEG = 2
    ROTATE_270_DEG = 3
    FLIPPED = 4
    FLIPPED_ROTATE_90_DEG = 5
    FLIPPED_ROTATE_180_DEG = 6
    FLIPPED_ROTATE_270_DEG = 7


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalHyprland.Hyprland:
    """

:return: """
    pass


class Client(GObject.Object):
    """"""

    def kill(self) -> None:
        """

:param self: 
:return: """
        pass

    def focus(self) -> None:
        """

:param self: 
:return: """
        pass

    def move_to(self, ws: AstalHyprland.Workspace=None) -> None:
        """

:param self: 
:param ws: 
:return: """
        pass

    def toggle_floating(self) -> None:
        """

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Client:
        """

:return: """
        pass

    def get_address(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_mapped(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_hidden(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_x(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_y(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_width(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_height(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_workspace(self) -> AstalHyprland.Workspace:
        """

:param self: 
:return: """
        pass

    def get_floating(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_monitor(self) -> AstalHyprland.Monitor:
        """

:param self: 
:return: """
        pass

    def get_class(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_title(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_initial_class(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_initial_title(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_pid(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_xwayland(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_pinned(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_fullscreen(self) -> AstalHyprland.Fullscreen:
        """

:param self: 
:return: """
        pass

    def get_fullscreen_client(self) -> AstalHyprland.Fullscreen:
        """

:param self: 
:return: """
        pass

    def get_swallowing(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_focus_history_id(self) -> int:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: ClientPrivate


class ClientClass:
    """"""
    parent_class: GObject.ObjectClass


class ClientPrivate:
    """"""


class Hyprland(GObject.Object):
    """"""

    @staticmethod
    def get_default() -> AstalHyprland.Hyprland:
        """

:return: """
        pass

    def get_monitor(self, id: int=None) -> AstalHyprland.Monitor:
        """

:param self: 
:param id: 
:return: """
        pass

    def get_workspace(self, id: int=None) -> AstalHyprland.Workspace:
        """

:param self: 
:param id: 
:return: """
        pass

    def get_client(self, address: str=None) -> AstalHyprland.Client:
        """

:param self: 
:param address: 
:return: """
        pass

    def get_monitor_by_name(self, name: str=None) -> AstalHyprland.Monitor:
        """

:param self: 
:param name: 
:return: """
        pass

    def get_workspace_by_name(self, name: str=None) -> AstalHyprland.Workspace:
        """

:param self: 
:param name: 
:return: """
        pass

    def message(self, message: str=None) -> str:
        """

:param self: 
:param message: 
:return: """
        pass

    def message_async(self, message: str=None, _callback_:
        Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None
        ) -> None:
        """

:param self: 
:param message: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def message_finish(self, _res_: Gio.AsyncResult=None) -> str:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def dispatch(self, dispatcher: str=None, args: str=None) -> None:
        """

:param self: 
:param dispatcher: 
:param args: 
:return: """
        pass

    def move_cursor(self, x: int=None, y: int=None) -> None:
        """

:param self: 
:param x: 
:param y: 
:return: """
        pass

    def sync_monitors(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def sync_monitors_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def sync_workspaces(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def sync_workspaces_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def sync_clients(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def sync_clients_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Hyprland:
        """

:return: """
        pass

    def get_monitors(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_workspaces(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_clients(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_focused_workspace(self) -> AstalHyprland.Workspace:
        """

:param self: 
:return: """
        pass

    def get_focused_monitor(self) -> AstalHyprland.Monitor:
        """

:param self: 
:return: """
        pass

    def get_focused_client(self) -> AstalHyprland.Client:
        """

:param self: 
:return: """
        pass

    def get_binds(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_cursor_position(self) -> AstalHyprland.Position:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: HyprlandPrivate


class HyprlandClass:
    """"""
    parent_class: GObject.ObjectClass


class HyprlandPrivate:
    """"""


class Monitor(GObject.Object):
    """"""

    def focus(self) -> None:
        """

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Monitor:
        """

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

    def get_description(self) -> str:
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

    def get_serial(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_width(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_height(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_refresh_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_x(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_y(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_active_workspace(self) -> AstalHyprland.Workspace:
        """

:param self: 
:return: """
        pass

    def get_special_workspace(self) -> AstalHyprland.Workspace:
        """

:param self: 
:return: """
        pass

    def get_reserved_top(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_reserved_bottom(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_reserved_left(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_reserved_right(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_scale(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_transform(self) -> AstalHyprland.MonitorTransform:
        """

:param self: 
:return: """
        pass

    def get_focused(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_dpms_status(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_vrr(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_actively_tearing(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_disabled(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_current_format(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_available_modes(self) -> typing.Any:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: MonitorPrivate


class MonitorClass:
    """"""
    parent_class: GObject.ObjectClass


class MonitorPrivate:
    """"""


class Bind(GObject.Object):
    """"""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Bind:
        """

:return: """
        pass

    def get_locked(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_locked(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_mouse(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_mouse(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_release(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_release(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_repeat(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_repeat(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_long_press(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_long_press(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_non_consuming(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_non_consuming(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_has_description(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_has_description(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_modmask(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_modmask(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_submap(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_submap(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_key(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_key(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_keycode(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_keycode(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_catch_all(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_catch_all(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_description(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_dispatcher(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_dispatcher(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_arg(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_arg(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: BindPrivate


class BindClass:
    """"""
    parent_class: GObject.ObjectClass


class BindPrivate:
    """"""


class Position(GObject.Object):
    """"""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Position:
        """

:return: """
        pass

    def get_x(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_x(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_y(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_y(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: PositionPrivate


class PositionClass:
    """"""
    parent_class: GObject.ObjectClass


class PositionPrivate:
    """"""


class Workspace(GObject.Object):
    """"""

    @staticmethod
    def dummy(id: int=None, monitor: AstalHyprland.Monitor=None
        ) -> AstalHyprland.Workspace:
        """

:param id: 
:param monitor: 
:return: """
        pass

    def focus(self) -> None:
        """

:param self: 
:return: """
        pass

    def move_to(self, m: AstalHyprland.Monitor=None) -> None:
        """

:param self: 
:param m: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalHyprland.Workspace:
        """

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

    def get_monitor(self) -> AstalHyprland.Monitor:
        """

:param self: 
:return: """
        pass

    def get_clients(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_has_fullscreen(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_last_client(self) -> AstalHyprland.Client:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: WorkspacePrivate
    _clients: GLib.List


class WorkspaceClass:
    """"""
    parent_class: GObject.ObjectClass


class WorkspacePrivate:
    """"""
