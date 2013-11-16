//Presentation Manager functions
function close_window(el) {
	var wnd = el.parentNode.parentNode;
	wnd.parentNode.removeChild(wnd);
}

function align_wnd_iframe(wnd) {
	// When window resized, width of inner IFRAME is aligned auto (100%)
	// So we only need to align it's height
	$("#" + wnd + "_iframe").height($("#" + wnd).height() - 26 - 21);
}

function maximize_window(el, wnd) {
	//Maximize/Restore window
	if ($(el).attr("maximized") == "true") {
		$(el).attr("maximized", "false");
		$("#" + wnd).offset({top: 100, left: 100});
		$("#" + wnd).width(300);
		$("#" + wnd).height(250);
	}
	else {
		$(el).attr("maximized", "true");
		$("#" + wnd).offset({top: 0, left: 0});
		$("#" + wnd).width($(window).width()-12);
		$("#" + wnd).height($(window).height()-12);
	}

	align_wnd_iframe(wnd);
}

//Open new window/folder
function open_folder(src, title) {
	$.get('/ajax_query/get_window/', {"src": src, "title": title}, function(data){
		$("body").append(data);
	});
}

function open_program(src, title, width, height) {
	$.get('/ajax_query/get_window/', {"src": src, "title": title, "width": width, "height": height}, function(data){
		$("body").append(data);
	});
}

function open_dialog(dlg, title) {
	$.get('/ajax_query/get_dialog/', {"dlg": dlg, "title": title}, function(data){
		$("body").append(data);
	});
}

function shutdown() {
	//he he
	$("body").empty();
	$("body").append("<div id='shutdown' style='width: 100%; height: 500px;'></div>");
	$("#shutdown").css("background-image", "url('/appmedia/imgs/dialogs/shutdown_complete.png')");
	$("#shutdown").css("background-position", "center center");
	$("#shutdown").css("background-repeat", "no-repeat");
}

function lockup() {
	//$("body").append("<div id='lockup' style='width: 100%; height: 500px;'></div>");
	$("body").empty();
	$("html").css('background-image', "url('/appmedia/imgs/dialogs/lockup.png')");
}