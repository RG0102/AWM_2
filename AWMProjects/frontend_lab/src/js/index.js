import $ from 'jquery';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'font-awesome/css/font-awesome.min.css';
import L from 'leaflet';

console.log($);
console.log(L);

$(document).ready(function () {
    // Example AJAX request to your API
    $.ajax({
        url: 'https://api.example.com/data', // Replace with your API endpoint
        method: 'GET',
        success: function (data) {
            console.log(data);
            // Update the DOM based on the response
        },
        error: function (err) {
            console.error('Error:', err);
        }
    });

    // Example Leaflet map
    const map = L.map('map').setView([51.505, -0.09], 13);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);
});
