let pontos=0

$('button').click(function() {
    pontos = pontos + 1
    $('#pontuacao').text(pontos)

    if(pontos > 200) {
        alert('voce ganhou uma champions')
    }
})
