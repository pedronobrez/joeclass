function oneItem(category) {
    const categoryTitle = document.querySelectorAll('h1.' + category + '-title')
    const categoryList = document.querySelector('.' + category + '-start')
    for (const element of categoryTitle) {
        element.addEventListener('click', function() {
            categoryList.classList.toggle('show')
        })
    }
}

function showContent(category) {
    const categoryTitle = document.querySelectorAll('h1.' + category + '-title')
    const categoryList = document.querySelector('.' + category + '-start')
    for (const element of categoryTitle) {
        element.addEventListener('click', function() {
            categoryList.classList.toggle('show')
        })
    }
    const categoryLrsTitle = document.querySelectorAll('h1.' + category + '-lrs-title')
    const categoryLrsList = document.querySelector('.' + category + '-lrs-start')
    for (const element of categoryLrsTitle) {
        element.addEventListener('click', function() {
            categoryLrsList.classList.toggle('show')
        })
    }
    const categoryQuestionsTitle = document.querySelectorAll('h1.' + category + '-questions-title')
    const categoryQuestionsList = document.querySelector('.' + category + '-questions-start')
    for (const element of categoryQuestionsTitle) {
        element.addEventListener('click', function() {
            categoryQuestionsList.classList.toggle('show')
        })
    }

}

showContent('actions')
showContent('words')
showContent('expressions')