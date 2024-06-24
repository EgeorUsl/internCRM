const submitBtn = document.getElementById("actions-submit");
const firstnameInput = document.getElementById("first-name");
const lastnameInput = document.getElementById("last-name");
const emailInput = document.getElementById("email");
const cityInput = document.getElementById("city");
const branchInput = document.getElementById("branch");
const studingInput = document.getElementById("studing");
const educationInput = document.getElementById("education");
const targetInput = document.getElementById("target_internship");

function removeError(input) {
  const parent = input.parentNode;
  if (input.classList.contains("error")) {
    parent.querySelector(".error-label").remove();
    input.classList.remove("error");
  }
}

function createError(input, text) {
  removeError(input);
  const parent = input.parentNode;

  const errorLabel = document.createElement("label");

  errorLabel.classList.add("error-label");
  errorLabel.textContent = text;

  input.classList.add("error");

  parent.append(errorLabel);
}

firstnameInput.addEventListener("input", function(event) {
  removeError(firstnameInput);
});
lastnameInput.addEventListener("input", function(event) {
  removeError(lastnameInput);
});
emailInput.addEventListener("input", function(event) {
  removeError(emailInput);
});
studingInput.addEventListener("input", function(event) {
  removeError(studingInput);
});
educationInput.addEventListener("input", function(event) {
  removeError(educationInput);
});
targetInput.addEventListener("input", function(event) {
  removeError(targetInput);
});
branchInput.addEventListener("input", function(event) {
  removeError(branchInput);
});
cityInput.addEventListener("input", function(event) {
  removeError(cityInput);
});

const createCandidate = async (candidateData) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/api/v1/create_candidate",
      candidateData,
    );
    return response.data;
  } catch (error) {
    console.error("Error sending request:", error);
    throw error;
  }
};

submitBtn.addEventListener("click", function(event) {
  event.preventDefault();

  let isValid = true;

  if (branchInput.value.trim() === "") {
    createError(branchInput, "Выберете элемент из списка");
    isValid = false;
  }

  if (cityInput.value.trim() === "") {
    createError(cityInput, "Выберете элемент из списка");
    isValid = false;
  }

  if (firstnameInput.value.trim() === "") {
    createError(firstnameInput, "Заполните это обязательное поле");
    isValid = false;
  } else {
    if (!firstnameInput.checkValidity()) {
      createError(firstnameInput, "Неправильный формат имени");
      isValid = false;
    } else {
      removeError(firstnameInput);
    }
  }

  if (lastnameInput.value.trim() === "") {
    createError(lastnameInput, "Заполните это обязательное поле");
    isValid = false;
  } else {
    if (!lastnameInput.checkValidity()) {
      createError(lastnameInput, "Неправильный формат фамилии");
      isValid = false;
    } else {
      removeError(lastnameInput);
    }
  }

  if (emailInput.value.trim() === "") {
    createError(emailInput, "Заполните это обязательное поле");
    isValid = false;
  } else {
    if (!emailInput.checkValidity()) {
      createError(emailInput, "Неправильный формат электронной почты");
      isValid = false;
    } else {
      removeError(emailInput);
    }
  }

  if (educationInput.value.trim() === "") {
    createError(educationInput, "Заполните это обязательное поле");
    isValid = false;
  } else {
    if (!educationInput.checkValidity()) {
      createError(educationInput, "Неправильный формат образования");
      isValid = false;
    } else {
      removeError(educationInput);
    }
  }
  if (isValid) {
    candidateData = {
      first_name: firstnameInput.value,
      last_name: lastnameInput.value,
      email: emailInput.value,
      studing_place: studingInput.value,
      education: educationInput.value,
      target_internship: targetInput.value,
      city_id: cityInput.value,
      prefer_branch_id: branchInput.value,
    };

    createCandidate(candidateData)
      .then((createdCandidate) => {
        console.log("Created candidate:", createdCandidate);
      })
      .catch((error) => {
        // createError(submitBtn, "Ошибка ввода формы");
        console.error("Error:", error);
      });
  } else {
    console.log("Неправильно набрана форма");
  }
});
