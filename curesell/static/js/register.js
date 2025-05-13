$(function(){

	var error_name = false;
	var error_password = false;
	var error_check_password = false;


	$('#username').blur(function() {
		check_user_name();
	});

	$('#password').blur(function() {
		check_pwd();
	});

	$('#password2').blur(function() {
		check_cpwd();
	});

	function check_user_name(){
		var len = $('#username').val().length;
		if(len<2||len>20)
		{
			$('#username').next().html("Username must be 2 to 20 characters long")
			$('#username').next().show();
			error_name = true;
		}
		else
		{
			$('#username').next().hide();
			error_name = false;
		}
	}

	function check_pwd(){
		var len = $('#password').val().length;
		if(len<6||len>20)
		{
			$('#password').next().html("Password must be 6 to 20 characters long")
			$('#password').next().show();
			error_password = true;
		}
		else
		{
			$('#password').next().hide();
			error_password = false;
		}
	}


	function check_cpwd(){
		var pass = $('#password').val();
		var cpass = $('#password2').val();

		if(pass!=cpass)
		{
			$('#password2').next().html("Password doesn't match")
			$('#password2').next().show();
			error_check_password = true;
		}
		else
		{
			$('#password2').next().hide();
			error_check_password = false;
		}

	}

	$('#reg_form').submit(function() {
		check_user_name();
		check_pwd();
		check_cpwd();

		if(error_name == false && error_password == false && error_check_password == false)
		{
			return true;
		}
		else
		{
			return false;
		}

	});

})