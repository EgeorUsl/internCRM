(function() {
  let input = document.getElementById("username");
  let input2 = document.getElementById("password");
  let form = document.getElementById("msg-error");
  let elem = document.createElement("div");
  elem.id = "notify";
  elem.style.display = "none";
  form.appendChild(elem);

  input.addEventListener("invalid", function(event) {
    event.preventDefault();
    if (!event.target.validity.valid) {
      elem.textContent =
        "Имя пользователя должно содержать буквы, цифры, нижнее подчёркивание и быть не менее 3 символов";
      elem.className = "error";
      elem.style.display = "block";
    }
  });

  input2.addEventListener("invalid", function(event) {
    event.preventDefault();
    if (!event.target.validity.valid && input.validity.valid) {
      elem.textContent =
        "Пароль должен содержать буквы, цифры, специальные символы и быть не менее 8 символов";
      elem.className = "error";
      elem.style.display = "block";
    }
  });

  input.addEventListener("input", function(event) {
    if ("block" === elem.style.display) {
      elem.style.display = "none";
    }
  });

  input2.addEventListener("input", function(event) {
    if ("block" === elem.style.display) {
      elem.style.display = "none";
    }
  });
})();
