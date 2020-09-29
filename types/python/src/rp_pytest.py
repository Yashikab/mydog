# coding: utf-8
# python: 3.7.5
import argparse
from logging import getLogger, StreamHandler, Formatter, INFO
import os
from pathlib import Path

from const import LOGGER_FMT, LOGGER_DATE_FMT
from module.gettoken import GetToken

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
    # TODO: この辺もモジュール化したい
    parser = argparse.ArgumentParser(
        description="Pytest report to github pull request."
    )
    parser.add_argument(
        'dir',
        type=Path,
        help='Input python path or file for review.'
    )
    args = parser.parse_args()
    target_dir: Path = args.dir
    target_dir = target_dir.resolve()

    logger.debug('Check whether target path exists.')
    if not target_dir.exists():
        raise FileNotFoundError(f"Path {target_dir} did not exist.")

    logger.info('Getting github token.')
    gt = GetToken()
    access_token = gt.make_auth_header()

    # delete previous reviewdog comments
    # TODO: コメント削除をモジュール化する