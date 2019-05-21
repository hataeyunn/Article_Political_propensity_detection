function url(){
    var url = "Default";
    
    chrome.tabs.getSelected(null, function (tab) {
        document.getElementById('url').innerHTML = tab.url;
        url = tab.url;
    });

  
    chrome.tabs.getSelected(null, function (tab) {
        document.getElementById('Link1').innerHTML = url;       
    });


}


url();


