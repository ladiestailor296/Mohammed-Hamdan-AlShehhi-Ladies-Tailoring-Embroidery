// ultimate-website-automation.js

// ----- Products Management -----
let products = [];

function addProduct(name, imgUrl, angles=[]) {
    const product = {name, imgUrl, angles};
    products.push(product);
    renderProducts();
    console.log('Product Added:', name);
}

function removeProduct(name) {
    products = products.filter(p => p.name !== name);
    renderProducts();
    console.log('Product Removed:', name);
}

// Render products in slider or 3D viewer
function renderProducts() {
    const container = document.getElementById('product-slider');
    container.innerHTML = '';
    products.forEach(p => {
        const img = document.createElement('img');
        img.src = p.imgUrl;
        img.alt = p.name;
        img.className = 'product-image';
        container.appendChild(img);
    });
}

// ----- Automatic Adjustment -----
function autoAdjustImage(img, brightness=1, contrast=1, saturation=1) {
    img.style.filter = `brightness(${brightness}) contrast(${contrast}) saturate(${saturation})`;
}

// Apply adjustments to all product images
function adjustAllProducts(brightness=1, contrast=1, saturation=1){
    document.querySelectorAll('.product-image').forEach(img => autoAdjustImage(img, brightness, contrast, saturation));
}

// ----- 3D Product Viewer -----
function rotate3DProduct(img, angles){
    let i = 0;
    setInterval(()=>{
        img.src = angles[i % angles.length];
        i++;
    }, 200);
}

// ----- Firebase Analytics -----
function logEvent(name, params={}){
    if(typeof analytics !== 'undefined') analytics.logEvent(name, params);
    console.log('Analytics Event:', name, params);
}

// ----- Example Usage -----
addProduct('Jalabiya 1','https://via.placeholder.com/600x400?text=Jalabiya+1');
addProduct('Jalabiya 2','https://via.placeholder.com/600x400?text=Jalabiya+2');
adjustAllProducts(1.2,1.1,1.3);
