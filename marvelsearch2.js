// JavaScript for Name Data Lookup Demo
// Jim Skon, Kenyon College, 2017
var searchType;  // Save serach type here

$(document).ready(function () {
    searchType="Last";
    $("#search-btn").click(getMatches);
    $("#clear").click(clearResults);

    $(".dropdown-menu li a").click(function(){
	console.log("pick!"+$(this).text());
	$(this).parents(".btn-group").find('.selection').text($(this).text());
	searchType=$(this).text();
    });
});

function showInfo(divisionIdentity) {
  var x = document.getElementById(divisionIdentity);
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

// Build output table from comma delimited list
function nameTable(list) {
    var result = '<table class="w3-table-all w3-hoverable" border="2"><tr><th>Hero Name</th><th>Wiki Link</th><th>Additional Info</th><tr>';
    var a = list.split(",");
    var aLen = a.length;
    for (var i = 0; i < aLen; i+=10) {
	result += "<tr><td>"+a[i]+"</td><td><a href=\""+a[i+1]+"\"><font color=\"blue\">Link</font></a></td><td><button onclick=\"showInfo('myDIV"+i+"')\">Show</button><div id=\"myDIV"+i+"\" style=\"display:none;\"><ul><li>First Appearance: "+a[i+2]+"</li><li>Total Appearances: "+a[i+3]+"</li><li>Alignment: "+a[i+4]+"</li><li>Status: "+a[i+5]+"</li><li>Identity: "+a[i+6]+"</li><li>Gender: "+a[i+7]+"</li><li>Eyes: "+a[i+8]+"</li><li>Hair: "+a[i+9]+"</li></ul></div></td><tr>";
    }
    result += "</table>";
    return result;
}



function processResults(results) {
    $('#searchresults').empty();
    $('#searchresults').append(nameTable(results));
}

function clearResults() {
    $('#searchresults').empty();
}

function getMatches() {
    if ($('#search').val().length < 2) return;
    $('#searchresults').empty();
    name = $("#search").val();
    params = "name=" + name + "&type_select=" + searchType;
      $.ajax(
      {
      type: "POST",
      url: "/cgi-bin/harrington1_marvelclient.py",
      data: params,
      dataType: "text",
      success:  processResults,
      error: function(request, ajaxOptions, thrownError)
	  {
	      $("#debug").text("error with get:"+request+thrownError);
	  }
      });
}
