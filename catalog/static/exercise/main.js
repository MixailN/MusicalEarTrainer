let tasks_id;
let point = -1;
const url_template = "http://127.0.0.1:8000/catalog/task/?q=";

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
    // let btn = $("#answer-btn")[0]
    // btn.setAttribute("form", "form")
    $("#form")[0].addEventListener("submit", async function (event) {
        event.preventDefault()
        let ans = $('input[name=answer_list]:checked').val()
        console.log(ans)
        let json = await check(ans)
        console.log(json)
    })
}



function get_task() {
    point++;
    let url = url_template + tasks_id[point]
    url = encodeURI(url)
    return fetch(url).then(response => {
        return response.text()
    })
}

function check(ans) {
    const csrftoken = Cookies.get('csrftoken');
    let url = url_template + tasks_id[point] + "&ans=" + ans
    let data = { q: tasks_id[point], ans: ans}
    url = encodeURI(url)
    return fetch(url, {method: 'POST', headers: {'X-CSRFToken': csrftoken, body: JSON.stringify(data)}}).then(response => {
        return response.json()
    })
}

