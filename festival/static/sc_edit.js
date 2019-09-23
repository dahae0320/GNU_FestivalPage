var bDisplay = true;
function doDisplay(){
    var con = document.getElementById("nightpg");
    var con1 = document.getElementById("daypg");
    if(con.style.display=='block'&& con1.style.display=='none'){
        con.style.display = 'none';
        con1.style.display= 'block';
    }else{
        con1.style.display= 'block';
        con.style.display = 'none';
    }
}
function doDisplay1(){
    var con = document.getElementById("daypg");
    var con1 = document.getElementById("nightpg");
    if(con.style.display=='block'){
        con.style.display = 'none';
        con1.style.display ='block';
    }else{
        con1.style.display = 'block';
        con.style.display = 'none';
    }
}
