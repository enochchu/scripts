def ffmpeg(args):
    err = None
    command = ["ffmpeg"] + args
    import subprocess
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,universal_newlines=True)

    for line in process.stdout:
        print(line)