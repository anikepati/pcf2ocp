import os

def detect_app_type(project_path):
    files = os.listdir(project_path)
    if any(f.endswith(".csproj") for f in files):
        return "dotnet"
    elif any(f.endswith(".java") or f == "pom.xml" for f in files):
        return "java"
    return "unknown"

def generate_migration_plan(app_type, files):
    plan = []
    if app_type == "dotnet":
        plan.append("✅ .NET Core app detected.")
        plan.append("🔄 Replace Cloud Foundry buildpack with Dockerfile.")
        plan.append("🔐 Migrate VCAP_SERVICES to Kubernetes Secrets/ConfigMaps.")
        plan.append("📦 Use OpenShift ImageStream or container registry.")
    elif app_type == "java":
        plan.append("✅ Java Spring Boot app detected.")
        plan.append("🔄 Migrate Spring Cloud Connectors to Spring Config/Bindings.")
        plan.append("🔐 Replace VCAP_SERVICES with env vars or ConfigMaps.")
    else:
        plan.append("⚠️ Unknown project type. Manual review needed.")
    plan.append("🚀 Generate Kubernetes deployment + service YAML.")
    return "\n".join(plan)

def write_plan_to_file(plan_text, output_path):
    with open(os.path.join(output_path, "migration_plan.md"), "w") as f:
        f.write("# Migration Plan\n\n")
        f.write(plan_text)
