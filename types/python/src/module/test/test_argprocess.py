# coding: utf-8
# python: 3.7

from pathlib import Path
import pytest
from module.argprocess import getCommonArgs


class TestGetCommonArgs:

    def test_getCommonArgs(self):
        description = "Test world"
        target_path = Path('./')
        target_abs_path = target_path.resolve()
        args = [str(target_path)]
        args_dict = getCommonArgs(args, description)

        assert args_dict['path'] == target_abs_path

    def test_getCommonArgs_err(self):
        description = "Test world"
        target_path = Path('../hogeee')
        args = [str(target_path)]
        with pytest.raises(FileNotFoundError):
            getCommonArgs(args, description)
