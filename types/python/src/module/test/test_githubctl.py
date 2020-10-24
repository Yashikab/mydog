# coding: utf-8
# python: 3.7
import dataclasses
from github import Github
from module import GithubControl
import pytest


@dataclasses.dataclass
class Comment:
    id: int
    body: str

    def delete(self):
        pass


class TestGithubControl:
    def test_gh_ctl_err(self):
        with pytest.raises(Exception):
            GithubControl(Github())

    def test_delcomments(self, mocker):
        mocker.patch.object(Github, "get_repo")
        mocker.patch.object(Github.get_repo().get_issue(),
                            "get_comments",
                            return_value=[Comment(id=1, body='test_gh'),
                                          Comment(id=2, body='test2'),
                                          Comment(id=3, body='test3')])
        mocker.patch.object(Github.get_repo().get_issue().as_pull_request(),
                            "get_review_comments",
                            return_value=[Comment(id=11, body='pr_test_gh'),
                                          Comment(id=12, body='pr_test2'),
                                          Comment(id=13, body='pr_test3')])
        com_del = mocker.patch.object(Comment, "delete")
        ghc = GithubControl(Github())
        ghc.del_comments('test_gh')
        assert com_del.call_count == 2
