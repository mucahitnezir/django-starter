$(document).ready(function () {

    // Portfolio isotope
    if ($.fn.isotope) {
        const $grid = $('#portfolio-list').isotope({
            itemSelector: '.portfolio-list-item'
        });

        $('#portfolio-filter-buttons').on('click', 'button', function () {
            const filterValue = $(this).data('filter');
            $grid.isotope({filter: filterValue});
        });
        $grid.isotope({filter: '*'});
    }

});
