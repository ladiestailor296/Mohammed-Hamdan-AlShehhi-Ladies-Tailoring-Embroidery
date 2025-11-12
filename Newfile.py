import os
import subprocess
import webbrowser

# =========================
# Configuration
# =========================
GITHUB_REPO = "https://github.com/ladiestailor296/Mohammed-Hamdan-AlShehhi-Ladies-Tailoring-Embroidery.git"
LOCAL_BRANCH = "main"
DEPLOY_URL = "https://ladiestailor296.github.io/Mohammed-Hamdan-AlShehhi-Ladies-Tailoring-Embroidery/"

# =========================
# Functions
# =========================
def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

def check_git_status():
    print("\n[1] Checking git status...")
    run_command("git status")

def commit_and_push():
    print("\n[2] Committing and pushing changes...")
    run_command('git add .')
    run_command('git commit -m "Automated commit from Newfile.py"')
    run_command(f"git push origin {LOCAL_BRANCH}")

def open_live_site():
    print(f"\n[3] Opening live site: {DEPLOY_URL}")
    webbrowser.open(DEPLOY_URL)

def main():
    print("=== Ultimate Website Deployment Tracker Automation ===")
    check_git_status()
    commit_and_push()
    open_live_site()
    print("\n✅ Automation completed. Check progress manually in ultimate-website-master-tracker.html")

if __name__ == "__main__":
    main()
