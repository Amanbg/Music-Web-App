
$(document).on('ready', function(){
	$('.addtrackform').hide();
	$('.verticalline').hide();
	$(document).on('click', '.addform', function(event){
		$('.base').animate({
			'marginLeft' : "-=233px" //moves left
		});
		$('.addtrackform').show();
		$('.verticalline').fadeIn(960);
	})

	$('.addgenreform').hide();
	$(document).on('click', '.addform-genre', function(event){
		$('.base').animate({
			'marginLeft' : "-=233px" //moves left
		});
		$('.addgenreform').show();
		$('.verticalline').fadeIn(960);
	})

	$(document).on('click', '#hidetrackform', function(event){
		$('.base').animate({
			'marginLeft' : "+=233px" //moves right
		});
		$('.verticalline').hide();
		$('.addtrackform').hide();
	})

	$(document).on('click', '#hidegenreform', function(event){
		$('.base').animate({
			'marginLeft' : "+=233px" //moves right
		});
		$('.verticalline').hide();
		$('.addgenreform').hide();
	})


	$(document).on('click', '.edit', function(event){
        event.preventDefault();

        $this = $(this);
        trackid_obj=$this.data('trackid');
        tracktitle_obj = $this.data('tracktitle');
        trackgenre_obj = $this.data('trackgenre');
        trackrating_obj = $this.data('trackrating');

       	$("input[name='trackid']").val(trackid_obj); 
        $("input[name='title']").val(tracktitle_obj);
        $("input[name='genre']").val(trackgenre_obj);
        $("input[name='rating']").val(trackrating_obj);

        var modal = document.getElementById('myModal');
        var span = document.getElementsByClassName("close")[0];
        
        modal.style.display = "block";

        span.onclick = function() {
            modal.style.display = "none";
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

        $(".add-new-form-container").find(".editbtn").click(function (evt) {
        	evt.preventDefault();
        	addnew_track_submit();
		});
     
    });

    $('form.add-new-form').find('input#title').on('change', function(){
        value = $(this).val();
        if(!(value == "") || !(value == null)) {
            $('add-new-form').submit();
        }
    });

    $('form.add-new-form').find('input#genre').on('change', function(){
        value = $(this).val();
        if(!(value == "") || !(value == null)) {
            $('add-new-form').submit();
        }
    });

    $('form.add-new-form').find('input#rating').on('change', function(){
        value = $(this).val();
        if(!(value == "") || !(value == null)) {
            $('add-new-form').submit();
        }
    });


	function addnew_track_submit() {
    	$.ajax({
           	type: "POST",
           	url: "/track/",
           	data: $("#add-new-form").serialize(), // serializes the form's elements.
           	success: function(data){
           		console.log("print");
            	if(alert("Changes saved Successfully!!")){}
                else
                   	window.location.reload(); 
            }
          
    	});
	}
});