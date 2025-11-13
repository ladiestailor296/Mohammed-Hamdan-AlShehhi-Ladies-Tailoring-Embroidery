import subprocess

# =========================
# Configuration
# =========================
ALL_FILES = [
    "professional-website-features-tracker.html",
    "products.html",
    "auto-editor.js",
    "auto-editor-v2.js",
    "ai-chat.html",
    "ai-chat-v2.html",
    "ads-integration.js",
    "ads-integration-v2.js",
    "index.html",
    "contact-map.js",
    "multilingual-support.js",
    "login-discounts.js",
    "customers.html",
    "newsletter-signup.html",
    "newsletter-handler.js",
    "analytics-tracker.js",
    "faq.html",
    "support-chat.js"
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

def select_files(files):
    """Allow user to select files to commit."""
    print("\n📂 Available files to commit:\n")
    for i, file in enumerate(files, 1):
        print(f"{i}. {file}")
    print("\nEnter file numbers separated by comma (e.g., 1,3,5) or 'all' for all files:")
    choice = input("Your choice: ").strip()
    if choice.lower() == "all":
        return files
    selected = []
    for num in choice.split(","):
        try:
            idx = int(num.strip()) - 1
            if 0 <= idx < len(files):
                selected.append(files[idx])
        except ValueError:
            continue
    return selected

def get_commit_message(default_msg):
    """Prompt user for custom commit message or use default."""
    print(f"\nDefault commit message: '{default_msg}'")
    msg = input("Enter custom commit message or press Enter to use default: ").strip()
    return msg if msg else default_msg

# =========================
# Main Flow
# =========================
def main():
    print("=== Advanced Git Commit & Push Script ===\n")

    ensure_branch(BRANCH)

    # Select files
    files_to_commit = select_files(ALL_FILES)
    if not files_to_commit:
        print("⚠️ No files selected. Exiting.")
        return

    # Stage files
    for file in files_to_commit:
        run_command(f"git add {file}")

    # Commit message
    default_msg = f"Auto-update: {', '.join(files_to_commit[:5])}" + (f", and {len(files_to_commit)-5} more files" if len(files_to_commit) > 5 else "")
    commit_msg = get_commit_message(default_msg)

    # Commit
    run_command(f'git commit -m "{commit_msg}"')

    # Push
    run_command(f"git push origin {BRANCH}")

    print("\n🎉 Selected files committed and pushed successfully!")

if __name__ == "__main__":
    main()
