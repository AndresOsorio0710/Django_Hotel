((d) =>{
    const $btnMenu = d.querySelector(".menu-btn"),$menu = d.querySelector(".links");

    $btnMenu.addEventListener("click", (e)=>{
        $menu.classList.toggle("is-active");
        console.log("clik")
    });

    d.addEventListener("click", (e)=>{
        if(!e.target.mathches(".links a")) return false;
        $menu.classList.remove("is-active");
    });
})(document)