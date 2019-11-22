var commands = {
    "commandos" : [
        'SAY, hello world ', 'MOVE, 30, 40'





        // {
        //     "command": "SAY",
        //     "param1": "hello world",
        //     "param2": "",
        //     "param3":""
        // },
        // {
        //     "command": "SAY",
        //     "param1": "hello world",
        //     "param2": "",
        //     "param3":""
        // },
        // {
        //     "command": "SAY",
        //     "param1": "hello world",
        //     "param2": "",
        //     "param3":""
        // }
    ]
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
                comando = name;
                commands.commandos.push(comando);
                console.log(commands.commandos[2])

                break;

            case "MATH":
                comando = ((name.concat($('#op-1').val())).concat($('#mathDropdown').html())).concat($("#op-2").val());
                commands.commandos.push(comando);
                console.log(commands.commandos[0])
                break;
            
            // case "COUNT":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("COUNT").style.display='block';
            //     break;
            
            // case "MOVE":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("MOVE").style.display='block';
            //     break;

            // case "TURN":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("TURN").style.display='block';
            //     break;

            // case "LIFT":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("LIFT").style.display='block';
            //     break;

            // case "LIGHTS":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("LIGHTS").style.display='block';
            //     break;

            // case "ANIMATION":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("ANIMATION").style.display='block';
            //     break;
            
            // case "CUBE_LIGHT":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("PICKUP").style.display='none'
            //     document.getElementById("CUBE_LIGHT").style.display='block'
            //     break;
            
            // case "PICKUP":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='block'
            //     break;
            // case "ROLL_CUBE":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     document.getElementById("CUBE_LIGHT").style.display='none'
            //     document.getElementById("PICKUP").style.display='block'
            //     break;
            
            // case "WHEELIE":
            //         document.getElementById("SAY").style.display='none';
            //         document.getElementById("MATH").style.display='none';
            //         document.getElementById("COUNT").style.display='none';
            //         document.getElementById("MOVE").style.display='none';
            //         document.getElementById("TURN").style.display='none';
            //         document.getElementById("LIFT").style.display='none';
            //         document.getElementById("LIGHTS").style.display='none';
            //         document.getElementById("ANIMATION").style.display='none';
            //         document.getElementById("CUBE_LIGHT").style.display='none'
            //         document.getElementById("PICKUP").style.display='block'
            //         break;
            
            default:
                comando=comando;
        }
        $("#scriptPreview").html(compiledScriptTemplate(commands))
        event.preventDefault();
    });



});


function addCommand(object){
    commands.commandos.push(object)
}

function deleteCommand(){

}



function reloadCommandes(){
    var scriptTemaplate = $("#scriptTemplate").html();
    var compiledScriptTemplate = Handlebars.compile(scriptTemaplate)
    $("#scriptPreview").html(compiledScriptTemplate(commands))
    console.log("list")
}