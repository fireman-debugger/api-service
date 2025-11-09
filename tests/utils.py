# utils.py

import logging
import datetime
from typing import List, Dict

class DateTimeUtil:
    @staticmethod
    def get_current_date_time() -> str:
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class LoggerUtil:
    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

class StringUtil:
    @staticmethod
    def is_empty(s: str) -> bool:
        return s is None or s.strip() == ""

    @staticmethod
    def to_camel_case(s: str) -> str:
        words = s.split("_")
        return words[0] + "".join(word.capitalize() for word in words[1:])

class ListUtil:
    @staticmethod
    def get_unique_elements(lst: List) -> List:
        return list(set(lst))

class DictUtil:
    @staticmethod
    def get_key_by_value(dictionary: Dict, value) -> str:
        for key, val in dictionary.items():
            if val == value:
                return key
        return None