import subprocess

# =========================
# Configuration
# =========================
BRANCH = "main"
COMMIT_MESSAGE = (
    "Auto commit: Updated all new and changed files for full website update"
)

# =========================
# Helper Function
# =========================
def run_command(cmd):
    """Run a shell command and print output/errors."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

# =========================
# Main Flow
# =========================
def main():
    print("=== Auto Git Commit & Push Script v2 ===")
    
    # Stage all new and modified files
    run_command("git add -A")
    
    # Commit changes
    run_command(f'git commit -m "{COMMIT_MESSAGE}"')
    
    # Push to remote
    run_command(f"git push origin {BRANCH}")
    
    print("\n✅ All new and changed files committed and pushed successfully!")

if __name__ == "__main__":
    main()
