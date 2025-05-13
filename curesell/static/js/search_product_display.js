document.addEventListener('DOMContentLoaded', function() {
    // 商品点击跳转
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', () => {
            // window.location.href = `/product/${card.dataset.id}`; // 需根据实际路由修改
            window.location.href = `/detail/?prod_id=${card.dataset.id}`;
        });
    });
});

$(document).ready(function() {
    // 显示排序选项
    $('.sort-btn').click(function() {
      $('.sort-options').toggle();
    });

    // 应用排序选项
    $('.apply-btn').click(function() {
      var selectedOptions = [];
      $('.sort-options input:checked').each(function() {
        selectedOptions.push($(this).val());
      });
      // 这里可以将 selectedOptions 发送到后端进行排序处理
      console.log('Selected sorting options:', selectedOptions);
      $('.sort-options').hide();
    });
  });
  
$(document).ready(function() {
    // 假设后端返回的搜索结果是一个包含商品信息的数组
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
  
    // 动态生成商品卡片
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
    // 实现具体排序逻辑（需与后端配合）
    console.log('Applying sorts:', sorts);
}