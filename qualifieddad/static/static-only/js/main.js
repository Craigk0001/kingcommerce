/**
 * Listen to scroll to change header opacity class
 */
function checkScroll(){
    var startY = $('.navbar-transparent').height() * 2; //The point where the navbar changes in px
    if($(window).scrollTop() > startY){
        $('.navbar-transparent').addClass("scrolled");
    }else{
        $('.navbar-transparent').removeClass("scrolled");
    }
}
if($('#navbar').length > 0){
    $(window).on("scroll load resize", function(){
        checkScroll();
    });
}
// Card Hover
/**
 * Make the whole card a lickable link
 */
$(".hover-card").click(function() {
  window.location = $(this).find("a").attr("href");
  return false;
});
// End Card Hover
// PRODUCT DETAIL PAGE
// Select primary image on page load
window.onload = function loadImage(imgr) {
    imgr = document.getElementById("primaryImg")
    // Get the expanded image
    var expandImg = document.getElementById("expandedImg");
    // Use the same src in the expanded image as the image being clicked on from the grid
    expandImg.src = imgr.src;
}
// Products tab
function onloadProductImg(imgr) {
  alert(imgr);
  // Get the expanded image
  var expandImg = document.getElementById("expandedImg");
  // Use the same src in the expanded image as the image being clicked on from the grid
  expandImg.src = imgr.src;
  // Show the container element (hidden with CSS)
  expandImg.parentElement.style.display = "block";
}
function selectProductImg(imgs) {
  // Get the expanded image
  var expandImg = document.getElementById("expandedImg");
  // Use the same src in the expanded image as the image being clicked on from the grid
  expandImg.src = imgs.src;
  // Show the container element (hidden with CSS)
  expandImg.parentElement.style.display = "block";
}
// End Products Tab
// Product Slider
// $('#carouselExample').on('slide.bs.carousel', function (e) {
//     var $e = $(e.relatedTarget);
//     var idx = $e.index();
//     var itemsPerSlide = 4;
//     var totalItems = $('.carousel-item').length;
//     if (idx >= totalItems-(itemsPerSlide-1)) {
//         var it = itemsPerSlide - (totalItems - idx);
//         for (var i=0; i);
//       };
//   };
// );
// End Product Slider
// WISHLIST

// Wishlist End

// MAKE PRODUCT DIV A CLICKABLE LINK
$(".product").click(function() {
  window.location = $(this).find("a").attr("href");
  return false;
});
// CART
var deleteIdElement = document.getElementById('delete-button')
deleteIdElement.addEventListener('click', function() {
    var deleteId = this.dataset.deleteId;
    alert('remove item from cart: ' + deleteId);
});
// END CART
//QUANTITY PLUS AND MINUS
$('.btn-number').click(function(e){
    e.preventDefault();

    fieldName = $(this).attr('data-field');
    type      = $(this).attr('data-type');
    var input = $("input[name='"+fieldName+"']");
    var currentVal = parseInt(input.val());
    if (!isNaN(currentVal)) {
        if(type == 'minus') {

            if(currentVal > input.attr('min')) {
                input.val(currentVal - 1).change();
            }
            if(parseInt(input.val()) == input.attr('min')) {
                $(this).attr('disabled', true);
            }

        } else if(type == 'plus') {

            if(currentVal < input.attr('max')) {
                input.val(currentVal + 1).change();
            }
            if(parseInt(input.val()) == input.attr('max')) {
                $(this).attr('disabled', true);
            }

        }
    } else {
        input.val(0);
    }
});
$('.input-number').focusin(function(){
   $(this).data('oldValue', $(this).val());
});
$('.input-number').change(function() {

    minValue =  parseInt($(this).attr('min'));
    maxValue =  parseInt($(this).attr('max'));
    valueCurrent = parseInt($(this).val());

    name = $(this).attr('name');
    if(valueCurrent >= minValue) {
        $(".btn-number[data-type='minus'][data-field='"+name+"']").removeAttr('disabled')
    } else {
        alert('Sorry, the minimum value was reached');
        $(this).val($(this).data('oldValue'));
    }
    if(valueCurrent <= maxValue) {
        $(".btn-number[data-type='plus'][data-field='"+name+"']").removeAttr('disabled')
    } else {
        alert('Sorry, the maximum value was reached');
        $(this).val($(this).data('oldValue'));
    }


});
$(".input-number").keydown(function (e) {
        // Allow: backspace, delete, tab, escape, enter and .
        if ($.inArray(e.keyCode, [46, 8, 9, 27, 13, 190]) !== -1 ||
             // Allow: Ctrl+A
            (e.keyCode == 65 && e.ctrlKey === true) ||
             // Allow: home, end, left, right
            (e.keyCode >= 35 && e.keyCode <= 39)) {
                 // let it happen, don't do anything
                 return;
        }
        // Ensure that it is a number and stop the keypress
        if ((e.shiftKey || (e.keyCode < 48 || e.keyCode > 57)) && (e.keyCode < 96 || e.keyCode > 105)) {
            e.preventDefault();
        }
    });
//END QUANTITY PLUS AND MINUS
// CART MANAGEMENT

/* Set rates + misc */
var taxRate = 0.00;
var shippingRate = 15.00;
var fadeTime = 300;

/* Assign actions */
$('.product-quantity input').change( function() {
  updateQuantity(this);
});

$('.product-removal span').click( function() {
  removeItem(this);
});


/* Recalculate cart */
function recalculateCart()
{
  var subtotal = 0;
  var savings = 0;
  var total_quantity = 0;

  /* Sum up row totals */
  $('.cart-item').each(function () {
    subtotal += parseFloat($(this).children().children().children().children().children('.product-line-price').text());
    savings += parseFloat($(this).children().children().children().children().children('.product-line-savings').text());
    total_quantity += parseFloat($(this).children().children().children().children().children('.product-line-quantity').text());
  });

  /* Calculate totals */
  var tax = subtotal * taxRate;
  var shipping = (subtotal > 0 ? shippingRate : 0);
  var total = subtotal + tax + shipping;

  /* Update totals display */
  $('.totals-value').fadeOut(fadeTime, function() {
    $('#cart-subtotal').html(subtotal.toFixed(2));
    $('#cart-savings').html(savings.toFixed(2));
    $('#cart-tax').html(tax.toFixed(2));
    $('#cart-shipping').html(shipping.toFixed(2));
    $('#cart-total').html(total.toFixed(2));
    $('#cart-total-b').html(total.toFixed(2));
    $('#cart-quantity').html(total_quantity.toFixed(0));
    if(total == 0){
      $('.checkout').fadeOut(fadeTime);
    }else{
      $('.checkout').fadeIn(fadeTime);
    }
    $('.totals-value').fadeIn(fadeTime);
  });
}


/* Update quantity */
function updateQuantity(quantityInput)
{
  /* Calculate line price */
  var productRow = $(quantityInput).parent().parent().parent().parent();
  var price = parseFloat(productRow.children().children().children().children('.product-price').text());
  var savings = parseFloat(productRow.children().children().children().children('.product-savings').text());
  var shipping = parseFloat(productRow.children().children().children('.product-shipping').text());
  var quantity = $(quantityInput).val();
  var linePrice = price * quantity;
  var lineSavings = savings * quantity;
  var lineShipping = shipping * quantity;
  var lineQuantity = parseFloat(quantity);

  /* Update line price display and recalc cart totals */
  productRow.each(function () {
    $(this).children().children().children('.item-totals-value').fadeOut(fadeTime, function() {
      $(this).children().children('.product-line-price').text(linePrice.toFixed(2));
      $(this).children().children('.product-line-savings').text(lineSavings.toFixed(2));
      $(this).children().children('.product-line-quantity').text(parseFloat(quantity).toFixed(0));
      recalculateCart();
      $(this).fadeIn(fadeTime);
    });
  });
  // productRow.children().children().children().children().children('.product-line-price').each(function () {
  //   $(this).fadeOut(fadeTime, function() {
  //     $(this).text(linePrice.toFixed(2));
  //     // $(this).text(lineSavings.toFixed(2));
  //     // $(this).text(parseFloat(quantity).toFixed(0));
  //     recalculateCart();
  //     $(this).fadeIn(fadeTime);
  //   });
  // });
  // productRow.children().children().children().children().children('.product-line-savings').each(function () {
  //   $(this).fadeOut(fadeTime, function() {
  //     $(this).text(lineSavings.toFixed(2));
  //     recalculateCart();
  //     $(this).fadeIn(fadeTime);
  //   });
  // });
  // productRow.children().children().children().children().children('.product-line-quantity').each(function () {
  //   $(this).fadeOut(fadeTime, function() {
  //     $(this).text(parseFloat(quantity).toFixed(0));
  //     recalculateCart();
  //     $(this).fadeIn(fadeTime);
  //   });
  // });
}


/* Remove item from cart */
function removeItem(removeButton)
{
  /* Remove row from DOM and recalc cart total */
  var productRow = $(removeButton).parent().parent();
  productRow.slideUp(fadeTime, function() {
    productRow.remove();
    recalculateCart();
  });
}

// END CART MANAGEMENT
$('.radio-group .radio').click(function(){
    $(this).parent().find('.radio').removeClass('selected');
    $(this).addClass('selected');
    var val = $(this).attr('data-value');
    //alert(val);
    $(this).parent().find('input').val(val);
});
