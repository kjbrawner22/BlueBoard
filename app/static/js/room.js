$(document).ready(function() {
	var quill = new Quill('#editor', {
    theme: 'snow'
	});

	var socket = io.connect('http://' + document.domain + ':' + location.port);
  socket.on('connect', function() {
    socket.emit('connected', {});
  });
});