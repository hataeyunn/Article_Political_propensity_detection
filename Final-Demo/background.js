var _url = "";
var _title = "";
var return_json="";
chrome.browserAction.onClicked.addListener(function(tab) {
    // Send a message to the active tab
    
});

  chrome.runtime.onMessage.addListener(
    function(request, sender, sendResponse) {
      if( request.message === "open_new_tab" ) {
        //chrome.tabs.create({"url": request.url});
      }
    }
);

chrome.extension.onMessage.addListener(function(request) {
    switch(request.type) {
        case "clicked":
                chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
                function(tabs){
                   _url = tabs[0].url;
                   _title = tabs[0].title;
                }
             );

        break;

        case "show":
			show();
        break;
        case "summarize":
            let values = JSON.parse(return_json);

            alert(values.summarize);
            window.onload = function what(){
                document.getElementById('summarize').innerHTML = values.summarize;
                };

        break;
        case "scrap":
			scrap();
        break;
        
        case "show-scrap":
            changePopup();
        break;
		
    }
    return true;
});

var scrap = function() {
    let values = JSON.parse(return_json);

	let information = {
		"url" : _url,
        "title" : _title,
        "keywords": values.keywords
	};
	let info = JSON.stringify(information);
	if(_url!=""&&information!={}) localStorage.setItem(localStorage.length,info);
	alert("즐겨찾기 추가완료");

}

var show = function() {
    alert("기다려주세요. 분석중입니다.");
    var http = new XMLHttpRequest();

    http.open("POST","http://34.73.96.234:5000/capstone",true)
    http.onreadystatechange = function(){
        if (http.readyState==4){
            if(http.status==200){
                return_json = http.responseText;
               
                var values = JSON.parse(return_json);
                var keywords =values.keywords;
                keywords = keywords.replace('[','');
                keywords = keywords.replace(']','')
                keywords = keywords.split(',')
		if(keywords.length>1)
                {var result = values.result.replace('키워드',keywords[0]+keywords[1])
                }
		else{
		var result = values.result.replace('키워드',keywords[0])
		}


		alert(result);

            }
        }
    };
    http.setRequestHeader("Content-Type", "application/json");
    http.send(JSON.stringify({"url":_url}))

}
function changePopup(){
    chrome.tabs.onUpdated.addListener(function(tabId, changeInfo, tab) {
            chrome.browserAction.setPopup({
                tabId: tabId,
                popup: 'browseraction/scrap.html'
            });
        
    });
}

