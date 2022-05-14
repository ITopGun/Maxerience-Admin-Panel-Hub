$(document).ready(function(){
    $('#pdf-input').change(function(){
        var file = this.files[0]
        if(file) {
            $("#pdf-upload-btn").attr("file-upload", "true")
            $('#pdf-preview-name').text(file.name)
            $("#import-pdf-wrap").hide()
            $('#pdf-preview-wrap').show()
        }
    })
    $("#pdf-upload-btn").click(function(e){
        e.preventDefault();
        if($("#pdf-upload-btn").attr("file-upload")) {
            var file = document.querySelector("#pdf-input").files[0]
            var description = $('#pdf-description').val()
            var pdfData = new FormData();
            pdfData.append('file', file);
            pdfData.append('description', description);
            pdfData.append('page_name', page_name);
            pdfData.append('csrfmiddlewaretoken', csrf_token);
            jQuery.ajax({
                type: "POST",
                url: '/solution/',
                data: pdfData,
                contentType: false,
                processData: false,
                success: function (result) {
                    if (result.status === 200) {
                        $("#pdf-upload-btn").attr("file-upload", "false")
                        $('#pdf-preview-wrap').hide()
                        $("#import-pdf-wrap").show()
                        $(".pdf-card-wrap").append($('<div />').html(`
                            <a class="btn-card" href="${ result.dir }" target="_blank">
                                <div class="card">
                                    <img src="/static/assets/image/pdf.png">
                                    <label>${ result.title }</label>
                                </div>
                            </a>
                            <button class="btn btn-danger pdf-del-btn" data-id="${ result.id }">Delete</button>
                            <h4 style="margin-left:30px;">${ result.description }</h4>
                        `))
                        $('#pdf-description').val('')
                        tata.success('Success', 'File upload is successed.')
                    } else {
                        tata.error('Error', result.message)
                        $('#pdf-description').val('')
                    }
                }
            });
        }
    })
    $('.pdf-card-wrap').on('click', '.pdf-del-btn', function(e){
        var _this = e.target;
        var id=$(_this).attr('data-id');
        jQuery.ajax({
            type: "DELETE",
            url: '/solution/'+id,
            headers: {'X-CSRFToken': csrf_token},
            data: {
                csrfmiddlewaretoken: csrf_token,
                id: id
            },
            dataType: 'json',
            async: false,
            success: function (result) {
                if (result.status === 200) {
                    tata.success('success', result.message)
                    $(_this).parent().remove()
                } else {
                    tata.error('Error', result.message)
                }
            }
        });
    })
})