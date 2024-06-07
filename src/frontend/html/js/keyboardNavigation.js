document.addEventListener("keydown", function (event) {
  if (event.key === "ArrowDown" || event.key === "ArrowRight") {
    event.preventDefault();
    const currentIndex = idKeyboardArray.indexOf(document.activeElement.id);
    if (currentIndex < idKeyboardArray.length - 1) {
      document.getElementById(idKeyboardArray[currentIndex + 1]).focus();
    }
  } else if (event.key === "ArrowUp" || event.key === "ArrowLeft") {
    event.preventDefault();
    const currentIndex = idKeyboardArray.indexOf(document.activeElement.id);
    if (currentIndex > 0) {
      document.getElementById(idKeyboardArray[currentIndex - 1]).focus();
    }
  }
});
