from gi.repository import GObject as GObject

class Input:
    FIFO: int
    PORTAUDIO: int
    PIPEWIRE: int
    ALSA: int
    PULSE: int
    SNDIO: int
    SHMEM: int
    WINSCAP: int

def get_default():
    """    gets the default Cava object.
    @returns: 
    @rtype: Cava
    """

class Cava(GObject.Object):
    @staticmethod
    def get_default():
        """        gets the default Cava object.
        @returns: 
        @rtype: Cava
        """
    def get_active(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_autosens(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_bars(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_channels(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_framerate(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_high_cutoff(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_input(self):
        """        
        @returns: 
        @rtype: Input
        """
    def get_low_cutoff(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_noise_reduction(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_samplerate(self):
        """        
        @returns: 
        @rtype: int
        """
    def get_source(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_stereo(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_values(self):
        """        
        @rtype: None
        """
    def set_active(self, active=None):
        """        
        @type active: bool
        @returns: 
        @rtype: None
        """
    def set_autosens(self, autosens=None):
        """        
        @type autosens: bool
        @returns: 
        @rtype: None
        """
    def set_bars(self, bars=None):
        """        
        @type bars: int
        @returns: 
        @rtype: None
        """
    def set_channels(self, channels=None):
        """        
        @type channels: int
        @returns: 
        @rtype: None
        """
    def set_framerate(self, framerate=None):
        """        
        @type framerate: int
        @returns: 
        @rtype: None
        """
    def set_high_cutoff(self, high_cutoff=None):
        """        
        @type high_cutoff: int
        @returns: 
        @rtype: None
        """
    def set_input(self, input=None):
        """        
        @type input: Input
        @returns: 
        @rtype: None
        """
    def set_low_cutoff(self, low_cutoff=None):
        """        
        @type low_cutoff: int
        @returns: 
        @rtype: None
        """
    def set_noise_reduction(self, noise=None):
        """        
        @type noise: float
        @returns: 
        @rtype: None
        """
    def set_samplerate(self, samplerate=None):
        """        
        @type samplerate: int
        @returns: 
        @rtype: None
        """
    def set_source(self, source=None):
        """        
        @type source: str
        @returns: 
        @rtype: None
        """
    def set_stereo(self, stereo=None):
        """        
        @type stereo: bool
        @returns: 
        @rtype: None
        """

class CavaClass:
    @property
    def parent_class(self): ...
