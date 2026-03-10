// var nome = prompt("Como você chama?")
//
// if (nome == null) {
//     alert("Recaregue a pagína")
// } else {
//
//     let correto = confirm("Você se chama" + nome + "?")
//
//     if (correto) {
//         alert(nome + " Bem-vindo ao site recursos")
//
//     } else {
//         alert("Recarregue a pagína")
//     }
//
//



function LimpaInputLogin(){

    const inputEmail = document.getElementById('form-email')
    const inputSenha = document.getElementById('form-senha')

    inputEmail.value = ''
    inputSenha.value = ''
}

document.addEventListener("DOMContentLoaded", function (){

  const formLogin = document.getElementById("form-login")

  formLogin.addEventListener("submit", function (event){

      const inputEmail = document.getElementById("form-email")
      const inputSenha = document.getElementById("form-senha")

      let temErro = false

      // Verificar se os inputs estão vazios
      if (inputEmail.value === ''){
          inputEmail.classList.add('is-invalid')
          temErro = true
      } else{
          inputEmail.classList.remove('is-invalid')
      }

      if (inputSenha.value === ''){
          inputSenha.classList.add('is-invalid')
          temErro = true
      } else{
          inputSenha.classList.remove('is-invalid')
      }

      if (temErro) {
          event.preventDefault()
          alert("Preencher todos os campos")
      }

  })

})