// shopping cart

const products = [
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 1,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 2,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 3,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 4,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
]

const category = [...new Set(products.map((item) =>
    {return item}))]

    let i = 0;
document.querySelector(".container").innerHTML = category.map((item) =>
{
    var {image,title,price} = item;
    return(
        `<div class="box">
            <img src=${image} alt="">
            <h4>${title}</h4>
            <h5>${price}</h5>
        <div class="cart" onclick='addtocart("+(i++)+")>
          <a href="#"><i class="bx bx-cart"></i></a>
        </div>
      </div>`
    )
}).join('')