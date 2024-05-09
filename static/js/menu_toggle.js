document.querySelector('.menu-toggle').addEventListener('click', function(event) {
    event.stopPropagation(); // Impede que o evento de clique seja propagado para o documento
    document.querySelector('.menu-topo').classList.toggle('show');
});

// Fecha o menu quando clicar em qualquer lugar fora dele
document.addEventListener('click', function(event) {
    const menu = document.querySelector('.menu-topo');
    if (!menu.contains(event.target) && !event.target.classList.contains('menu-toggle')) {
        menu.classList.remove('show');
    }
});