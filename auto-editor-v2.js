// auto-editor.js

// Function: Adjust image automatically
function adjustImage(imgElement) {
    // Resize image
    imgElement.width = 300;
    imgElement.height = 400;

    // Canvas filter for brightness and contrast
    const canvas = document.createElement('canvas');
    canvas.width = imgElement.width;
    canvas.height = imgElement.height;
    const ctx = canvas.getContext('2d');

    ctx.filter = 'brightness(1.2) contrast(1.1)';
    ctx.drawImage(imgElement, 0, 0, imgElement.width, imgElement.height);

    // Replace original image with adjusted image
    imgElement.src = canvas.toDataURL();
}

// Apply adjustment to all product images
document.querySelectorAll('#products-container img').forEach(img => adjustImage(img));
