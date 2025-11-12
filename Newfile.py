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
    """Run a shell command and print output"""
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

def commit_and_push(message="Automated commit from Newfile.py"):
    print("\n[2] Committing and pushing changes...")
    run_command("git add .")
    run_command(f'git commit -m "{message}"')
    run_command(f"git push origin {LOCAL_BRANCH}")

def open_live_site():
    print(f"\n[3] Opening live site: {DEPLOY_URL}")
    webbrowser.open(DEPLOY_URL)

def update_tracker_html():
    """Optional: Open tracker HTML to manually verify progress"""
    tracker_file = "ultimate-website-live-tracker.html"
    if os.path.exists(tracker_file):
        print(f"\nOpening tracker HTML: {tracker_file}")
        webbrowser.open(tracker_file)
    else:
        print("\nTracker HTML not found. Skipping manual check.")

# =========================
# Main Execution
# =========================
def main():
    print("=== Ultimate Website Deployment Tracker Automation ===")
    check_git_status()
    commit_and_push()
    open_live_site()
    update_tracker_html()
    print("\n✅ Automation completed. Check progress manually in ultimate-website-live-tracker.html")

if __name__ == "__main__":
    main()
