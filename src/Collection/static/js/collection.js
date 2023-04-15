const bounce = document.querySelector('.light .bounce');
const addCollection = document.querySelector('.add-collect')
const addCollectionInput = document.querySelector('.add-collect form input')
const noteInput = document.querySelector('.left textarea')
const button = document.querySelector('.button')
const select = document.querySelector('#etat-lecture')
const body = document.querySelector('body')
const title = document.querySelector('.item-tag h3')
const inputText = document.querySelector('.searching input')
inputText.disabled = true
inputText.style.border = '1px dotted #912727'
inputText.style.color = '#912727'
inputText.placeholder = "Champs desactiver..."

const shortcut = (parentOfInputInForm,labelfounder)=> {
    parentOfInputInForm = document.querySelector('form')
    let allInputInLeftClass = parentOfInputInForm.querySelectorAll(`${labelfounder}`)

    for(let i=1;i<allInputInLeftClass.length;i++) {
        if(bounce.style.transform === 'translateX(35px)') {
            allInputInLeftClass[i].style.backgroundColor = '#3F3E3E';
            allInputInLeftClass[i].style.color = 'white';
            allInputInLeftClass[i].style.fontSize = '1.3rem'
        }

    }
}

const removeShortcut = (parentOfInputInForm,labelalreadyfound) => {
    parentOfInputInForm = document.querySelector('form')
    let allInputInLeftClass = parentOfInputInForm.querySelectorAll(`${labelalreadyfound}`)

        for(let i=1;i<allInputInLeftClass.length;i++) {
             if(bounce.style.transform !== 'translateX(35px)') {
                allInputInLeftClass[i].style.backgroundColor = '';
                allInputInLeftClass[i].style.color = '';
                allInputInLeftClass[i].style.fontSize = ''
             }
         }
}

const specialySelectShortcut = (fixSelectTag,finalyGetSelectTag) => {
    fixSelectTag = document.querySelector(`${fixSelectTag}`)
    finalyGetSelectTag = fixSelectTag.querySelector(`${finalyGetSelectTag}`)

    for(let i=1;i<finalyGetSelectTag.length;i++) {

        if(bounce.style.transform === 'translateX(35px)') {
            finalyGetSelectTag[i].style.backgroundColor = '#3F3E3E';
            finalyGetSelectTag[i].style.color = 'white';
            finalyGetSelectTag[i].style.fontSize = '1.3rem'
        }
    }
}

const specialyNoteShortcut = (fixNoteTag,finalyGetNoteTextarea) => {
    fixNoteTag = document.querySelector(`${fixNoteTag}`)
    finalyGetNoteTextarea = fixNoteTag.querySelector(`${finalyGetNoteTextarea}`)

        if (bounce.style.transform === 'translateX(35px)') {

            finalyGetNoteTextarea.style.backgroundColor = '#3F3E3E';
            finalyGetNoteTextarea.style.color = 'white';
            finalyGetNoteTextarea.style.fontSize = '1.3rem'
        }

}

const specialySelectRemoveShortcut = (fixNoteTag,finalyGetNoteTextarea) => {
    fixNoteTag = document.querySelector(`${fixNoteTag}`)
    finalyGetNoteTextarea = fixNoteTag.querySelector(`${finalyGetNoteTextarea}`)

        if (bounce.style.transform !== 'translateX(35px)') {

            finalyGetNoteTextarea.style.backgroundColor = '';
            finalyGetNoteTextarea.style.color = '';
            finalyGetNoteTextarea.style.fontSize = ''
        }

}

bounce.addEventListener('click', ()=>{

    if(bounce.style.transform !== 'translateX(35px)') {
        bounce.style.transform = 'translateX(35px)'
        bounce.style.background = ' linear-gradient(66.43deg, #000000 79.29%, rgba(234, 226, 226, 0) 170.09%)'
        bounce.style.filter = 'drop-shadow(4px 4px 24px rgba(0, 0, 0, 0.25));'
        bounce.style.boxShadow = 'inset 0px -1px 2px rgba(0, 0, 0, 0.25)'
        bounce.style.border = '1px solid white'

        addCollection.style.backgroundColor = 'black'
        addCollection.style.border = '1px solid white'
        addCollection.style.borderRadius = '20px'
        addCollectionInput.style.backgroundColor = '#3F3E3E';
        addCollectionInput.style.color = '#FFFFFF';
        addCollectionInput.style.boxShadow = '0px 4px 4px rgba(0, 0, 0, 0.25)'

        body.style.backgroundColor = 'black'
        title.style.color = 'white'
        button.style.backgroundColor = '#3F3E3E'
        button.style.color = 'white'

        // un boucle pour cibler les input dans la class parentOfLeftInput
        shortcut('form', 'input')
        shortcut('form', 'textarea')
        shortcut('form', 'select')

        specialySelectShortcut('.left', 'select')
        specialyNoteShortcut('form','#id_note')
        specialyNoteShortcut('form', '#id_status')

    } else {
        bounce.style.transform = ''
        bounce.style.background = ''
        bounce.style.filter = ''
        bounce.style.border = ''

        addCollection.style.background = ''
        addCollectionInput.style.backgroundColor = ''
        addCollectionInput.style.color = ''

        button.style.backgroundColor = ''
        button.style.color = ''

        noteInput.style.color = '';
        noteInput.style.backgroundColor = '';
        noteInput.style.color = '';
        noteInput.style.fontSize = ''
        body.style.backgroundColor = ''
        body.style.backgroundColor = ''

        // tu me dira c'est des pattes de recreer une boucle alors que tu peux refactor mais j'ai la flemme bro
        removeShortcut('form', 'input')
        removeShortcut('form', 'textarea')
        removeShortcut('form', 'select')
        specialySelectRemoveShortcut('form', '#id_status')
    }

})