// attempt to fetch product data from the server
fetch('/products')
.then(response => response.json())
.then(data => {
    const productCardsContainer = document.getElementById('product-cards');
    // Sort products by date in descending order by default
    data.sort((a, b) => new Date(b.date) - new Date(a.date));
    data.forEach(product => {
        const productCard = document.createElement('a');
        productCard.href = `/product/${product.id}`;
        productCard.className = 'product-card';

        const productName = document.createElement('div');
        productName.className = 'product-name';
        productName.textContent = product.name;

        const productPrice = document.createElement('div');
        productPrice.className = 'product-price';
        productPrice.textContent = `$${product.price} / lb`;

        const productImage = document.createElement('img');
        productImage.className = 'product-image';
        productImage.src = product.image;

        productCard.appendChild(productName);
        productCard.appendChild(productPrice);
        productCard.appendChild(productImage);

        productCardsContainer.appendChild(productCard);
    });
});