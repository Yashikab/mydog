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
            self.__repo = gh.get_repo(f"{REPO_OWNER}/{REPO_NAME}")
            self.__issue = self.__repo.get_issue(int(ISSUE_NO))
            self.__pr = self.__issue.as_pull_request()
        except Exception as e:
            raise Exception(f"{e}")

    def del_comments(self, marker: str) -> None:
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
        comment_list = list(self.__issue.get_comments())
        comment_list += list(self.__pr.get_review_comments())

        self.logger.info('start to delete previous target comments.')

        for comment in comment_list:
            if marker in comment.body:
                self.logger.debug(f'{comment.id} will be deleted.')
                comment.delete()
        self.logger.info('deleted comments.')

    def create_comment(self, body: str) -> None:
        self.__issue.create_comment(body)
