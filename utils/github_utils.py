from git import Repo
import os

def clone_repo(git_url, clone_to="./repo"):
    if os.path.exists(clone_to):
        return clone_to

    #token = os.environ.get("GITHUB_TOKEN")
    token ="https://<your-username>:<your-token>@github.com/<your-username>/<repo>.git"
    if token:
        git_url = git_url.replace("https://", f"https://{token}@")

    Repo.clone_from(git_url, clone_to)
    return clone_to

def create_new_branch(repo_path, branch_name="openshift-migration"):
    repo = Repo(repo_path)
    git = repo.git
    git.checkout('-b', branch_name)
    return repo

def commit_and_push(repo, message="Added migration plan and OpenShift files"):
    repo.git.add(all=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push(refspec=f"{repo.active_branch.name}:{repo.active_branch.name}")
