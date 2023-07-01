// shopping cart

const products = [
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
    {
        id : 0,
        image: "movie-1.png",
        title: "Spiderman",
        price: 2000,
    },
]

const category = [...new Set(products.map((item) =>
    {return item}))]

    let i = 0;
document.querySelector(".root").innerHTML = category.map((item) =>
{
    var {image,title,price} = item;
    return(
        div class = "box"
    )
})