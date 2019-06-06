window.onload = function() {
	chrome.extension.sendMessage({
		type: "clicked"
	});
	document.getElementById("button_1").onclick = function() {
		chrome.extension.sendMessage({
	        type: "show"
	    });
	}
	document.getElementById("button_2").onclick = function() {
		chrome.extension.sendMessage({
	        type: "summarize"
	    });
	}
	document.getElementById("button_3").onclick = function() {
		chrome.extension.sendMessage({
	        type: "scrap"
	    });
	}
	document.getElementById("button_4").onclick = function() {
		chrome.extension.sendMessage({
	        type: "show-scrap"
	    });
	}
}