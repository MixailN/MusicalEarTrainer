$(document).ready(() => {
    $('#start')[0].addEventListener('click', function (event) {
        console.log("clicked")
        event.preventDefault()
        window.location.href = "http://127.0.0.1:8000/catalog/";
    })
})