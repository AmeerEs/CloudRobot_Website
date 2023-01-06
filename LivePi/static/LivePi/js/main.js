
(function ($) {
    "use strict";

    
    /*==================================================================
    [ Validate ]*/
    var input = $('.validate-input .input100');

    $('.validate-form').on('submit',function(){
        var check = true;

        for(var i=0; i<input.length; i++) {
            if(validate(input[i]) == false){
                showValidate(input[i]);
                check=false;
            }
        }

        return check;
    });


    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function validate (input) {
        if($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        }
        else {
            if($(input).val().trim() == ''){
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }


    
    $(".forward-btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_command: 'forward'
            },
            success: function(response) {
                $(".forward-btn").text(response.seconds)
            }
        })
    })

    $(".left-btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_command: 'left'
            },
            success: function(response) {
                $(".left-btn").text(response.seconds)
            }
        })
    })

    $(".right-btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_command: 'right'
            },
            success: function(response) {
                $(".right-btn").text(response.seconds)
            }
        })
    })

    $(".backward-btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_command: 'backward'
            },
            success: function(response) {
                $(".backward-btn").text(response.seconds)
            }
        })
    })

    $(".stop-btn").click(function(){
        $.ajax({
            url: '',
            type: 'get',
            data: {
                button_command: 'stop'
            },
            success: function(response) {
                $(".stop-btn").text(response.seconds)
            }
        })
    })

})(jQuery);