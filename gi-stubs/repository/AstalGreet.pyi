# -*- coding: utf-8 -*-
from gi.repository import Gio
from gi.repository import AstalGreet
from gi.repository import GObject
import typing
import enum


class ErrorType(enum.Enum):
    """"""
    AUTH_ERROR = 0
    ERROR = 1


class AuthMessageType(enum.Enum):
    """"""
    VISIBLE = 0
    SECRET = 1
    INFO = 2
    ERROR = 3


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def login(username: str=None, password: str=None, cmd: str=None, _callback_:
    Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None) -> None:
    """Shorthand for creating a session, posting the password, and starting the session with the given `cmd` which is parsed with [func@
GLib.shell_parse_argv].

:param username: User to login to
:param password: Password of the user
:param cmd: Command to start the session with
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def login_finish(_res_: Gio.AsyncResult=None) -> None:
    """

:param _res_: 
:return: """
    pass


def login_with_env(username: str=None, password: str=None, cmd: str=None,
    env: typing.Any=None, env_length1: int=None, _callback_:
    Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None) -> None:
    """Same as [func@AstalGreet.login] but allow for setting additonal env in the form of `name=value` pairs.

:param username: User to login to
:param password: Password of the user
:param cmd: Command to start the session with
:param env: Additonal env vars to set for the session
:param env_length1: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def login_with_env_finish(_res_: Gio.AsyncResult=None) -> None:
    """

:param _res_: 
:return: """
    pass


class Request(GObject.Object):
    """Base Request type."""

    def send(self, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """Send this request to greetd.

:param self: 
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def send_finish(self, _res_: Gio.AsyncResult=None) -> AstalGreet.Response:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def get_type_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_type_name(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: RequestPrivate


class RequestClass:
    """"""
    parent_class: GObject.ObjectClass


class RequestPrivate:
    """"""


class CreateSession(AstalGreet.Request):
    """Creates a session and initiates a login attempted for the given user. The session is ready to be started if a success is returned."""

    def __init__(self, username: str=None) -> None:
        """

:param self: 
:param username: 
:return: """
        pass

    @staticmethod
    def new(username: str=None) -> AstalGreet.CreateSession:
        """

:param username: 
:return: """
        pass

    def get_username(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_username(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: AstalGreet.Request
    priv: CreateSessionPrivate


class CreateSessionClass:
    """"""
    parent_class: AstalGreet.RequestClass


class CreateSessionPrivate:
    """"""


class PostAuthMesssage(AstalGreet.Request):
    """Answers an authentication message. If the message was informative (info, error), then a response does not need to be set in this 
message. The session is ready to be started if a success is returned."""

    def __init__(self, response: str=None) -> None:
        """

:param self: 
:param response: 
:return: """
        pass

    @staticmethod
    def new(response: str=None) -> AstalGreet.PostAuthMesssage:
        """

:param response: 
:return: """
        pass

    def get_response(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_response(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: AstalGreet.Request
    priv: PostAuthMesssagePrivate


class PostAuthMesssageClass:
    """"""
    parent_class: AstalGreet.RequestClass


class PostAuthMesssagePrivate:
    """"""


class StartSession(AstalGreet.Request):
    """Requests for the session to be started using the provided command line, adding the supplied environment to that created by PAM. The session 
will start after the greeter process terminates"""

    def __init__(self, cmd: typing.Any=None, cmd_length1: int=None, env:
        typing.Any=None, env_length1: int=None) -> None:
        """

:param self: 
:param cmd: 
:param cmd_length1: 
:param env: 
:param env_length1: 
:return: """
        pass

    @staticmethod
    def new(cmd: typing.Any=None, cmd_length1: int=None, env: typing.Any=
        None, env_length1: int=None) -> AstalGreet.StartSession:
        """

:param cmd: 
:param cmd_length1: 
:param env: 
:param env_length1: 
:return: """
        pass

    def get_cmd(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def set_cmd(self, value: typing.Any=None, value_length1: int=None) -> None:
        """

:param self: 
:param value: 
:param value_length1: 
:return: """
        pass

    def get_env(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass

    def set_env(self, value: typing.Any=None, value_length1: int=None) -> None:
        """

:param self: 
:param value: 
:param value_length1: 
:return: """
        pass
    parent_instance: AstalGreet.Request
    priv: StartSessionPrivate


class StartSessionClass:
    """"""
    parent_class: AstalGreet.RequestClass


class StartSessionPrivate:
    """"""


class CancelSession(AstalGreet.Request):
    """Cancels the session that is currently under configuration."""

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalGreet.CancelSession:
        """

:return: """
        pass
    parent_instance: AstalGreet.Request
    priv: CancelSessionPrivate


class CancelSessionClass:
    """"""
    parent_class: AstalGreet.RequestClass


class CancelSessionPrivate:
    """"""


class Response(GObject.Object):
    """Base Response type."""
    parent_instance: GObject.Object
    priv: ResponsePrivate


class ResponseClass:
    """"""
    parent_class: GObject.ObjectClass


class ResponsePrivate:
    """"""


class Success(AstalGreet.Response):
    """Indicates that the request succeeded."""
    parent_instance: AstalGreet.Response
    priv: SuccessPrivate


class SuccessClass:
    """"""
    parent_class: AstalGreet.ResponseClass


class SuccessPrivate:
    """"""


class Error(AstalGreet.Response):
    """Indicates that the request succeeded."""

    def get_error_type(self) -> AstalGreet.ErrorType:
        """

:param self: 
:return: """
        pass

    def get_description(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: AstalGreet.Response
    priv: ErrorPrivate


class ErrorClass:
    """"""
    parent_class: AstalGreet.ResponseClass


class ErrorPrivate:
    """"""


class AuthMessage(AstalGreet.Response):
    """Indicates that the request succeeded."""

    def get_message_type(self) -> AstalGreet.AuthMessageType:
        """

:param self: 
:return: """
        pass

    def get_message(self) -> str:
        """

:param self: 
:return: """
        pass
    parent_instance: AstalGreet.Response
    priv: AuthMessagePrivate


class AuthMessageClass:
    """"""
    parent_class: AstalGreet.ResponseClass


class AuthMessagePrivate:
    """"""
