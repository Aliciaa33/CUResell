document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', () => {
            // window.location.href = `/product/${card.dataset.id}`; // 需根据实际路由修改
            window.location.href = `/detail/?prod_id=${card.dataset.id}`;
        });
    });
});

$(document).ready(function() {
    $('.sort-btn').click(function() {
      $('.sort-options').toggle();
    });

    $('.apply-btn').click(function() {
      var selectedOptions = [];
      $('.sort-options input:checked').each(function() {
        selectedOptions.push($(this).val());
      });

      console.log('Selected sorting options:', selectedOptions);
      $('.sort-options').hide();
    });
  });
  
$(document).ready(function() {

    var searchResults = [
      {
        name: 'Heirloom tomato',
        price: '$5.99 / lb',
        image: '/static/img/logo.jpg'
      },
      {
        name: 'Organic ginger',
        price: '$12.99 / lb',
        image: '/static/img/logo.jpg'
      }
    ];
  

    var productGrid = $('#product-grid');
    searchResults.forEach(function(product) {
      var productCard = `
        <div class="product-card">
          <img src="${product.image}" alt="${product.name}" class="product-image">
          <h3 class="product-title">${product.name}</h3>
          <p class="product-price">${product.price}</p>
        </div>
      `;
      productGrid.append(productCard);
    });
  });

function sortProducts(sorts) {
    console.log('Applying sorts:', sorts);
}