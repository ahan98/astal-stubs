from gi.repository import GObject as GObject

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    
    @returns: 
    @rtype: AstalPowerProfiles.PowerProfiles
    """

class PowerProfiles(GObject.Object):
    '''Client for <ulink url="https://freedesktop-team.pages.debian.net/power-profiles-daemon/gdbus-org.freedesktop.UPower.PowerProfiles.html">
  PowerProfiles</ulink>.'''
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created PowerProfiles
        @rtype: PowerProfiles
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created PowerProfiles
        @rtype: PowerProfiles
        """
    @staticmethod
    def get_default():
        """        Gets the default singleton PowerProfiles instance.
        @returns: 
        @rtype: AstalPowerProfiles.PowerProfiles
        """
    def hold_profile(self, profile=None, reason=None, application_id=None):
        """        This forces the passed profile (either 'power-saver' or 'performance') to be activated until either the caller 
        quits, [method@AstalPowerProfiles.PowerProfiles.release_profile] is called, or the [property@
        AstalPowerProfiles.PowerProfiles:active_profile] is changed by the user. When conflicting profiles are requested to be held, the 'power-saver
        ' profile will be activated in preference to the 'performance' profile. Those holds will be automatically cancelled if the user 
        manually switches to another profile, and the [signal@AstalPowerProfiles.PowerProfiles::profile_released] signal will be emitted.
        @type profile: str
        @type reason: str
        @type application_id: str
        @returns: 
        @rtype: int
        """
    def release_profile(self, cookie=None):
        """        This removes the hold that was set on a profile.
        @type cookie: int
        @returns: 
        @rtype: None
        """
    def get_active_profile(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_active_profile(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def get_icon_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_actions(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_active_profile_holds(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_performance_degraded(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_profiles(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_version(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class PowerProfilesClass:
    @property
    def parent_class(self): ...

class PowerProfilesPrivate: ...

class Profile:
    @property
    def profile(self): ...
    @property
    def cpu_driver(self): ...
    @property
    def platform_driver(self): ...
    @property
    def driver(self): ...

class Hold:
    @property
    def application_id(self): ...
    @property
    def profile(self): ...
    @property
    def reason(self): ...
