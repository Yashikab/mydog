# coding: utf-8
# python: 3.7
from github import Github
import module
from module import (
    const,
    GithubControl
)
import pytest
import os


class TestGithubControl:
    def test_gh_ctl_err(self):
        with pytest.raises(Exception):
            GithubControl(Github())

    def test_delcomments(self, mocker, monkeypatch):

        # gh_mock = mocker.Mock(Github)
        # rp_mock = mocker.Mock(Repository)
        # issue_mock = mocker.Mock(Issue)
        # mocker.patch.object(Github, "get_repo", return_value=rp_mock)
        # gh_issue_mock = mocker.patch.object(rp_mock, "get_issue", return_value=issue_mock)
        # gh_pr = mocker.patch.object(Issue, "as_pull_request")

        # gh_issue_mock.get_comments.return_value = ('test', 'a', 'b')
        # gh_pr.get_comments.return_value = ('c', 'test', 'd')
        
        mocker.patch.object(module.const, "ISSUE_NO", "840")
        mocker.patch.object(Github, "get_repo")
        mocker.patch.object(Github.get_repo().get_issue(),
                            "get_comments",
                            return_value=('test', 'a', 'b'))
        ghc = GithubControl(Github())
        cnt = ghc.del_comments('test')
        assert cnt == 2
