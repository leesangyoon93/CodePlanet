/**
 * Created by sangyoon on 2017. 5. 14..
 */
$(document).ready(function () {
    $('.btn_start').click(function () {
        window.location.href = "/class"
    });

    $('.btn_cancel').click(function () {
        window.history.back();
    });

    $('.btn_class').click(function () {
        window.location.href = "/class"
    })

    $('.btn_checkemail').click(function () {
        if ($('.input_email').val() == "") alert("이메일을 입력해주세요.")
        var emailRegex = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
        if (emailRegex.test($('.input_email').val()) == true) {
            $.ajax({
                'url': '/checkEmail',
                'type': 'POST',
                'data': {'email': $('.input_email').val()},
                'success': function(data) {
                    if(data.result == 'success') alert('가입 가능한 이메일입니다.')
                    else {
                        $('.input_email').text("");
                        alert("이미 사용중인 이메일입니다.")
                    }

                }
            })
        }
        else alert("이메일 형식을 정확히 입력해주세요.")
    })

    $('.form_signup').submit(function () {
        var isValid = true;

        $('.input').each(function () {
            if ($(this).val() == "") {
                isValid = false;
                alert("입력창을 모두 입력해주세요.");
            }
        })

        if (isValid) {
            var emailRegex = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/;
            if (emailRegex.test($('.input_email').val()) == true) {
                $.ajax({
                'url': '/signup',
                'type': 'POST',
                'data': $(this).serialize(),
                'success': function(data) {
                    if(data.result == 'success') {
                        alert("회원가입에 성공했습니다.");
                        window.location.href = "/login"
                    }
                    else alert("회원가입에 실패했습니다.");
                }
            })
            }
            else alert("이메일 형식을 정확히 입력해주세요.")

        }
    })

    $('.form_login').submit(function () {
        if ($('.input_email').val() == "") alert("아이디를 입력해주세요.");
        else if ($('.input_password').val() == "") alert("비밀번호를 입력해주세요.");
        else {
            $.ajax({
                type: 'POST',
                data: $(this).serialize(),
                url: '/login',
                success: function (data) {
                    if (data.result == 'error') alert('이메일주소 또는 비밀번호가 올바르지 않습니다');
                    else window.location.href = "/after_login"
                }
            })
        }
    });
})