 
 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
 $(document).ready(function() {
  $("#sortable1").sortable({
    connectWith: ".connectedSortable",

    update: function(event, ui) {
      var serial = $('#sortable1').sortable('serialize');
      $.ajax({
        url: "/eytpanelv1/slider/",
        type: "post",
        data: { 'content': serial, 'csrfmiddlewaretoken' : csrftoken } 
      });
    },

  }).disableSelection();
});

function file_delete(id){
  Swal.fire({
  title: 'Are you sure?',
  text: "You won't be able to revert this!",
  icon: 'warning',
  showCancelButton: true,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: 'Yes, delete it!'
}).then((result) => {
  if (result.isConfirmed) {
    Swal.fire(
    'Deleted!',
    'Your file has been deleted.',
    'success'
  ).then(function(){
    window.location.href="/eytpanelv1/slider/file_delete/"+id+"/"
  })
  }
})
}


document.addEventListener("DOMContentLoaded", function(file) {
Dropzone.options.mydz = {
    dictDefaultMessage: "Resimleri Buraya Sürükleyip Bırakabilirsiniz.",
    maxFilesize: 5,
    accept: function(file,done){

      if (file.type != "image/jpeg" && file.type != "image/png"   && file.type != "image/jpg") {
        Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Something went wrong!',
              footer: '<a href>Why do I have this issue?</a>'
            }).then(function() {
              window.location = "/eytpanelv1/slider";
          }); 
       }
       else { 
        done();
        setTimeout(function(){ 
          window.location.href = "/eytpanelv1/slider/";
        },1000);
       }
      
    }
}});

  
  
