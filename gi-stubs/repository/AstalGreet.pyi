from gi.repository import AstalGreet as AstalGreet, GObject as GObject

class ErrorType:
    AUTH_ERROR: int
    ERROR: int

class AuthMessageType:
    VISIBLE: int
    SECRET: int
    INFO: int
    ERROR: int

MAJOR_VERSION: int
MINOR_VERSION: int
MICRO_VERSION: int
VERSION: str

def login(username=None, password=None, cmd=None, _callback_=None, _callback__target=None):
    """    Shorthand for creating a session, posting the password, and starting the session with the given `cmd` which is parsed with [func@
    GLib.shell_parse_argv].
    @param username: User to login to
    @param password: Password of the user
    @param cmd: Command to start the session with
    @type username: str
    @type password: str
    @type cmd: str
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def login_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: None
    """
def login_with_env(username=None, password=None, cmd=None, env=None, env_length1=None, _callback_=None, _callback__target=None):
    """    Same as [func@AstalGreet.login] but allow for setting additonal env in the form of `name=value` pairs.
    @param username: User to login to
    @param password: Password of the user
    @param cmd: Command to start the session with
    @param env: Additonal env vars to set for the session
    @type username: str
    @type password: str
    @type cmd: str
    @type env_length1: int
    @type _callback_: Gio.AsyncReadyCallback
    @type _callback__target: gpointer
    @returns: 
    @rtype: None
    """
def login_with_env_finish(_res_=None):
    """    
    @type _res_: Gio.AsyncResult
    @returns: 
    @rtype: None
    """

class Request(GObject.Object):
    """Base Request type."""
    def send(self, _callback_=None, _callback__target=None):
        """        Send this request to greetd.
        @type _callback_: Gio.AsyncReadyCallback
        @type _callback__target: gpointer
        @returns: 
        @rtype: None
        """
    def send_finish(self, _res_=None):
        """        
        @type _res_: Gio.AsyncResult
        @returns: 
        @rtype: AstalGreet.Response
        """
    def get_type_name(self):
        """        
        @returns: 
        @rtype: str
        """
    def get_type_name(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class RequestClass:
    @property
    def parent_class(self): ...

class RequestPrivate: ...

class CreateSession(AstalGreet.Request):
    """Creates a session and initiates a login attempted for the given user. The session is ready to be started if a success is returned."""
    def __init__(self, username=None) -> None:
        """        
        @type username: str
        @returns: Newly created CreateSession
        @rtype: CreateSession
        """
    @staticmethod
    def new(username=None):
        """        
        @type username: str
        @returns: Newly created CreateSession
        @rtype: CreateSession
        """
    def get_username(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_username(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class CreateSessionClass:
    @property
    def parent_class(self): ...

class CreateSessionPrivate: ...

class PostAuthMesssage(AstalGreet.Request):
    """Answers an authentication message. If the message was informative (info, error), then a response does not need to be set in this 
message. The session is ready to be started if a success is returned."""
    def __init__(self, response=None) -> None:
        """        
        @type response: str
        @returns: Newly created PostAuthMesssage
        @rtype: PostAuthMesssage
        """
    @staticmethod
    def new(response=None):
        """        
        @type response: str
        @returns: Newly created PostAuthMesssage
        @rtype: PostAuthMesssage
        """
    def get_response(self):
        """        
        @returns: 
        @rtype: str
        """
    def set_response(self, value=None):
        """        
        @type value: str
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class PostAuthMesssageClass:
    @property
    def parent_class(self): ...

class PostAuthMesssagePrivate: ...

class StartSession(AstalGreet.Request):
    """Requests for the session to be started using the provided command line, adding the supplied environment to that created by PAM. The session 
will start after the greeter process terminates"""
    def __init__(self, cmd=None, cmd_length1=None, env=None, env_length1=None) -> None:
        """        
        @type cmd_length1: int
        @type env_length1: int
        @returns: Newly created StartSession
        @rtype: StartSession
        """
    @staticmethod
    def new(cmd=None, cmd_length1=None, env=None, env_length1=None):
        """        
        @type cmd_length1: int
        @type env_length1: int
        @returns: Newly created StartSession
        @rtype: StartSession
        """
    def get_cmd(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def set_cmd(self, value=None, value_length1=None):
        """        
        @type value_length1: int
        @returns: 
        @rtype: None
        """
    def get_env(self, result_length1=None):
        """        
        @type result_length1: int
        @rtype: None
        """
    def set_env(self, value=None, value_length1=None):
        """        
        @type value_length1: int
        @returns: 
        @rtype: None
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class StartSessionClass:
    @property
    def parent_class(self): ...

class StartSessionPrivate: ...

class CancelSession(AstalGreet.Request):
    """Cancels the session that is currently under configuration."""
    def __init__(self, **kwargs) -> None:
        """        
        @returns: Newly created CancelSession
        @rtype: CancelSession
        """
    @staticmethod
    def new():
        """        
        @returns: Newly created CancelSession
        @rtype: CancelSession
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class CancelSessionClass:
    @property
    def parent_class(self): ...

class CancelSessionPrivate: ...

class Response(GObject.Object):
    """Base Response type."""
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ResponseClass:
    @property
    def parent_class(self): ...

class ResponsePrivate: ...

class Success(AstalGreet.Response):
    """Indicates that the request succeeded."""
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class SuccessClass:
    @property
    def parent_class(self): ...

class SuccessPrivate: ...

class Error(AstalGreet.Response):
    """Indicates that the request succeeded."""
    def get_error_type(self):
        """        
        @returns: 
        @rtype: AstalGreet.ErrorType
        """
    def get_description(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class ErrorClass:
    @property
    def parent_class(self): ...

class ErrorPrivate: ...

class AuthMessage(AstalGreet.Response):
    """Indicates that the request succeeded."""
    def get_message_type(self):
        """        
        @returns: 
        @rtype: AstalGreet.AuthMessageType
        """
    def get_message(self):
        """        
        @returns: 
        @rtype: str
        """
    @property
    def parent_instance(self): ...
    @property
    def priv(self): ...

class AuthMessageClass:
    @property
    def parent_class(self): ...

class AuthMessagePrivate: ...
