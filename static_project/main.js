$(document).ready(function(){
  console.log('Working from the base');

  // Message Box close
  $('.message .close')
    .on('click', function() {
      $(this)
        .closest('.message')
        .transition('fade');
    });

  $('#modal-btn').click(function(){
    $('.ui.modal')
      .modal('show');
  })
});
