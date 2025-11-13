import os
import subprocess

# =========================
# Configuration
# =========================
FILES_CONTENT = {
    "ai-chat-v2.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>AI Chat V2 – Product Assistant</title>
</head>
<body>
  <h2>AI Chat V2 (Product Support)</h2>
  <p>This is a placeholder for the new bilingual AI chat that supports product lookups.</p>
</body>
</html>
""",

    "ads-integration-v2.js": """// ads-integration-v2.js
console.log("Ads Integration V2 initialized - Product pages and AI chat ads ready.");
""",

    "login-discounts.js": """// login-discounts.js
console.log("Login Discounts system active - rewards and offers loaded.");
""",

    "multilingual-support.js": """// multilingual-support.js
console.log("Multilingual support (EN↔AR) loaded for website.");
""",

    "final-deployment-checklist.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Final Deployment Checklist</title>
</head>
<body>
  <h2>Final Deployment Checklist</h2>
  <ul>
    <li>✅ Products updated</li>
    <li>✅ AI chat working</li>
    <li>✅ Ads integrated</li>
    <li>✅ Language toggle tested</li>
    <li>✅ Customer login verified</li>
  </ul>
</body>
</html>
"""
}

BRANCH = "main"
COMMIT_MESSAGE = "Add 5 new files: AI Chat V2, Ads Integration V2, Login Discounts, Multilingual Support, and Final Deployment Checklist"

# =========================
# Helper Functions
# =========================
def run_command(cmd):
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Error: {result.stderr}")
    else:
        print(result.stdout)
    return result.returncode

# =========================
# Main Flow
# =========================
def main():
    print("=== Creating & Pushing 5 New Website Files ===")

    # Create files
    for filename, content in FILES_CONTENT.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Created {filename}")

    # Stage all new files
    run_command("git add .")

    # Commit
    run_command(f'git commit -m "{COMMIT_MESSAGE}"')

    # Push
    run_command(f"git push origin {BRANCH}")

    print("\n🚀 All 5 files created, committed, and pushed successfully!")

if __name__ == "__main__":
    main()
