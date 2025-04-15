$(function(){
    
	var error_email = true;

	$('#email').blur(function() {
		check_email();
	});

	function check_email(){
		var email = $('#email').val();
		if(email.endsWith('@link.cuhk.edu.hk'))
		{
            $('#email').next().hide();
			error_email = false;
		}
		else
		{
			$('#email').next().html("Email should end with @link.cuhk.edu.hk")
			$('#email').next().show();
			error_email = true;
		}
	}

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