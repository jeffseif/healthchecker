import psutil


def stats():
    cpu = (100 - (
        psutil
        .cpu_times_percent()
        .idle
    ))
    memory = (
        psutil
        .virtual_memory()
        .percent
    )
    users = sorted({user.name for user in psutil.users()})
    disk = (
        psutil
        .disk_usage('/')
        .percent
    )
    return f'''\
    CPU: {cpu:.0f}%
    Mem: {memory:.0f}%
    Disk: {disk:.0f}%
    Users: {users}
    '''
