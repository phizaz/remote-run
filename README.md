# RemoteRun

Running your script on a remote machine as if it were on your local one.

*By syncing your files on the local machine to the remote one.*

**RemoteRun** also provide the ability to **continue** from your last step, that means if you quit during the process you can do RemoteRun and continue from where you left!

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

This will initiate your `.remoterunrc` configuration file, and `.remoterunignore` igonre file (listing all the files that will not be transfered to the remote host). 

They should initially look like this

For `.remtoerunrc` (YAML style) which will give you a good head-start. Note the `command` section will run a command in your local machine, and ofcourse `remote` will run a command on your remote machine.

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

