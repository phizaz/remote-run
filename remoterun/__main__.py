if __name__ == '__main__':
    from .remoterun import __version__, run, init
    import argparse
    parser = argparse.ArgumentParser('RemoteRun (v. {})'.format(__version__))
    parser.add_argument('--init', default=False, action='store_true', help='init the required files in the current directory')
    args = parser.parse_args()
    if args.init:
        init()
    else:
        run()