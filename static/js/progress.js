let val;
let intervalID;

// get time element

function progress() {
    val = 0;
    document.getElementById("myButton").disabled = true;
    intervalID = setInterval("updateProgress()", 50);
}

function updateProgress() {
    val += 1;
    document.getElementById("myProgress").value = val;
    document.getElementById("myProgress").innerText = val + "%";
    console.log("progress:", val, "%");

    if (val == 100) {
        clearInterval(intervalID);
        document.getElementById("myButton").disabled = false;
        alert('会議終わり!!');
    }
}