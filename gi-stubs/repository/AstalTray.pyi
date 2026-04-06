# -*- coding: utf-8 -*-
from gi.repository import GLib
import typing
from gi.repository import AstalTray
import enum
from gi.repository import Gio
from gi.repository import GObject
from gi.repository import GdkPixbuf


class Category(enum.Enum):
    """"""
    APPLICATION = 0
    COMMUNICATIONS = 1
    SYSTEM = 2
    HARDWARE = 3


def category_to_nick(self) -> str:
    """

:param self: 
:return: """
    pass


def category_from_string(value: str=None) -> AstalTray.Category:
    """

:param value: 
:return: """
    pass


class Status(enum.Enum):
    """"""
    PASSIVE = 0
    ACTIVE = 1
    NEEDS_ATTENTION = 2


def status_to_nick(self) -> str:
    """

:param self: 
:return: """
    pass


def status_from_string(value: str=None) -> AstalTray.Status:
    """

:param value: 
:return: """
    pass


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalTray.Tray:
    """Get the singleton instance of [class@AstalTray.Tray]

:return: """
    pass


class TrayItem(GObject.Object):
    """"""

    def about_to_show(self) -> None:
        """tells the tray app that its menu is about to be opened, so it can update the menu if needed. You should call this method before openening the 
menu.

:param self: 
:return: """
        pass

    def activate(self, x: int=None, y: int=None) -> None:
        """Send an activate request to the tray app.

:param self: 
:param x: 
:param y: 
:return: """
        pass

    def secondary_activate(self, x: int=None, y: int=None) -> None:
        """Send a secondary activate request to the tray app.

:param self: 
:param x: 
:param y: 
:return: """
        pass

    def scroll(self, delta: int=None, orientation: str=None) -> None:
        """Send a scroll request to the tray app. valid values for the orientation are "horizontal" and "vertical".

:param self: 
:param delta: 
:param orientation: 
:return: """
        pass

    def to_json_string(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_title(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_category(self) -> AstalTray.Category:
        """

:param self: 
:return: """
        pass

    def get_status(self) -> AstalTray.Status:
        """

:param self: 
:return: """
        pass

    def get_tooltip(self) -> AstalTray.Tooltip:
        """

:param self: 
:return: """
        pass

    def get_tooltip_markup(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_tooltip_text(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_id(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_is_menu(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_icon_theme_path(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_icon_pixbuf(self) -> GdkPixbuf.Pixbuf:
        """

:param self: 
:return: """
        pass

    def get_gicon(self) -> Gio.Icon:
        """

:param self: 
:return: """
        pass

    def get_item_id(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_menu_path(self) -> GLib.ObjectPath:
        """

:param self: 
:return: """
        pass

    def get_menu_model(self) -> Gio.MenuModel:
        """

:param self: 
:return: """
        pass

    def get_action_group(self) -> Gio.ActionGroup:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: TrayItemPrivate


class TrayItemClass:
    """"""
    parent_class: GObject.ObjectClass


class TrayItemPrivate:
    """"""


class Tray(GObject.Object):
    """"""

    @staticmethod
    def get_default() -> AstalTray.Tray:
        """Get the singleton instance of [class@AstalTray.Tray]

:return: """
        pass

    def get_item(self, item_id: str=None) -> AstalTray.TrayItem:
        """gets the TrayItem with the given item-id.

:param self: 
:param item_id: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalTray.Tray:
        """

:return: """
        pass

    def get_items(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_items_model(self) -> Gio.ListModel:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: TrayPrivate


class TrayClass:
    """"""
    parent_class: GObject.ObjectClass
    item_added: typing.Any
    item_removed: typing.Any


class TrayPrivate:
    """"""


class Pixmap:
    """"""
    width: int
    height: int
    bytes: typing.Any
    bytes_length1: int


class Tooltip:
    """"""
    icon_name: str
    icon: typing.Any
    icon_length1: int
    title: str
    description: str
