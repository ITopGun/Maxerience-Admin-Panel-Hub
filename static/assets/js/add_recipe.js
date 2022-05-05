var validEmailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
$(document).ready(function () {

$(".main-wrapper").on('click', '#add-recipe-btn, #edit-recipe-btn', function(e){
	e.preventDefault();
	var title, category, description, ingredients, method, prepare_time, cook_time, image;
	title = $("#recipe_title").val()
	category = $("#recipe_category").val()
	description = $("#recipe_description").val()
	ingredients = $('#recipe_ingredients').tagsinput('items')
	method = tinymce.get("recipe_method").getContent();
	prepare_time = $("#recipe_prepare_time").val()
	cook_time = $("#recipe_cook_time").val()
	image = document.getElementById('recipe_image').files[0]

	if(title == '') {
		tata.error('Error', 'Input title field.')
	} else if(ingredients.length == 0) {
		tata.error('Error', 'Input ingredients field.')
	} else if(method == '') {
		tata.error('Error', 'Input method.')
	} else {
		var recipeData = new FormData();
		recipeData.append('csrfmiddlewaretoken', csrf_token);
		recipeData.append('title', title);
		recipeData.append('category', category);
		recipeData.append('description', description)
		recipeData.append('ingredients', JSON.stringify(ingredients))
		recipeData.append('method', method)
		recipeData.append('prepare_time', prepare_time)
		recipeData.append('cook_time', cook_time)
		if($('#recipe_image').attr('filenone') == 'false') recipeData.append('image', image)
		var url = '/add-recipe/'
		if($(this).attr('id') == 'edit-recipe-btn') {
			url = '/edit-recipe/'
			var pathname = window.location.pathname.split('/')
			var slug = pathname[pathname.length - 2]
			recipeData.append('slug', slug)
			var edit_image_num = $('.imageuploadify-details').length
			recipeData.append('edit_image_num', edit_image_num)
		}
		jQuery.ajax({
            type: "POST",
            url: url,
            data: recipeData,
            contentType: false,
            processData: false,
            success: function (result) {
                if (result.status === 200) {
                    console.log("sdfsdfsdf")
                } else {
                    tata.error('Error', result.message)
                }
            }
        });
	}
})

})