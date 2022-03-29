from tqdm import tqdm
import requests


class ProgressBarDownloadError(Exception):
    pass


def download(url, filename="filename") -> None:
    r = requests.get(url, allow_redirects=True)

    block_size = 1024
    total_size_in_bytes = int(r.headers.get('content-length', 0))

    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    with open(filename, 'wb') as file:
        for data in r.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

    progress_bar.close()

    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        raise ProgressBarDownloadError("ProgressBarDownloadError: Cannot Get Total Size in Bytes")
