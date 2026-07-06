import os
import json
import pandas as pd

errors = []
project_dirs = [d for d in os.listdir('.') if d.startswith('project-') and os.path.isdir(d)]

print(f"Found {len(project_dirs)} projects: {project_dirs}")

for project in project_dirs:
    readme = os.path.join(project, 'README.md')
    if not os.path.exists(readme):
        errors.append(f"MISSING README: {readme}")
    else:
        print(f"OK: {readme}")

    data_dir = os.path.join(project, 'data')
    if os.path.exists(data_dir):
        files = [f for f in os.listdir(data_dir) if not f.startswith('.')]
        print(f"OK: {project}/data/ — {len(files)} files")
        for f in files:
            fpath = os.path.join(data_dir, f)
            try:
                if f.endswith('.xlsx'):
                    df = pd.read_excel(fpath, nrows=5)
                    print(f"  OK: {f} — {len(df.columns)} columns")
                elif f.endswith('.csv'):
                    df = pd.read_csv(fpath, nrows=5)
                    print(f"  OK: {f} — {len(df.columns)} columns")
                elif f.endswith('.json'):
                    with open(fpath) as jf:
                        json.load(jf)
                    print(f"  OK: {f} — valid JSON")
            except Exception as e:
                errors.append(f"ERROR reading {fpath}: {e}")

if errors:
    print("\nVALIDATION ERRORS:")
    for e in errors:
        print(f"  {e}")
    raise SystemExit(1)

print(f"\nAll assets validated across {len(project_dirs)} projects.")
