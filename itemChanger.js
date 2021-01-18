const baseURL = "http://192.168.178.239:5000/board/"
const length = 12
function changeValue(e) {
    if(e.innerText == "o") {
        e.innerText = "x"
        e.classList.add("edited")
    }
    else {
        e.innerText = "o"
        e.classList.remove("edited")
    }
}

function sendMatrixToPi() {
    var items = document.getElementsByClassName("item")
    var valueArray = Array.from(Array(length), () => new Array(length))
    for(var i = 0; i < items.length; i++) {
        var quotient = Math.floor(i/length)
        valueArray[quotient][i-(quotient*length)] = items[i].innerText
    }
    var json = JSON.stringify(valueArray)
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", baseURL + "new", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(json)
}

function doRandom() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", baseURL + "random", true);
    xhttp.send()
}

function sendTerminate() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", baseURL + "terminate", true);
    xhttp.send()
}

function reset() {
    var items = document.getElementsByClassName("item")
    for(var i = 0; i < items.length; i++) {
        items[i].innerText = 'o'
        items[i].classList.remove("edited")
    }
}

