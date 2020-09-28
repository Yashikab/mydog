# coding: utf-8
# python3.7.5
import argparse
from github import Github
from logging import getLogger, StreamHandler, Formatter, INFO
import os
import subprocess

from const import LOGGER_FMT, LOGGER_DATE_FMT
from module.gettoken import GetToken

logger = getLogger(__name__)


def main():

    parser = argparse.ArgumentParser(
        description="Reviewdog with python"
    )

    parser.add_argument(
        '-d',
        '--dir',
        type=str,
        required=True
    )
    args = parser.parse_args()

    logger.info('Getting github token.')
    gt = GetToken()
    access_token = gt.make_auth_header()

    # delete previous reviewdog comments
    logger.info('start to delete previous reviewdog comments.')

    g = Github(access_token)

    repo_owner = os.getenv("DRONE_REPO_OWNER")
    repo_name = os.getenv("DRONE_REPO_NAME")
    issue_no = os.getenv("DRONE_PULL_REQUEST")

    repo = g.get_repo(f"{repo_owner}/{repo_name}")
    issue = repo.get_issue(int(issue_no))

    pr = issue.as_pull_request()
    # prのreview commentとissueのコメントの一覧を結合
    comment_list = list(issue.get_comments())
    comment_list += list(pr.get_review_comments())

    dog_marker = \
        '<sub>reported by [reviewdog]'\
        '(https://github.com/reviewdog/reviewdog) :dog:</sub>'

    for comment in comment_list:
        if dog_marker in comment.body:
            logger.debug(f'{comment.id} will be deleted.')
            comment.delete()
    logger.info('delete comments: done.')

    # report by reviewdog
    logger.info('Report from reviewdog')

    os.environ["REVIEWDOG_GITHUB_API_TOKEN"] = access_token

    cmd1 = ["flake8", args.dir]
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
    issue.create_comment(body_msg)


if __name__ == '__main__':
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

    main()
