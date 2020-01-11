jQuery('document').ready(function(){
    
    var input_task;
    input_task = jQuery('#deflaut-input').clone();

    jQuery('#add-task').on('click', function(){
        jQuery('#project-task').append(input_task);
        input_task = jQuery('#deflaut-input').clone();
    })

});

