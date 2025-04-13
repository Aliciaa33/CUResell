function validateForm() {
    let isValid = true;
  
    // Title validation
    const title = document.getElementById('prod_title');
    const titleError = document.getElementById('prod_title_error');
    if (title.value.trim() === '') {
      titleError.style.display = 'block';
      isValid = false;
    } else {
      titleError.style.display = 'none';
    }
  
    // Image validation
    const image = document.getElementById('prod_image');
    const imageError = document.getElementById('prod_image_error');
    if (!image.files || image.files.length === 0) {
      imageError.style.display = 'block';
      isValid = false;
    } else {
      imageError.style.display = 'none';
    }
  
    // Price validation
    const price = document.getElementById('prod_price');
    const priceError = document.getElementById('prod_price_error');
    if (!price.value.trim() || isNaN(price.value) || parseFloat(price.value) <= 0) {
      priceError.style.display = 'block';
      isValid = false;
    } else {
      priceError.style.display = 'none';
    }
  
    // Description validation
    const description = document.getElementById('description');
    const descriptionError = document.getElementById('description_error');
    if (description.value.trim() === '') {
      descriptionError.style.display = 'block';
      isValid = false;
    } else {
      descriptionError.style.display = 'none';
    }
  
    return isValid; // Prevent form submission if validation fails
  }