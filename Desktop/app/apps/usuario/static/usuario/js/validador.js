$(document).ready(
    function(){$("#formulario").validate(
    {
        rules:{
            username:{
                required:true    
            },
            name:{
                required:true
            },
            lastname:{
                required:true
            },
            password:{
                required:true
            },
            password2:{
                required:true
            }
        },
        messages:{
            username:{
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
    })
})
