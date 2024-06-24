// Choose city
const btnChooseCity = document.getElementById("choose-city");
const ChooseCity = document.getElementById("select-current-city");

btnChooseCity.addEventListener("click", () => {
  modal.style.display = "block";
  backdrop.style.display = "block";
  document.getElementById("html-code").innerHTML = `
        <label>Выберите город проведения стажировки:</label>
        <br>
        <select id="select-current-city">
        </select>
        <br><br>
        <a href="#" id="submitCity" class="submitLeftBtn">Выбрать</a>`;

  axios
    .get("http://localhost:8000/api/v1/cities")
    .then((response) => {
      const cities = response.data;

      cities.forEach((city) => {
        const option = document.createElement("option");
        option.value = city.id;
        if (city.id == currentCity) option.selected = true;
        option.textContent = city.city_name;
        document.getElementById("select-current-city").appendChild(option);
      });
      document.getElementById("submitCity").addEventListener("click", () => {
        currentCity = document.getElementById("select-current-city").value;
        localStorage.setItem("currentCity", currentCity);
        modal.style.display = "none";
        backdrop.style.display = "none";
        checkSw();
      });
    })
    .catch((error) => {
      console.error("Ошибка при получении данных:", error);
    });
});

// Convert cand to intern
const btnConvCand = document.getElementById("convert-candidates");

btnConvCand.addEventListener("click", () => {
  modal.style.display = "block";
  backdrop.style.display = "block";
  document.getElementById("html-code").innerHTML = `
        <label>Введите условие отбора стажеров:</label>
        <br>
        <input type="text" id="condition-input"/>
        <br><br>
        <a href="#" id="submitCondCand" class="submitLeftBtn">Отобрать стажеров</a>`;

  document.getElementById("submitCondCand").addEventListener("click", () => {
    axios
      .post(
        "http://localhost:8000/api/v1/create_interns",
        {
          city_in: currentCity,
          condition: document.getElementById("condition-input").value.trim(),
        },
        {
          withCredentials: true,
        },
      )
      .catch((error) => {
        console.log(
          document.getElementById("condition-input").value.trim(),
          currentCity,
        );
        console.error(error);
      });
    modal.style.display = "none";
    backdrop.style.display = "none";
    checkSw();
  });
});

// Delete cand or intern
const btnDelman = document.getElementById("the-end");

btnDelman.addEventListener("click", () => {
  modal.style.display = "block";
  backdrop.style.display = "block";
  document.getElementById("html-code").innerHTML = `
        <label>Выберите, чьи записи удалить:</label>
        <br>
        <select id="select-delete">
        <option value="candidates">Кандидаты</option>
        <option value="interns">Стажеры</option>
        <option value="all">Удалить всех</option>
        </select>
        <br><br>
        <a href="#" id="submitDel" class="submitLeftBtn">Отобрать стажеров</a>`;

  const selectDel = document.getElementById("select-delete");
  document.getElementById("submitDel").addEventListener("click", () => {
    if (selectDel.value === "candidates" || selectDel.value == "all") {
      axios
        .delete(
          `http://localhost:8000/api/v1/delete_candidates_by_city/${currentCity}`,
          {
            withCredentials: true,
          },
        )
        .catch((error) => {
          console.error(error);
        });
    }
    if (selectDel.value === "interns" || selectDel.value == "all") {
      axios
        .delete(
          `http://localhost:8000/api/v1/delete_interns_by_city/${currentCity}`,
          {
            withCredentials: true,
          },
        )
        .catch((error) => {
          console.error(error);
        });
    }
    modal.style.display = "none";
    backdrop.style.display = "none";
    checkSw();
  });
});
