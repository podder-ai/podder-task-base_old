import io
import os
import subprocess
import zipfile
from pathlib import Path
from urllib.parse import urlparse

import click
import requests
import pip._internal


class PodderLibInstall(object):
    def __init__(self, download_url:str) -> None:
        if download_url == '':
            download_url = os.environ.get('DOWNLOAD_URL')
        if download_url == '' or download_url == None:
            click.secho("Must set download_url!", fg='red')
            raise ValueError

        # download_url = "https://podder-downloads.s3.amazonaws.com/podder-lib/podder_lib-0.0.3-py3-none-any.whl?AWSAccessKeyId=AKIA3TKXHAVOFQ6RYZ6S&Signature=TkZkKt3vZOblQKUt8eIJ%2Bihb8I4%3D&Expires=1556280420"
        self.download_url = download_url

    def execute(self) -> None:
        file_path = self._download_from_s3(self.download_url)
        self._install_podder_lib(file_path)

    def _download_from_s3(self, url: str) -> str:
        click.echo("Downloading the podder_lib...")
        request = requests.get(url, stream=True)

        file_path = urlparse(url).path
        extract_path = Path.home().resolve().joinpath(Path(file_path).name)
        with extract_path.open("wb") as f:
            f.write(request.content)

        return str(extract_path)

    def _install_podder_lib(self, file_path: str) -> None:
        click.echo("Uninstalling podder-lib (interface package)...")
        pip._internal.main(['uninstall', 'podder-lib', '-y'])

        click.echo("Installing podder-lib (full package)...")
        pip._internal.main(['install', file_path])
