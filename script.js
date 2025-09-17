document.getElementById("registerForm").addEventListener("submit", async (e) => {
  e.preventDefault();

  const formData = {
    name: e.target.name.value,
    email: e.target.email.value,
    pack: e.target.pack.value,
    message: e.target.message.value
  };

  const res = await fetch("/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(formData)
  });

  const data = await res.json();
  document.getElementById("response").textContent = data.message;
});
