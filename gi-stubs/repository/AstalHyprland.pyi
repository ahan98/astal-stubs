from gi.repository import GObject as GObject

class Fullscreen:
    CURRENT: int
    NONE: int
    MAXIMIZED: int
    FULLSCREEN: int

class MonitorTransform:
    NORMAL: int
    ROTATE_90_DEG: int
    ROTATE_180_DEG: int
    ROTATE_270_DEG: int
    FLIPPED: int
    FLIPPED_ROTATE_90_DEG: int
    FLIPPED_ROTATE_180_DEG: int
    FLIPPED_ROTATE_270_DEG: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    
    @returns: 
    @rtype: AstalHyprland.Hyprland
    """

class Client(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Client
        @rtype: Client
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Client
        @rtype: Client
        """
    def kill(self):
        """        
        @returns: 
        @rtype: None
        """
    def focus(self):
        """        
        @returns: 
        @rtype: None
        """
    def move_to(self, ws=None):
        """        
        @type ws: AstalHyprland.Workspace
        @returns: 
        @rtype: None
        """
    def toggle_floating(self):
        """        
        @returns: 
        @rtype: None
        """
    def get_address(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_mapped(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_hidden(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_x(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_y(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_width(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_height(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_workspace(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def get_floating(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_monitor(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Monitor
        """
    def get_class(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_title(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_initial_class(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_initial_title(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_pid(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_xwayland(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_pinned(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_fullscreen(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Fullscreen
        """
    def get_fullscreen_client(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Fullscreen
        """
    def get_swallowing(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_focus_history_id(self):
        """        
        @returns: 
        @rtype: int
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ClientClass:
    @property
    def parent_class(self): ...

class ClientPrivate: ...

class Hyprland(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Hyprland
        @rtype: Hyprland
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Hyprland
        @rtype: Hyprland
        """
    @staticmethod
    def get_default():
        """        
        @returns: 
        @rtype: AstalHyprland.Hyprland
        """
    def get_monitor(self, id=None):
        """        
        @type id: int
        @returns: 
        @rtype: AstalHyprland.Monitor
        """
    def get_workspace(self, id=None):
        """        
        @type id: int
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def get_client(self, address=None):
        """        
        @type address: str
        @returns: 
        @rtype: AstalHyprland.Client
        """
    def get_monitor_by_name(self, name=None):
        """        
        @type name: str
        @returns: 
        @rtype: AstalHyprland.Monitor
        """
    def get_workspace_by_name(self, name=None):
        """        
        @type name: str
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def message(self, message=None):
        """        
        @type message: str
        @returns: 
        @rtype: str
        """
    def message_async(self, message=None, _callback_=None, _callback__target=None):
        """        
        @type message: str
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def message_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: str
        """
    def dispatch(self, dispatcher=None, args=None):
        """        
        @type dispatcher: str
        @type args: str
        @returns: 
        @rtype: None
        """
    def move_cursor(self, x=None, y=None):
        """        
        @type x: int
        @type y: int
        @returns: 
        @rtype: None
        """
    def sync_monitors(self, _callback_=None, _callback__target=None):
        """        
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def sync_monitors_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def sync_workspaces(self, _callback_=None, _callback__target=None):
        """        
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def sync_workspaces_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def sync_clients(self, _callback_=None, _callback__target=None):
        """        
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def sync_clients_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    def get_monitors(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_workspaces(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_clients(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_focused_workspace(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def get_focused_monitor(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Monitor
        """
    def get_focused_client(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Client
        """
    def get_binds(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_cursor_position(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Position
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class HyprlandClass:
    @property
    def parent_class(self): ...

class HyprlandPrivate: ...

class Monitor(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Monitor
        @rtype: Monitor
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Monitor
        @rtype: Monitor
        """
    def focus(self):
        """        
        @returns: 
        @rtype: None
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
    def get_description(self):
        """        
        @returns: 
        @rtype: str
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
    def get_serial(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_width(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_height(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_refresh_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_x(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_y(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_active_workspace(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def get_special_workspace(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Workspace
        """
    def get_reserved_top(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_reserved_bottom(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_reserved_left(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_reserved_right(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_scale(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_transform(self):
        """        
        @returns: 
        @rtype: AstalHyprland.MonitorTransform
        """
    def get_focused(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_dpms_status(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_vrr(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_actively_tearing(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_disabled(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_current_format(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_available_modes(self):
        """        
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class MonitorClass:
    @property
    def parent_class(self): ...

class MonitorPrivate: ...

class Bind(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Bind
        @rtype: Bind
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Bind
        @rtype: Bind
        """
    def get_locked(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_locked(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_mouse(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_mouse(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_release(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_release(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_repeat(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_repeat(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_long_press(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_long_press(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_non_consuming(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_non_consuming(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_has_description(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_has_description(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_modmask(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_modmask(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_submap(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_submap(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_key(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_key(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_keycode(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_keycode(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_catch_all(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_catch_all(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_description(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_dispatcher(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_dispatcher(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_arg(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_arg(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class BindClass:
    @property
    def parent_class(self): ...

class BindPrivate: ...

class Position(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Position
        @rtype: Position
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Position
        @rtype: Position
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
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class PositionClass:
    @property
    def parent_class(self): ...

class PositionPrivate: ...

class Workspace(GObject.Object):
    @staticmethod
    def dummy(id=None, monitor=None):
        """        
        @type id: int
        @type monitor: AstalHyprland.Monitor
        @returns: Newly created Workspace
        @rtype: Workspace
        """
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Workspace
        @rtype: Workspace
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Workspace
        @rtype: Workspace
        """
    def focus(self):
        """        
        @returns: 
        @rtype: None
        """
    def move_to(self, m=None):
        """        
        @type m: AstalHyprland.Monitor
        @returns: 
        @rtype: None
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
    def get_monitor(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Monitor
        """
    def get_clients(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_has_fullscreen(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_last_client(self):
        """        
        @returns: 
        @rtype: AstalHyprland.Client
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class WorkspaceClass:
    @property
    def parent_class(self): ...

class WorkspacePrivate: ...
