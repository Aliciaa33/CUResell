$(function(){
	// --- Add CSRF helper and setup here ---
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^GET|HEAD|OPTIONS|TRACE$/.test(settings.type)) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
	// --- End CSRF setup ---
    
	// Email Checking start
	var error_email = true;

	$('#email').blur(function() {
		check_email();
	});

	function check_email(){
		var email = $('#email').val();
		if(email.endsWith('@link.cuhk.edu.hk'))
		{
            // $('#email').next().hide();
			// error_email = false;
			$.ajax({
				url: '/check_email/', // Change to your backend endpoint
				type: 'POST',
				data: { email: email },
				success: function(response) {
					if(response.exists) {
						$('#email').next().html("Email already exists");
						$('#email').next().show();
						error_email = true;
					} else {
						$('#email').next().hide();
						error_email = false;
					}
				}
        	});
		}
		else
		{
			$('#email').next().html("Email should end with @link.cuhk.edu.hk")
			$('#email').next().show();
			error_email = true;
		}
	}
	// Email Checking end

	$('#verify_form').submit(function() {
		check_email();
	
		if(error_email)
		{
			return false;
		}
		else
		{
			return true;
		}

	});
})