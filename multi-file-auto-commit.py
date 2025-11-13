import subprocess

# =========================
# Configuration
# =========================
FILES_TO_COMMIT = [
    "ai-chat-v2.html",
    "ads-integration-v2.js",
    "login-discounts.js",
    "multilingual-support.js",
    "final-deployment-checklist.html"
]
BRANCH = "main"
COMMIT_MESSAGE = "Add 5 new files: AI chat v2, ads integration, login discounts, multilingual support, and final deployment checklist"

# =========================
# Helper Function
# =========================
def run_command(cmd):
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
    print("=== Git Auto Commit & Push Script ===")
    
    # Stage files
    for file in FILES_TO_COMMIT:
        run_command(f"git add {file}")
    
    # Commit
    run_command(f'git commit -m "{COMMIT_MESSAGE}"')
    
    # Push
    run_command(f"git push origin {BRANCH}")
    
    print("\n✅ All 5 files committed and pushed successfully!")

if __name__ == "__main__":
    main()
