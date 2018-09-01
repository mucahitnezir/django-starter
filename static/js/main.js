$(document).ready(function () {

    // Portfolio isotope
    if ($.fn.isotope) {
        var $grid = $('#portfolio-list').isotope({
            itemSelector: '.portfolio-list-item'
        });

        $('#portfolio-filter-buttons').on('click', 'button', function () {
            var filterValue = $(this).data('filter');
            $grid.isotope({filter: filterValue});
        });
    }

});
