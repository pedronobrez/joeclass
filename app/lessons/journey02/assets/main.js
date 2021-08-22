
            var galleryTop = new Swiper('.gallery-top', {
                keyboard: {
                    enabled: true,
                    onlyInViewport: false,
                },
                nextButton: '.swiper-button-next',
                prevButton: '.swiper-button-prev',
                spaceBetween: 10,
            });
            galleryTop.params.control = galleryThumbs;
            galleryThumbs.params.control = galleryTop;
            