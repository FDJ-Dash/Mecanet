$(document).on('ready', main);

function main () {
	$('#talleres').on('click', 'a', cargar_contenido_taller);
}

function cargar_contenido_taller (data) {
	var id = $(data.currentTarget).data('id');
    console.log(data, id);
	$.get('cargar-contenido-taller/' + id, cargar_taller)
}

function cargar_taller(data){
	var contenido = $('#contenido-taller');
	
	contenido.html('');

	$('<a class="regresar">').html('Regresar').appendTo(contenido);

	$('<h2>').html(data.nombre).appendTo(contenido);

	$('<iframe src="http://www.youtube.com/embed/' + data.url + '" allowfullscreen>').appendTo(contenido);

	$('<p>').html(data.descripcion).appendTo(contenido);

	$('#taller').css('left', '-110%');
	contenido.css('left', '0');

	contenido.on('click', 'a', function(){
		contenido.css('left', '-110%');
		$('#taller').css('left', '0');
	});
}