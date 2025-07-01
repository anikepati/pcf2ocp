import click
from utils.github_utils import clone_repo, create_new_branch, commit_and_push
from analyzers.pcf_analyzer import find_manifest_and_code
from agents.migration_agent import analyze_pcf_file
from generators.openshift_generator import generate_openshift_deployment
from migration_plan.planner import detect_app_type, generate_migration_plan, write_plan_to_file
from dotenv import load_dotenv
import os

    # Load environment variables from .env file
load_dotenv()
DBName =os.getenv('DATABASE_URL')
@click.command()
@click.option("--repo-url", prompt="GitHub repo URL", help="Public GitHub repo to analyze")
def run_migration(repo_url):
    print("🔁 Cloning repo...")
    repo_path = clone_repo(repo_url)

    print("🔍 Scanning for PCF files...")
    files = find_manifest_and_code(repo_path)

    for file in files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            print(f"🧠 Analyzing {file} ...")
            result = analyze_pcf_file(content)
            print(result)

    print("🧠 Detecting app type...")
    app_type = detect_app_type(repo_path)
    plan = generate_migration_plan(app_type, files)
    write_plan_to_file(plan, repo_path)

    print("🚀 Generating OpenShift Deployment YAML")
    yaml = generate_openshift_deployment(app_name="my-app", image="my-image")
    with open(f"{repo_path}/openshift_deployment.yaml", 'w') as f:
        f.write(yaml)

    print("📦 Creating new branch and committing changes...")
    repo = create_new_branch(repo_path)
    commit_and_push(repo)
    print("✅ Migration complete and pushed to new branch!")

if __name__ == "__main__":
    run_migration()
