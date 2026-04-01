from gi.repository import GObject as GObject

class Urgency:
    LOW: int
    NORMAL: int
    CRITICAL: int

class ClosedReason:
    EXPIRED: int
    DISMISSED_BY_USER: int
    CLOSED: int
    UNDEFINED: int

class State:
    DRAFT: int
    SENT: int
    RECEIVED: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Get the singleton instance of [class@AstalNotifd.Notifd]
    @returns: 
    @rtype: AstalNotifd.Notifd
    """
def send_notification(notification=None, _callback_=None, _callback__target=None):
    """    Send a notification. This function does not depend on Notifd and can be used with any notification server. The [class@
    AstalNotifd.Notification] passed to this function is never the same instance that [method@AstalNotifd.Notifd.get_notification] returns. This 
    function will set the state of the passed notification from `DRAFT` to `SENT` after which the notification can no longer be mutated.
    @type notification: AstalNotifd.Notification
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def send_notification_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: None
    """

class Action(GObject.Object):
    """Notification action."""
    def __init__(self, id=None, label=None) -> None:
        """        
        @type id: str
        @type label: str
        @returns: Newly created Action
        @rtype: Action
        """
    @staticmethod
    def new(id=None, label=None):
        """        
        @type id: str
        @type label: str
        @returns: Newly created Action
        @rtype: Action
        """
    def invoke(self):
        """        Invoke this action. Note that this method just notifies the client that this action was invoked by the user. If for example this notification 
        persists through the lifetime of the sending application this action will have no effect.
        @returns: 
        @rtype: None
        """
    def get_id(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_id(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_label(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_label(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ActionClass:
    @property
    def parent_class(self): ...

class ActionPrivate: ...

class Notifd(GObject.Object):
    """The Notification daemon.
This class queues up to become the next daemon, while acting as a proxy in the meantime."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Notifd
        @rtype: Notifd
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Notifd
        @rtype: Notifd
        """
    @staticmethod
    def get_default():
        """        Get the singleton instance
        @returns: 
        @rtype: AstalNotifd.Notifd
        """
    def get_notification(self, id=None):
        """        Gets the [class@AstalNotifd.Notification] with id or null if there is no such Notification.
        @type id: int
        @returns: 
        @rtype: AstalNotifd.Notification
        """
    def get_ignore_timeout(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_ignore_timeout(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_dont_disturb(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_dont_disturb(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_default_timeout(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_default_timeout(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_notifications(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class NotifdClass:
    @property
    def parent_class(self): ...
    @property
    def notified(self): ...
    @property
    def resolved(self): ...

class NotifdPrivate: ...

class Notification(GObject.Object):
    """Class representing a notification."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Notification
        @rtype: Notification
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Notification
        @rtype: Notification
        """
    def dismiss(self):
        """        Resolve this notification with [enum@AstalNotifd.ClosedReason.DISMISSED_BY_USER].
        @returns: 
        @rtype: None
        """
    def expire(self):
        """        Resolve this notification with [enum@AstalNotifd.ClosedReason.EXPIRED]. Note that there should be no reason to use this method because 
        expiration should be left to the daemon.
        @returns: 
        @rtype: None
        """
    def invoke(self, action_id=None):
        """        Invoke an [class@AstalNotifd.Action] of this notification.
        @type action_id: str
        @returns: 
        @rtype: None
        """
    def add_action(self, action=None):
        """        
        @type action: AstalNotifd.Action
        @returns: 
        @rtype: AstalNotifd.Notification
        """
    def set_hint(self, name=None, value=None):
        """        
        @type name: str
        @type value: GLib.Variant
        @returns: 
        @rtype: AstalNotifd.Notification
        """
    def get_hint(self, name=None):
        """        
        @type name: str
        @returns: 
        @rtype: GLib.Variant
        """
    def get_state(self):
        """        
        @returns: 
        @rtype: AstalNotifd.State
        """
    def get_time(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_id(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_id(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_app_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_app_name(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_app_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_app_icon(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_summary(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_summary(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_body(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_body(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_expire_timeout(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_expire_timeout(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_actions(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_hints(self):
        """        
        @returns: 
        @rtype: GLib.Variant
        """
    def get_image(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_image(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_action_icons(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_action_icons(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_category(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_category(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_desktop_entry(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_desktop_entry(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_resident(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_resident(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_sound_file(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_sound_file(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_sound_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_sound_name(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_suppress_sound(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_suppress_sound(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_transient(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_transient(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_x(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_x(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_y(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_y(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_urgency(self):
        """        
        @returns: 
        @rtype: AstalNotifd.Urgency
        """
    def set_urgency(self, value=None):
        """        
        @type value: AstalNotifd.Urgency
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class NotificationClass:
    @property
    def parent_class(self): ...

class NotificationPrivate: ...
