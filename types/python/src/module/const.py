# coding: utf-8
# python: 3.7
import os

LOGGER_FMT = '[%(asctime)s] %(name)s %(levelname)s: %(message)s'
LOGGER_DATE_FMT = '%Y-%m-%d %H:%M:%S'

REPO_OWNER = os.getenv("DRONE_REPO_OWNER")
REPO_NAME = os.getenv("DRONE_REPO_NAME")
ISSUE_NO = os.getenv("DRONE_PULL_REQUEST")
