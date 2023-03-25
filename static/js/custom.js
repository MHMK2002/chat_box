function saveAvatar(token) {
    const avatar = document.getElementById('user_avatar').src;
    const data = {
        'avatar': avatar,
        'csrfmiddlewaretoken': token
    }
    console.log(data);
    $.ajax({
        url: "/profile/save_avatar",
        type: "POST",
        data: data,
        success: function (response) {
            console.log(response);
        }
    });
}

function changeInformation(token){
    console.log('changeInformation')
    const element = document.getElementById('edit-icon');
    if (element.classList.contains('bxs-save')){
        const data = {
            'first_name': document.getElementById('first_name').value,
            'last_name': document.getElementById('last_name').value,
            'username': document.getElementById('username').value,
            'phone_number': document.getElementById('phone_number').value,
            'location': document.getElementById('location').value,
            'short_about_me': document.getElementById('short_about_me').value,
            'about_me': document.getElementById('about_me').value,
            'csrfmiddlewaretoken': token
        }
        $.ajax(
            {
                url: '/profile/update/personal-form',
                type: 'POST',
                data: data,
            }
        ).then(res=>{
            $('#personal-form').html(res);
        })
    }

}