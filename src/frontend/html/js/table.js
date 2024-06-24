const btnCand = document.getElementById("btnCand");
const btnIntern = document.getElementById("btnIntern");
const btnRefresh = document.getElementById("btnRefresh");
const BtnImage = document.querySelector(".btnimg");

// Table view
async function fetchCandidates() {
  try {
    const response = await axios.get(
      `http://localhost:8000/api/v1/candidates-by-city/${currentCity}`,
      { withCredentials: true },
    );

    const branches = await axios.get(`http://localhost:8000/api/v1/branches`, {
      withCredentials: true,
    });
    const branchDict = {};
    branches.data.forEach((branch) => {
      branchDict[branch.id] = branch.branch_name;
    });

    const statuses = await axios.get(`http://localhost:8000/api/v1/status`, {
      withCredentials: true,
    });
    const statusDict = {};
    statuses.data.forEach((status) => {
      statusDict[status.id] = status.status_name;
    });

    let candidates = response.data;
    const viewTable = document.getElementById("view-db-list");
    viewTable.innerHTML = ``;
    viewTable.innerHTML = `<div class="table person">
        <div class="table-header">
      <div class="header__item header-table-id">
        <a class="filter__link table-id" href="#">id</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-firstname filter__link--number" href="#">Имя</a>
      </div>
      <div class="header__item">
        <a class="table-lastname filter__link filter__link--number" href="#">Фамилия</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-email filter__link--number" href="#">E-mail</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-studing-place filter__link--number" href="#">Место учёбы</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-education filter__link--number" href="#">Образование</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-status filter__link--number" href="#">Статус</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-prefer-branch filter__link--number" href="#">Программа стажировки</a>
      </div>
      <div class="header__item">
        <a class="filter__link table-scores filter__link--number" href="#">Баллы</a>
      </div>
    </div >
        <div class="table-content">
        </div>
  </div > `;
    const tableContentNode = document.querySelector(".table-content");

    candidates.forEach((candidate) => {
      const tableRow = document.createElement("div");
      let chessTable = false;
      chessTable = !chessTable;

      if (chessTable) tableRow.classList.add("row-white");
      tableRow.classList.add("table-row");

      tableRow.innerHTML = `
          <div class="table-data table-data-id">${candidate.id}</div>
          <div class="table-data">${candidate.first_name}</div>
          <div class="table-data">${candidate.last_name}</div>
          <div class="table-data">${candidate.email}</div>
          <div class="table-data">${candidate.studing_place}</div>
          <div class="table-data">${candidate.education}</div>
          <div class="table-data">${statusDict[candidate.status_id]}</div>
          <div class="table-data">${branchDict[candidate.prefer_branch_id]}</div>
          <div class="table-data">${candidate.scores}</div>
        `;
      tableContentNode.appendChild(tableRow);
    });
  } catch (error) {
    console.error("Error fetching candidates:", error);
  }
}

async function fetchInterns() {
  try {
    const statuses = await axios.get(`http://localhost:8000/api/v1/status`, {
      withCredentials: true,
    });
    const statusDict = {};
    statuses.data.forEach((status) => {
      statusDict[status.id] = status.status_name;
    });

    const branches = await axios.get(`http://localhost:8000/api/v1/branches`, {
      withCredentials: true,
    });
    const branchDict = {};
    branches.data.forEach((branch) => {
      branchDict[branch.id] = branch.branch_name;
    });

    const groups = await axios.get(
      `http://localhost:8000/api/v1/branches/groups`,
      { withCredentials: true },
    );
    const groupsDict = {};
    groups.data.forEach((group) => {
      groupsDict[group.id] = group.branch_name;
    });

    const groupDict = {};
    groups.data.forEach((group) => {
      groupDict[group.id] = group.group_name;
    });

    const branchgroup = await axios.get(
      `http://localhost:8000/api/v1/branches_with_groups`,
      { withCredentials: true },
    );
    const branchgroupsDict = {};
    branchgroup.data.forEach((group) => {
      branchgroupsDict[group.branch_name] = group.groups;
    });

    const viewTable = document.getElementById("view-db-list");
    let nullableGroup = false;
    const interns = await axios.get(
      `http://localhost:8000/api/v1/interns-by-city/${currentCity}`,
      {
        withCredentials: true,
      },
    );
    viewTable.innerHTML = ``;
    interns.data.forEach((intern) => {
      if (intern.group_id === null) nullableGroup = true;
    });

    let chessTable = false;
    let htmlInternTable = `<div class="table person">
          <div class="table-header">
            <div class="header__item header-table-id">
              <a class="filter__link" href="#">id</a>
            </div>
            <div class="header__item">
              <a class="filter__link table-firstname filter__link--number" href="#">Имя</a>
            </div>
            <div class="header__item">
              <a class="table-lastname filter__link filter__link--number" href="#">Фамилия</a>
            </div>
            <div class="header__item">
              <a class="filter__link table-email filter__link--number" href="#">E-mail</a>
            </div>
            <div class="header__item">
              <a class="filter__link table-studing-place filter__link--number" href="#">Место учёбы</a>
            </div>
            <div class="header__item">
              <a class="filter__link table-education filter__link--number" href="#">Образование</a>
            </div>
            <div class="header__item">
              <a class="filter__link table-status filter__link--number" href="#">Статус</a>
            </div>
          </div>`;

    if (nullableGroup) {
      viewTable.innerHTML = `<h3>Стажеры без назначенной группы</h3>${htmlInternTable}
          <div class="table-content" id="table-null-group">
          </div></div><br><hr>
      <div id="later-null"></div>`;
    } else {
      viewTable.innerHTML = `<div id="later-null">`;
    }
    const InternLists = document.getElementById("later-null");
    const inputIntern = document.getElementById(`table-null-group`);

    // if (interns.data == ) {
    //   const internRow = document.createElement("div");
    //   internRow.classList.add("table-row");
    //   internRow.innerHTML = `
    //           <div class="table-data table-data-id" style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>
    //           <div class="table-data style="color=#666">-</div>`;
    //
    //   inputIntern.appendChild(internRow);
    // }

    interns.data.forEach((intern) => {
      const internRow = document.createElement("div");
      if (intern.group_id === null) {
        internRow.classList.add("table-row");
        chessTable = !chessTable;

        if (chessTable) internRow.classList.add("row-white");

        internRow.innerHTML = `
              <div class="table-data table-data-id">${intern.id}</div>
              <div class="table-data">${intern.first_name}</div>
              <div class="table-data">${intern.last_name}</div>
              <div class="table-data">${intern.email}</div>
              <div class="table-data">${intern.studing_place}</div>
              <div class="table-data">${intern.education}</div>
              <div class="table-data">${statusDict[intern.status_id]}</div>`;

        inputIntern.appendChild(internRow);
      }
    });

    branchgroup.data.forEach((branch) => {
      const programList = document.createElement("div");
      programList.classList.add("program");
      programList.innerHTML = `
  <h4 class="program-title">${branch.branch_name}</h4>`;
      const programContent = document.createElement("div");
      programContent.classList.add("program-content");
      programContent.setAttribute("id", branch.branch_name);

      branch.groups.forEach((group) => {
        const groupList = document.createElement("div");
        groupList.classList.add("group");
        groupList.innerHTML = `
            <h4 class="group-title">${group}</h4>
            <div class="group-content">
      ${htmlInternTable}<div id="${branch.branch_name}_${group}" class="table-content"></div>`;
        programContent.appendChild(groupList);
      });
      programList.appendChild(programContent);
      InternLists.appendChild(programList);
    });
    interns.data.forEach((intern) => {
      const inputIntern = document.getElementById(
        `${branchDict[intern.branch_id]}_${groupDict[intern.group_id]}`,
      );
      const internRow = document.createElement("div");
      if (intern.group_id != null) {
        internRow.classList.add("table-row");
        chessTable = !chessTable;
        if (chessTable) internRow.classList.add("row-white");

        internRow.innerHTML = `
              <div class="table-data table-data-id">${intern.id ? intern.id : "-"}</div >
              <div class="table-data">${intern.first_name ? intern.first_name : "-"}</div>
              <div class="table-data">${intern.last_name ? intern.last_name : "-"}</div>
              <div class="table-data">${intern.email ? intern.email : "-"}</div>
              <div class="table-data">${intern.studing_place ? intern.studing_place : "-"}</div>
              <div class="table-data">${intern.education ? intern.education : "-"}</div>
              <div class="table-data">${statusDict[intern.status_id] ? statusDict[intern.status_id] : "-"}</div>`;

        inputIntern.appendChild(internRow);
      }
    });

    document.querySelectorAll(".program-title").forEach((title) => {
      title.addEventListener("click", () => {
        title.classList.toggle("open");
        title.parentElement.querySelectorAll(".group").forEach((groups) => {
          groups.classList.toggle("open");
        });
      });
    });

    document.querySelectorAll(".group-title").forEach((title) => {
      title.addEventListener("click", () => {
        title.classList.toggle("open");
        title.parentElement
          .querySelector(".group-content")
          .classList.toggle("open");
      });
    });
  } catch (error) {
    console.error("Error fetching interns:", error);
  }
}

async function checkSw() {
  if (btnCand.classList.contains("selected")) {
    fetchCandidates();
  } else {
    if (btnIntern.classList.contains("selected")) {
      fetchInterns();
    }
  }
}
checkSw();

btnRefresh.addEventListener("click", function(event) {
  BtnImage.classList.add("rotating");
  checkSw();
  setTimeout(function() {
    BtnImage.classList.remove("rotating");
  }, 2000);
});

btnCand.addEventListener("click", function(event) {
  checkSw();
});
btnIntern.addEventListener("click", function(event) {
  checkSw();
});
