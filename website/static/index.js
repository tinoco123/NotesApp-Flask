if (window.history.replaceState) { // verificamos disponibilidad
    window.history.replaceState(null, null, window.location.href);
}
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}