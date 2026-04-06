# -*- coding: utf-8 -*-
from gi.repository import GLib
import typing
from gi.repository import Gio
from gi.repository import AstalIO
import enum
from gi.repository import GObject


class AppError(enum.Enum):
    """"""
    NAME_OCCUPIED = 0
    TAKEOVER_FAILED = 1


MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '0'
VERSION = '0.1.0'


def acquire_socket(app: AstalIO.Application=None, sock: str=None
    ) -> Gio.SocketService:
    """Starts a [class@Gio.SocketService] and binds `XDG_RUNTIME_DIR/astal/<instance_name>.sock`. This socket is then used by the astal 
cli. Not meant for public usage, but for [method@AstalIO.Application.acquire_socket].

:param app: 
:param sock: 
:return: """
    pass


def get_instances() -> GLib.List:
    """Get a list of running Astal.Application instances. It is the equivalent of `astal --list`.

:return: """
    pass


def quit_instance(instance: str=None) -> None:
    """Quit an an Astal instances. It is the equivalent of `astal --quit -i instance`.

:param instance: 
:return: """
    pass


def open_inspector(instance: str=None) -> None:
    """Open the Gtk debug tool of an an Astal instances. It is the equivalent of `astal --inspector -i instance`.

:param instance: 
:return: """
    pass


def toggle_window_by_name(instance: str=None, window: str=None) -> None:
    """Toggle a Window of an Astal instances. It is the equivalent of `astal -i instance --toggle window`.

:param instance: 
:param window: 
:return: """
    pass


def send_message(instance: str=None, request: str=None) -> str:
    """Use [func@AstalIO.send_request] instead.

:param instance: 
:param request: 
:return: """
    pass


def send_request(instance: str=None, request: str=None) -> str:
    """Send a request to an Astal instances. It is the equivalent of `astal -i instance "request content"`.

:param instance: 
:param request: 
:return: """
    pass


def read_sock(conn: Gio.SocketConnection=None, _callback_:
    Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None) -> None:
    """Read the socket of an Astal.Application instance.

:param conn: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def read_sock_finish(_res_: Gio.AsyncResult=None) -> str:
    """

:param _res_: 
:return: """
    pass


def write_sock(conn: Gio.SocketConnection=None, response: str=None,
    _callback_: Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None
    ) -> None:
    """Write the socket of an Astal.Application instance.

:param conn: 
:param response: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def write_sock_finish(_res_: Gio.AsyncResult=None) -> None:
    """

:param _res_: 
:return: """
    pass


def read_file(path: str=None) -> str:
    """Read the contents of a file synchronously.

:param path: 
:return: """
    pass


def read_file_async(path: str=None, _callback_: Gio.AsyncReadyCallback=None,
    _callback__target: typing.Any=None) -> None:
    """Read the contents of a file asynchronously.

:param path: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def read_file_finish(_res_: Gio.AsyncResult=None) -> str:
    """

:param _res_: 
:return: """
    pass


def write_file(path: str=None, content: str=None) -> None:
    """Write content to a file synchronously.

:param path: 
:param content: 
:return: """
    pass


def write_file_async(path: str=None, content: str=None, _callback_:
    Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None) -> None:
    """Write content to a file asynchronously.

:param path: 
:param content: 
:param _callback_: 
:param _callback__target: 
:return: """
    pass


def write_file_finish(_res_: Gio.AsyncResult=None) -> None:
    """

:param _res_: 
:return: """
    pass


def monitor_file(path: str=None, callback: GObject.Closure=None
    ) -> Gio.FileMonitor:
    """Monitor a file for changes. If the path is a directory, monitor it recursively. The callback will be called passed two parameters: the path of 
the file that changed and an [enum@Gio.FileMonitorEvent] indicating the reason.

:param path: 
:param callback: 
:return: """
    pass


class Daemon(Gio.Application, AstalIO.Application):
    """"""

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """Handler for an incoming request.

:param self: 
:param request: Body of the request
:param conn: The connection which expects the response.
:return: """
        pass

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """Handler for an incoming request.

:param self: 
:param request: Body of the request
:param conn: The connection which expects the response.
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalIO.Daemon:
        """

:return: """
        pass
    parent_instance: Gio.Application
    priv: DaemonPrivate


class DaemonClass:
    """"""
    parent_class: Gio.ApplicationClass
    request: typing.Any


class DaemonPrivate:
    """"""


class Process(GObject.Object):
    """`Process` provides shortcuts for [class@Gio.Subprocess] with sane defaults."""

    def kill(self) -> None:
        """Force quit the subprocess.

:param self: 
:return: """
        pass

    def signal(self, signal_num: int=None) -> None:
        """Send a signal to the subprocess.

:param self: 
:param signal_num: Signal number to be sent
:return: """
        pass

    def write(self, _in: str=None) -> None:
        """Write a line to the subprocess' stdin synchronously.

:param self: 
:param _in: String to be written to stdin
:return: """
        pass

    def write_async(self, _in: str=None, _callback_: Gio.AsyncReadyCallback
        =None, _callback__target: typing.Any=None) -> None:
        """Write a line to the subprocess' stdin asynchronously.

:param self: 
:param _in: String to be written to stdin
:param _callback_: 
:param _callback__target: 
:return: """
        pass

    def write_finish(self, _res_: Gio.AsyncResult=None) -> None:
        """

:param self: 
:param _res_: 
:return: """
        pass

    def __init__(self, cmd: typing.Any=None, cmd_length1: int=None) -> None:
        """See [func@AstalIO.Process.subprocessv]

:param self: 
:param cmd: 
:param cmd_length1: 
:return: """
        pass

    @staticmethod
    def new(cmd: typing.Any=None, cmd_length1: int=None) -> AstalIO.Process:
        """See [func@AstalIO.Process.subprocessv]

:param cmd: 
:param cmd_length1: 
:return: """
        pass

    @staticmethod
    def subprocessv(cmd: typing.Any=None, cmd_length1: int=None
        ) -> AstalIO.Process:
        """Start a new subprocess with the given command.
The first element of the vector is executed with the remaining elements as the argument list.

:param cmd: 
:param cmd_length1: 
:return: """
        pass

    @staticmethod
    def subprocess(cmd: str=None) -> AstalIO.Process:
        """Start a new subprocess with the given command which is parsed using [func@GLib.shell_parse_argv].

:param cmd: 
:return: """
        pass

    @staticmethod
    def execv(cmd: typing.Any=None, cmd_length1: int=None) -> str:
        """Execute a command synchronously. The first element of the vector is executed with the remaining elements as the argument list.

:param cmd: 
:param cmd_length1: 
:return: stdout of the subprocess"""
        pass

    @staticmethod
    def exec(cmd: str=None) -> str:
        """Execute a command synchronously. The command is parsed using [func@GLib.shell_parse_argv].

:param cmd: 
:return: stdout of the subprocess"""
        pass

    @staticmethod
    def exec_asyncv(cmd: typing.Any=None, cmd_length1: int=None, _callback_:
        Gio.AsyncReadyCallback=None, _callback__target: typing.Any=None
        ) -> None:
        """Execute a command asynchronously. The first element of the vector is executed with the remaining elements as the argument list.

:param cmd: 
:param cmd_length1: 
:param _callback_: 
:param _callback__target: 
:return: stdout of the subprocess"""
        pass

    @staticmethod
    def exec_asyncv_finish(_res_: Gio.AsyncResult=None) -> str:
        """

:param _res_: 
:return: """
        pass

    @staticmethod
    def exec_async(cmd: str=None, _callback_: Gio.AsyncReadyCallback=None,
        _callback__target: typing.Any=None) -> None:
        """Execute a command asynchronously. The command is parsed using [func@GLib.shell_parse_argv].

:param cmd: 
:param _callback_: 
:param _callback__target: 
:return: stdout of the subprocess"""
        pass

    @staticmethod
    def exec_finish(_res_: Gio.AsyncResult=None) -> str:
        """

:param _res_: 
:return: """
        pass

    def get_argv(self, result_length1: int=None) -> typing.Any:
        """

:param self: 
:param result_length1: 
:return: """
        pass
    parent_instance: GObject.Object
    priv: ProcessPrivate


class ProcessClass:
    """"""
    parent_class: GObject.ObjectClass


class ProcessPrivate:
    """"""


class Time(GObject.Object):
    """`Time` provides shortcuts for GLib timeout functions."""

    @staticmethod
    def interval_prio(interval: int=None, prio: int=None, fn:
        GObject.Closure=None) -> AstalIO.Time:
        """Start an interval timer with default Priority.

:param interval: 
:param prio: 
:param fn: 
:return: """
        pass

    @staticmethod
    def timeout_prio(timeout: int=None, prio: int=None, fn: GObject.Closure
        =None) -> AstalIO.Time:
        """Start a timeout timer with default Priority.

:param timeout: 
:param prio: 
:param fn: 
:return: """
        pass

    @staticmethod
    def idle_prio(prio: int=None, fn: GObject.Closure=None) -> AstalIO.Time:
        """Start an idle timer with default priority.

:param prio: 
:param fn: 
:return: """
        pass

    @staticmethod
    def interval(interval: int=None, fn: GObject.Closure=None) -> AstalIO.Time:
        """Start an interval timer. Ticks immediately then every `interval` milliseconds.

:param interval: Tick every milliseconds.
:param fn: Optional callback.
:return: """
        pass

    @staticmethod
    def timeout(timeout: int=None, fn: GObject.Closure=None) -> AstalIO.Time:
        """Start a timeout timer which ticks after `timeout` milliseconds.

:param timeout: Tick after milliseconds.
:param fn: Optional callback.
:return: """
        pass

    @staticmethod
    def idle(fn: GObject.Closure=None) -> AstalIO.Time:
        """Start a timer which will tick when there are no higher priority tasks pending.

:param fn: Optional callback.
:return: """
        pass

    def cancel(self) -> None:
        """Cancel timer and emit [signal@AstalIO.Time::cancelled]

:param self: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalIO.Time:
        """

:return: """
        pass
    parent_instance: GObject.Object
    priv: TimePrivate


class TimeClass:
    """"""
    parent_class: GObject.ObjectClass


class TimePrivate:
    """"""


class VariableBase(GObject.Object):
    """"""

    def emit_changed(self) -> None:
        """

:param self: 
:return: """
        pass

    def emit_dropped(self) -> None:
        """

:param self: 
:return: """
        pass

    def emit_error(self, err: str=None) -> None:
        """

:param self: 
:param err: 
:return: """
        pass

    def __init__(self) -> None:
        """

:param self: 
:return: """
        pass

    @staticmethod
    def new() -> AstalIO.VariableBase:
        """

:return: """
        pass
    parent_instance: GObject.Object
    priv: VariableBasePrivate


class VariableBaseClass:
    """"""
    parent_class: GObject.ObjectClass


class VariableBasePrivate:
    """"""


class Variable(AstalIO.VariableBase):
    """"""

    def __init__(self, init: GObject.Value=None) -> None:
        """

:param self: 
:param init: 
:return: """
        pass

    @staticmethod
    def new(init: GObject.Value=None) -> AstalIO.Variable:
        """

:param init: 
:return: """
        pass

    def poll(self, interval: int=None, exec: str=None, transform:
        GObject.Closure=None) -> AstalIO.Variable:
        """

:param self: 
:param interval: 
:param exec: 
:param transform: 
:return: """
        pass

    def pollv(self, interval: int=None, execv: typing.Any=None,
        execv_length1: int=None, transform: GObject.Closure=None
        ) -> AstalIO.Variable:
        """

:param self: 
:param interval: 
:param execv: 
:param execv_length1: 
:param transform: 
:return: """
        pass

    def pollfn(self, interval: int=None, fn: GObject.Closure=None
        ) -> AstalIO.Variable:
        """

:param self: 
:param interval: 
:param fn: 
:return: """
        pass

    def watch(self, exec: str=None, transform: GObject.Closure=None
        ) -> AstalIO.Variable:
        """

:param self: 
:param exec: 
:param transform: 
:return: """
        pass

    def watchv(self, execv: typing.Any=None, execv_length1: int=None,
        transform: GObject.Closure=None) -> AstalIO.Variable:
        """

:param self: 
:param execv: 
:param execv_length1: 
:param transform: 
:return: """
        pass

    def start_poll(self) -> None:
        """

:param self: 
:return: """
        pass

    def start_watch(self) -> None:
        """

:param self: 
:return: """
        pass

    def stop_poll(self) -> None:
        """

:param self: 
:return: """
        pass

    def stop_watch(self) -> None:
        """

:param self: 
:return: """
        pass

    def is_polling(self) -> bool:
        """

:param self: 
:return: """
        pass

    def is_watching(self) -> bool:
        """

:param self: 
:return: """
        pass

    def get_value(self, result: GObject.Value=None) -> None:
        """

:param self: 
:param result: 
:return: """
        pass

    def set_value(self, value: GObject.Value=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass
    parent_instance: AstalIO.VariableBase
    priv: VariablePrivate


class VariableClass:
    """"""
    parent_class: AstalIO.VariableBaseClass


class VariablePrivate:
    """"""


class Application:
    """This interface is used internally in Astal3 and Astal4, not meant for public usage."""

    def quit(self) -> None:
        """

:param self: 
:return: """
        pass

    def quit(self) -> None:
        """

:param self: 
:return: """
        pass

    def inspector(self) -> None:
        """

:param self: 
:return: """
        pass

    def inspector(self) -> None:
        """

:param self: 
:return: """
        pass

    def toggle_window(self, window: str=None) -> None:
        """

:param self: 
:param window: 
:return: """
        pass

    def toggle_window(self, window: str=None) -> None:
        """

:param self: 
:param window: 
:return: """
        pass

    def acquire_socket(self) -> None:
        """

:param self: 
:return: """
        pass

    def acquire_socket(self) -> None:
        """

:param self: 
:return: """
        pass

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """

:param self: 
:param request: 
:param conn: 
:return: """
        pass

    def request(self, request: str=None, conn: Gio.SocketConnection=None
        ) -> None:
        """

:param self: 
:param request: 
:param conn: 
:return: """
        pass

    def get_instance_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def get_instance_name(self) -> str:
        """

:param self: 
:return: """
        pass

    def set_instance_name(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass

    def set_instance_name(self, value: str=None) -> None:
        """

:param self: 
:param value: 
:return: """
        pass


class ApplicationIface:
    """"""
    parent_iface: GObject.TypeInterface
    quit: typing.Any
    inspector: typing.Any
    toggle_window: typing.Any
    acquire_socket: typing.Any
    request: typing.Any
    get_instance_name: typing.Any
    set_instance_name: typing.Any
