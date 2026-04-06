# -*- coding: utf-8 -*-
from gi.repository import GLib
import typing
from gi.repository import GObject
from gi.repository import AstalApps
MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


class Application(GObject.Object):
    """Object representing an applications .desktop file."""

    def get_key(self, key: str=None) -> str:
        """Get a value from the .desktop file by its key.

:param self: 
:param key: 
:return: """
        pass

    def launch(self) -> bool:
        """Launches this application. The launched application inherits the environment of the launching process

:param self: 
:return: """
        pass

    def fuzzy_match(self, term: str=None, result: AstalApps.Score=None
        ) -> None:
        """Calculate a score for an application using fuzzy matching algorithm.

:param self: 
:param term: 
:param result: 
:return: """
        pass

    def exact_match(self, term: str=None, result: AstalApps.Score=None
        ) -> None:
        """Calculate a score using exact string algorithm.

:param self: 
:param term: 
:param result: 
:return: """
        pass

    def get_app(self) -> GLib.DesktopAppInfo:
        """

:param self: 
:return: """
        pass

    def set_app(self, value: GLib.DesktopAppInfo=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_frequency(self) -> int:
        """

:param self: 
:return: """
        pass

    def set_frequency(self, value: int=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_entry(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_wm_class(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_executable(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_icon_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_keywords(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def get_categories(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: ApplicationPrivate


class ApplicationClass:
    """"""
    parent_class: GObject.ObjectClass


class ApplicationPrivate:
    """"""


class Apps(GObject.Object):
    """This object can be used to query applications. Multipliers can be set to customize [struct@AstalApps.Score] results from queries which 
then are summed and sorted accordingly."""

    def fuzzy_score(self, search: str=None, a: AstalApps.Application=None
        ) -> float:
        """Calculate a score for an application using fuzzy matching algorithm. Taking this Apps' include settings into consideration .

:param self: 
:param search: 
:param a: 
:return: """
        pass

    def exact_score(self, search: str=None, a: AstalApps.Application=None
        ) -> float:
        """Calculate a score for an application using exact string algorithm. Taking this Apps' include settings into consideration .

:param self: 
:param search: 
:param a: 
:return: """
        pass

    def fuzzy_query(self, search: str=None) -> GLib.List:
        """Query the `list` of applications with a fuzzy matching algorithm.

:param self: 
:param search: 
:return: """
        pass

    def exact_query(self, search: str=None) -> GLib.List:
        """Query the `list` of applications with a simple string matching algorithm.

:param self: 
:param search: 
:return: """
        pass

    def reload(self) -> None:
        """Reload the `list` of Applications.

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalApps.Apps:
        """

:return: """
        pass

    def get_show_hidden(self) -> bool:
        """

:param self: 
:return: """
        pass

    def set_show_hidden(self, value: bool=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_list(self) -> GLib.List:
        """

:param self: 
:return: """
        pass

    def get_min_score(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_min_score(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_name_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_name_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_entry_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_entry_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_executable_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_executable_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_description_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_description_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_keywords_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_keywords_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def get_categories_multiplier(self) -> float:
        """

:param self: 
:return: """
        pass

    def set_categories_multiplier(self, value: float=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: AppsPrivate


class AppsClass:
    """"""
    parent_class: GObject.ObjectClass


class AppsPrivate:
    """"""


class Score:
    """"""
    name: int
    entry: int
    executable: int
    description: int
    keywords: int
    categories: int
