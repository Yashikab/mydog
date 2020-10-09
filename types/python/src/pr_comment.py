# coding: utf-8
# python: 3.7.5
from logging import getLogger, StreamHandler, Formatter, INFO
from module.const import LOGGER_FMT, LOGGER_DATE_FMT
from module import (
    GetToken,
    getCommonArgs
)

logger = getLogger(__name__)
handler = StreamHandler()
fmt = Formatter(
    fmt=LOGGER_FMT,
    datefmt=LOGGER_DATE_FMT
)
handler.setFormatter(fmt)

logger.addHandler(handler)
logger.setLevel(INFO)
getLogger('module').addHandler(handler)
getLogger('module').setLevel(INFO)


def main():
    # args = sys.argv[1:]
    pass
