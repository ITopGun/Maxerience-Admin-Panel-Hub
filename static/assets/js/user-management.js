const removeUser = (self, userId) => {
    jQuery.ajax({
        type: "DELETE",
        url: '/user-management/'+userId,
        headers: {'X-CSRFToken': csrf_token},
        data: {
            csrfmiddlewaretoken: csrf_token,
            id: userId
        },
        dataType: 'json',
        async: false,
        success: function (result) {
            if (result.status === 200) {
                tata.success('success', result.message)
                $(self).parent().parent().remove()
                var firstTds = $('tbody>tr>td:first-child')
                for(var i=0;i<firstTds.length;i++) {
                    $(firstTds[i]).text(i+1);
                }
            } else {
                tata.error('Error', result.message)
            }
        }
    });
}

const activeChange = (self, userId) => {
    jQuery.ajax({
        type: "PUT",
        url: '/user-management/'+userId,
        headers: {'X-CSRFToken': csrf_token},
        data: {
            csrfmiddlewaretoken: csrf_token,
            id: userId,
            is_active: $(self).val()
        },
        dataType: 'json',
        async: false,
        success: function (result) {
            if (result.status === 200) {
                tata.success('success', result.message)
            } else {
                tata.error('Error', result.message)
            }
        }
    });
}