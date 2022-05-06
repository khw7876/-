    function create_id() {

        let id = $('#id1').val()
        console.log(id)
        let password = $('#password').val()


        $.ajax({
            type: 'POST',
            url: '/login/save',
            data: {id_give: id, pw_give : password},
            success: function (response) {
                alert("가입을 축하합니다.")
                window.location.reload("/")
            }
        });
    }
    function login(){
        let id = $('#id1').val()
        let pw = $('#password').val()

        $.ajax({
            type: 'POST',
            url: '/login',
            data: {id_give: id, pw_give : pw},
            success: function (response) {
                if (response['result'] == 'success'){
                $.cokie('mytoken', response['token'], {path:'/'});
                window.location.replace("/")
                }else {
                    alert(response['msg'])
                }
            }
            });

    }
