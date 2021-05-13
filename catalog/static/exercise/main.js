let tasks_id;
let point = -1;
const url_template = "http://127.0.0.1:8000/catalog/task/?q=";

$(document).ready(() => {
    let test = $("#tasks")[0];
    tasks_id = $.parseJSON($.trim(test.textContent));
    console.log(tasks_id);
    insert_task();

});

async function insert_task() {
    let task = $("#task")[0];
    if (task !== undefined) {
        task.remove()
    }
    let elem = $("#title");
    task = await get_task();
    elem.after(task);
    let audio = $("#sound")[0];
    $("#play-btn")[0].addEventListener("click", function (event) {
        event.preventDefault();
        audio.play();
    });
    // let btn = $("#answer-btn")[0]
    // btn.setAttribute("form", "form")
    $("#form")[0].addEventListener("submit", async function (event) {
        $("#answer-btn")[0].setAttribute("disabled", true);
        event.preventDefault();
        let ans = $('input[name=answer_list]:checked');
        console.log(ans);
        let json = await check(ans.val());
        console.log(json)
        let val = json.answer
        ans.parent().css("background", "red")
        $('[value=' + val + ']').parent().css("background", "green")
        if (point === tasks_id.length - 1) {
            insert_finish()
            return
        }
        insert_next()
    })
}

function insert_next() {
    $("#buttons-container").append($('<button id="next">Next</button>'))
    $("#next")[0].addEventListener("click", function (event) {
        event.preventDefault()
        insert_task()
    })
}

function insert_finish() {
    $("#buttons-container").append($('<button id="finish">Finish</button>'))
    $("#finish")[0].addEventListener("click", function (event) {
        event.preventDefault()
        window.location.href = "http://127.0.0.1:8000/catalog/";
    })
}

function get_task() {
    point++;
    let url = url_template + tasks_id[point];
    url = encodeURI(url);
    return fetch(url).then(response => {
        return response.text()
    })
}

function check(ans) {
    const csrftoken = Cookies.get('csrftoken');
    let url = url_template + tasks_id[point] + "&ans=" + ans;
    let data = {q: tasks_id[point], ans: ans};
    url = encodeURI(url);
    return fetch(url, {
        method: 'POST',
        headers: {'X-CSRFToken': csrftoken},
        body: JSON.stringify(data)
    }).then(response => {
        return response.json()
    })
}

