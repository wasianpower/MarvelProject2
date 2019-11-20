// JavaScript for Name Data Lookup Demo
// Jim Skon, Kenyon College, 2017
var searchType;  // Save serach type here

$(document).ready(function () {
    searchType="ARTIST";
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
function artTable(list) {
    var result = '<table class="w3-table-all w3-hoverable" border="2"><tr><th><h2>Results:</h2></th><tr>';
    var a = list.split(",");
    var aLen = a.length;
    for (var i = 0; i < aLen; i+=1) {
	result += "<tr><td><h3>"+a[i]+"</h3></td><td>"
	}
    result += "</table>";
    return result;

}



function processResults(results) {
    $('#searchresults').empty();
    $('#searchresults').append(artTable(results));
}

function clearResults() {
    $('#searchresults').empty();
}

function getMatches() {
    if ($('#search').val().length < 1) return;
    $('#searchresults').empty();
    name = $("#search").val();
    params = "find=" + name + "&operation=" + searchType;
      $.ajax(
      {
      type: "POST",
      url: "/cgi-bin/harrington1_search.py",
      data: params,
      dataType: "text",
      success:  processResults,
      error: function(request, ajaxOptions, thrownError)
	  {
	      $("#debug").text("error with get:"+request+thrownError);
	  }
      });
}