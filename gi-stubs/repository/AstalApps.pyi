from gi.repository import GObject as GObject

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

class Application(GObject.Object):
    """Object representing an applications .desktop file."""
    def get_key(self, key=None):
        """        Get a value from the .desktop file by its key.
        @type key: str
        @returns: 
        @rtype: str
        """
    def launch(self):
        """        Launches this application. The launched application inherits the environment of the launching process
        @returns: 
        @rtype: bool
        """
    def fuzzy_match(self, term=None, result=None):
        """        Calculate a score for an application using fuzzy matching algorithm.
        @type term: str
        @type result: AstalApps.Score
        @returns: 
        @rtype: None
        """
    def exact_match(self, term=None, result=None):
        """        Calculate a score using exact string algorithm.
        @type term: str
        @type result: AstalApps.Score
        @returns: 
        @rtype: None
        """
    def get_app(self):
        """        
        @returns: 
        @rtype: GLib.DesktopAppInfo
        """
    def set_app(self, value=None):
        """        
        @type value: GLib.DesktopAppInfo
        @returns: 
        @rtype: None
        """
    def get_frequency(self):
        """        
        @returns: 
        @rtype: int
        """
    def set_frequency(self, value=None):
        """        
        @type value: int
        @returns: 
        @rtype: None
        """
    def get_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_entry(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_wm_class(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_executable(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_keywords(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_categories(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ApplicationClass:
    @property
    def parent_class(self): ...

class ApplicationPrivate: ...

class Apps(GObject.Object):
    """This object can be used to query applications. Multipliers can be set to customize [struct@AstalApps.Score] results from queries which 
then are summed and sorted accordingly."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Apps
        @rtype: Apps
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Apps
        @rtype: Apps
        """
    def fuzzy_score(self, search=None, a=None):
        """        Calculate a score for an application using fuzzy matching algorithm. Taking this Apps' include settings into consideration .
        @type search: str
        @type a: AstalApps.Application
        @returns: 
        @rtype: float
        """
    def exact_score(self, search=None, a=None):
        """        Calculate a score for an application using exact string algorithm. Taking this Apps' include settings into consideration .
        @type search: str
        @type a: AstalApps.Application
        @returns: 
        @rtype: float
        """
    def fuzzy_query(self, search=None):
        """        Query the `list` of applications with a fuzzy matching algorithm.
        @type search: str
        @returns: 
        @rtype: GLib.List
        """
    def exact_query(self, search=None):
        """        Query the `list` of applications with a simple string matching algorithm.
        @type search: str
        @returns: 
        @rtype: GLib.List
        """
    def reload(self):
        """        Reload the `list` of Applications.
        @returns: 
        @rtype: None
        """
    def get_show_hidden(self):
        """        
        @returns: 
        @rtype: bool
        """
    def set_show_hidden(self, value=None):
        """        
        @type value: bool
        @returns: 
        @rtype: None
        """
    def get_list(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    def get_min_score(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_min_score(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_name_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_name_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_entry_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_entry_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_executable_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_executable_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_description_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_description_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_keywords_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_keywords_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_categories_multiplier(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_categories_multiplier(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class AppsClass:
    @property
    def parent_class(self): ...

class AppsPrivate: ...

class Score:
    @property
    def name(self): ...
    @property
    def entry(self): ...
    @property
    def executable(self): ...
    @property
    def description(self): ...
    @property
    def keywords(self): ...
    @property
    def categories(self): ...
