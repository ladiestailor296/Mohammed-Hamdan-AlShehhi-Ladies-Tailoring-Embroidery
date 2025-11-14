import os

folder = "../faq"
os.makedirs(folder, exist_ok=True)

for i in range(1, 31):
    filename = f"faq-{i}.html"
    content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FAQ {i}</title>
</head>
<body>
    <h1>FAQ {i}</h1>
    <p>Placeholder content for FAQ {i}. Answer your customer's common question here.</p>
</body>
</html>"""
    with open(os.path.join(folder, filename), "w") as f:
        f.write(content)

print("FAQ 1–30 files created successfully!")
