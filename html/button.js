
function getInfo() {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "http://192.168.239.126/cgi-bin/get-info.py?vehicle_number=" + vehicle_number, true);

    xhr.send();

    // Output from above url

    xhr.onload = function () {
        var output = xhr.responseText;
        window.location.href = "ownerInfo.html";
        document.getElementById("output").innerHTML = output;
    }

}

function printer(id) {
    var keyword = document.getElementById(id);
    return keyword.value;
}



