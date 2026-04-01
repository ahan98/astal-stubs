from gi.repository import AstalIO as AstalIO, Gtk as Gtk

class MouseButton:
    PRIMARY: int
    MIDDLE: int
    SECONDARY: int
    BACK: int
    FORWARD: int

class WindowAnchor:
    NONE: int
    TOP: int
    RIGHT: int
    LEFT: int
    BOTTOM: int

class Exclusivity:
    NORMAL: int
    EXCLUSIVE: int
    IGNORE: int

class Layer:
    BACKGROUND: int
    BOTTOM: int
    TOP: int
    OVERLAY: int

class Keymode:
    NONE: int
    EXCLUSIVE: int
    ON_DEMAND: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def widget_set_css(widget=None, css=None):
    """    
    @type widget: Gtk.Widget
    @type css: str
    @returns: 
    @rtype: None
    """
def widget_get_css(widget=None):
    """    
    @type widget: Gtk.Widget
    @returns: 
    @rtype: str
    """
def widget_set_class_names(widget=None, class_names=None, class_names_length1=None):
    """    
    @type widget: Gtk.Widget
    @type class_names_length1: int
    @returns: 
    @rtype: None
    """
def widget_get_class_names(widget=None):
    """    
    @type widget: Gtk.Widget
    @returns: 
    @rtype: GLib.List
    """
def widget_toggle_class_name(widget=None, class_name=None, condition=None):
    """    
    @type widget: Gtk.Widget
    @type class_name: str
    @type condition: bool
    @returns: 
    @rtype: None
    """
def widget_set_cursor(widget=None, cursor=None):
    """    
    @type widget: Gtk.Widget
    @type cursor: str
    @returns: 
    @rtype: None
    """
def widget_get_cursor(widget=None):
    """    
    @type widget: Gtk.Widget
    @returns: 
    @rtype: str
    """
def widget_set_click_through(widget=None, click_through=None):
    """    
    @type widget: Gtk.Widget
    @type click_through: bool
    @returns: 
    @rtype: None
    """
def widget_get_click_through(widget=None):
    """    
    @type widget: Gtk.Widget
    @returns: 
    @rtype: bool
    """

class Box(Gtk.Box):
    def __init__(self, vertical=None, children=None) -> None:
        """        
        @type vertical: bool
        @type children: GLib.List
        @returns: Newly created Box
        @rtype: Box
        """
    @staticmethod
    def new(vertical=None, children=None):
        """        
        @type vertical: bool
        @type children: GLib.List
        @returns: Newly created Box
        @rtype: Box
        """
    def get_vertical(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_vertical(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_children(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def set_children(self, value=None):
        """        
        @type value: GLib.List
        @returns: 
        @rtype: None
        """
    def get_child(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_child(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class BoxClass:
    @property
    def parent_class(self): ...

class BoxPrivate: ...

class Button(Gtk.Button):
    """This button has no extra functionality on top if its base [class@Gtk.Button] class.
The purpose of this Button subclass is to have a destructable struct as the argument in GJS event handlers."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Button
        @rtype: Button
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Button
        @rtype: Button
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ButtonClass:
    @property
    def parent_class(self): ...

class ButtonPrivate: ...

class CenterBox(Gtk.Box, Gtk.Buildable):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created CenterBox
        @rtype: CenterBox
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created CenterBox
        @rtype: CenterBox
        """
    def get_vertical(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_vertical(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_start_widget(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_start_widget(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    def get_end_widget(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_end_widget(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    def get_center_widget(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_center_widget(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class CenterBoxClass:
    @property
    def parent_class(self): ...

class CenterBoxPrivate: ...

class CircularProgress(Gtk.Bin):
    """CircularProgress is a subclass of [class@Gtk.Bin] which provides a circular progress bar with customizable properties such as starting 
and ending points, progress value, and visual features like rounded ends and inversion of progress direction."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created CircularProgress
        @rtype: CircularProgress
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created CircularProgress
        @rtype: CircularProgress
        """
    def get_start_at(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_start_at(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_end_at(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_end_at(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_value(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_value(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_inverted(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_inverted(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_rounded(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_rounded(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class CircularProgressClass:
    @property
    def parent_class(self): ...

class CircularProgressPrivate: ...

class EventBox(Gtk.EventBox):
    """EventBox is a [class@Gtk.EventBox] subclass which is meant to fix an issue with its [signal@Gtk.Widget::enter_notify_event] and 
[signal@Gtk.Widget::leave_notify_event] when nesting EventBoxes
Its css selector is `eventbox`."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created EventBox
        @rtype: EventBox
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created EventBox
        @rtype: EventBox
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class EventBoxClass:
    @property
    def parent_class(self): ...

class EventBoxPrivate: ...

class Icon(Gtk.Image):
    """[class@Gtk.Image] subclass meant to be used only for icons.
It's size is calculated from `font-size` css property. Its css selector is `icon`."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Icon
        @rtype: Icon
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Icon
        @rtype: Icon
        """
    @staticmethod
    def lookup_icon(icon=None):
        """        
        @type icon: str
        @returns: 
        @rtype: Gtk.IconInfo
        """
    def get_pixbuf(self):
        """        
        @returns: 
        @rtype: GdkPixbuf.Pixbuf
        """
    def set_pixbuf(self, value=None):
        """        
        @type value: GdkPixbuf.Pixbuf
        @returns: 
        @rtype: None
        """
    def get_g_icon(self):
        """        
        @returns: 
        @rtype: Gio.Icon
        """
    def set_g_icon(self, value=None):
        """        
        @type value: Gio.Icon
        @returns: 
        @rtype: None
        """
    def get_icon(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_icon(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class IconClass:
    @property
    def parent_class(self): ...

class IconPrivate: ...

class Label(Gtk.Label):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Label
        @rtype: Label
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Label
        @rtype: Label
        """
    def get_truncate(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_truncate(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_justify_fill(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_justify_fill(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class LabelClass:
    @property
    def parent_class(self): ...

class LabelPrivate: ...

class LevelBar(Gtk.LevelBar):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created LevelBar
        @rtype: LevelBar
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created LevelBar
        @rtype: LevelBar
        """
    def get_vertical(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_vertical(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class LevelBarClass:
    @property
    def parent_class(self): ...

class LevelBarPrivate: ...

class Overlay(Gtk.Overlay):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Overlay
        @rtype: Overlay
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Overlay
        @rtype: Overlay
        """
    def add_overlay(self, widget=None):
        """        
        @type widget: Gtk.Widget
        @returns: 
        @rtype: None
        """
    def get_pass_through(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_pass_through(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_overlay(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_overlay(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    def get_overlays(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def set_overlays(self, value=None):
        """        
        @type value: GLib.List
        @returns: 
        @rtype: None
        """
    def get_child(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def set_child(self, value=None):
        """        
        @type value: Gtk.Widget
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class OverlayClass:
    @property
    def parent_class(self): ...

class OverlayPrivate: ...

class Scrollable(Gtk.ScrolledWindow):
    """Subclass of [class@Gtk.ScrolledWindow] which has its policy default to [enum@Gtk.PolicyType.AUTOMATIC].
Its css selector is `scrollable`. Its child getter returns the child of the inner [class@Gtk.Viewport], instead of the viewport."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Scrollable
        @rtype: Scrollable
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Scrollable
        @rtype: Scrollable
        """
    def get_child(self):
        """        
        @returns: 
        @rtype: Gtk.Widget
        """
    def get_hscroll(self):
        """        
        @returns: 
        @rtype: Gtk.PolicyType
        """
    def set_hscroll(self, value=None):
        """        
        @type value: Gtk.PolicyType
        @returns: 
        @rtype: None
        """
    def get_vscroll(self):
        """        
        @returns: 
        @rtype: Gtk.PolicyType
        """
    def set_vscroll(self, value=None):
        """        
        @type value: Gtk.PolicyType
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ScrollableClass:
    @property
    def parent_class(self): ...

class ScrollablePrivate: ...

class Slider(Gtk.Scale):
    """Subclass of [class@Gtk.Scale] which adds a signal and property for the drag state."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Slider
        @rtype: Slider
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Slider
        @rtype: Slider
        """
    def get_vertical(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_vertical(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_dragging(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_value(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_value(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_min(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_min(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_max(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_max(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_step(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_step(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_page(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_page(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class SliderClass:
    @property
    def parent_class(self): ...

class SliderPrivate: ...

class Stack(Gtk.Stack):
    """Subclass of [class@Gtk.Stack] that has a children setter which invokes [method@Gt.Stack.add_named] with the child's [property
@Gtk.Widget:name] property."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Stack
        @rtype: Stack
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Stack
        @rtype: Stack
        """
    def get_shown(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_shown(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_children(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def set_children(self, value=None):
        """        
        @type value: GLib.List
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class StackClass:
    @property
    def parent_class(self): ...

class StackPrivate: ...

class Window(Gtk.Window):
    """Subclass of [class@Gtk.Window] which integrates GtkLayerShell as class fields."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Window
        @rtype: Window
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Window
        @rtype: Window
        """
    def get_current_monitor(self):
        """        Get the current [class@Gdk.Monitor] this window resides in.
        @returns: 
        @rtype: Gdk.Monitor
        """
    def get_inhibit(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_inhibit(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_namespace(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_namespace(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_anchor(self):
        """        
        @returns: 
        @rtype: Astal.WindowAnchor
        """
    def set_anchor(self, value=None):
        """        
        @type value: Astal.WindowAnchor
        @returns: 
        @rtype: None
        """
    def get_exclusivity(self):
        """        
        @returns: 
        @rtype: Astal.Exclusivity
        """
    def set_exclusivity(self, value=None):
        """        
        @type value: Astal.Exclusivity
        @returns: 
        @rtype: None
        """
    def get_layer(self):
        """        
        @returns: 
        @rtype: Astal.Layer
        """
    def set_layer(self, value=None):
        """        
        @type value: Astal.Layer
        @returns: 
        @rtype: None
        """
    def get_keymode(self):
        """        
        @returns: 
        @rtype: Astal.Keymode
        """
    def set_keymode(self, value=None):
        """        
        @type value: Astal.Keymode
        @returns: 
        @rtype: None
        """
    def get_gdkmonitor(self):
        """        
        @returns: 
        @rtype: Gdk.Monitor
        """
    def set_gdkmonitor(self, value=None):
        """        
        @type value: Gdk.Monitor
        @returns: 
        @rtype: None
        """
    def get_margin_top(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_margin_top(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_margin_bottom(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_margin_bottom(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_margin_left(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_margin_left(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_margin_right(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_margin_right(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def set_margin(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_monitor(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_monitor(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class WindowClass:
    @property
    def parent_class(self): ...

class WindowPrivate: ...

class Application(Gtk.Application, AstalIO.Application):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Application
        @rtype: Application
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Application
        @rtype: Application
        """
    def reset_css(self):
        """        Remove all [class@Gtk.StyleContext] providers.
        @returns: 
        @rtype: None
        """
    def get_window(self, name=None):
        """        Get a window by its [property@Gtk.Widget:name] that has been added to this app using [method@Gtk.Application.add_window].
        @type name: str
        @returns: 
        @rtype: Gtk.Window
        """
    def apply_css(self, style=None, reset=None):
        """        Add a new [class@Gtk.StyleContext] provider.
        @param style: Css string or a path to a css file.
        @type style: str
        @type reset: bool
        @returns: 
        @rtype: None
        """
    def add_icons(self, path=None):
        """        Shortcut for [method@Gtk.IconTheme.prepend_search_path].
        @type path: str
        @returns: 
        @rtype: None
        """
    def request(self, request=None, conn=None):
        """        Handler for an incoming request.
        @param request: Body of the request
        @param conn: The connection which expects the response.
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    def request(self, request=None, conn=None):
        """        Handler for an incoming request.
        @param request: Body of the request
        @param conn: The connection which expects the response.
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    def get_monitors(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_windows(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_gtk_theme(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_gtk_theme(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_icon_theme(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_icon_theme(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_cursor_theme(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_cursor_theme(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ApplicationClass:
    @property
    def parent_class(self): ...
    @property
    def request(self): ...

class ApplicationPrivate: ...

class ClickEvent:
    """Struct for [struct@Gdk.EventButton]"""
    def init(self, event=None):
        """        
        @type event: Gdk.EventButton
        @returns: 
        @rtype: None
        """
    @property
    def release(self): ...
    @property
    def time(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def modifier(self): ...
    @property
    def button(self): ...

class HoverEvent:
    """Struct for [struct@Gdk.EventCrossing]"""
    def init(self, event=None):
        """        
        @type event: Gdk.EventCrossing
        @returns: 
        @rtype: None
        """
    @property
    def lost(self): ...
    @property
    def time(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def modifier(self): ...
    @property
    def mode(self): ...
    @property
    def detail(self): ...

class ScrollEvent:
    """Struct for [struct@Gdk.EventScroll]"""
    def init(self, event=None):
        """        
        @type event: Gdk.EventScroll
        @returns: 
        @rtype: None
        """
    @property
    def time(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def modifier(self): ...
    @property
    def direction(self): ...
    @property
    def delta_x(self): ...
    @property
    def delta_y(self): ...

class MotionEvent:
    """Struct for [struct@Gdk.EventMotion]"""
    def init(self, event=None):
        """        
        @type event: Gdk.EventMotion
        @returns: 
        @rtype: None
        """
    @property
    def time(self): ...
    @property
    def x(self): ...
    @property
    def y(self): ...
    @property
    def modifier(self): ...
