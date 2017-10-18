/**
 * Created by sangyoon on 2017. 7. 29..
 */
$(document).ready(function () {
    $('.form_createStudent').submit(function () {
        if ($('.name').val() == "" || $('.email').val() == "") alert('학생 정보를 모두 입력해주세요.');
        else {
            $.ajax({
                url: '/createStudent',
                type: 'POST',
                data: $(this).serialize(),
                success: function (data) {
                    if (data.result == 'success') {
                        alert("학생 추가가 완료되었습니다.");
                        window.location.reload();
                    }
                    else alert("학생 추가 과정에 문제가 발생했습니다.")
                }
            })
        }
    });

    $('.btn_detail_student').click(function () {
        window.location.href = '/detail_student?studentId=' + $(this).attr('id') +
            '&classRoomId=' + $('.text_className').attr('id') + '&chapter=1'
    });

    $('.btn_show_all_student').click(function () {
        window.history.back();
    });

    $(".all_check").click(function () {
        if ($(".allCheck").prop("checked")) {
            $("input[name=studentCheck]").prop("checked", true);
        } else {
            $("input[name=studentCheck]").prop("checked", false);
        }
    })
});