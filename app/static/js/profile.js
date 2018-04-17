$(document).ready(function() {
	$('#invite-submit').click(function() {
		console.log('clicked');
		var code = $('#invite-input').val();
		window.location.href = "/invite/" + code;
	});
});