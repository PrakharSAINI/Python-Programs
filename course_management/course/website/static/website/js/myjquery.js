$("#register_button").click(function(){
		var name=$("#InputName").val();
		var email=$("#InputEmail").val();
		var pwd=$("#InputPass").val();
		$.ajax({
			type: 'POST',
			url: "registering",
			data: {"user_name":name,"user_email":email,"user_pass":pwd},
			success: function(response){
				window.location.replace("login")
			},
			error: function(err){}
		});

	});

$("#login_button").click(function(){
		var email=$("#InputEmail").val();
		var pwd=$("#InputPass").val();
		$.ajax({
			type: 'POST',
			url: "logging",
			data: {"user_email":email,"user_pass":pwd},
			success: function(response){
				window.location.replace(response)
			},
			error: function(err){}
		});
	});
