# coding: utf-8
# python: 3.7.5
from logging import getLogger, StreamHandler, Formatter, INFO
from pathlib import Path
import sys

from module.const import LOGGER_FMT, LOGGER_DATE_FMT
from module.gettoken import GetToken
from module.argprocess import getCommonArgs


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
    args = sys.argv[1:]
    description = "Pytest report to github pull request."
    args_dict = getCommonArgs(args, description)
    target_path: Path = args_dict['dir']

    logger.info('Getting github token.')
    gt = GetToken()
    access_token = gt.make_auth_header()

    # delete previous reviewdog comments
    # TODO: コメント削除をモジュール化する