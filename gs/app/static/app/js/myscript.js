$('.plus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[2]
    console.log("Pid=",id)
    $.ajax({
        type: "GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =",data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})


//
$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml= this.parentNode.children[2]
    console.log("Pid=",id)
    $.ajax({
        type: "GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            console.log("data =",data);
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})


// $('.remove-cart').click(function(){
   
    
//     var id=$(this).attr("pid").toString();
//     var eml= this
//     console.log("Pid=",id)

     
// })

$('.remove-cart').click(function(){
    var id = $(this).attr("pid").toString();
    var eml = this;

    console.log("Pid =", id);

    $.ajax({
        type: "GET",
        url: "/removecart/",
        data: {
            prod_id: id
        },
        success: function (data) {
            // Handle the success response here if needed.
            // You can remove the cart item from the DOM if the server successfully removes it from the database.
            // For example, you can use 'eml' to remove the cart item from the DOM using jQuery's remove() method.
            $(eml).closest('.cart-item').remove();

            // Update other elements on the page if needed, e.g., update the cart total amount, item count, etc.
            document.getElementById("amount").innerText = data.amount;
            document.getElementById("totalamount").innerText = data.totalamount;
        },
        error: function (error) {
            // Handle the error response here if needed.
            console.log("Error:", error);
        }
    });
});


$('.plus-wishlist').click(function(){
    var id=$(this).attr("pid").toString();
    console.log("this is plus id::",id)
    $.ajax({
        type:"GET",
        url:"/pluswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = 'http://localhost:8000/product-detail/${id}'
        }
    })
})


$('.minus-wishlist').click(function(){
    var id= $(this).attr("pid").toString();
    console.log("this is minus id::",id)
    $.ajax({
        type:"GET",
        url:"/minuswishlist",
        data:{
            prod_id:id
        },
        success:function(data){
            window.location.href = 'http://localhost:8000/product-detail/${id}'
        }
    })
})



/* whatsapp_icon.js */
document.addEventListener("DOMContentLoaded", function () {
    var whatsappIcon = document.getElementById("whatsapp-icon");
  
    whatsappIcon.addEventListener("click", function () {
      // Replace 'YOUR_PHONE_NUMBER' with the actual WhatsApp number including the country code.
      var phoneNumber = "+919604802874";
      window.open("https://wa.me/" +919604802874, "_blank");
    });
  });
  





