from gi.repository import GObject as GObject

class Category:
    APPLICATION: int
    COMMUNICATIONS: int
    SYSTEM: int
    HARDWARE: int

def category_to_nick(self):
    """    
    @returns: 
    @rtype: str
    """
def category_from_string(value=None):
    """    
    @type value: str
    @returns: 
    @rtype: AstalTray.Category
    """

class Status:
    PASSIVE: int
    ACTIVE: int
    NEEDS_ATTENTION: int

def status_to_nick(self):
    """    
    @returns: 
    @rtype: str
    """
def status_from_string(value=None):
    """    
    @type value: str
    @returns: 
    @rtype: AstalTray.Status
    """

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Get the singleton instance of [class@AstalTray.Tray]
    @returns: 
    @rtype: AstalTray.Tray
    """

class TrayItem(GObject.Object):
    def about_to_show(self):
        """        tells the tray app that its menu is about to be opened, so it can update the menu if needed. You should call this method before openening the 
        menu.
        @returns: 
        @rtype: None
        """
    def activate(self, x=None, y=None):
        """        Send an activate request to the tray app.
        @type x: int
        @type y: int
        @returns: 
        @rtype: None
        """
    def secondary_activate(self, x=None, y=None):
        """        Send a secondary activate request to the tray app.
        @type x: int
        @type y: int
        @returns: 
        @rtype: None
        """
    def scroll(self, delta=None, orientation=None):
        '''        Send a scroll request to the tray app. valid values for the orientation are "horizontal" and "vertical".
        @type delta: int
        @type orientation: str
        @returns: 
        @rtype: None
        '''
    def to_json_string(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_title(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_category(self):
        """        
        @returns: 
        @rtype: AstalTray.Category
        """
    def get_status(self):
        """        
        @returns: 
        @rtype: AstalTray.Status
        """
    def get_tooltip(self):
        """        
        @returns: 
        @rtype: AstalTray.Tooltip
        """
    def get_tooltip_markup(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_tooltip_text(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_id(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_is_menu(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_icon_theme_path(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_icon_pixbuf(self):
        """        
        @returns: 
        @rtype: GdkPixbuf.Pixbuf
        """
    def get_gicon(self):
        """        
        @returns: 
        @rtype: Gio.Icon
        """
    def get_item_id(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_menu_path(self):
        """        
        @returns: 
        @rtype: GLib.ObjectPath
        """
    def get_menu_model(self):
        """        
        @returns: 
        @rtype: Gio.MenuModel
        """
    def get_action_group(self):
        """        
        @returns: 
        @rtype: Gio.ActionGroup
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class TrayItemClass:
    @property
    def parent_class(self): ...

class TrayItemPrivate: ...

class Tray(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Tray
        @rtype: Tray
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Tray
        @rtype: Tray
        """
    @staticmethod
    def get_default():
        """        Get the singleton instance of [class@AstalTray.Tray]
        @returns: 
        @rtype: AstalTray.Tray
        """
    def get_item(self, item_id=None):
        """        gets the TrayItem with the given item-id.
        @type item_id: str
        @returns: 
        @rtype: AstalTray.TrayItem
        """
    def get_items(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_items_model(self):
        """        
        @returns: 
        @rtype: Gio.ListModel
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class TrayClass:
    @property
    def parent_class(self): ...
    @property
    def item_added(self): ...
    @property
    def item_removed(self): ...

class TrayPrivate: ...

class Pixmap:
    @property
    def width(self): ...
    @property
    def height(self): ...
    @property
    def bytes(self): ...
    @property
    def bytes_length1(self): ...

class Tooltip:
    @property
    def icon_name(self): ...
    @property
    def icon(self): ...
    @property
    def icon_length1(self): ...
    @property
    def title(self): ...
    @property
    def description(self): ...
