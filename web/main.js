var num;
function getMatriceNo(){
    num = document.getElementById("matrice_no").value
    var container = document.getElementById("myContainerDiv");
    // var html;
    var i=0;
    for(i = 0; i < num; i++)
    {
        container.innerHTML += "<br/><input type=text id=box"+ (i+1) +"  placeholder="+"'Enter number of rows in matrix'"+ (i+1) +" style="+"'width: 300px;'"+"/> <br/>";
    }
    container.innerHTML +="<br/><input type ='text' id=box" + (i+1) + " placeholder=" + "'Enter number of columns in matrix'" + ""+ (i) +" style="+"'width: 300px;'"+"/> <br/>";
    
}
function callPython(){
    // console.log(num);
    var list = [];
    var i=0;
    for(i = 0; i <= num; i++)
    {
        // console.log(document.getElementById("box"+(i+1)).value);
        list[i] = document.getElementById("box"+(i+1)).value;     
    }
    // console.log(list);
    eel.start_algorithm(num,list)(display)
}

function display(result){
    console.log(result);

}
