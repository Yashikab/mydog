# coding: utf-8
# python3.7.5
from github import Github
from logging import getLogger, StreamHandler, Formatter, INFO
import os
from pathlib import Path
import subprocess
import sys

from module.const import LOGGER_FMT, LOGGER_DATE_FMT
from module.gettoken import GetToken
from module.argprocess import getCommonArgs
from module.delcomments import deleteComments
from module import GithubControl

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
    description = "Reviewdog with python"
    args_dict = getCommonArgs(args, description)

    target_path: Path = args_dict['dir']
    logger.info(f"Target Path is {target_path}")

    logger.info('Getting github token.')
    gt = GetToken()
    access_token = gt.make_auth_header()

    # delete previous reviewdog comments
    logger.info('start to delete previous reviewdog comments.')

    g = Github(access_token)
    ghc = GithubControl(g)

    dog_marker = \
        '<sub>reported by [reviewdog]'\
        '(https://github.com/reviewdog/reviewdog) :dog:</sub>'
    ghc.deleteComments(g, dog_marker)

    # report by reviewdog
    logger.info('Report from reviewdog')

    os.environ["REVIEWDOG_GITHUB_API_TOKEN"] = access_token

    cmd1 = ["flake8", target_path]
    cmd2 = [
        "reviewdog",
        "-reporter=github-pr-review",
        "-f=pep8",
        "-diff=\"git diff master\""]
    pipe = subprocess.Popen(
        cmd1,
        stdout=subprocess.PIPE
    )
    reviewdog_result = subprocess.run(
        cmd2,
        stdin=pipe.stdout,
        stdout=subprocess.PIPE
    )

    review_list = reviewdog_result.stdout.decode().split('\n')
    # 末尾改行があるため取り除く
    del review_list[-1]
    if len(review_list) == 0:
        body_msg = f":100: All OK!\n{dog_marker}"
    else:
        body_msg = f"You received {len(review_list)} indications.\n "\
                   f"{dog_marker}"
    ghc.issue.create_comment(body_msg)


if __name__ == '__main__':
    main()
