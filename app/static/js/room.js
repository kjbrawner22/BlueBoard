$(document).ready(function() {
	var quill = new Quill('#editor', {
    theme: 'snow'
	});

	var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('connect', function() {
    socket.emit('connected', {});

    socket.on('disconnect', function() {
    	socket.emit('disconnected');
    });
  });

  socket.on('status', function(data) {
  	$('#chat-body').append(data.msg + "\n");
  });

  socket.on('receive message', function(data) {
  	$('#chat-body').append(data.msg + "\n");
  });


});