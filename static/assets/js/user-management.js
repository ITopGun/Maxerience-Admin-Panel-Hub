$(document).ready(function(){

$("#all-check").change(function(){
    const allChecked = $(this).get(0).checked;
    if(allChecked) $("#delete-row").get(0).disabled = false;
    else $("#delete-row").get(0).disabled = true;
    $('.checkbox input[type=checkbox]').map((index, ele) => {
        $(ele).get(0).checked = allChecked;
    })
})

$("#delete-row").click(function(){
    let delUsers = [];
    $('tbody .checkbox input[type=checkbox]').map((index, ele) => {
        let trChecked = $(ele).get(0).checked;
        if(trChecked) {
            delUsers.push($(ele).closest('tr').attr('user-id'))
        }
    })

    jQuery.ajax({
        type: "DELETE",
        url: '/user-management/'+delUsers[0],
        headers: {'X-CSRFToken': csrf_token},
        data: {
            csrfmiddlewaretoken: csrf_token,
            id: JSON.stringify(delUsers)
        },
        dataType: 'json',
        async: false,
        success: function (result) {
            if (result.status === 200) {
                tata.success('success', result.message)
                $('tbody tr').map((index, ele) => {
                    if($(ele).find('.checkbox-danger input[type=checkbox]:checked').length) $(ele).remove();
                })
                $("#all-check").get(0).checked = false;
            } else {
                tata.error('Error', result.message)
            }
        }
    });
})

$('body').on('click', 'tbody .checkbox input[type=checkbox]', function(){
    const allChecked = ($('tbody .checkbox input[type=checkbox]').length === $('tbody .checkbox input[type=checkbox]:checked').length)
    if(allChecked) $("#all-check").get(0).checked = true;
    else $("#all-check").get(0).checked = false;

    if($('tbody .checkbox input[type=checkbox]:checked').length) $("#delete-row").get(0).disabled = false;
    else $("#delete-row").get(0).disabled = true;
})

$('body').on('change', '.custom-control', function (e) {
    let checked = e.target.checked;
    let activeTxt = $(e.target).hasClass('status') ? 'Active' : 'Administrator';
    let inactiveTxt = $(e.target).hasClass('status') ? 'Inactive' : 'User';
    if(checked) {
        $(e.target).next('label').text(activeTxt);
    } else {
        $(e.target).next('label').text(inactiveTxt);
    }
    let trEle = $(e.target).closest('tr');
    let userId = trEle.attr('user-id');
    let is_active = trEle.find('input[type=checkbox].status').get(0).checked ? 1 : 0;
    let is_staff = trEle.find('input[type=checkbox].role').get(0).checked ? 1 : 0;

    jQuery.ajax({
        type: "PUT",
        url: '/user-management/'+userId,
        headers: {'X-CSRFToken': csrf_token},
        data: {
            csrfmiddlewaretoken: csrf_token,
            id: userId,
            is_active: is_active,
            is_staff: is_staff
        },
        dataType: 'json',
        async: false,
        success: function (result) {
            if (result.status === 200) {
                tata.success('Success', result.message)
            } else {
                tata.error('Error', result.message)
            }
        }
    });
});
})