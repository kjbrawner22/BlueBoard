$(document).ready(function() {
	var quill = new Quill('#editor', {
    theme: 'snow'
	});

	var socket = io.connect('http://' + document.domain + ':' + location.port);
  var textUpdated = false;
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

  socket.on('updated text', function(data){
    console.log("updating contents")
    if(data.delta != quill.getContents()) {
    	textUpdated = true;
    	quill.updateContents(data.delta);
    }
  });

  quill.on('text-change', function(delta, source)  {
  	if(textUpdated) {
  		textUpdated = false;
  	} else {
  		socket.emit('text change', {"delta": delta});
  	}
  });
});