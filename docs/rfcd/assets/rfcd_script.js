document.addEventListener("DOMContentLoaded", function() {
    var bookParts = document.querySelectorAll('.book-part');
    
    bookParts.forEach(function(bookPart, index) {
        // Add a line break after "Fundamentos:" or "Ciência de Dados:"
        var regex = /(\w+):\s*(\w+)/g;
        bookPart.innerHTML = bookPart.innerHTML.replace(regex, "$1:<br>$2");

        var collapseId = 'collapse-part-' + index;
        
        // Create a new div for the collapsible content
        var collapseDiv = document.createElement('div');
        collapseDiv.className = 'collapse show';
        collapseDiv.id = collapseId;

        // Move the chapters into the collapse div
        var chapters = bookPart.nextElementSibling;
        while (chapters && !chapters.classList.contains('book-part')) {
            var nextChapter = chapters.nextElementSibling;
            collapseDiv.appendChild(chapters);
            chapters = nextChapter;
        }

        // Insert the collapse div after the book-part element
        bookPart.parentNode.insertBefore(collapseDiv, bookPart.nextElementSibling);

        // Modify book-part to be clickable
        bookPart.setAttribute('data-toggle', 'collapse');
        bookPart.setAttribute('data-target', '#' + collapseId);
        bookPart.style.cursor = 'pointer';

        // Add a caret or other indicator to show it’s collapsible (currently done with css ::after)
        //var caret = document.createElement('span');
        //caret.innerHTML = ' &#9660;'; // Down arrow
        //bookPart.appendChild(caret);
    });
});
