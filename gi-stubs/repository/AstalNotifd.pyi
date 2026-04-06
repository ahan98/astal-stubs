# -*- coding: utf-8 -*-
from gi.repository import Gio
import typing
from gi.repository import GLib
from gi.repository import AstalNotifd
import enum
from gi.repository import GObject


class Urgency(enum.Enum):
    """"""
    LOW = 0
    NORMAL = 1
    CRITICAL = 2


class ClosedReason(enum.Enum):
    """"""
    EXPIRED = 1
    DISMISSED_BY_USER = 2
    CLOSED = 3
    UNDEFINED = 4


class State(enum.Enum):
    """"""
    DRAFT = 0
    SENT = 1
    RECEIVED = 2


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalNotifd.Notifd:
    """Get the singleton instance of [class@AstalNotifd.Notifd]

:return: """
    pass


def send_notification(notification: AstalNotifd.Notification=None,
    _callback_: Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None
    ) -> None:
    """Send a notification. This function does not depend on Notifd and can be used with any notification server. The [class@
AstalNotifd.Notification] passed to this function is never the same instance that [method@AstalNotifd.Notifd.get_notification] returns. This 
function will set the state of the passed notification from `DRAFT` to `SENT` after which the notification can no longer be mutated.

:param notification: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def send_notification_finish(_res_: Gio.AsyncResult=None) -> None:
    """

:param _res_: 
:return: """
    pass


class Action(GObject.Object):
    """Notification action."""

    def __init__(self, id: str=None, label: str=None) -> None:
        """

:param self: 
:param id: 
:param label: 
:return: """
        pass

    @staticmethod
    def new(id: str=None, label: str=None) -> AstalNotifd.Action:
        """

:param id: 
:param label: 
:return: """
        pass

    def invoke(self) -> None:
        """Invoke this action. Note that this method just notifies the client that this action was invoked by the user. If for example this notification 
persists through the lifetime of the sending application this action will have no effect.

:param self: 
:return: """
        pass

    def get_id(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_id(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_label(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_label(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: ActionPrivate


class ActionClass:
    """"""
    parent_class: GObject.ObjectClass


class ActionPrivate:
    """"""


class Notifd(GObject.Object):
    """The Notification daemon.
This class queues up to become the next daemon, while acting as a proxy in the meantime."""

    @staticmethod
    def get_default() -> AstalNotifd.Notifd:
        """Get the singleton instance

:return: """
        pass

    def get_notification(self, id: int=None) -> AstalNotifd.Notification:
        """Gets the [class@AstalNotifd.Notification] with id or null if there is no such Notification.

:param self: 
:param id: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalNotifd.Notifd:
        """

:return: """
        pass

    def get_ignore_timeout(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_ignore_timeout(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_dont_disturb(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_dont_disturb(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_default_timeout(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_default_timeout(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_notifications(self) -> GLib.List:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: NotifdPrivate


class NotifdClass:
    """"""
    parent_class: GObject.ObjectClass
    notified: typing.Any
    resolved: typing.Any


class NotifdPrivate:
    """"""


class Notification(GObject.Object):
    """Class representing a notification."""

    def dismiss(self) -> None:
        """Resolve this notification with [enum@AstalNotifd.ClosedReason.DISMISSED_BY_USER].

:param self: 
:return: """
        pass

    def expire(self) -> None:
        """Resolve this notification with [enum@AstalNotifd.ClosedReason.EXPIRED]. Note that there should be no reason to use this method because 
expiration should be left to the daemon.

:param self: 
:return: """
        pass

    def invoke(self, action_id: str=None) -> None:
        """Invoke an [class@AstalNotifd.Action] of this notification.

:param self: 
:param action_id: 
:return: """
        pass

    def add_action(self, action: AstalNotifd.Action=None
        ) -> AstalNotifd.Notification:
        """

:param self: 
:param action: 
:return: """
        pass

    def set_hint(self, name: str=None, value: GLib.Variant=None
        ) -> AstalNotifd.Notification:
        """

:param self: 
:param name: 
:param value: 
:return: """
        pass

    def get_hint(self, name: str=None) -> GLib.Variant:
        """

:param self: 
:param name: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalNotifd.Notification:
        """

:return: """
        pass

    def get_state(self) -> AstalNotifd.State:
        """

:param self: 
:return: """
        pass

    def get_time(self) -> int:
        """

:param self: 
:return: """
        pass

    def get_id(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_id(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_app_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_app_name(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_app_icon(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_app_icon(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_summary(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_summary(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_body(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_body(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_expire_timeout(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_expire_timeout(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_actions(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_hints(self) -> GLib.Variant:
        """

:param self: 
:return: """
        pass

    def get_image(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_image(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_action_icons(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_action_icons(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_category(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_category(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_desktop_entry(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_desktop_entry(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_resident(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_resident(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_sound_file(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_sound_file(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_sound_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_sound_name(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_suppress_sound(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_suppress_sound(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_transient(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_transient(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
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

    def get_urgency(self) -> AstalNotifd.Urgency:
        """

:param self: 
:return: """
        pass

    def set_urgency(self, value: AstalNotifd.Urgency=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: NotificationPrivate


class NotificationClass:
    """"""
    parent_class: GObject.ObjectClass


class NotificationPrivate:
    """"""
