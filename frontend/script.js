document.getElementById("ngoForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const desc = document.getElementById("desc").value;

  const response = await fetch("http://127.0.0.1:8000/match", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ description: desc }),
  });

  const data = await response.json();
  document.getElementById("output").innerText = data.recommendation;
});

