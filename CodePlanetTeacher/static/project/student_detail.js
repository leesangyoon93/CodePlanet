$(document).ready(function () {

    var getUrlParameter = function getUrlParameter(sParam) {
        var sPageURL = decodeURIComponent(window.location.search.substring(1)),
            sURLVariables = sPageURL.split('&'),
            sParameterName,
            i;

        for (i = 0; i < sURLVariables.length; i++) {
            sParameterName = sURLVariables[i].split('=');

            if (sParameterName[0] === sParam) {
                return sParameterName[1] === undefined ? true : sParameterName[1];
            }
        }
    };

    $("input[type=radio][name=radio_chapter][value=" + getUrlParameter("chapter") + "]").attr('checked', true);

    $('input[type=radio][name=radio_chapter]').change(function () {
        window.location.href = '/detail_student?studentId=' + getUrlParameter("studentId") +
            '&classRoomId=' + getUrlParameter("classRoomId") + '&chapter=' + this.value
    });

    $('.btn_show_all_student').click(function() {
        history.back();
    })
});