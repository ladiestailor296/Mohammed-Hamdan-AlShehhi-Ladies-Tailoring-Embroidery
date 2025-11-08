/* 💫 Firebase Database Logic - v26.9+ */

const db = firebase.firestore();
const productsContainer = document.getElementById("product-slider");

// ✅ Load products automatically from Firestore
db.collection("products").onSnapshot(snapshot => {
  productsContainer.innerHTML = "";
  snapshot.forEach(doc => {
    const p = doc.data();
    const div = document.createElement("div");
    div.classList.add("slide");
    div.innerHTML = `
      <img src="${p.image}" alt="${p.name_en}">
      <p>${p.name_en} / ${p.name_ar}</p>
      <p><strong>AED ${p.price}</strong></p>
    `;
    productsContainer.appendChild(div);
  });
});
