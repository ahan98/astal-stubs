# -*- coding: utf-8 -*-
from gi.repository import Gio
import typing
from gi.repository import GObject
MAJOR_VERSION = '0'
MICRO_VERSION = '0'
MINOR_VERSION = '1'
VERSION = '0.1.0'


class Pam(GObject.Object):
    """For simple authentication using only a password, using the [func@AstalAuth.Pam.authenticate]
method is recommended. Look at the simple examples for how to use it.

There is also a way to get access to the pam conversation, to allow for a more complex
authentication process, like using multiple factor authentication. Generally it can be used like
this:

1. create the Pam object.
2. set username and service if so required. It has sane defaults, so in most cases you can skip
this.
3. connect to the signals.
   After an `auth-*` signal is emitted, it has to be responded with exactly one
[method@AstalAuth.Pam.supply_secret] call. The secret is a string containing the user input. For
[auth-info][signal@AstalAuth.Pam::auth-info:] and [auth-error][signal@AstalAuth.Pam::auth-error:]
it should be `NULL`. Not connecting those signals, is equivalent to calling
[method@AstalAuth.Pam.supply_secret] with `NULL` immediately after the signal is emitted.
4. start authentication process using [method@AstalAuth.Pam.start_authenticate].
5. it is possible to reuse the same Pam object for multiple sequential authentication attempts.
Just call [method@AstalAuth.Pam.start_authenticate] again after the `success` or `fail` signal
was emitted."""

    @staticmethod
    def authenticate(password: str=None, result_callback:
        Gio.AsyncReadyCallback=None, user_data: typing.Any=None) -> bool:
        """Requests authentication of the provided password using the PAM (Pluggable Authentication Modules)
system.

:param password: the password to be authenticated
:param result_callback: a GAsyncReadyCallback   to call when the request is satisfied
:param user_data: the data to pass to callback function
:return: """
        pass

    @staticmethod
    def authenticate_finish(res: Gio.AsyncResult=None) -> gssize:
        """

:param res: 
:return: """
        pass

    def get_service(self) -> str:
        """Fetches the service from AsalAuthPam object.

:param self: a AstalAuthPam
:return: the service of the AsalAuthPam object. This string is owned by the object and must not be modified or freed."""
        pass

    def get_username(self) -> str:
        """Fetches the username from AsalAuthPam object.

:param self: a AstalAuthPam object
:return: the username of the AsalAuthPam object. This string is owned by the object and must not be modified or freed."""
        pass

    def set_service(self, service: str=None) -> None:
        """Sets the service to be used for authentication. This must be set to
before calling start_authenticate.
Changing it afterwards has no effect on the authentication process.

Defaults to `astal-auth`.

:param self: a AstalAuthPam object
:param service: the pam service used for authentication
:return: """
        pass

    def set_username(self, username: str=None) -> None:
        """Sets the username to be used for authentication. This must be set to
before calling start_authenticate.
Changing it afterwards has no effect on the authentication process.

Defaults to the owner of the process.

:param self: a AstalAuthPam object
:param username: the new username
:return: """
        pass

    def start_authenticate(self) -> bool:
        """starts a new authentication process using the PAM (Pluggable Authentication Modules) system.
Note that this will cancel an already running authentication process
associated with this AstalAuthPam object.

:param self: a AstalAuthPam Object
:return: """
        pass

    def supply_secret(self, secret: str=None) -> None:
        """provides pam with a secret. This method must be called exactly once after a
auth-* signal is emitted.

:param self: a AstalAuthPam Object
:param secret: the secret to be provided to pam. Can be NULL.
:return: """
        pass


class PamClass:
    """"""
    parent_class: GObject.ObjectClass
