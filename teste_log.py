import os
import logging
from logging.config import dictConfig
from os.path import abspath, dirname, join

# LOGGING_CONFIG = {
#     'version': 1,
#     'loggers': {
#         '': {  # root logger
#             'level': 'NOTSET',
#             'handlers': ['debug_console_handler', 'info_rotating_file_handler', 'error_file_handler', 'critical_mail_handler'],
#         },
#         'my.package': {
#             'level': 'WARNING',
#             'propagate': False,
#             'handlers': ['info_rotating_file_handler', 'error_file_handler'],
#         },
#     },
#     'handlers': {
#         'debug_console_handler': {
#             'level': 'DEBUG',
#             'formatter': 'info',
#             'class': 'logging.StreamHandler',
#             'stream': 'ext://sys.stdout',
#         },
#         'info_rotating_file_handler': {
#             'level': 'INFO',
#             'formatter': 'info',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': 'info.log',
#             'mode': 'a',
#             'maxBytes': 1048576,
#             'backupCount': 10
#         },
#         'error_file_handler': {
#             'level': 'WARNING',
#             'formatter': 'error',
#             'class': 'logging.FileHandler',
#             'filename': 'error.log',
#             'mode': 'a',
#         },
#         'critical_mail_handler': {
#             'level': 'CRITICAL',
#             'formatter': 'error',
#             'class': 'logging.handlers.SMTPHandler',
#             'mailhost' : 'localhost',
#             'fromaddr': 'monitoring@domain.com',
#             'toaddrs': ['dev@domain.com', 'qa@domain.com'],
#             'subject': 'Critical error with application name'
#         }
#     },
#     'formatters': {
#         'info': {
#             'format': '%(asctime)s-%(levelname)s-%(name)s::%(module)s|%(lineno)s:: %(message)s'
#         },
#         'error': {
#             'format': '%(asctime)s-%(levelname)s-%(name)s-%(process)d::%(module)s|%(lineno)s:: %(message)s'
#         },
#     },
#
# }

#dictConfig(LOGGING_CONFIG)

#logging.info("testing an info log entry with LOGGING_CONFIG")
#logging.warning("testing a warning log entry with LOGGING_CONFIG")

base_dir = abspath(dirname(__file__))
logs_target = join(base_dir + "/logs", "python_logs.log")

logging_schema = {
    # Always 1. Schema versioning may be added in a future release of logging
    "version": 1,
    # "Name of formatter" : {Formatter Config Dict}
    "formatters": {
        # Formatter Name
        "standard": {
            # class is always "logging.Formatter"
            "class": "logging.Formatter",
            # Optional: logging output format
            "format": "%(asctime)s\t%(levelname)s\t%(filename)s\t%(message)s",
            # Optional: asctime format
            "datefmt": "%d %b %y %H:%M:%S"
        }
    },
    # Handlers use the formatter names declared above
    "handlers": {
        # Name of handler
        "console": {
            # The class of logger. A mixture of logging.config.dictConfig() and
            # logger class-specific keyword arguments (kwargs) are passed in here.
            "class": "logging.StreamHandler",
            # This is the formatter name declared above
            "formatter": "standard",
            "level": "INFO",
            # The default is stderr
            "stream": "ext://sys.stdout"
        },
        # Same as the StreamHandler example above, but with different
        # handler-specific kwargs.
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "standard",
            "level": "INFO",
            "filename": logs_target,
            "mode": "a",
            "encoding": "utf-8",
            "maxBytes": 500000,
            "backupCount": 4
        }
    },
    # Loggers use the handler names declared above
    "loggers": {
        "": {
            # Use a list even if one handler is used
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False
        }
    },
    # Just a standalone kwarg for the root logger
    "root": {
        "level": "INFO",
        "handlers": ["file"]
    }
}

dictConfig(logging_schema)
logging.info("testing an info log entry with logging_schema")
logging.warning("testing a warning log entry with logging_schema")
