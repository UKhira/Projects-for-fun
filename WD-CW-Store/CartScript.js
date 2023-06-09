// shopping cart
const products = [
    {
        id : 0,
        image: "movie-1.png",
        title: "Sonic: The Hedgehog 2",
        price: 2000,
    },
    {
        id : 1,
        image: "movie-2.png",
        title: "Morbius",
        price: 1000,
    },
    {
        id : 2,
        image: "movie-3.png",
        title: "Adam Project",
        price: 900,
    },
    {
        id : 3,
        image: "movie-4.png",
        title: "Free Guy",
        price: 2500,
    },
    {
        id : 4,
        image: "movie-5.png",
        title: "Batman",
        price: 2000,
    },
    {
        id : 5,
        image: "movie-6.png",
        title: "Uncharted",
        price: 2000,
    },
    {
        id : 6,
        image: "movie-7.png",
        title: "Death on the nile",
        price: 900,
    },
    {
        id : 7,
        image: "movie-8.png",
        title: "The kingsman",
        price: 2500,
    },
]

const category = [...new Set(products.map((item) =>
    {return item}))]
    
    let i = 0;
document.getElementById("root").innerHTML = category.map((item) =>
{
    var {image,title,price} = item;
    return(
        `<div class = 'box'>
            <img src=${image} alt="Movie">
            <h4>${title}</h4>
            <h5>LKR: ${price}</h5>
            <div class="cart">` +
                    "<i class='bx bx-cart' onclick='addtocart("+(i++)+")'> </i>" +
            `</div>
        </div>` 
    );
}).join('')



var cart = [];

function addtocart(cartIcon){
    cart.push({...category[cartIcon]});
    displaycart();
}

function delElement(cartIcon){
    cart.splice(cartIcon,1);
    displaycart();
}

function displaycart(cartIcon){

    let j = 0; total = 0;

    document.getElementById("count").innerHTML = cart.length;
    document.getElementById("total").innerHTML = "$ " + 0 +".00";

    if(cart.length == 0){
        document.getElementById('cartItem').innerHTML = "Your Cart is empty";
    }
    else {
        document.getElementById('cartItem').innerHTML = cart.map((items) =>
        {
            var {image, title, price} = items;

            total = total+price;
            document.getElementById("total").innerHTML = "LKR: " + total + " .00";

            return(
                `<div class='cart-item'>
                <div class='row-img'>
                    <img class='rowimg' src=${image}>
                </div>
                <p style='font-size: 13px;'>${title}</p>
                <p style='font-size: 13px;'>LKR: ${price}.00</p>` +
                "<i class='bx bx-trash' style='color: gold;' onclick='delElement(" + (j++) + ")'></i></div>"
            );
        }).join('');
    }
}