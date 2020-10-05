# coding: utf-8
# python: 3.7
from github import Github
from module import GithubControl
import pytest


class TestGithubControl:
    def test_gh_ctl_err(self):
        with pytest.raises(Exception):
            GithubControl(Github())

    def test_delcomments(self, mocker):

        # gh_mock = mocker.Mock(Github)
        # gh_mock.get_repo.return_value = Github.get_repo
        
        # gh_repo = gh_mock.get_repo()
        # gh_repo.return_value = 'Repository'
        # gh_issue = gh_repo.get_issue()
        # gh_issue.return_value = 'Issue'
        # gh_pr = gh_issue.as_pull_request()
        # gh_pr.return_value = 'PullRequest'

        # gh_issue.get_comments.return_value = ('test', 'a', 'b')
        # gh_pr.get_comments.return_value = ('c', 'test', 'd')

        ghc = GithubControl(gh_mock)
        cnt = ghc.del_comments('test')
        assert cnt == 2
