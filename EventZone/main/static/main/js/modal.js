console.log('Hello world!');

let popupBg = document.querySelector('.popup__content'); 
let popup = document.querySelector('.popup'); 
let openPopupButtons = document.querySelectorAll('.open-popup'); 
let closePopupButton = document.querySelector('.close__popup'); 
let body = document.querySelector('body');



openPopupButtons.forEach((button) => {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        popupBg.classList.add('active');
        popup.classList.add('active');
        
    })
});

closePopupButton.addEventListener('click', () => {

    let updateInfo = document.querySelectorAll('.update__info');
    updateInfo.forEach(function(item)
    {
        item.classList.remove('active');

            let btnInfoClose = document.querySelectorAll('.btn__info');
            btnInfoClose.forEach(function(item)
            {
                item.classList.remove('active');
            })
    })
    popupBg.classList.remove('active');
    popup.classList.remove('active');
});

document.addEventListener('click', (e) => {
    if (e.target === popupBg) {
        popupBg.classList.remove('active');
        popup.classList.remove('active'); 
    }
});