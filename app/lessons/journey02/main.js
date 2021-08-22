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
        }showContent('WARM-UP')
showContent('STRUCTURE')
showContent('ACTIONS')
showContent('ACTIONS-LSR')
showContent('ACTIONS-QUESTIONS')
showContent('WORDS')
showContent('WORDS-LSR')
showContent('WORDS-QUESTIONS')
showContent('EXPRESSIONS')
showContent('EXPRESSIONS-LSR')
showContent('EXPRESSIONS-QUESTIONS')
