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
                console.log("Form data successfully submitted!");
            },
            error: function(xhr, status, error) {
                console.log("Error occurred while submitting the form data:", error);
            }
        });

    });
});
