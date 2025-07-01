# PCF to OpenShift Migration Agent

## Overview

This AI-powered agent:
- Clones a GitHub repo
- Analyzes .NET Core or Java apps using PCF
- Generates a migration plan
- Writes OpenShift YAML configs
- Pushes changes to a new branch

## Usage

```bash
uv venv  
source .venv/bin/activate
uv add -r requirements.txt
export OPENAI_API_KEY=your-api-key
python cli/main.py
