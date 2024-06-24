axios
  .get("http://localhost:8000/api/v1/auth/users/me", { withCredentials: true })
  .then((response) => {
    window.location.href = "admin.html";
  })
  .catch((error) => { });
