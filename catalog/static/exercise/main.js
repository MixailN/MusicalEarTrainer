var tasks_id;
var point = 0;
var url_template = "http://127.0.0.1:8000/catalog/task/?q="

$(document).ready(() => {
    let test = $("#tasks")[0];
    tasks_id = $.parseJSON($.trim(test.textContent));
    console.log(tasks_id);
    insert_task()

    // var data = '';
    // $(".test").click(() => {
    //     $.get(url, function (tmp) {
    //         data = tmp;
    // });
    // fetch(url + '?task=4').then(
    //     response => { return response.text() }
    // ).then(
    //     resText => {
    //         console.log(resText);
    //         $(document).write
    //     }
    // )
})

async function insert_task() {
    let task = $("#task")[0]
    if (task !== undefined) {
        task.remove()
    }
    let elem = $("#title")
    task = await get_task()
    elem.after(task)
    let btn = $("#answer-btn")[0]
    btn.setAttribute("form", "form")
    $("#form")[0].addEventListener("submit", function (event) {
        insert_task()
        event.preventDefault()
    })
}



function get_task() {
    let url = url_template + tasks_id[point]
    return fetch(url).then(response => {
        point++;
        return response.text()
    })
}