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
    def __init__(self) -> None:
        pass

    def execute(self) -> None:
        url = self._get_download_url()
        file_path = self._download_from_s3(url)
        self._install_podder_lib(file_path)

    def _get_download_url(self) -> str:
        click.echo("Downloading podder_lib url...")
        # [TODO] このurl設定部分は後からpodder-management-webからURLを取得する処理に差し替え
        # api_request_url = "http://*****/****/***"
        # request = requests.get(api_request_url, stream=True)
        # download_url = request.text
        download_url = "https://podder-lib-download.s3.amazonaws.com/podder_lib-0.0.3-py3-none-any.whl?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIA3TKXHAVOFQ6RYZ6S%2F20190417%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20190417T074808Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=8106346113379603b63decece1a7b7efbaffd64bcbd457281e5808a71615f24e"

        return download_url

    def _download_from_s3(self, url: str) -> str:
        click.echo("Downloading the podder_lib...")
        request = requests.get(url, stream=True)

        file_path = urlparse(url).path
        extract_path = Path("/root/").resolve().joinpath(Path(file_path).name)
        with extract_path.open("wb") as f:
            f.write(request.content)

        return str(extract_path)

    def _install_podder_lib(self, file_path: str) -> None:
        click.echo("Uninstalling podder-lib (interface package)...")
        pip._internal.main(['uninstall', 'podder-lib'])

        click.echo("Installing podder-lib (full package)...")
        pip._internal.main(['install', file_path])
