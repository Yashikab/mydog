# coding: utf-8
# python: 3.7.5
from github import Github
from logging import getLogger, StreamHandler, Formatter, INFO
from pathlib import Path
import subprocess
import sys

from module.const import LOGGER_FMT, LOGGER_DATE_FMT
from module import (
    GetToken,
    getCommonArgs,
    GithubControl,
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
    description = "Pytest report to github pull request."
    args_dict = getCommonArgs(args, description)
    target_path: Path = args_dict['dir']
    logger.info(f"Target Path is {target_path}")

    logger.info('Getting github token.')
    gt = GetToken()
    access_token = gt.make_auth_header()

    # delete previous pytest comments
    logger.info('start to delete previous pytest comments.')
    g = Github(access_token)
    ghc = GithubControl(g)
    marker = \
        '<sub>reported by [pytest]'\
        '(https://docs.pytest.org/en/stable/) :police:</sub>'
    ghc.del_comments(marker)

    # report from pytest
    # pytest_filepath = Path.cwd().joinpath("pytest_raw.xml")
    pytest_result = subprocess.run(
        ["pytest", f"--cov={target_path}", "--cov-branch"],
        stdout=subprocess.PIPE)

    pytest_outfmt = pytest_result.stdout.decode()

    body_msg = (
        "## Test Coverage\n"
        "```"
        f"{pytest_outfmt}"
        "```\n\n"
        f"{marker}"
    )
    logger.info(body_msg)
    ghc.issue.create_comment(body_msg)


if __name__ == '__main__':
    main()
