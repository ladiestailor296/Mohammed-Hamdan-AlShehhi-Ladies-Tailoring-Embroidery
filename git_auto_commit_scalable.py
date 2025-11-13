import subprocess

# =========================
# Configuration
# =========================
FILES_TO_COMMIT = [
    "newsletter-signup.html",
    "newsletter-handler.js",
    "analytics-tracker.js",
    "faq.html",
    "support-chat.js",
    "products.html",
    "index.html",
    "contact-map.js",
    "multilingual-support.js",
    "login-discounts.js",
    "customers.html"
    # Aage aur files add kar sakte ho
]

BRANCH = "main"

# =========================
# Helper Functions
# =========================
def run_command(cmd):
    """Run a shell command and print output."""
    print(f"> {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr.strip()}")
    else:
        print(f"✅ {result.stdout.strip()}")
    return result.returncode

def ensure_branch(branch):
    """Check if branch exists, if not create it."""
    result = subprocess.run(f"git rev-parse --verify {branch}", shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"⚠️ Branch '{branch}' does not exist. Creating it...")
        run_command(f"git checkout -b {branch}")
    else:
        print(f"🌿 Branch '{branch}' exists. Switching to it...")
        run_command(f"git checkout {branch}")

def generate_commit_message(files):
    """Generate commit message from file list."""
    if not files:
        return "Update repository"
    summary = ", ".join(files[:5])
    if len(files) > 5:
        summary += f", and {len(files)-5} more files"
    return f"Auto-update: {summary}"

# =========================
# Main Flow
# =========================
def main():
    print("=== Git Scalable Auto Commit & Push Script ===\n")

    if not FILES_TO_COMMIT:
        print("⚠️ No files specified to commit. Exiting.")
        return

    # Ensure branch exists
    ensure_branch(BRANCH)

    # Stage all files
    for file in FILES_TO_COMMIT:
        run_command(f"git add {file}")

    # Generate commit message automatically
    commit_message = generate_commit_message(FILES_TO_COMMIT)
    print(f"\n💬 Commit message: {commit_message}\n")

    # Commit
    run_command(f'git commit -m "{commit_message}"')

    # Push
    run_command(f"git push origin {BRANCH}")

    print("\n🎉 All files committed and pushed successfully!")

if __name__ == "__main__":
    main()
