const submitBtn = document.getElementById("actions-submit");
const firstnameInput = document.getElementById("first-name");
const lastnameInput = document.getElementById("last-name");
const emailInput = document.getElementById("email");
const studingInput = document.getElementById("studing");
const educationInput = document.getElementById("education");
const targetInput = document.getElementById("target_internship");

const createCandidate = async (candidateData) => {
  try {
    const response = await axios.post("/create_candidate", candidateData);
    return response.data;
  } catch (error) {
    console.error("Error creating candidate:", error);
    throw error;
  }
};

submitBtn.addEventListener("click", function(event) {
  event.preventDefault();
  let idInputArray = [
    firstnameInput,
    lastnameInput,
    emailInput,
    studingInput,
    educationInput,
    targetInput,
  ];
  let idOptionalInputArray = [];

  let isValid = true;

  for (input in idInputArray) {
    if (input.value.trim() === "" && input in idOptionalInputArray) {
      nameError.textContent = "Заполните это обязательное поле";
      isValid = false;
    } else {
      if (!nameInput.checkValidity()) {
        nameError.textContent = "Неправильный формат имени";
        isValid = false;
      } else {
        nameError.textContent = "";
      }
    }
  }

  if (isValid) {
    candidateData = {
      first_name: "John",
      last_name: "Doe",
      email: "john.doe@example.com",
      studing_place: "University of Example",
      education: "Bachelor of Science",
      target_internship: "Software Engineering",
      city: "New York",
      prefer_branch: "IT",
      resume_filename: "john_doe_resume.pdf",
    };

    createCandidate(candidateData)
      .then((createdCandidate) => {
        console.log("Created candidate:", createdCandidate);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  } else {
    // Выводим сообщение об ошибке или делаем что-то еще
    console.log("Ошибка в заполнении формы");
  }
});
