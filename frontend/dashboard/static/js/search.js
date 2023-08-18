

$("#example_filter").on('input','input', function (e) {
    var qq = document.getElementById('search').value;
    var type = document.getElementById('label_id').title;
    var url = $("#example_filter").attr("data-url")
    // console.log(url)
    $.ajax({
      // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      url: url,
      data: {
        q: qq,
        action: type
      },
      success: function (data) {
        // console.log(data);
        $("tbody").html();
        $("tbody").html(data);
      },
    });
});

// this function will be call in ajax_call.js after certain ajax request
function src_after_file_ajax(){
  console.log('ggggggg')
// $("#tableContainer").on('change', function (e) {
$("#example_filter").on('input','input', function (e) {

    var qq = document.getElementById('search').value;
    var type = document.getElementById('label_id').title;
    var url = $("#example_filter").attr("data-url")
    console.log('something just happened')
    $.ajax({
      // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
      url: url,
      data: {
        q: qq,
        action: type
      },
      success: function (data) {
        // console.log(data);
        $("tbody").html(); //#tableContainer
        $("tbody").html(data);
      },
    });
});


}
