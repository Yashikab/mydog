# coding: utf-8
# python: 3.7
from github import Github
from logging import getLogger

from module.const import (
    REPO_NAME,
    REPO_OWNER,
    ISSUE_NO
)


class GithubControl:

    def __init__(self, gh: Github):
        self.logger = getLogger('module').getChild(__class__.__name__)

        try:
            self.repo = gh.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
            self.issue = self.repo.get_issue(int(ISSUE_NO))
            self.pr = self.issue.as_pull_request()
        except Exception as e:
            raise Exception(f"{e}")

    def del_comments(self, marker: str) -> int:
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

        # prのreview commentとissueのコメントの一覧を結合
        comment_list = list(self.issue.get_comments())
        comment_list += list(self.pr.get_review_comments())

        print(comment_list)
        self.logger.info('start to delete previous target comments.')
        count = 0
        for comment in comment_list:
            if marker in comment.body:
                self.logger.debug(f'{comment.id} will be deleted.')
                comment.delete()
                count += 1
        self.logger.info(f'deleted {count} comments.')

        return count
