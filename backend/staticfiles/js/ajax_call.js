document.addEventListener("readystatechange", (event) => {
  if (document.readyState === 'complete') {
    $("#tableContainer").hide();
  }
});

$("#check").click(function () {
    var url = $("#ResultForm").attr("data-url");
    var url_file = $("#ResultForm").attr("data-url-file");
    // var paperAuthorId = $(this).val();
    var level_id = $('#id_level').val();
    var section_id = $('#id_section').val();
    var semester_id = $('#id_semester').val();
    var check_file = $('button').val()

// This student detail to check their results
    if (check_file=='') {
        console.log('is empty');
        $.ajax({
          url: url,
          data: {
            level: level_id,
            section: section_id,
            semester: semester_id,
          },
          success: function (data) {
            // console.log(data)
            // $("#selectForm").hide();
            $("#tableContainer").show();
            $("#tableContainer").html(data);
            src_after_file_ajax()
          },
        });
    }else{

// This pull out results files for download
        console.log('is not enmpty');
        $.ajax({
          url: url_file,
          data: {
            level: level_id,
            section: section_id,
            semester: semester_id,
          },
          success: function (data) {
            // console.log(data)
            // $("#selectForm").hide();
            $("#tableContainer").show();
            $("#tableContainer").html(data);
            src_after_file_ajax()
          },
        });
    };
});

