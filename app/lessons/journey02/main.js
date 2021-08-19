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
            const categoryLrsTitle = document.querySelectorAll('h1.' + category + '-LRS-title')
            const categoryLrsList = document.querySelector('.' + category + '-LRS-start')
            for (const element of categoryLrsTitle) {
                element.addEventListener('click', function() {
                    categoryLrsList.classList.toggle('show')
                })
            }
            const categoryQuestionsTitle = document.querySelectorAll('h1.' + category + '-QUESTIONS-title')
            const categoryQuestionsList = document.querySelector('.' + category + '-QUESTIONS-start')
            for (const element of categoryQuestionsTitle) {
                element.addEventListener('click', function() {
                    categoryQuestionsList.classList.toggle('show')
                })
            }

        }showContent('WARM-UP')
showContent('STRUCTURE')
showContent('ACTIONS')
showContent('ACTIONS-LSR')
showContent('ACTIONS-QUESTIONS')
showContent('WORDS-')
showContent('WORDS-LSR')
showContent('WORDS-QUESTIONS')
showContent('EXPRESSIONS')
showContent('EXPRESSIONS-LSR')
showContent('EXPRESSIONS-QUESTIONS')
