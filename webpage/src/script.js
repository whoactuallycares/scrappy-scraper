LOAD_IMAGES = true
// Converts image urls into a string of html images
function urls_to_elements(image_urls)
{
    res = "";
    if(LOAD_IMAGES)
        image_urls.forEach((url) => res += `<img src="${url}"></img>`);
    return res;
};

function format_price(price_raw)
{
    if(price_raw <= 1)
        return "Dohodou";

    return Intl.NumberFormat().format(price_raw)
};

// Creates a html card from listing data
function create_card_element(listing)
{
    
    container = document.createElement("div");
    document.body.appendChild(container);
    container.innerHTML = `
    <h1><a href="https://www.sreality.cz/detail/prodej/byt/a/b/${listing.id}">Real listing</a></h1>
    <h2>${listing.name}</h2>
    <h2>${format_price(listing.price)}</h2>
    <h2>${listing.location}</h2>
    ${urls_to_elements(listing.image_urls)}
    `;
};

// Creates all cards for a listing
function generate_cards(listings)
{
    document.title = `Scraped listings (${listings.length})`; // Show number of listings in tab name
    listings.forEach((listing) => create_card_element(listing));
}

// Requests listing data from the database
function fetch_listings()
{
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/listings"); // Send request to "listings" path in casethere end up being more endpoints

    xhr.setRequestHeader("Accept", "application/json");
    xhr.setRequestHeader("Content-Type", "application/json");

    xhr.onload = () => generate_cards(JSON.parse(xhr.responseText));
    xhr.send();
};

// Immediately fetch data from database and display it
fetch_listings()