var title = "title";
var url = "url";


chrome.tabs.getSelected(null, function(tab) {
	myURL = tab.url;
});

// listening for an event / one-time requests
// coming from the popup
chrome.extension.onMessage.addListener(function(request, sender, sendResponse) {
    switch(request.type) {
        case "scrap":
			getUrl();
           setTimeout(() => {
			scrap( );
		   }, 500); 
		break;
		case "show":
			getUrl();
			setTimeout(() => {
				show();
			   }, 500); 
		break;
    }
    return true;
});

// listening for an event / long-lived connections
// coming from devtools

function post_to_url(path, params, method) {
    method = method || "post"; // Set method to post by default, if not specified.
    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var url = document.createElement("form");
    url.setAttribute("method", method);
    url.setAttribute("action", path);
    for(var key in params){
    var hiddenField = document.createElement("input");
    hiddenField.setAttribute("type", "hidden");
    hiddenField.setAttribute("name",key)
    hiddenField.setAttribute("value", params[key]);
    url.appendChild(hiddenField);
    }
    document.body.appendChild(url);
    url.submit();
}

// send a message to the content script
var colorDivs = function() {
	chrome.tabs.getSelected(null, function(tab){
	    chrome.tabs.sendMessage(tab.id,{type: "colors-div", color: "#000000"});
	    // setting a badge
		chrome.browserAction.setBadgeText({text: "red!"});
	});
}
var show = function() {
	alert("결과보기")
	
	var ho = post_to_url('http://34.73.96.234:5000/capstone',{'url':url});


}
var scrap = function() {
	alert("즐겨찾기 추가완료");
	let information = {
		"url" : url,
		"title" : title
	};
	let info = JSON.stringify(information);
	if(url!="url"&&information!={}) localStorage.setItem(localStorage.length,info);

}
var getUrl =function(){
	chrome.tabs.getSelected(null, function(tab) {
		url = tab.url;
		title = tab.title;
	});
}
