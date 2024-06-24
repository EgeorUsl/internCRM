const selectElementCity = document.getElementById("city");
const selectElementBranch = document.getElementById("branch");

axios
  .get("http://localhost:8000/api/v1/cities")
  .then((response) => {
    const cities = response.data;

    cities.forEach((city) => {
      const option = document.createElement("option");
      option.value = city.id;
      option.textContent = city.city_name;
      selectElementCity.appendChild(option);
    });
  })
  .catch((error) => {
    console.error("Ошибка при получении данных:", error);
  });

axios
  .get("http://localhost:8000/api/v1/branches")
  .then((response) => {
    const branches = response.data;

    branches.forEach((branch) => {
      const option = document.createElement("option");
      option.value = branch.id;
      option.textContent = branch.branch_name;
      selectElementBranch.appendChild(option);
    });
  })
  .catch((error) => {
    console.error("Ошибка при получении данных:", error);
  });
