# Configuration file for jupyterhub.

#------------------------------------------------------------------------------
# Configurable configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# SingletonConfigurable configuration
#------------------------------------------------------------------------------

# A configurable that only allows one instance.
# 
# This class is for classes that should only have one instance of itself or
# *any* subclass. To create and retrieve such a class use the
# :meth:`SingletonConfigurable.instance` method.

#------------------------------------------------------------------------------
# Application configuration
#------------------------------------------------------------------------------

# This is an application.

# The Logging format template
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Set the log level by value or name.
# c.Application.log_level = 30

# The date format used by logging formatters for %(asctime)s
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

#------------------------------------------------------------------------------
# JupyterHub configuration
#------------------------------------------------------------------------------

# An Application for starting a Multi-User Jupyter Notebook server.

# DEPRECATED, use Authenticator.admin_users instead.
# c.JupyterHub.admin_users = traitlets.Undefined

# The Proxy Auth token.
# 
# Loaded from the CONFIGPROXY_AUTH_TOKEN env variable by default.
# c.JupyterHub.proxy_auth_token = ''

# The ip for this process
# c.JupyterHub.hub_ip = 'localhost'

# File in which to store the cookie secret.
# c.JupyterHub.cookie_secret_file = 'jupyterhub_cookie_secret'

# Answer yes to any questions (e.g. confirm overwrite)
# c.JupyterHub.answer_yes = False

# Path to SSL certificate file for the public facing interface of the proxy
# 
# Use with ssl_key
# c.JupyterHub.ssl_cert = ''

# The public facing ip of the proxy
# c.JupyterHub.ip = ''

# Purge and reset the database.
# c.JupyterHub.reset_db = False

# The public facing port of the proxy
c.JupyterHub.port = 80

# Paths to search for jinja templates.
# c.JupyterHub.template_paths = traitlets.Undefined

# The port for this process
# c.JupyterHub.hub_port = 8081

# Generate default config file
# c.JupyterHub.generate_config = False

# Grant admin users permission to access single-user servers.
# 
# Users should be properly informed if this is enabled.
# c.JupyterHub.admin_access = False

# File to write PID Useful for daemonizing jupyterhub.
c.JupyterHub.pid_file = '/run/jupyterhub.pid'

# show debug output in configurable-http-proxy
# c.JupyterHub.debug_proxy = False

# Include any kwargs to pass to the database connection. See
# sqlalchemy.create_engine for details.
# c.JupyterHub.db_kwargs = traitlets.Undefined

# The base URL of the entire application
# c.JupyterHub.base_url = '/'

# Class for authenticating users.
# 
# This should be a class with the following form:
# 
# - constructor takes one kwarg: `config`, the IPython config object.
# 
# - is a tornado.gen.coroutine
# - returns username on success, None on failure
# - takes two arguments: (handler, data),
#   where `handler` is the calling web.RequestHandler,
#   and `data` is the POST form data from the login page.
# c.JupyterHub.authenticator_class = <class 'jupyterhub.auth.PAMAuthenticator'>

# Number of days for a login cookie to be valid. Default is two weeks.
# c.JupyterHub.cookie_max_age_days = 14

# Set a logging.FileHandler on this file.
# c.JupyterHub.extra_log_file = ''

# The ip for the proxy API handlers
# c.JupyterHub.proxy_api_ip = 'localhost'

# The prefix for the hub server. Must not be '/'
# c.JupyterHub.hub_prefix = '/hub/'

# The location of jupyterhub data files (e.g. /usr/local/share/jupyter/hub)
# c.JupyterHub.data_files_path = '/usr/local/share/jupyter/hub'

# Extra log handlers to set on JupyterHub logger
# c.JupyterHub.extra_log_handlers = traitlets.Undefined

# Whether to shutdown single-user servers when the Hub shuts down.
# 
# Disable if you want to be able to teardown the Hub while leaving the single-
# user servers running.
# 
# If both this and cleanup_proxy are False, sending SIGINT to the Hub will only
# shutdown the Hub, leaving everything else running.
# 
# The Hub should be able to resume from database state.
# c.JupyterHub.cleanup_servers = True

# Whether to shutdown the proxy when the Hub shuts down.
# 
# Disable if you want to be able to teardown the Hub while leaving the proxy
# running.
# 
# Only valid if the proxy was starting by the Hub process.
# 
# If both this and cleanup_servers are False, sending SIGINT to the Hub will
# only shutdown the Hub, leaving everything else running.
# 
# The Hub should be able to resume from database state.
# c.JupyterHub.cleanup_proxy = True

# The cookie secret to use to encrypt cookies.
# 
# Loaded from the JPY_COOKIE_SECRET env variable by default.
# c.JupyterHub.cookie_secret = b''

# 
# c.JupyterHub.tornado_settings = traitlets.Undefined

# The command to start the http proxy.
# 
# Only override if configurable-http-proxy is not on your PATH
# c.JupyterHub.proxy_cmd = traitlets.Undefined

# Interval (in seconds) at which to check if the proxy is running.
# c.JupyterHub.proxy_check_interval = 30

# Path to SSL key file for the public facing interface of the proxy
# 
# Use with ssl_cert
# c.JupyterHub.ssl_key = ''

# The port for the proxy API handlers
# c.JupyterHub.proxy_api_port = 0

# Supply extra arguments that will be passed to Jinja environment.
# c.JupyterHub.jinja_environment_options = traitlets.Undefined

# url for the database. e.g. `sqlite:///jupyterhub.sqlite`
# c.JupyterHub.db_url = 'sqlite:///jupyterhub.sqlite'

# log all database transactions. This has A LOT of output
# c.JupyterHub.debug_db = False

# The class to use for spawning single-user servers.
# 
# Should be a subclass of Spawner.
# c.JupyterHub.spawner_class = <class 'jupyterhub.spawner.LocalProcessSpawner'>

# The config file to load
# c.JupyterHub.config_file = 'jupyterhub_config.py'

# Interval (in seconds) at which to update last-activity timestamps.
# c.JupyterHub.last_activity_interval = 300

#------------------------------------------------------------------------------
# LoggingConfigurable configuration
#------------------------------------------------------------------------------

# A parent class for Configurables that log.
# 
# Subclasses have a log trait, and the default behavior is to get the logger
# from the currently running Application.

#------------------------------------------------------------------------------
# Spawner configuration
#------------------------------------------------------------------------------

# Base class for spawning single-user notebook servers.
# 
# Subclass this, and override the following methods:
# 
# - load_state - get_state - start - stop - poll

# The notebook directory for the single-user server
# 
# `~` will be expanded to the user's home directory
# c.Spawner.notebook_dir = ''

# Interval (in seconds) on which to poll the spawner.
# c.Spawner.poll_interval = 30

# Timeout (in seconds) before giving up on a spawned HTTP server
# 
# Once a server has successfully been spawned, this is the amount of time we
# wait before assuming that the server is unable to accept connections.
# c.Spawner.http_timeout = 30

# Whitelist of environment variables for the subprocess to inherit
# c.Spawner.env_keep = traitlets.Undefined

# Timeout (in seconds) before giving up on the spawner.
# 
# This is the timeout for start to return, not the timeout for the server to
# respond. Callers of spawner.start will assume that startup has failed if it
# takes longer than this. start should return when the server process is started
# and its location is known.
# c.Spawner.start_timeout = 60

# Enable debug-logging of the single-user server
# c.Spawner.debug = False

# The IP address (or hostname) the single-user server should listen on
# c.Spawner.ip = 'localhost'

# The command used for starting notebooks.
# c.Spawner.cmd = traitlets.Undefined

# Extra arguments to be passed to the single-user server
c.Spawner.args = [ "--matplotlib=inline" ]

#------------------------------------------------------------------------------
# LocalProcessSpawner configuration
#------------------------------------------------------------------------------

# A Spawner that just uses Popen to start local processes.

# Seconds to wait for process to halt after SIGINT before proceeding to SIGTERM
# c.LocalProcessSpawner.INTERRUPT_TIMEOUT = 10

# Seconds to wait for process to halt after SIGTERM before proceeding to SIGKILL
# c.LocalProcessSpawner.TERM_TIMEOUT = 5

# Seconds to wait for process to halt after SIGKILL before giving up
# c.LocalProcessSpawner.KILL_TIMEOUT = 5

#------------------------------------------------------------------------------
# Authenticator configuration
#------------------------------------------------------------------------------

# A class for authentication.
# 
# The API is one method, `authenticate`, a tornado gen.coroutine.

# set of usernames of admin users
# 
# If unspecified, only the user that launches the server will be admin.
c.Authenticator.admin_users = { 'bioinfo' }

# Username whitelist.
# 
# Use this to restrict which users can login. If empty, allow any user to
# attempt login.
# c.Authenticator.whitelist = traitlets.Undefined

#------------------------------------------------------------------------------
# LocalAuthenticator configuration
#------------------------------------------------------------------------------

# Base class for Authenticators that work with local *ix users
# 
# Checks for local users, and can attempt to create them if they exist.

# Automatically whitelist anyone in this group.
# c.LocalAuthenticator.group_whitelist = traitlets.Undefined

# If a user is added that doesn't exist on the system, should I try to create
# the system user?
c.LocalAuthenticator.create_system_users = True

#------------------------------------------------------------------------------
# PAMAuthenticator configuration
#------------------------------------------------------------------------------

# Authenticate local *ix users with PAM

# The encoding to use for PAM
# c.PAMAuthenticator.encoding = 'utf8'

# The PAM service to use for authentication.
# c.PAMAuthenticator.service = 'login'
