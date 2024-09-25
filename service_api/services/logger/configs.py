from service_api.settings import RuntimeSettings


logger_configs = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "std_format": {
            "format": "[%(asctime)s %(name)s] [%(levelname)s] [%(module)s:%(funcName)s:%(lineno)s] %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": RuntimeSettings.log_level,
            "formatter": "std_format",
        }
    },
    "loggers": {
        "app": {
            "level": RuntimeSettings.log_level,
            "handlers": ["console"],
            "propagate": False,
        },
    },
}
