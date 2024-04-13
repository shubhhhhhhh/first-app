(function(){
    
    const a  = document.getElementById("a")
    document.getElementById("btn").addEventListener("click",()=>{
        console.log("here we come home after success page")
        a.innerHTML = "innerhtml changed"
    })
})()