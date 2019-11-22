var commands = {
    "request_timestamp": '',
    // [ 'SAY,HI','MOVE,50,100'] example of format
    "lmr" : [ ]
}

$(document).ready(function(){

    var scriptTemaplate = $("#scriptTemplate").html();
    var compiledScriptTemplate = Handlebars.compile(scriptTemaplate)
    $("#scriptPreview").html(compiledScriptTemplate(commands))


    $(document).on('click', "#btn-add", function(event){
        console.log('add')
        var name= document.getElementById('actionDropdown').innerHTML;
        var comando = ''
        switch(name){
            case "SAY":
                comando = name.concat(',' + $("#sayText").val());
                commands.lmr.push(comando);
                break;

            case "MATH":
                comando = ((name.concat(',' + $('#op-1').val() + ',')).concat($('#mathDropdown').html() + ',')).concat($("#op-2").val());
                commands.lmr.push(comando);
                break;
            
            case "COUNT":
                comando = name.concat(','+$('#countText').val())
                commands.lmr.push(comando);
                break;
            
            case "MOVE":
                comando = (name.concat(','+$('#move1').val())).concat(','+$('#move2').val())
                commands.lmr.push(comando);
                break;

            case "TURN":
                comando = name.concat(','+$('#turn').val());
                commands.lmr.push(comando);
                break;

            case "LIFT":
                comando = name.concat(','+$('#lift').val());
                commands.lmr.push(comando);
                break;

            case "LIGHTS":
                comando = name.concat(','+$('#lightsDropdown').html());
                commands.lmr.push(comando);
                break;

            case "ANIMATION":
                comando = name.concat(','+$('#animationDropdown').html());
                commands.lmr.push(comando);
                break;
            
            case "CUBE_LIGHT":
                comando = name
                commands.lmr.push(comando);
                break;
            
            // case "PICKUP_CUBE":
            //     comando = name.concat(','+$('#pickupDropdown').html());
            //     commands.lmr.push(comando);
            //     break;
            // case "ROLL_CUBE":
            //     comando = name.concat(','+$('#pickupDropdown').html());
            //     commands.lmr.push(comando);
            //     break;
            
            // case "WHEELIE": 
            //     comando = name.concat(','+$('#pickupDropdown').html());
            //     commands.lmr.push(comando);        
            //     break;
            
            default:
                comando=name;
                commands.lmr.push(comando);        

        }
        $("#scriptPreview").html(compiledScriptTemplate(commands))
        event.preventDefault();
    });

    $(document).on('click','#delete',function(event){
        console.log('delete')
        console.log($(this).data('delete'))
        for( var i in commands.lmr){ 
            if ( commands.lmr[i] === $(this).data('delete')){
              commands.lmr.splice(i, 1); 
            }
         }
        $("#scriptPreview").html(compiledScriptTemplate(commands))
        event.preventDefault();
    });


    $(document).on('click','#btn-clear',function(event){
        commands.lmr = []
        $("#scriptPreview").html(compiledScriptTemplate(commands))
        event.preventDefault();
    });

    $(document).on('click', '#btn-execute',function(event){
        var commandsText = JSON.stringify(commands)
        console.log(commandsText)
        $.ajax({
            url: 'http://lex:5000/lex/',
            type: "post",
            contentType: 'application/json;charset=UTF-8',
            dataType: "json",
            data : JSON.stringify(commands),
            success : function(response) {
                console.log(response);
              },
              error : function(xhr) {
                console.log(xhr);
              }
        });
        event.preventDefault();
    });

});


function deleteCommand(){

}



function reloadCommandes(){
    var scriptTemaplate = $("#scriptTemplate").html();
    var compiledScriptTemplate = Handlebars.compile(scriptTemaplate)
    $("#scriptPreview").html(compiledScriptTemplate(commands))
    console.log("list")
}