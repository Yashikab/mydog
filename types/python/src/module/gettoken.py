# coding: utf=8
# python: 3.7
# token取得のメソッド

from datetime import datetime, timedelta
import jwt
from logging import getLogger, StreamHandler, Formatter, INFO
import os
import requests

from module.const import LOGGER_FMT, LOGGER_DATE_FMT


class GetToken:

    logger = getLogger('module').getChild(__class__.__name__)

    @classmethod
    def make_auth_header(cls) -> str:
        """ token取得

        INSTALLATION_ID, APP_IDを環境変数に入れておく
        """
        cls.logger.info('Start to get token.')
        installation_id = os.getenv('INSTALLATION_ID')
        utcnow = datetime.utcnow() + timedelta(seconds=-5)
        duration = timedelta(seconds=30)
        payload = {
            "iat": utcnow,
            "exp": utcnow + duration,
            "iss": os.getenv("APP_ID")
        }
        pem = cls._get_private_pem()
        encoded = jwt.encode(payload, pem, "RS256")
        headers = {
            "Authorization": "Bearer " + encoded.decode('utf-8'),
            "Accept": "application/vnd.github.machine-man-preview+json"
            }

        auth_url = \
            f"https://api.github.com/app/installations/{installation_id}/"\
            f"access_tokens"
        r = requests.post(auth_url, headers=headers)

        if not r.ok:
            cls.logger.error(r.json()['message'])
            r.raise_for_status()
        token = r.json()['token']
        cls.logger.info('Successfully get token.')
        return token

    def _get_private_pem(self) -> str:
        """Private keyの取得

        secretでPRIVATE_KEYを登録しておく
        """
        key = os.getenv("PRIVATE_KEY")
        return key


if __name__ == '__main__':
    handler = StreamHandler()
    fmt = Formatter(
        fmt=LOGGER_FMT,
        datefmt=LOGGER_DATE_FMT
    )
    handler.setFormatter(fmt)

    logger = getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(INFO)
    getLogger('module').addHandler(handler)
    getLogger('module').setLevel(INFO)

    logger.info('gettoken has called as script.')
    token = GetToken.make_auth_header()
    logger.info('save as file.')
    with open('/src/token.conf', 'w') as f:
        f.write(token)
    logger.info('done.')
