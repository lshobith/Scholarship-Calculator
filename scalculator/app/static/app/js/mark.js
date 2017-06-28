function markIt(element_ref) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'mark');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    var csrftoken = getCookie('csrftoken');
    xhr.setRequestHeader("X-CSRFToken", csrftoken);
    var element_id = element_ref.id;
    var thenumber = element_id.replace( /^\D+/g, '');
    var remove_cmd = 'remove' + thenumber.toString();
    var save_cmd = 'save' + thenumber.toString();
    var badge_id = 'badge' + thenumber.toString();
    var final_string = 'scholarship_id=' + element_id;
    xhr.onload = function () {
        console.log(xhr.responseText);
        if (element_id == remove_cmd && xhr.responseText == 'remove ok') {
            element_ref.style.display = 'none';
            var opp_element = document.getElementById(save_cmd);
            opp_element.style.display = 'block';
            document.getElementById(badge_id).style.visibility = 'hidden';
        } else if (element_id == save_cmd && xhr.responseText == 'save ok') {
            element_ref.style.display = 'none';
            var opp_element = document.getElementById(remove_cmd);
            opp_element.style.display = 'block';
            document.getElementById(badge_id).style.visibility = 'visible';
        }
    };
    xhr.send(final_string);
}