from gi.repository import GObject as GObject, Gio as Gio

class PlaybackStatus:
    PLAYING: int
    PAUSED: int
    STOPPED: int

class Loop:
    UNSUPPORTED: int
    NONE: int
    TRACK: int
    PLAYLIST: int

class Shuffle:
    UNSUPPORTED: int
    ON: int
    OFF: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def get_default():
    """    Gets the default singleton Mpris instance.
    @returns: 
    @rtype: AstalMpris.Mpris
    """

class Mpris(GObject.Object, Gio.ListModel):
    """Manager object that monitors the session DBus for Mpris players to appear and disappear."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Mpris
        @rtype: Mpris
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Mpris
        @rtype: Mpris
        """
    @staticmethod
    def get_default():
        """        Gets the default singleton Mpris instance.
        @returns: 
        @rtype: AstalMpris.Mpris
        """
    def get_players(self):
        """        
        @returns: 
        @rtype: GLib.List
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class MprisClass:
    @property
    def parent_class(self): ...

class MprisPrivate: ...

class Player(GObject.Object):
    """Object which tracks players through their mpris DBus interface. The most simple way is to use [class@AstalMpris.Mpris] which tracks 
every player, but [class@AstalMpris.Player] can be constructed for dedicated players too."""
    def __init__(self, name=None) -> None:
        '''        Construct a Player that tracks a dbus name. For example "org.mpris.MediaPlayer2.spotify". The "org.mpris.MediaPlayer2." 
        prefix can be omitted so simply "spotify" would mean the same. [property@AstalMpris.Player:available] indicates whether the player 
        is actually running or not.
        @param name: dbus name of the player.
        @type name: str
        @returns: Newly created Player
        @rtype: Player
        '''
    @staticmethod
    def new(name=None):
        '''        Construct a Player that tracks a dbus name. For example "org.mpris.MediaPlayer2.spotify". The "org.mpris.MediaPlayer2." 
        prefix can be omitted so simply "spotify" would mean the same. [property@AstalMpris.Player:available] indicates whether the player 
        is actually running or not.
        @param name: dbus name of the player.
        @type name: str
        @returns: Newly created Player
        @rtype: Player
        '''
    def quit(self):
        """        Causes the media player to stop running. The media player may refuse to allow clients to shut it down. In this case, the [property@
        AstalMpris.Player:can_quit] property is false and this method does nothing.
        @returns: 
        @rtype: None
        """
    def toggle_fullscreen(self):
        """        Toggle [property@AstalMpris.Player:fullscreen] state.
        @returns: 
        @rtype: None
        """
    def next(self):
        """        Skips to the next track in the tracklist. If there is no next track (and endless playback and track repeat are both off), stop 
        playback. If [property@AstalMpris.Player:can_go_next] is `false` this method has no effect.
        @returns: 
        @rtype: None
        """
    def previous(self):
        """        Skips to the previous track in the tracklist. If there is no previous track (and endless playback and track repeat are both off), 
        stop playback. If [property@AstalMpris.Player:can_go_previous] is `false` this method has no effect.
        @returns: 
        @rtype: None
        """
    def pause(self):
        """        Pauses playback. If playback is already paused, this has no effect. If [property@AstalMpris.Player:can_pause] is `false` this method has 
        no effect.
        @returns: 
        @rtype: None
        """
    def play_pause(self):
        """        Pauses playback. If playback is already paused, resumes playback. If playback is stopped, starts playback.
        @returns: 
        @rtype: None
        """
    def stop(self):
        """        Stops playback. If playback is already stopped, this has no effect. If [property@AstalMpris.Player:can_control] is `false` this method 
        has no effect.
        @returns: 
        @rtype: None
        """
    def play(self):
        """        Starts or resumes playback. If already playing, this has no effect. If paused, playback resumes from the current position. If [property@
        AstalMpris.Player:can_play] is `false` this method has no effect.
        @returns: 
        @rtype: None
        """
    def open_uri(self, uri=None):
        """        uri scheme should be an element of [property@AstalMpris.Player:supported_uri_schemes] and the mime-type should match one of the elements 
        of [property@AstalMpris.Player:supported_mime_types].
        @param uri: Uri of the track to load.
        @type uri: str
        @returns: 
        @rtype: None
        """
    def loop(self):
        """        Change [property@AstalMpris.Player:loop_status] from none to track, from track to playlist, from playlist to none.
        @returns: 
        @rtype: None
        """
    def shuffle(self):
        """        Toggle [property@AstalMpris.Player:shuffle_status].
        @returns: 
        @rtype: None
        """
    def get_meta(self, key=None):
        """        Lookup a key from [property@AstalMpris.Player:metadata]. This method is useful for languages that fail to introspect hashtables.
        @type key: str
        @returns: 
        @rtype: GLib.Variant
        """
    def get_bus_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_available(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_quit(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_fullscreen(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_set_fullscreen(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_raise(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_identity(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_entry(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_supported_uri_schemes(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_supported_mime_types(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def get_loop_status(self):
        """        
        @returns: 
        @rtype: AstalMpris.Loop
        """
    def set_loop_status(self, value=None):
        """        
        @type value: AstalMpris.Loop
        @returns: 
        @rtype: None
        """
    def get_shuffle_status(self):
        """        
        @returns: 
        @rtype: AstalMpris.Shuffle
        """
    def set_shuffle_status(self, value=None):
        """        
        @type value: AstalMpris.Shuffle
        @returns: 
        @rtype: None
        """
    def get_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_rate(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_volume(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_volume(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_position(self):
        """        
        @returns: 
        @rtype: float
        """
    def set_position(self, value=None):
        """        
        @type value: float
        @returns: 
        @rtype: None
        """
    def get_playback_status(self):
        """        
        @returns: 
        @rtype: AstalMpris.PlaybackStatus
        """
    def get_minimum_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_maximum_rate(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_can_go_next(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_go_previous(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_play(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_pause(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_seek(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_can_control(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_metadata(self):
        """        
        @returns: 
        @rtype: GLib.Variant
        """
    def get_trackid(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_length(self):
        """        
        @returns: 
        @rtype: float
        """
    def get_art_url(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_album(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_album_artist(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_artist(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_lyrics(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_title(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_composer(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_comments(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_cover_art(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class PlayerClass:
    @property
    def parent_class(self): ...

class PlayerPrivate: ...
