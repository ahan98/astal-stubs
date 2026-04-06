# -*- coding: utf-8 -*-
import enum
from gi.repository import Gio
from gi.repository import AstalMpris
from gi.repository import GLib
from gi.repository import GObject
import typing


class PlaybackStatus(enum.Enum):
    """"""
    PLAYING = 0
    PAUSED = 1
    STOPPED = 2


class Loop(enum.Enum):
    """"""
    UNSUPPORTED = 0
    NONE = 1
    TRACK = 2
    PLAYLIST = 3


class Shuffle(enum.Enum):
    """"""
    UNSUPPORTED = 0
    ON = 1
    OFF = 2


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def get_default() -> AstalMpris.Mpris:
    """Gets the default singleton Mpris instance.

:return: """
    pass


class Mpris(GObject.Object, Gio.ListModel):
    """Manager object that monitors the session DBus for Mpris players to appear and disappear."""

    @staticmethod
    def get_default() -> AstalMpris.Mpris:
        """Gets the default singleton Mpris instance.

:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalMpris.Mpris:
        """

:return: """
        pass

    def get_players(self) -> GLib.List:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: MprisPrivate


class MprisClass:
    """"""
    parent_class: GObject.ObjectClass


class MprisPrivate:
    """"""


class Player(GObject.Object):
    """Object which tracks players through their mpris DBus interface. The most simple way is to use [class@AstalMpris.Mpris] which tracks 
every player, but [class@AstalMpris.Player] can be constructed for dedicated players too."""

    def _raise(self) -> None:
        """Brings the player's user interface to the front using any appropriate mechanism available. The media player may be unable to control how 
its user interface is displayed, or it may not have a graphical user interface at all. In this case, the [property@
AstalMpris.Player:can_raise] is `false` and this method does nothing.

:param self: 
:return: """
        pass

    def quit(self) -> None:
        """Causes the media player to stop running. The media player may refuse to allow clients to shut it down. In this case, the [property@
AstalMpris.Player:can_quit] property is false and this method does nothing.

:param self: 
:return: """
        pass

    def toggle_fullscreen(self) -> None:
        """Toggle [property@AstalMpris.Player:fullscreen] state.

:param self: 
:return: """
        pass

    def next(self) -> None:
        """Skips to the next track in the tracklist. If there is no next track (and endless playback and track repeat are both off), stop 
playback. If [property@AstalMpris.Player:can_go_next] is `false` this method has no effect.

:param self: 
:return: """
        pass

    def previous(self) -> None:
        """Skips to the previous track in the tracklist. If there is no previous track (and endless playback and track repeat are both off), 
stop playback. If [property@AstalMpris.Player:can_go_previous] is `false` this method has no effect.

:param self: 
:return: """
        pass

    def pause(self) -> None:
        """Pauses playback. If playback is already paused, this has no effect. If [property@AstalMpris.Player:can_pause] is `false` this method has 
no effect.

:param self: 
:return: """
        pass

    def play_pause(self) -> None:
        """Pauses playback. If playback is already paused, resumes playback. If playback is stopped, starts playback.

:param self: 
:return: """
        pass

    def stop(self) -> None:
        """Stops playback. If playback is already stopped, this has no effect. If [property@AstalMpris.Player:can_control] is `false` this method 
has no effect.

:param self: 
:return: """
        pass

    def play(self) -> None:
        """Starts or resumes playback. If already playing, this has no effect. If paused, playback resumes from the current position. If [property@
AstalMpris.Player:can_play] is `false` this method has no effect.

:param self: 
:return: """
        pass

    def open_uri(self, uri: str=None) -> None:
        """uri scheme should be an element of [property@AstalMpris.Player:supported_uri_schemes] and the mime-type should match one of the elements 
of [property@AstalMpris.Player:supported_mime_types].

:param self: 
:param uri: Uri of the track to load.
:return: """
        pass

    def loop(self) -> None:
        """Change [property@AstalMpris.Player:loop_status] from none to track, from track to playlist, from playlist to none.

:param self: 
:return: """
        pass

    def shuffle(self) -> None:
        """Toggle [property@AstalMpris.Player:shuffle_status].

:param self: 
:return: """
        pass

    def get_meta(self, key: str=None) -> GLib.Variant:
        """Lookup a key from [property@AstalMpris.Player:metadata]. This method is useful for languages that fail to introspect hashtables.

:param self: 
:param key: 
:return: """
        pass

    def __init__(self, name: str=None) -> None:
        """Construct a Player that tracks a dbus name. For example "org.mpris.MediaPlayer2.spotify". The "org.mpris.MediaPlayer2." 
prefix can be omitted so simply "spotify" would mean the same. [property@AstalMpris.Player:available] indicates whether the player 
is actually running or not.

:param self: 
:param name: dbus name of the player.
:return: """
        pass

    @staticmethod
    def new(name: str=None) -> AstalMpris.Player:
        """Construct a Player that tracks a dbus name. For example "org.mpris.MediaPlayer2.spotify". The "org.mpris.MediaPlayer2." 
prefix can be omitted so simply "spotify" would mean the same. [property@AstalMpris.Player:available] indicates whether the player 
is actually running or not.

:param name: dbus name of the player.
:return: """
        pass

    def get_bus_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_available(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_quit(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_fullscreen(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_set_fullscreen(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_raise(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_identity(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_entry(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_supported_uri_schemes(self, result_length1: int=None
        ) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_supported_mime_types(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_loop_status(self) -> AstalMpris.Loop:
        """

:param self: 
:return: """
        pass

    def set_loop_status(self, value: AstalMpris.Loop=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_shuffle_status(self) -> AstalMpris.Shuffle:
        """

:param self: 
:return: """
        pass

    def set_shuffle_status(self, value: AstalMpris.Shuffle=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_rate(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_volume(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_volume(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_position(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_position(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_playback_status(self) -> AstalMpris.PlaybackStatus:
        """

:param self: 
:return: """
        pass

    def get_minimum_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_maximum_rate(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_can_go_next(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_go_previous(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_play(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_pause(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_seek(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_can_control(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_metadata(self) -> GLib.Variant:
        """

:param self: 
:return: """
        pass

    def get_trackid(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_length(self) -> float:
        """

:param self: 
:return: """
        pass

    def get_art_url(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_album(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_album_artist(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_artist(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_lyrics(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_title(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_composer(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_comments(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_cover_art(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: PlayerPrivate


class PlayerClass:
    """"""
    parent_class: GObject.ObjectClass


class PlayerPrivate:
    """"""
