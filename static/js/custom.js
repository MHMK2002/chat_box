function saveAvatar(token) {
    const avatar = $('#profile-img-file-input')[0].files[0];
    const formData = new FormData();
    formData.append('avatar', avatar);
    formData.append('csrfmiddlewaretoken', token);
    $.ajax(
        {
            url: '/profile/update/avatar',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        }
    ).done();
}

function changeInformation(token) {
    console.log('changeInformation')
    const element = document.getElementById('edit-icon');
    if (element.classList.contains('bxs-save')) {
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
        ).then(res => {
            $('#personal-form').html(res);
        })
    }

}

function setStatus(status, token) {
    const formData = new FormData();
    formData.append('status', status);
    formData.append('csrfmiddlewaretoken', token);
    $.ajax(
        {
            url: '/profile/update/status',
            type: 'POST',
            method: 'POST',
            data: formData,
            processData: false,
            contentType: false,
        }
    ).done();

    const status_color = document.getElementById('status_color');
    status_color.classList.remove('text-success')
    status_color.classList.remove('text-warning')
    status_color.classList.remove('text-danger')

    $('#status').html(status);
    if (status === 'active') {
        status_color.classList.add('text-success')
    } else if (status === 'away') {
        status_color.classList.add('text-warning')
    } else {
        status_color.classList.add('text-danger')
    }
}

