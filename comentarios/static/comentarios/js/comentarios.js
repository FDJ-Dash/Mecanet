$(document).on('ready', main_comentarios);
var csrftoken

function main_comentarios() {
    csrftoken = getCookie('csrftoken');

	$.ajaxSetup({
	 // data: {csrfmiddlewaretoken: '{{ csrf_token }}' },
		beforeSend: function(xhr, settings) {
			if(settings.type == "POST"){
			  //  xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
			    xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
/*
    $.ajax({
        //url : "create_post/", // the endpoint
        type : "POST", // http method
        data : {
            //the_post : $('#post-text').val(),
            the_post : $('#crear-pregunta input:visible').val(),
            csrfmiddlewaretoken: '{{ csrf_token }}'
        }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#crear-pregunta input:visible').val(''); // remove the value from the input
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "
                +errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
*/
	$('#preguntas button').on('click', enviar_pregunta);

	$('#preguntas').on('click', 'a', cargar_respuestas);
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function enviar_pregunta() {
	var input = $('#crear-pregunta input:visible');

	if(input.val() != ''){
		$.post('/guardar-pregunta/', { pregunta: input.val() }, actualizar_preguntas);
	}
}

function actualizar_preguntas (data) {
	var ul = $('#preguntas ul');

	ul.html('');
	$('#crear-pregunta input:visible').val('');

	$.each(data.preguntas, function(i, elemento){
		$('<li><a data-id="' + elemento.id + '">' + elemento.titulo + '</a></li>').appendTo(ul);
	});
}

function cargar_respuestas(data) {
	var id = $(data.currentTarget).data('id');

	$.get('/cargar-respuestas/' + id, mostrar_respuestas);
}

function mostrar_respuestas (data) {
	var respuestas = $('#respuestas');

	respuestas.html('');


	var pregunta = $('#preguntas a[data-id="' + data.pregunta + '"]').html();

	var div = $('<div>');

	$('<a class="regresar">').html('Regresar').appendTo(div);

	div.append('<p data-id="' + data.pregunta + '">' + pregunta + '</p>');

	$('<a class="responder">').html('Responder').appendTo(div).on('click', responder);

	div.appendTo(respuestas);


	var ul = $('<ul>')

	$.each(data.respuestas, function(i, elemento){
		$('<li>').html(elemento).appendTo(ul);
	});

	ul.appendTo(respuestas);

	$('#comentarios').css('right', '-110%');
	respuestas.css('right', '0');

	respuestas.on('click', '.regresar', function(){
		respuestas.css('right', '-110%');
		$('#comentarios').css('right', '0');
	});

}

function responder(data) {
	var div = $('<div id="responder">');

	$('<textarea placeholder="Escribe tu respuesta">').appendTo(div);
	$('<button>').html('Enviar Respuesta').appendTo(div).on('click', enviar_respuesta);

	$('#respuestas div:first').after(div);
}

function enviar_respuesta() {
	var respuesta = $('#responder textarea');

	if(respuesta.val() != ''){
		$.post(
			'/guardar-respuesta/',
			{ respuesta: respuesta.val(), pregunta: $('#respuestas p').data('id') },
			actualizar_respuestas
		);
	}
}

function actualizar_respuestas(data) {
	var ul = $('#respuestas ul');

	ul.html('');

	$.each(data.respuestas, function(i, elemento){
		$('<li>').html(elemento).appendTo(ul);
	});

	$('#responder').remove();
}