import logging.config
import structlog
from config import settings

from rich.logging import RichHandler
import traceback
from structlog.processors import TimeStamper


def remove_record_key(logger, method_name, event_dict):
    if "_record" in event_dict:
        del event_dict["_record"]
    if "_from_structlog" in event_dict:
        del event_dict["_from_structlog"]
    return event_dict

def format_for_GCP(logger, method_name, event_dict):
    event_dict['severity'] = event_dict.get('level', 'unknown').upper()
    event_dict['message'] = event_dict.get('event', 'unknown')

    # NOTE: We add the exec info string output to the "message" key so that GCP cloud logging can use it for log grouping/aggregation.
    # GCP CLoud logging does not look at the json payload for automated grouping. 
    # It only parses the string value "message" for automatic grouping.
    exc_info = event_dict.get("exc_info")
    if exc_info:
            # Extract and format the traceback
            traceback_string = "".join(traceback.format_exception(*exc_info))
            # Add the stack trace to the event message (or a separate key)
            event_dict['message'] += f"\n{traceback_string}"  # Modify as needed
    return event_dict


def extract_error_info(event):
  if "error" in event:
    error_data = event["error"]
    return {
      "error_code": error_data.get("code"),
      "error_message": error_data.get("message"),
    }
  return {}

   

def rich_handler_factory():
    return RichHandler(rich_tracebacks=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "plain": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                remove_record_key,
                structlog.dev.ConsoleRenderer(), 
                ],
        },
        "json": {
            "()": structlog.stdlib.ProcessorFormatter,
            "processors": [
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.stdlib.add_log_level,
                format_for_GCP,
                structlog.stdlib.PositionalArgumentsFormatter(),
                structlog.processors.UnicodeDecoder(),              
                structlog.processors.dict_tracebacks, 
                structlog.processors.JSONRenderer(),
                ],
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "json",
        },
        "rich": {
            "()": rich_handler_factory,    
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console" if not settings.dev_mode else "rich"],
    },
}

logging.config.dictConfig(LOGGING)





