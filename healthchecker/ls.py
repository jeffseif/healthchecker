import subprocess

def ls():
    return subprocess.run(['ls', '-l'], stdout=subprocess.PIPE).stdout
