axios
  .get("http://localhost:8000/api/v1/auth/users/me", { withCredentials: true })
  .then((responce) => { })
  .catch((error) => {
    window.location.href = "index.html";
  });
