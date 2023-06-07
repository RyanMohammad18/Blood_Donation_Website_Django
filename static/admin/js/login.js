var card= document.getElementById("card");

function openRegister(){
    card.style.transform = "rotateY(-180deg)";
}
function openLogin(){
    card.style.transform = "rotateY(0deg)";
}
function validate()
{
    let uemail = document.getElementById("uemail");
    let upassword = document.getElementById("upassword").nodeValue;

    

    if( upassword<5)
    {
        alert("Password Too Short");
        return false;
    }
    else{
        return true;
    }

}



