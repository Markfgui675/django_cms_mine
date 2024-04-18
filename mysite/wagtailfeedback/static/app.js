
const form = document.querySelector("#form")
const campo = document.querySelector("#slug-hide")

form.addEventListener('submit', function(event){
    event.preventDefault()
    const input = campo.value
    console.log(input)
})

const novoValor = "Novo valor do input";
const campo2 = document.getElementById("id_slug");
campo.value = novoValor;



