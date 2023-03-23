function saveAvatar(){
    var data = new FormData();
    data.append('avatar', $('#user_avatar').attr('src'));
    console.log(2);
    $.ajax({
        url: '/profile/save_avatar',
        method: 'POST',
        data: data,
        cache: false,
        contentType: false,
        processData: false,
    }).done(function(data){
        console.log(1);
        console.log(data);
    });
}