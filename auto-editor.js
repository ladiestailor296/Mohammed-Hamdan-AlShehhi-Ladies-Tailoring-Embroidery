// auto-editor.js - v30+ full automation
// Images, Videos, 3D models

// --- IMAGE ADJUSTMENT ---
function adjustImage(img) {
    img.width = 300;
    img.height = 400;

    const canvas = document.createElement('canvas');
    canvas.width = img.width;
    canvas.height = img.height;
    const ctx = canvas.getContext('2d');

    ctx.filter = 'brightness(1.2) contrast(1.1)';
    ctx.drawImage(img, 0, 0, img.width, img.height);

    img.src = canvas.toDataURL();
}

// --- VIDEO ADJUSTMENT ---
function adjustVideo(video) {
    video.width = 300;
    video.height = 400;
    video.autoplay = true;
    video.muted = true;
    video.loop = true;
}

// --- 3D MODEL PREVIEW ---
function init3DModel(modelContainer) {
    if (typeof THREE === 'undefined') return;

    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, modelContainer.clientWidth / modelContainer.clientHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(modelContainer.clientWidth, modelContainer.clientHeight);
    modelContainer.appendChild(renderer.domElement);

    const loader = new THREE.GLTFLoader();
    const url = modelContainer.dataset.model;
    loader.load(url, function(gltf) {
        scene.add(gltf.scene);
        camera.position.z = 5;

        const animate = function () {
            requestAnimationFrame(animate);
            gltf.scene.rotation.y += 0.01;
            renderer.render(scene, camera);
        };
        animate();
    });
}

// --- APPLY TO ALL PRODUCTS ---
document.querySelectorAll('#products-container img').forEach(adjustImage);
document.querySelectorAll('#products-container video').forEach(adjustVideo);
document.querySelectorAll('.product-3d').forEach(init3DModel);
