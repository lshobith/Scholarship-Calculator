// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function onSignIn(googleUser) {
    var id_token = googleUser.getAuthResponse().id_token;
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'gverify');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    var csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    xhr.onload = function () {
        console.log(xhr.responseText);
        if (xhr.responseText === 'Sign in failed') {
            console.log('stub');
        } else if (xhr.responseText === 'new user') {
            document.location.href = 'fxprofile';
        } else {
            document.location.href = 'eligible';
        }
    };
    xhr.send('idtoken=' + id_token);
}