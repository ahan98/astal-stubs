from gi.repository import GObject as GObject

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def is_supported():
    """    
    @returns: 
    @rtype: bool
    """
def get_default():
    """    Returns the singleton River instance.
    @returns: 
    @rtype: AstalRiver.River
    """

class River(GObject.Object):
    """This class creates a connection to the river compositor."""
    def __init__(self, **kwargs) -> None:
        """        Creates a new River object. It is recommended to use the [func@AstalRiver.get_default] method instead of this method.
        @returns: Newly created River
        @rtype: River
        """
    @staticmethod
    def new():
        """        Creates a new River object. It is recommended to use the [func@AstalRiver.get_default] method instead of this method.
        @returns: Newly created River
        @rtype: River
        """
    @staticmethod
    def get_default():
        """        Returns the singleton River instance.
        @returns: 
        @rtype: AstalRiver.River
        """
    def find_output_by_wl_output(self, wl_output=None):
        """        Looks up an output based on its underlying wl_output object.
        @type wl_output: Wl.Output
        @returns: 
        @rtype: AstalRiver.Output
        """
    def find_output_by_astal_wl_output(self, wl_output=None):
        """        Looks up an output based on its underlying [class@AstalWl.Output] object.
        @type wl_output: AstalWl.Output
        @returns: 
        @rtype: AstalRiver.Output
        """
    def find_output_by_name(self, name=None):
        """        Looks up an output based on its underlying name.
        @type name: str
        @returns: 
        @rtype: AstalRiver.Output
        """
    def find_output_by_id(self, id=None):
        """        Looks up an output based on its underlying wayland id.
        @type id: int
        @returns: 
        @rtype: AstalRiver.Output
        """
    def run_command(self, cmd=None, cmd_length1=None, output=None):
        """        executes a given command, similar to riverctl.
        @type cmd_length1: int
        @type output: str
        @returns: 
        @rtype: bool
        """
    def run_command_async(self, cmd=None, cmd_length1=None, _callback_=None, _callback__target=None):
        """        executes a given command, similar to riverctl.
        @type cmd_length1: int
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def run_command_finish(self, _res_=None, output=None):
        """        
        @type _res_: Gio.AsyncResult
        @type output: str
        @returns: 
        @rtype: bool
        """
    def new_layout(self, namespace=None):
        """        creates a new Layout object with a given namespace.
        @type namespace: str
        @returns: 
        @rtype: AstalRiver.Layout
        """
    def get_outputs(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_focused_output(self):
        """        
        @returns: 
        @rtype: AstalRiver.Output
        """
    def get_focused_output_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_focused_view(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_mode(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class RiverClass:
    @property
    def parent_class(self): ...

class RiverPrivate: ...

class Output(GObject.Object):
    """Represents a display output device."""
    def get_output(self):
        """        
        @returns: 
        @rtype: AstalWl.Output
        """
    def get_focused_tags(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_focused_tags(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_occupied_tags(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_urgent_tags(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_focused_view(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_layout_name(self):
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

class LayoutDemandResult(GObject.Object):
    def __init__(self, layout_name=None, rectangles=None) -> None:
        """        
        @type layout_name: str
        @type rectangles: GLib.List
        @returns: Newly created LayoutDemandResult
        @rtype: LayoutDemandResult
        """
    @staticmethod
    def new(layout_name=None, rectangles=None):
        """        
        @type layout_name: str
        @type rectangles: GLib.List
        @returns: Newly created LayoutDemandResult
        @rtype: LayoutDemandResult
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...
    @property
    def layout_name(self): ...
    @property
    def rectangles(self): ...

class LayoutDemandResultClass:
    @property
    def parent_class(self): ...

class LayoutDemandResultPrivate: ...

class Layout(GObject.Object):
    """Allows implementing a custom windows Layout generator."""
    def set_layout_demand_closure(self, closure=None):
        """        Sets the Closure to be called when a new layout is requested. The Closure is of type [callback@AstalRiver.LayoutDemandCallback].
        The Closure must return a [class@AstalRiver.LayoutDemandResult] containing exactly as many [struct@AstalWl.Rectangle] objects as 
        requested. Each rectangle represents the position and size of each window. Before the result is applied, each rectangle is croped to ensure it lies 
        entirely within the usable area.
        @type closure: GObject.Closure
        @returns: 
        @rtype: None
        """
    def get_namespace(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...
    @property
    def layout_demand_closure(self): ...

class LayoutClass:
    @property
    def parent_class(self): ...

class LayoutPrivate: ...
