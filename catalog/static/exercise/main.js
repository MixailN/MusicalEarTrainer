$(document).ready(() => {
    let url = $(location).attr('href') + '?task=4'
    var data = '';
$(".test").click(() => {
    $.get(url, function (tmp) {
        data = tmp;
    });
    // fetch(url + '?task=4').then(
    //     response => { return response.text() }
    // ).then(
    //     resText => {
    //         console.log(resText);
    //         $(document).write
    //     }
    // )
})
})