def ffmpeg(args):
    err = None
    command = ["ffmpeg"] + args
    import subprocess
    ffmpeg = subprocess.Popen(command)

    while err == None:
        out, err = ffmpeg.communicate()

        import time
        time.sleep(1)

    if err:
        print(" ".join(command))
        raise Exception(err)