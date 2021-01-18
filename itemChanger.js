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
    var valueArray = Array.from(Array(12), () => new Array(12))
    for(var i = 0; i < items.length; i++) {
        var quotient = Math.floor(i/12)
        valueArray[quotient][i-(quotient*12)] = items[i].innerText
    }
    var json = JSON.stringify(valueArray)
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://192.168.178.239:5000/board/new", true);
    xhttp.setRequestHeader("Content-Type", "application/json");
    xhttp.send(json)
}

function doRandom() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://192.168.178.239:5000/board/random", true);
    xhttp.send()
}

function sendTerminate() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "http://192.168.178.239:5000/board/terminate", true);
    xhttp.send()
}

function reset() {
    var items = document.getElementsByClassName("item")
    for(var i = 0; i < items.length; i++) {
        items[i].innerText = 'o'
        items[i].classList.remove("edited")
    }
}

