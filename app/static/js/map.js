let map;
let geocoder;

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 2,
        center: { lat: 0, lng: 0 },
    });

    geocoder = new google.maps.Geocoder();

    // Retrieve data from div
    let places = JSON.parse(document.getElementById('placesData').textContent);

    places.forEach((place) => {
        // Concatenate city and country for the geocoder
        let address = place.city + ', ' + place.country;
        geocoder.geocode({ address: address }, (results, status) => {
            if (status === "OK") {
                new google.maps.Marker({
                    map,
                    position: results[0].geometry.location,
                });
            } else {
                alert("Geocode was not successful for the following reason: " + status);
            }
        });
    });
}

window.onload = initMap; 

