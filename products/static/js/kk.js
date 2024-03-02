(function(){
    const a  = document.getElementById("a")
    document.getElementById("btn").addEventListener("click",()=>{
        a.innerHTML = "innerhtml changed"
    })
})()