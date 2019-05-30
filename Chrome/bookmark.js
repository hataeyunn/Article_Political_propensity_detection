function GetUrls()
{
chrome.tabs.query({}, function (tabs) {
    for (var i = 0; i < tabs.length; i++)
    {
        document.write("<a href='" + tabs[i].url + "' target='_blank'>" + "<b>" + tabs[i].title + "</b>" + "</a></br><button style=\"width:150px;height:30px;\" data-title=\""+tabs[i].title+"\" data-url=\""+tabs[i].url+"\">Bookmark above link</button>" + "</br>" + "</br>");
    }
    var buttons = document.getElementsByTagName("button");
    for(var i=0; i<buttons.length; i++)
    {
        buttons[i].addEventListener('click',function(){addBookmark(this.getAttribute("data-url"), this.getAttribute("data-title"));})
    }
});
}
window.addEventListener("DOMContentLoaded", GetUrls());

var BookmarkFolder, bookmarkBar, finalMessage="";

chrome.bookmarks.getTree(findOrCreateDestinationFolder);

function findOrCreateDestinationFolder(rootNodes)
{
    var rootNode;
    if(rootNodes.length>0)
    {
        rootNode = rootNodes[0];
    }
    BookmarkFolder = findBookmarksFolder(rootNode, "A.P.K Bookmarks");
    if(!BookmarkFolder)
    {
        bookmarkBar = findBookmarksFolder(rootNode,"Bookmarks bar");
        chrome.bookmarks.create({parentId:bookmarkBar?bookmarkBar.id:"1",title:"A.P.K Bookmarks"}, function(bmk){
            BookmarkFolder=bmk;
            finalMessage += "Destination Folder created under Bookmarks bar.\n"
        });
    }
    else
    {
        finalMessage += "\n"
    }
}

function findBookmarksFolder(rootNode, searchString)
{
    if(rootNode.url)
    {
        return null;
    }
    else if(rootNode.title.indexOf(searchString)>=0)
    {
        return rootNode;
    }
    for(var i=0; i<rootNode.children.length; i++)
    {
        var dest = findBookmarksFolder(rootNode.children[i], searchString);
        if(dest)
        {
            return dest;
        }
    }
    return null;
}

function addBookmark(bookmarkURL, bookmarktitle)
{
    if(BookmarkFolder)
    {
        chrome.bookmarks.create({title:bookmarktitle,parentId:BookmarkFolder.id,url:bookmarkURL});
        finalMessage += "Added bookmark." + "\n" + "(" + bookmarktitle + ")" + "\n";
    }
    else
    {
        finalMessage += "Could not add bookmark.\n";
    }
    alert(finalMessage);
}