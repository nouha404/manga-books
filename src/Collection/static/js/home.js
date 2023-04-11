const bounce = document.querySelector('.light .bounce');
const light = document.querySelector('.light')
const header = document.querySelector('header');
const inputText = document.querySelector('.searching input')
const h1Text = document.querySelector('.cover h1')
const bannerCollection = document.querySelector('.collections')
const itemTag = document.querySelector('.item-tag h3')
const body = document.querySelector('body')
const collectionBg = document.querySelector('.items-bg')
const profil = document.querySelector('.profil')


bounce.addEventListener('click', ()=>{
    if(bounce.style.transform != 'translateX(35px)') {
        bounce.style.transform = 'translateX(35px)'
        header.style.background = 'black'

        bounce.style.background = ' linear-gradient(66.43deg, #000000 79.29%, rgba(234, 226, 226, 0) 170.09%)'
        bounce.style.filter = 'drop-shadow(4px 4px 24px rgba(0, 0, 0, 0.25));'
        bounce.style.boxShadow = 'inset 0px -1px 2px rgba(0, 0, 0, 0.25)'
        light.style.background = '#D9D9D9'
        bounce.style.border = '1px solid white'
        inputText.style.background = 'white'
        inputText.style.color = 'black'
        h1Text.style.color = 'black'
        h1Text.style.textShadow = '0px 4px 4px rgba(0, 0, 0, 0.25)'
        bannerCollection.style.backgroundColor = 'black'
        bannerCollection.style.border = '1px solid white'
        itemTag.style.color = 'white'
        body.style.backgroundColor = 'black'
        collectionBg.style.backgroundColor = 'black'
        collectionBg.style.border = '1px solid white'
        profil.style.border = '1px solid #FFFFFF'
    } else {
        bounce.style.transform = ''
        header.style.background = ''
        bounce.style.background = ''
        bounce.style.filter = ''
        light.style.background = '#D9D9D9'
        inputText.style.background = ''
        inputText.style.color = ''
        bounce.style.border = ''
        h1Text.style.color = ''
        bannerCollection.style.backgroundColor = ''
        bannerCollection.style.border = ''
        itemTag.style.color = ''
        body.style.backgroundColor = ''
        collectionBg.style.backgroundColor = ''
        collectionBg.style.border = ''
        profil.style.border = ''
    }

})