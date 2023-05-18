$(function(){
    var loadForm = function(){
      console.log('yoyoyoy');
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function(){
          $('#formModel').modal('show');
        },
        success: function(response){
          $("#formModel .modal-content").html(response.html_form);
        },
      });
    };
  
    var saveForm = function () {
      var form = $(this);
      $.ajax({
        url: form.attr("action"),
        data: form.serialize(),
        type: form.attr("method"),
        dataType: 'json',
        success: function (response) {
          if (response.form_is_valid) {
            $("#expense-table tbody").html(response.table_html);
            $("#formModel").modal("hide");  
          } else {
            $("#formModel .modal-content").html(response.html_form);
          }
        }
      });
      return false;
    };
  


    $("#create-btn").click(loadForm);
    $("#formModel").on("submit", ".create-form", saveForm);


    $("#expense-table").on("click", "#update-btn", loadForm);
    $("#formModel").on("submit", ".update-form", saveForm);

    $("#expense-table").on("click", "#delete-btn", loadForm);
    $("#formModel").on("submit", ".delete-form", saveForm);

  });
  