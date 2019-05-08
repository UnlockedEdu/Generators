import os
import logging
import logging.config


def setup_logging():
    """Setup logging configuration."""
    app_log_level = os.getenv('APP_LOG_LEVEL', 'DEBUG')
    log_dir = os.getenv('LOG_DIR', 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
            'simple': {
                'format': '[%(asctime)s] - (%(name)s) - [(%(module)s)] [%(levelname)s]: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'level': app_log_level,
                'formatter': 'simple',
                'stream': 'ext://sys.stdout',
            },
            'standard_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': app_log_level,
                'formatter': 'simple',
                'filename': os.path.join(log_dir, 'stdout.log'),
                'maxBytes': 10485760,
                'backupCount': '3',
                'encoding': 'utf8',
            },
            'error_file_handler': {
                'class': 'logging.handlers.RotatingFileHandler',
                'level': 'ERROR',
                'formatter': 'simple',
                'filename': os.path.join(log_dir, 'errors.log'),
                'maxBytes': 10485760,
                'backupCount': '3',
                'encoding': 'utf8',
            },
        },
        'root': {
            'level': app_log_level,
            'handlers': ['default', 'standard_file_handler', 'error_file_handler']
        }
    })


setup_logging()
logger = logging.getLogger(__name__)
