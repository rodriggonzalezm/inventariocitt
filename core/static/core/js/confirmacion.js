function eliminarcortina(id) {
  Swal.fire({
    title: 'Estas seguro?',
    text: "No podras deshacer esta accion",
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Si, Eliminar!',
    cancelButtonText: 'Cancelar'
  }).then((result) => {
    if (result.value) {
      window.location.href = "/eliminarcortina/"+id+"/"
      
    }
  })
}