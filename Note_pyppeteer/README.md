使用pyppeteer截图

```
pip install pyppeteer
```


需要修改 connnection.py, 默认20s会关闭窗口

```
self._ws = websockets.client.connect(
            self._url, max_size=None, loop=self._loop, ping_interval=None, ping_timeout=None)
```

提示:

> [0505/060845.882080:ERROR:zygote_host_impl_linux.cc(89)] Running as root without --no-sandbox is not supported.

[参考:http://wyq.me/](http://wyq.me/){:target="_blank"}

修改lancher.py 


```
self.chrome_args.extend([
                '--headless',
                '--disable-gpu',
                '--hide-scrollbars',
                '--mute-audio',
                '--no-sandbox',
            ])
```

Linux 下首次使用pypeteer, 提示urllib3 ssl错误, 可修改 chrimium_downloader.py

```
import certifi

def download_zip(url: str) -> BytesIO:
    """Download data from url."""
    logger.warning('start chromium download.\n'
                   'Download may take a few minutes.')

    # disable warnings so that we don't need a cert.
    # see https://urllib3.readthedocs.io/en/latest/advanced-usage.html for more
    urllib3.disable_warnings()

    with urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                             ca_certs=certifi.where()) as http:
```

也可以自行下载对应版本的chromium

根据以下代码, 获取安装路径和版本号:

```
from pyppeteer import __chromium_revision__, __pyppeteer_home__
from pathlib import Path
import os

DOWNLOADS_FOLDER = Path(__pyppeteer_home__) / 'local-chromium'

REVISION = os.environ.get('PYPPETEER_CHROMIUM_REVISION', __chromium_revision__)

print(DOWNLOADS_FOLDER)

print(REVISION)
```

