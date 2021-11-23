document.addEventListener("DOMContentLoaded", function(event) {
var progress = document.getElementById('bar-prog'); 
setInterval(function() {
	progress.value = parseInt(progress.value) + 1;
}, 1000);
}

document.addEventListener("DOMContentLoaded", function(event) {
//get the modal
var modal = document.getElementById('id01');

//when the user clicks anywhere outside of the modal, closes it
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }

}

function validateForm() {
if (isEmpty(document.getElementById('data_2').value.trim())) {
alert('NAME is required!');
return false;
}
if (isEmpty(document.getElementById('data_4').value.trim())) {
alert('EMAIL is required!');
return false;
}
if (!validateEmail(document.getElementById('data_4').value.trim())) {
alert('EMAIL must be a valid email address!');
return false;
}
return true;
}
function isEmpty(str) { return (str.length === 0 || !str.trim()); }
function validateEmail(email) {
var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,15}(?:\.[a-z]{2})?)$/i;
return isEmpty(email) || re.test(email);
}

});

function validateForm() {
if (isEmpty(document.getElementById('data_2').value.trim())) {
alert('NAME is required!');
return false;
}
if (isEmpty(document.getElementById('data_4').value.trim())) {
alert('EMAIL is required!');
return false;
}
if (!validateEmail(document.getElementById('data_4').value.trim())) {
alert('EMAIL must be a valid email address!');
return false;
}
return true;
}
function isEmpty(str) { return (str.length === 0 || !str.trim()); }
function validateEmail(email) {
var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,15}(?:\.[a-z]{2})?)$/i;
return isEmpty(email) || re.test(email);
}
