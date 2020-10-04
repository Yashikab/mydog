# coding: utf-8
# python: 3.7
from github import Github
from module import GithubControl
import pytest


class TestGithubControl:
    def test_gh_ctl_err(self):
        with pytest.raises(Exception):
            GithubControl(Github())
