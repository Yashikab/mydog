# coding: utf-8
# python: 3.7
from module.delcomments import deleteComments
from github import Github
import pytest


class TestDelComments:
    def test_delComments_err(self):
        with pytest.raises(Exception):
            deleteComments(Github(), '')
