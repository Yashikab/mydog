# coding: utf-8
# python: 3.7
from github import Github
from logging import getLogger

from module.const import (
    REPO_NAME,
    REPO_OWNER,
    ISSUE_NO
)


def deleteComments(gh: Github, marker: str) -> int:
    """markerが入るコメントを削除する

    Parameters
    ----------
        gh : Github
            pygithub
        marker : str
            コメント内にmarker文字列が含まれたらそのコメントを削除する

    Returns
    -------
        count : int
            削除したコメントの数
    """
    logger = getLogger('module').getChild(__name__)

    try:
        repo = gh.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
        issue = repo.get_issue(int(ISSUE_NO))
        pr = issue.as_pull_requjest()
    except Exception:
        raise Exception("Couldn't get github repo, issue, pr info.")

    # prのreview commentとissueのコメントの一覧を結合
    comment_list = list(issue.get_comments())
    comment_list += list(pr.get_review_comments())

    logger.info('start to delete previous target comments.')
    count = 0
    for comment in comment_list:
        if marker in comment.body:
            logger.debug(f'{comment.id} will be deleted.')
            comment.delete()
            count += 1
    logger.info(f'deleted {count} comments.')

    return count
