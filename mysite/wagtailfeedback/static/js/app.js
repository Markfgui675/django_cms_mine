
const form = document.querySelector("#form")
const campo = document.querySelector("#slug-hide")

form.addEventListener('click', function(event){
    const input = campo.value
    const slug = input
    const campo_slug = document.getElementById("id_slug")
    campo_slug.value = slug
})

