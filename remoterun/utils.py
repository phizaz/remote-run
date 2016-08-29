def source_dir():
    from os.path import dirname
    return dirname(__file__)


def caller_dir():
    import os
    return os.getcwd()


def path_config():
    from os.path import join
    return join(caller_dir(), '.remoterunrc')


def path_lockfile():
    from os.path import join
    return join(caller_dir(), '.remoterun_lock')


def path_ignorefile():
    from os.path import join
    return join(caller_dir(), '.remoterunignore')


def path_default_ignorefile():
    from os.path import join
    return join(source_dir(), '.remoterunignore')


def path_default_config():
    from os.path import join
    return join(source_dir(), '.remoterunrc')


def load_config_path(path):
    from os.path import exists
    if not exists(path):
        return None
    with open(path) as handle:
        import yaml
        conf = yaml.load(handle)
    return conf


def load_config():
    return load_config_path(path_config())


def load_ignore():
    with open(path_ignorefile()) as handle:
        ignores = list(map(lambda x: x.strip(), handle.readlines()))
    return ignores


def load_lockfile():
    from os.path import exists
    if not exists(path_lockfile()):
        return None
    with open(path_lockfile()) as handle:
        content = handle.readline()
    return content


def save_lockfile(step):
    with open(path_lockfile(), 'w') as handle:
        handle.write(step)


def delete_lockfile():
    from os import remove
    remove(path_lockfile())


def get_current_step():
    return load_lockfile()


def merge_dict(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d


def injecting_vals(conf, arg):
    return merge_dict(conf, {'arg': arg})


def run_command_attach_output(command, shell=False):
    import subprocess
    import sys
    p = subprocess.Popen(command, stderr=sys.stderr, stdout=sys.stdout, stdin=sys.stdin, shell=shell)
    p.wait()
    if p.returncode is not 0:
        raise Exception('run_command_attach_output with command {} exit with {}'.format(command, p.returncode))
    return p.returncode


def run_command_with_terminal(command):
    raise NotImplementedError
