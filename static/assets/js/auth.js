var validEmailRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
$(document).ready(function () {

$("#signup-btn").on('click', function(e){
	e.preventDefault();
	var email, password, cpassword, term_condition;
	email = $("#email").val()
	password = $("#password").val()
	cpassword = $("#cpassword").val()

	if((email == '') || (password == '') || (cpassword == '')) {
		tata.error('Error', 'Input fields correctly.')
	} else if(!email.match(validEmailRegex)) {
		tata.error('Error', 'Email is not valid.')
	} else if(password.length < 8) {
		tata.error('Error', 'Use 8 characters or more for your password.')
	} else if(password != cpassword) {
		tata.error('Error', 'Passwords do not match.')
	} else {
		jQuery.ajax({
            type: "POST",
            url: '/signup/',
            data: {
                csrfmiddlewaretoken: csrf_token,
                email: email,
                password: password,
                cpassword: cpassword
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
	}
});

$("#signin-btn").on('click', function(e){
	e.preventDefault();
	var email, password;
	email = $("#email").val()
	password = $("#password").val()
	if((email == '') || (password == '')) {
		tata.error('Error', 'Input fields correctly.')
	} else if(!email.match(validEmailRegex)) {
		tata.error('Error', 'Email is not valid.')
	} else if(password.length < 8) {
		tata.error('Error', 'Use 8 characters or more for your password.')
	} else {
		jQuery.ajax({
            type: "POST",
            url: '/login/',
            data: {
                csrfmiddlewaretoken: csrf_token,
                email: email,
                password: password
            },
            dataType: 'json',
            async: false,
            success: function (result) {
                if (result.status === 200) {
                    window.location = '/'
                } else {
                    tata.error('Error', result.message)
                }
            }
        });
	}
});

});