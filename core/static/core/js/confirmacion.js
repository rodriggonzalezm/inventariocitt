function confirmarEliminacion(id) {
    Swal.fire({
        title: 'Estas seguro?',
        text: "Este cambio no se puede revertir!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/eliminarcortinas/"+id+"/";
        }
      })
}