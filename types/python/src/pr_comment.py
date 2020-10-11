# coding: utf-8
# python: 3.7.5
from github import Github
from logging import getLogger, StreamHandler, Formatter, INFO
from pathlib import Path
import sys

from module.const import LOGGER_FMT, LOGGER_DATE_FMT
from module import (
    GetToken,
    getCommonArgs,
    GithubControl
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
    args = sys.argv[1:]
    description = "Comment to Issue with target file."
    args_dict = getCommonArgs(args, description)
    filepath: Path = args_dict["path"]
    logger.info(f"Target Path is {filepath}")

    logger.info('Getting github token.')
    access_token = GetToken.make_auth_header()

    logger.info('make body')
    with open(filepath, 'r') as f:
        msg_body = f.read()

    ghc = GithubControl(access_token)
    logger.info('insert comment.')
    ghc.create_comment(msg_body)


if __name__ == '__main__':
    main()
