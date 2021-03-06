# RemoteRun

Running your script on a remote machine as if it were on your local one.

*By syncing your files on the local machine to the remote and executing from there.*

**RemoteRun** also provides the ability to **continue** from your last step, that means if you quit during the process you can do RemoteRun and continue from where you left!

# Installation

RemoteRun requires **Python 3** (python 2 might work), **rsync** and **ssh** installed on your system (and your path)

```
pip install remote-run
```

# Usage

```
cd /your/project/path
remoterun --init
```

This will initiate your `.remoterunrc` configuration file, and `.remoterunignore` ignore file (listing all the files that will not be transfered to the remote host). 

They should initially look like this:

For `.remtoerunrc` (YAML style) which will give you a good head-start. Note the `command` section will run a command in your local machine, and of course `remote` will run a command on your remote machine.

```
host: user@host
remote_path: /remote/path/without/trailing/slash

steps:
  - name: sync to the remote
    command: [rsync, -a, --exclude-from=.remoterunignore, ./, "{host}:{remote_path}"]
  - name: test echo on the remote
    remote: [echo, test]
  - name: sync back from the remote
    command: [rsync, -a, --exclude-from=.remoterunignore, "{host}:{remote_path}/", ./]
```

For `.remoterunignore`

```
.remoterunignore
.remoterun_lock
.remoterunrc
.git
.gitignore
.DS_Store
```

After you tailored all the configs for your project, just run `remoterun` and everything just works!

# Some Concrete Example

1. [Using RemoteRun with docker + docker-compose to run a python script.](https://gist.github.com/phizaz/34cd5383755dce33d6a13a3a1bcee4cf)
