$(document).ready(function() {
    $("#submit_btn").click(function(event) {
        event.preventDefault();
        
        var formData = new FormData();
        formData.append("csrfmiddlewaretoken", $("input[name='csrfmiddlewaretoken']").val());
        formData.append("title", $("#id_title").val());
        formData.append("description", $("#id_description").val());
        formData.append("amount", parseInt($("#id_amount").val()));
        formData.append("category", $("#id_category").val());

        $.ajax({
            type: "POST",
            url: "",
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                $("#id_title").val("");
                $("#id_description").val("");
                $("#id_amount").val("");
                $("#id_category").val("");
            },
            error: function(xhr, status, error) {
                console.log("Error occurred while submitting the form data:", error);
            }
        });

    });
    $(document).ready(function() {
        $("#delete_btn").click(function(event) {
            mythis = this;
            event.preventDefault();
    
            // Get the expense ID from the HTML attribute or any other way that you're using
            var expenseId = $(this).attr("data-expense-id");
    
            // Send an AJAX request to delete the expense
            $.ajax({
                type: "DELETE",
            url: "/" + expenseId + "/delete/",
            headers: {
                "X-CSRFToken": $("input[name='csrfmiddlewaretoken']").val()
            },
            success: function(response) {
                location.reload();
            },
            error: function(xhr, status, error) {
                console.log("Error occurred while deleting the expense:", error);
            }
            });
        });
    });
    
});
