// using jQuery
function notifyNow(message, type){
    $.notify(
        message, 
        type, 
        { elementPosition: 'top middle', globalPosition: 'top middle' }
    );
}


    
$(document).ready(function () {
    $("#messages").fadeIn(1000).delay(3000).fadeOut(1000);
    // search placeholder
    function addToPlaceholder(toAdd, el) {
        el.attr('placeholder', el.attr('placeholder') + toAdd);
        // Delay between symbols "typing"
        return new Promise(resolve => setTimeout(resolve, 70))
    }

    // Clear placeholder attribute in given element
    function clearPlaceholder(el) {
        el.attr("placeholder", "");
    }

    // Print one phrase
    function printPhrase(phrase, el) {
        return new Promise(resolve => {
            // Clear placeholder before typing next phrase
            clearPlaceholder(el);
            let letters = phrase.split('');
            // For each letter in phrase
            letters.reduce(
                (promise, letter, index) => promise.then(_ => {
                    // Resolve promise when all letters are typed
                    if (index === letters.length - 1) {
                        // Delay before start next phrase "typing"
                        setTimeout(resolve, 400);
                    }
                    return addToPlaceholder(letter, el);
                }),
                Promise.resolve()
            );
        });
    }

    // Print given phrases to element
    function printPhrases(phrases, el) {
        // For each phrase
        // wait for phrase to be typed
        // before start typing next
        phrases.reduce(
            (promise, phrase) => promise.then(_ => printPhrase(phrase, el)),
            Promise.resolve()
        );
    }

    // Start typing
    function runSearchHelp() {
        let phrases = [
            "e.g. Rajshahi",
            "e.g. Pizza",
            "e.g Master Chef"
        ];
        printPhrases(phrases, $('#search_input'));
    }
    runSearchHelp();



    /*[ Back to top ]
    ===========================================================*/
    var windowH = $(window).height()/2;

    $(window).on('scroll',function(){
        if ($(this).scrollTop() > windowH) {
            $("#myBtn").css('display','flex');
        } else {
            $("#myBtn").css('display','none');
        }
    });

    $('#myBtn').on("click", function(){
        $('html, body').animate({scrollTop: 0}, 600);
    });




    /*	MOBILE */
    $("#btn_expand").click(function () {
        $("#cartMenuContainer").removeClass("d-none");
        $("#cartMenuContainer").addClass("fixed-top mt-5");
    });
    $("#close_btn").click(function () {
        $("#cartMenuContainer").addClass("d-none");
        $("#cartMenuContainer").removeClass("fixed-top mt-5");
    });

});