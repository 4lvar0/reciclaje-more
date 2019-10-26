$(document).ready(
    function(){
    $("#formulario").validate(
    {

        rules:{
            usuario:{
                required:true    
            },
            nombre:{
                required:true
            },
            apellido:{
                required:true
            },
            mail:{
                required:true
            },
            contraseña:{
                required:true
            }
        },
        messages:{
            usuario:{
                required:"Debe ingresar su usuario"    
            },
            nombre:{
                required:"Debe ingresar su nombre",
            },
            apellido:{
                required:"Debe ingresar su apellido",
            },
            mail:{
                required:"Debe ingresar su correo."
            },
            contraseña:{
                required:"Debe ingresar su contraseña."
            }
        }
    }
    )
})
