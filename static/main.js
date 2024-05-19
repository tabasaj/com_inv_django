$(document).ready(function(){

    // Navbar menu button
    $('.navbar-menu-btn').click(function(){
        $('.sidebar').addClass('show-sidebar')
        $('.sidebar').removeClass('hide-sidebar')
    })

    // Sidebar close button
    $('.sidebar-menu-btn').click(function(){
        $('.sidebar').removeClass('show-sidebar')
        $('.sidebar').addClass('hide-sidebar')
    })

    $(".sidebar ul .sidebar-name").click(function(){
        console.log($(this).closest('.drop-down-sidebar'))
    })
}) 