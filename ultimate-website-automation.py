# ultimate-website-automation.py
# Auto-image adjustments, batch Git commit, unlimited products

from PIL import Image, ImageEnhance
import os, subprocess

# ----- Automatic Image Adjustment -----
def adjust_image(input_path, output_path, brightness=1.0, contrast=1.0, saturation=1.0):
    img = Image.open(input_path).convert('RGB')
    img = ImageEnhance.Brightness(img).enhance(brightness)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    img = ImageEnhance.Color(img).enhance(saturation)
    img.save(output_path)
    print(f"Adjusted Image Saved: {output_path}")

# ----- Batch Git Commit -----
def git_commit_all(message="Auto Commit"):
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', message])
    subprocess.run(['git', 'push'])
    print("Git Commit & Push Done")

# ----- Example Usage -----
if __name__ == "__main__":
    # Adjust multiple product images
    product_folder = "products_images"
    for filename in os.listdir(product_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            adjust_image(os.path.join(product_folder, filename),
                         os.path.join(product_folder, "adjusted_"+filename),
                         brightness=1.2, contrast=1.1, saturation=1.3)
    
    # Commit changes to Git
    git_commit_all("Professional: Auto-adjusted all product images & pushed")
