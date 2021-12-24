def main():
    parser = parse_arguments()
    repo = initialize_repository_object()
    clone_default_code_if_needed(parser, repo)
    remote = get_or_configure_starmart_git_remote(repo, parser)
    if is_deploy(parser):
        remote.push()


def parse_arguments():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('action', nargs=1, help='Run init on a new project, or deploy to push the code', default='None')
    parser.parse_args()
    return parser


def initialize_repository_object():
    from git import Repo, InvalidGitRepositoryError
    try:
        repo = Repo('.')
    except InvalidGitRepositoryError:
        repo = Repo.init('.')
    return repo


def clone_default_code_if_needed(parser, repo):
    # cloning the default repository
    if parser.get_default('action') == 'init':
        repo.clone('https://github.com/starmart-io/starmart.git')
        # starts the git repository without anyting
        repo.remotes.remove(repo.remote('origin'))


def get_or_configure_starmart_git_remote(repo, parser):
    # checking if there's already a remote called starmart
    remote = None
    for r in repo.remotes:
        if r.name == 'starmart':
            remote = r
            break
    # if there's not, add one
    if remote is None:
        import webbrowser
        from starmart.server.Server import server
        webbrowser.open(f'https://starmart.io/development/login')

        def callback(url):
            remote = repo.create_remote('starmart', url=url)
            if is_deploy(parser):
                remote.push()
                exit(0) # this is needed to exit flask server

        # this blocks because of the server. that's why I set a callback
        server(callback)
    return remote


def is_deploy(parser):
    return parser.get_default('action') == 'deploy'





if __name__ == '__main__':
    main()
