from gi.repository import AstalIO as AstalIO, GObject as GObject, Gio as Gio

class AppError:
    NAME_OCCUPIED: int
    TAKEOVER_FAILED: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def acquire_socket(app=None, sock=None):
    """    Starts a [class@Gio.SocketService] and binds `XDG_RUNTIME_DIR/astal/<instance_name>.sock`. This socket is then used by the astal 
    cli. Not meant for public usage, but for [method@AstalIO.Application.acquire_socket].
    @type app: AstalIO.Application
    @type sock: str
    @returns: 
    @rtype: Gio.SocketService
    """
def get_instances():
    """    Get a list of running Astal.Application instances. It is the equivalent of `astal --list`.
    @returns: 
    @rtype: GLib.List
    """
def quit_instance(instance=None):
    """    Quit an an Astal instances. It is the equivalent of `astal --quit -i instance`.
    @type instance: str
    @returns: 
    @rtype: None
    """
def open_inspector(instance=None):
    """    Open the Gtk debug tool of an an Astal instances. It is the equivalent of `astal --inspector -i instance`.
    @type instance: str
    @returns: 
    @rtype: None
    """
def toggle_window_by_name(instance=None, window=None):
    """    Toggle a Window of an Astal instances. It is the equivalent of `astal -i instance --toggle window`.
    @type instance: str
    @type window: str
    @returns: 
    @rtype: None
    """
def send_message(instance=None, request=None):
    """    Use [func@AstalIO.send_request] instead.
    @type instance: str
    @type request: str
    @returns: 
    @rtype: str
    """
def send_request(instance=None, request=None):
    '''    Send a request to an Astal instances. It is the equivalent of `astal -i instance "request content"`.
    @type instance: str
    @type request: str
    @returns: 
    @rtype: str
    '''
def read_sock(conn=None, _callback_=None, _callback__target=None):
    """    Read the socket of an Astal.Application instance.
    @type conn: Gio.SocketConnection
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def read_sock_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: str
    """
def write_sock(conn=None, response=None, _callback_=None, _callback__target=None):
    """    Write the socket of an Astal.Application instance.
    @type conn: Gio.SocketConnection
    @type response: str
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def write_sock_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: None
    """
def read_file(path=None):
    """    Read the contents of a file synchronously.
    @type path: str
    @returns: 
    @rtype: str
    """
def read_file_async(path=None, _callback_=None, _callback__target=None):
    """    Read the contents of a file asynchronously.
    @type path: str
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def read_file_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: str
    """
def write_file(path=None, content=None):
    """    Write content to a file synchronously.
    @type path: str
    @type content: str
    @returns: 
    @rtype: None
    """
def write_file_async(path=None, content=None, _callback_=None, _callback__target=None):
    """    Write content to a file asynchronously.
    @type path: str
    @type content: str
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def write_file_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: None
    """
def monitor_file(path=None, callback=None):
    """    Monitor a file for changes. If the path is a directory, monitor it recursively. The callback will be called passed two parameters: the path of 
    the file that changed and an [enum@Gio.FileMonitorEvent] indicating the reason.
    @type path: str
    @type callback: GObject.Closure
    @returns: 
    @rtype: Gio.FileMonitor
    """

class Daemon(Gio.Application, AstalIO.Application):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Daemon
        @rtype: Daemon
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Daemon
        @rtype: Daemon
        """
    def request(self, request=None, conn=None):
        """        Handler for an incoming request.
        @param request: Body of the request
        @param conn: The connection which expects the response.
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    def request(self, request=None, conn=None):
        """        Handler for an incoming request.
        @param request: Body of the request
        @param conn: The connection which expects the response.
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class DaemonClass:
    @property
    def parent_class(self): ...
    @property
    def request(self): ...

class DaemonPrivate: ...

class Process(GObject.Object):
    """`Process` provides shortcuts for [class@Gio.Subprocess] with sane defaults."""
    def __init__(self, cmd=None, cmd_length1=None) -> None:
        """        See [func@AstalIO.Process.subprocessv]
        @type cmd_length1: int
        @returns: Newly created Process
        @rtype: Process
        """
    @staticmethod
    def new(cmd=None, cmd_length1=None):
        """        See [func@AstalIO.Process.subprocessv]
        @type cmd_length1: int
        @returns: Newly created Process
        @rtype: Process
        """
    def kill(self):
        """        Force quit the subprocess.
        @returns: 
        @rtype: None
        """
    def signal(self, signal_num=None):
        """        Send a signal to the subprocess.
        @param signal_num: Signal number to be sent
        @type signal_num: int
        @returns: 
        @rtype: None
        """
    def write(self, _in=None):
        """        Write a line to the subprocess' stdin synchronously.
        @param _in: String to be written to stdin
        @type _in: str
        @returns: 
        @rtype: None
        """
    def write_async(self, _in=None, _callback_=None, _callback__target=None):
        """        Write a line to the subprocess' stdin asynchronously.
        @param _in: String to be written to stdin
        @type _in: str
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def write_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: None
        """
    @staticmethod
    def subprocessv(cmd=None, cmd_length1=None):
        """        Start a new subprocess with the given command.
        The first element of the vector is executed with the remaining elements as the argument list.
        @type cmd_length1: int
        @returns: 
        @rtype: AstalIO.Process
        """
    @staticmethod
    def subprocess(cmd=None):
        """        Start a new subprocess with the given command which is parsed using [func@GLib.shell_parse_argv].
        @type cmd: str
        @returns: 
        @rtype: AstalIO.Process
        """
    @staticmethod
    def execv(cmd=None, cmd_length1=None):
        """        Execute a command synchronously. The first element of the vector is executed with the remaining elements as the argument list.
        @type cmd_length1: int
        @returns: stdout of the subprocess
        @rtype: str
        """
    @staticmethod
    def exec(cmd=None):
        """        Execute a command synchronously. The command is parsed using [func@GLib.shell_parse_argv].
        @type cmd: str
        @returns: stdout of the subprocess
        @rtype: str
        """
    @staticmethod
    def exec_asyncv(cmd=None, cmd_length1=None, _callback_=None, _callback__target=None):
        """        Execute a command asynchronously. The first element of the vector is executed with the remaining elements as the argument list.
        @type cmd_length1: int
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: stdout of the subprocess
        @rtype: None
        """
    @staticmethod
    def exec_asyncv_finish(_res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: str
        """
    @staticmethod
    def exec_async(cmd=None, _callback_=None, _callback__target=None):
        """        Execute a command asynchronously. The command is parsed using [func@GLib.shell_parse_argv].
        @type cmd: str
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: stdout of the subprocess
        @rtype: None
        """
    @staticmethod
    def exec_finish(_res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: str
        """
    def get_argv(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ProcessClass:
    @property
    def parent_class(self): ...

class ProcessPrivate: ...

class Time(GObject.Object):
    """`Time` provides shortcuts for GLib timeout functions."""
    @staticmethod
    def interval_prio(interval=None, prio=None, fn=None):
        """        Start an interval timer with default Priority.
        @type interval: int
        @type prio: int
        @type fn: GObject.Closure
        @returns: Newly created Time
        @rtype: Time
        """
    @staticmethod
    def timeout_prio(timeout=None, prio=None, fn=None):
        """        Start a timeout timer with default Priority.
        @type timeout: int
        @type prio: int
        @type fn: GObject.Closure
        @returns: Newly created Time
        @rtype: Time
        """
    @staticmethod
    def idle_prio(prio=None, fn=None):
        """        Start an idle timer with default priority.
        @type prio: int
        @type fn: GObject.Closure
        @returns: Newly created Time
        @rtype: Time
        """
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created Time
        @rtype: Time
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created Time
        @rtype: Time
        """
    @staticmethod
    def interval(interval=None, fn=None):
        """        Start an interval timer. Ticks immediately then every `interval` milliseconds.
        @param interval: Tick every milliseconds.
        @param fn: Optional callback.
        @type interval: int
        @type fn: GObject.Closure
        @returns: 
        @rtype: AstalIO.Time
        """
    @staticmethod
    def timeout(timeout=None, fn=None):
        """        Start a timeout timer which ticks after `timeout` milliseconds.
        @param timeout: Tick after milliseconds.
        @param fn: Optional callback.
        @type timeout: int
        @type fn: GObject.Closure
        @returns: 
        @rtype: AstalIO.Time
        """
    @staticmethod
    def idle(fn=None):
        """        Start a timer which will tick when there are no higher priority tasks pending.
        @param fn: Optional callback.
        @type fn: GObject.Closure
        @returns: 
        @rtype: AstalIO.Time
        """
    def cancel(self):
        """        Cancel timer and emit [signal@AstalIO.Time::cancelled]
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class TimeClass:
    @property
    def parent_class(self): ...

class TimePrivate: ...

class VariableBase(GObject.Object):
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created VariableBase
        @rtype: VariableBase
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created VariableBase
        @rtype: VariableBase
        """
    def emit_changed(self):
        """        
        @returns: 
        @rtype: None
        """
    def emit_dropped(self):
        """        
        @returns: 
        @rtype: None
        """
    def emit_error(self, err=None):
        """        
        @type err: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class VariableBaseClass:
    @property
    def parent_class(self): ...

class VariableBasePrivate: ...

class Variable(AstalIO.VariableBase):
    def __init__(self, init=None) -> None:
        """        
        @type init: GObject.Value
        @returns: Newly created Variable
        @rtype: Variable
        """
    @staticmethod
    def new(init=None):
        """        
        @type init: GObject.Value
        @returns: Newly created Variable
        @rtype: Variable
        """
    def poll(self, interval=None, exec=None, transform=None):
        """        
        @type interval: int
        @type exec: str
        @type transform: GObject.Closure
        @returns: 
        @rtype: AstalIO.Variable
        """
    def pollv(self, interval=None, execv=None, execv_length1=None, transform=None):
        """        
        @type interval: int
        @type execv_length1: int
        @type transform: GObject.Closure
        @returns: 
        @rtype: AstalIO.Variable
        """
    def pollfn(self, interval=None, fn=None):
        """        
        @type interval: int
        @type fn: GObject.Closure
        @returns: 
        @rtype: AstalIO.Variable
        """
    def watch(self, exec=None, transform=None):
        """        
        @type exec: str
        @type transform: GObject.Closure
        @returns: 
        @rtype: AstalIO.Variable
        """
    def watchv(self, execv=None, execv_length1=None, transform=None):
        """        
        @type execv_length1: int
        @type transform: GObject.Closure
        @returns: 
        @rtype: AstalIO.Variable
        """
    def start_poll(self):
        """        
        @returns: 
        @rtype: None
        """
    def start_watch(self):
        """        
        @returns: 
        @rtype: None
        """
    def stop_poll(self):
        """        
        @returns: 
        @rtype: None
        """
    def stop_watch(self):
        """        
        @returns: 
        @rtype: None
        """
    def is_polling(self):
        """        
        @returns: 
        @rtype: bool
        """
    def is_watching(self):
        """        
        @returns: 
        @rtype: bool
        """
    def get_value(self, result=None):
        """        
        @type result: GObject.Value
        @returns: 
        @rtype: None
        """
    def set_value(self, value=None):
        """        
        @type value: GObject.Value
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class VariableClass:
    @property
    def parent_class(self): ...

class VariablePrivate: ...

class Application:
    """This interface is used internally in Astal3 and Astal4, not meant for public usage."""
    def quit(self):
        """        
        @returns: 
        @rtype: None
        """
    def quit(self):
        """        
        @returns: 
        @rtype: None
        """
    def inspector(self):
        """        
        @returns: 
        @rtype: None
        """
    def inspector(self):
        """        
        @returns: 
        @rtype: None
        """
    def toggle_window(self, window=None):
        """        
        @type window: str
        @returns: 
        @rtype: None
        """
    def toggle_window(self, window=None):
        """        
        @type window: str
        @returns: 
        @rtype: None
        """
    def acquire_socket(self):
        """        
        @returns: 
        @rtype: None
        """
    def acquire_socket(self):
        """        
        @returns: 
        @rtype: None
        """
    def request(self, request=None, conn=None):
        """        
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    def request(self, request=None, conn=None):
        """        
        @type request: str
        @type conn: Gio.SocketConnection
        @returns: 
        @rtype: None
        """
    def get_instance_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_instance_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_instance_name(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    def set_instance_name(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """

class ApplicationIface:
    @property
    def parent_iface(self): ...
    @property
    def quit(self): ...
    @property
    def inspector(self): ...
    @property
    def toggle_window(self): ...
    @property
    def acquire_socket(self): ...
    @property
    def request(self): ...
    @property
    def get_instance_name(self): ...
    @property
    def set_instance_name(self): ...
