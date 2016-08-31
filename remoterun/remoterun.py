from __future__ import print_function

__version__ = '0.6'

def run_local(command, conf, arg):
    from . import utils
    _command = list(map(lambda x: x.format(**utils.injecting_vals(conf, arg)), command))
    print('exec: "{}"'.format(' '.join(_command)))
    code = utils.run_command_attach_output(_command)
    return code


def run_remote(command, conf, arg):
    from . import utils
    serialized_command = ' '.join(command).format(**utils.injecting_vals(conf, arg))
    print('remote exec: "{}"'.format(serialized_command))
    _command = [
        'ssh', '-T', conf['host'], '"cd {remote_path} && {command}"'.format(
            remote_path=conf['remote_path'],
            command=serialized_command
        )
    ]
    code = utils.run_command_attach_output(' '.join(_command), shell=True)
    return code

def run(arg):
    from . import utils
    conf = utils.load_config()
    if conf is None:
        raise Exception('no config found, .remoterunrc might not be created')

    assert 'host' in conf, '`host` is not defined'
    assert 'remote_path' in conf, '`remote_path` is not defined'
    assert 'steps' in conf, '`steps` is not defined'
    assert isinstance(conf['steps'], list), '`steps` must be a list'

    for step in conf['steps']:
        assert isinstance(step, dict), 'each `step` must be a dict'
        assert 'name' in step, '`step.name` is not defined'
        if 'command' in step:
            assert isinstance(step['command'], list)
        if 'remote' in step:
            assert isinstance(step['remote'], list)
        if 'command' not in step and 'remote' not in step:
            raise AssertionError('`step` should have either `command` or `remote`')

    current_step = utils.get_current_step()

    if current_step is None:
        current_step = conf['steps'][0]['name']
        utils.save_lockfile(current_step)

    all_steps = list(map(lambda x: x['name'], conf['steps']))
    if current_step not in all_steps:
        raise Exception('step {} not found in the .remoterunrc'.format(current_step))

    print('RemoteRun start running at step {}'.format(current_step))

    start = False
    for i, step in enumerate(conf['steps'], 1):
        if step['name'] == current_step:
            start = True

        if not start:
            continue

        utils.save_lockfile(step['name'])
        if 'command' in step:
            print('({}/{}) running "{}"'.format(i, len(conf['steps']), step['name']))
            run_local(step['command'], conf, arg)
        elif 'remote' in step:
            print('({}/{}) remote running "{}"'.format(i, len(conf['steps']), step['name']))
            run_remote(step['remote'], conf, arg)

    utils.delete_lockfile()

    print('RemoteRun finished!')

def init():
    from shutil import copy
    from . import utils
    print('creating initial config file .remoterunrc')
    copy(utils.path_default_config(), utils.path_config())
    print('creating initial ignore file .remoterunignore')
    copy(utils.path_default_ignorefile(), utils.path_ignorefile())

def main():
    import argparse
    parser = argparse.ArgumentParser('RemoteRun (v. {})'.format(__version__))
    parser.add_argument('arg', nargs='*', help='arguments passed to the .remoterunrc file, using by {arg[x]}')
    parser.add_argument('--init', default=False, action='store_true',
                        help='init the required files in the current directory')
    args = parser.parse_args()
    if args.init:
        init()
    else:
        run(args.arg)