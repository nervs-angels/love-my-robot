$(document).ready(function(){
    
    //code for changing the option displayed in the main dropdown
    $(document).on('click','#option', function(event){
        console.log('hola')
        console.log($(this).data('action'))
        console.log($(this).data('parent'))

        updateDropdown($(this).data('action'),$(this).data('parent'))

        //switch for conditional rendering of appropriate secondary dropdown according to the option selected in the main dropdown 
        switch(document.getElementById('actionDropdown').innerHTML){
            case "SAY":
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("SAY").style.display='block';
                break;

            case "MATH":
                document.getElementById("SAY").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'    
                document.getElementById("MATH").style.display='block';
                break;
            
            case "COUNT":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("COUNT").style.display='block';
                break;
            
            case "MOVE":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("MOVE").style.display='block';
                break;

            case "TURN":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("TURN").style.display='block';
                break;

            case "LIFT":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("LIFT").style.display='block';
                break;

            case "LIGHTS":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("LIGHTS").style.display='block';
                break;

            case "ANIMATION":
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
                document.getElementById("ANIMATION").style.display='block';
                break;
            
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
            
            // case "PICKUP_CUBE":
            //     document.getElementById("SAY").style.display='none';
            //     document.getElementById("MATH").style.display='none';
            //     document.getElementById("COUNT").style.display='none';
            //     document.getElementById("MOVE").style.display='none';
            //     document.getElementById("TURN").style.display='none';
            //     document.getElementById("LIFT").style.display='none';
            //     document.getElementById("LIGHTS").style.display='none';
            //     document.getElementById("ANIMATION").style.display='none';
            //     // document.getElementById("CUBE_LIGHT").style.display='none'
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
            //     // document.getElementById("CUBE_LIGHT").style.display='none'
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
            //         // document.getElementById("CUBE_LIGHT").style.display='none'
            //         document.getElementById("PICKUP").style.display='block'
            //         break;
            
            default:
                document.getElementById("SAY").style.display='none';
                document.getElementById("MATH").style.display='none';
                document.getElementById("COUNT").style.display='none';
                document.getElementById("MOVE").style.display='none';
                document.getElementById("TURN").style.display='none';
                document.getElementById("LIFT").style.display='none';
                document.getElementById("LIGHTS").style.display='none';
                document.getElementById("ANIMATION").style.display='none';
                // document.getElementById("CUBE_LIGHT").style.display='none'
                document.getElementById("PICKUP").style.display='none'
        }

        event.preventDefault();
    });

    //code for changing the option displayed in the secondary dropdown
    $(document).on('click','#option2', function(event){
        console.log('hola')
        console.log($(this).data('action'))
        console.log($(this).data('parent'))
        updateDropdown($(this).data('action'),$(this).data('parent'))

        event.preventDefault();
    });
    
    //function for updating the dropdown
    function updateDropdown(action,parent){
        document.getElementById(parent).innerHTML = action
        console.log("success")
    }

   
});


