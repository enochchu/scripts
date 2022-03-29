class ParamError(Exception):
    pass


def download_by_m3u8(url=None, filename="temp.mp4"):
    if url is None:
        raise ParamError('ParamError: No Referer URL')

    try:
        cmd = ['-i', url,
               '-bsf:a', 'aac_adtstoasc',
               '-vcodec', 'copy',
               '-c', 'copy',
               '-crf', '50', filename]

        from ffmpeg import ffmpeg
        ffmpeg(args=cmd)
    except OSError as e:
        return e.strerror
