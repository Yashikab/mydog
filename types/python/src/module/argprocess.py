import argparse
from pathlib import Path
from typing import Dict


def getCommonArgs(argv: list,
                  description: str = 'Command description') -> Dict[str, Path]:
    """ スクリプト共通の引数オプションなどを記述

    Parameters
    ----------
    description : str
        paserの説明(helpで参照される部分の追加)

    Returns
    -------
    parser : argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(
        description=description
    )
    parser.add_argument(
        'dir',
        type=Path,
        help='Input python path or file.'
    )

    args = parser.parse_args(argv)

    target_path: Path = args.dir
    target_path = target_path.resolve()

    if not target_path.exists():
        raise FileNotFoundError(f"Path {target_path} did not exist.")

    args_dict = {
        'dir': target_path
    }

    return args_dict
