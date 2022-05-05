var slug = ''
$(document).ready(function(){
    $(window).scroll(function(){
        if($(window).scrollTop() > 0){
            $('.header_area').addClass('show');
        } else {
            $('.header_area').removeClass('show');
        }
    });

    $('.delete-recipe-btn').on('click', function(){
        slug = $(this).data('slug')
    })

    $('#delete-confirm-btn').on('click', function(){
        jQuery.ajax({
            type: "POST",
            url: '/delete-recipe/',
            data: {
                csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
                slug: slug
            },
            dataType: 'json',
            async: false,
            success: function (result) {
                if (result.status === 200) {
                    $('.col[data-slug=' + result.message).remove()
                    tata.success('Success', 'Deleted Successfully.')
                } else {
                    tata.error('Error', result.message)
                }
            }
        });
    })
})