import os

features_folder = "features_pages"
os.makedirs(features_folder, exist_ok=True)

firebase_info = "Firebase Project: com.embroidery.jalabiya"

start_feature = 1
end_feature = 100

for i in range(start_feature, end_feature + 1):
    filename = f"feature-{i}.html"
    filepath = os.path.join(features_folder, filename)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Feature {i} – Mohammed Hamdan AlShehhi</title>
<link rel="stylesheet" href="../styles_config/style-professional.css">
<!-- {firebase_info} -->
</head>
<body>
<header><h1>Feature {i}</h1></header>
<section><p>Placeholder for Feature {i} content and UI components</p></section>
<footer>© Mohammed Hamdan AlShehhi | Dubai</footer>
</body>
</html>"""

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"✅ Created {filename}")
