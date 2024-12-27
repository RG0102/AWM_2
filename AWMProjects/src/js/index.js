import $ from "jquery";

$(document).ready(() => {
    $('#load-data').on('click', function () {
        $.ajax({
            url: 'https://jsonplaceholder.typicode.com/posts', // Example API
            method: 'GET',
            success: function (data) {
                const displayData = data.slice(0, 5).map(item => `
                    <div>
                        <h3>${item.title}</h3>
                        <p>${item.body}</p>
                    </div>
                `).join('');
                $('#api-data').html(displayData);
            },
            error: function (err) {
                $('#api-data').html('<p>Error fetching data.</p>');
            }
        });
    });
});
