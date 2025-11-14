# generate-styles-supporting.py
import os

# Folder paths
folders = {
    "styles": "styles_config",
    "supporting": "supporting_files"
}

firebase_info = "Firebase Project: com.embroidery.jalabiya"

# Create folders if not exist
for folder in folders.values():
    os.makedirs(folder, exist_ok=True)

# --- Styles: style-1.css → style-15.css ---
for i in range(1, 16):
    filename = f"style-{i}.css"
    filepath = os.path.join(folders["styles"], filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""/* Style {i} – Mohammed Hamdan AlShehhi */
body {{
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f7;
}}
/* Placeholder for theme {i} and Firebase info: {firebase_info} */
""")
    print(f"Created {filename}")

# --- Config: config-1.json → config-15.json ---
for i in range(1, 16):
    filename = f"config-{i}.json"
    filepath = os.path.join(folders["styles"], filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""{{
    "config_name": "Config {i}",
    "description": "Placeholder configuration file",
    "firebase_project": "{firebase_info}"
}}""")
    print(f"Created {filename}")

# --- Supporting: README-1.md → README-10.md ---
for i in range(1, 11):
    filename = f"README-{i}.md"
    filepath = os.path.join(folders["supporting"], filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""# README {i}
Professional website documentation placeholder
Firebase Project: {firebase_info}
""")
    print(f"Created {filename}")

# --- Supporting: analytics-1.js → analytics-12.js ---
for i in range(1, 13):
    filename = f"analytics-{i}.js"
    filepath = os.path.join(folders["supporting"], filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"""// Analytics {i} – Mohammed Hamdan AlShehhi
// Placeholder for analytics, tracking, or logs
// Firebase Project: {firebase_info}
""")
    print(f"Created {filename}")

print("✅ All 52 pending files (Styles & Supporting) created successfully!")
