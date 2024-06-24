async function login(username, password) {
  try {
    const data = new URLSearchParams();
    data.append("username", username);
    data.append("password", password);

    await axios.post("http://localhost:8000/api/v1/auth/jwt/login", data, {
      withCredentials: true,
    });
    window.location.href = "admin.html";
  } catch (error) {
    console.error("Error:", error);
  }
}

const submitBtn = document.getElementById("send_button");
const inputUsername = document.getElementById("username");
const inputPassword = document.getElementById("password");
const form = document.getElementById("msg-error");
let elem = document.createElement("div");
elem.id = "notify";
elem.style.display = "none";
form.appendChild(elem);

function validateForm() {
  let isValid = true;

  if (
    !inputUsername.validity.valid ||
    inputUsername.validity.patternMismatch ||
    inputUsername.value.trim() === ""
  ) {
    elem.textContent =
      "Имя пользователя может содержать буквы, цифры, нижнее подчёркивание и быть не менее 3 символов";
    elem.className = "error";
    elem.style.display = "block";
    isValid = false;
  } else {
    if (
      !inputPassword.validity.valid ||
      inputPassword.validity.patternMismatch ||
      inputPassword.value.trim() === ""
    ) {
      elem.textContent = "Пароль должен быть не менее 6 символов";
      elem.className = "error";
      elem.style.display = "block";
      isValid = false;
    } else {
      elem.style.display = "none";
    }
  }

  return isValid;
}

inputPassword.addEventListener("input", function(event) {
  if ("block" === elem.style.display) {
    elem.style.display = "none";
  }
});

inputUsername.addEventListener("input", function(event) {
  if ("block" === elem.style.display) {
    elem.style.display = "none";
  }
});

submitBtn.addEventListener("click", function(event) {
  event.preventDefault();
  if (validateForm()) {
    login(
      (username = inputUsername.value.trim()),
      (password = inputPassword.value.trim()),
    );
  }
});
