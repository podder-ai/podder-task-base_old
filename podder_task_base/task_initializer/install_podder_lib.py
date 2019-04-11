import io
import os
import subprocess
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import click
import requests


class InstallPodderLib(object):
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        url = self._get_download_url()
        file_path = self._download_from_s3(url)
        self._install_podder_lib(file_path)

    def _get_download_url(self) -> str:
        # [TODO] このurl設定部分は後からpodder-management-webからURLを取得する処理に差し替え
        url = "https://podder-test.s3.amazonaws.com/podder_lib-0.0.3.20190411-050820-py3-none-any.whl?Signature=LAgdb8%2FAJKfbO3A5uUrgZEDxR6A%3D&Expires=1557551302&AWSAccessKeyId=AKIA5KIWQTAA4EISQU65"
        return url

    def _download_from_s3(self, url: str) -> str:
        click.echo("Downloading the {}...".format(url))
        request = requests.get(url, stream=True)

        file_path = urlparse(url).path
        print(file_path)
        extract_path = Path("/root/").resolve().joinpath(Path(file_path).name)
        with extract_path.open("wb") as f:
            f.write(request.content)

        return str(extract_path)

    def _install_podder_lib(self, file_path: str) -> None:
        click.echo("Installing podder-lib...")

        command = ("pip3 install {}".format(file_path))
        p_status = self._execute_call(command)
        print(p_status)

    def _execute_call(self, command: str):
        click.echo(command)
        command_list = command.split(" ")

        p_status = subprocess.call(command_list)
        return p_status
