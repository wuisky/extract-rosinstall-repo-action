# extract-rosinstall-repo-action
This is a github action to extract repositories info in .rosinstall files.

## Input

```yaml
inputs:
  path:
    description: 'Path to start recursive find *.rosinstall file'
    required: false
    default: '.'
 ```
 
## Output

```yaml
outputs:
  stdout:
    description: 'The stdout output of the action'
```

### Output note

This action will parse all files with extension ".rosinstall" that is recursively found from path "inputs.path",
and merge all repository information into one string which is split by space.
For example, if you have a hoge.rosinstall file like:

```yaml
- git: {local-name: local-repoA, uri: 'git@github.com:userA/repoA.git', version: main}
- git: {local-name: local-repoB, uri: 'git@github.com:userB/repoB.git', version: master}
- git: {local-name: local-repoC, uri: 'git@github.com:userC/repoC.git', version: debug}
```

"outputs.stdout" will be:

```bash
userA/repoA@main userB/repoB@master userC/repoC@debug
```
Then you can use another action "wuisky/checkout@multi-repos" to checkout them at once.

## Usage

```yaml
name: checkout multiple repos
on: [pull_request]
jobs:
  multi_checkout:
    name: multi_checkout
    runs-on: ubuntu-latest
    steps:
      # assume that there is a .rosinstall file in your repo
      - name: checkout self repo
        uses: actions/checkout@v3
        with:
          path: src/${{ github.event.repository.name }}

      - name: parse rosinstall file
        id: find_repos
        uses:  wuisky/extract-rosinstall-repo-action@main
        with:
          path: .
          
      - name: checkout repos
        uses: wuisky/checkout@multi-repos
        with:
          path: src
          repositories: ${{ steps.find_repos.outputs.stdout }}
```
