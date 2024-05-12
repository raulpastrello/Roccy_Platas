(function () {
    select_dono = document.getElementById('select-variacoes');
    variation_preco = document.getElementById('variation-preco');
    variation_preco_promocional = document.getElementById('variation-preco-promocional');

    if (!select_dono) {
        return;
    }

    if (!variation_preco) {
        return;
    }

    select_dono.addEventListener('change', function () {
        preco = this.options[this.selectedIndex].getAttribute('data-preco');
        preco_promocional = this.options[this.selectedIndex].getAttribute('data-preco-promocional');


        if (preco && variation_preco) {
            variation_preco.innerHTML = preco;
        }
        
        if (variation_preco_promocional && preco_promocional) {
            variation_preco_promocional.innerHTML = preco_promocional;
        } else {
            variation_preco_promocional.innerHTML = preco;
            variation_preco.innerHTML = ''
        }

    })
})();

