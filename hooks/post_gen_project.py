import os
import subprocess

def init_git_repository():
    current_dir = os.getcwd()
    subprocess.run(['git', 'init'], cwd=current_dir)
    subprocess.run(['git', 'add', '.'], cwd=current_dir)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], cwd=current_dir)
    print('Git repository initialized.')

if __name__ == '__main__':
    init_git_repository()