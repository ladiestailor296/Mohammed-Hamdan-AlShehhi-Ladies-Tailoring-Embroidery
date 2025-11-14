# auto-commit-website-files.py
import os
import subprocess

# Folders to commit
folders_to_commit = [
    "products_pages",
    "features_pages",
    "templates_pages"
]

# Commit message
commit_message = "Add all professional HTML files – Products 1–150, Features 1–100, Templates 1–100 with Firebase placeholders"

# Add folders to git
for folder in folders_to_commit:
    if os.path.exists(folder):
        subprocess.run(["git", "add", folder])
        print(f"✅ Staged folder: {folder}")
    else:
        print(f"⚠️ Folder not found: {folder}")

# Commit changes
subprocess.run(["git", "commit", "-m", commit_message])
print(f"✅ Commit done with message:\n{commit_message}")

# Push to main branch
subprocess.run(["git", "push", "origin", "main"])
print("🚀 Pushed all changes to GitHub (main branch)")
