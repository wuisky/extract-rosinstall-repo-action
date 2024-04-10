#!/usr/bin/env python3
import argparse
import os
from typing import Generator

import yaml


def find_files_with_extension(directory: str, extension: str) -> Generator:
    if os.path.isfile(directory):
        yield directory

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                yield file_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',
                        '--path',
                        help='root path start to find *.rosinstall recursively',
                        default='./')
    args = parser.parse_args()
    repo_list = []
    for rosinstall_file in find_files_with_extension(args.path, '.rosinstall'):
        # print(rosinstall_file)
        with open(rosinstall_file, encoding='utf-8') as file:
            rosinstall_config = yaml.load(file, Loader=yaml.SafeLoader)
            for item in rosinstall_config:
                git_url = item['git']['uri']
                branch = item['git']['version']
                # print(f'{git_url} at {branch}')
                # self.check_repository_access(git_url, branch, g)a
                owner, repo_name_with_dot_git = git_url.split(':')[1].split('/')[-2:]
                repo_name = os.path.splitext(repo_name_with_dot_git)[0]
                # print(f'{owner}/{repo_name}@{branch}')
                repo_list.append(f'{owner}/{repo_name}@{branch}')
    result = ' '.join(repo_list)
    print(result)


if __name__ == '__main__':
    main()
