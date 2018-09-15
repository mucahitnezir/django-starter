$(document).ready(function () {

    // Header menu active class
    const urlPath = window.location.pathname;
    const activeLink = $("ul#header-menu a[href='"+ urlPath +"']");
    if (activeLink.hasClass('dropdown-item')) {
        activeLink.addClass('active');
        activeLink.parent().prev().addClass('active');
    } else {
        activeLink.parent().addClass('active');
    }

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
