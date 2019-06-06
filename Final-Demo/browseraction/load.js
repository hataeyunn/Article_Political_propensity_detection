
    //document.write("<h1 align=\"center\"><b>스크랩 된 기사 보기</b></h1>")

        for(var i=0; i<localStorage.length; i++)
        {   
            
            let value = localStorage.getItem(i);
            let values = JSON.parse(value);
            if(localStorage.getItem(i)!=null){ 
                document.write("<table class=\"table table-striped table-bordered \">");
                document.write("<tbody><tr><td>");
                document.write("<h4><b>기사 제목 :</b></h4>");
                document.write("</td></tr>");
                document.write("<tr><td>");
                document.write("<a href='" + values.url+"'target='_blank'>" + "<b>"+values.title+"</b>"+"</a>");
                document.write("</td></tr>");
                document.write("<tr><td>");
                document.write("<h4><b>Keywords :</b></h4>");
                document.write("</td></tr>");
                document.write("<tr><td>");
                document.write("<h5><b>"+ values.keywords+" </b></h5>");
                document.write("</td></tr></tbody></table>");
          

            }

        }
   
