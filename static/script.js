const form = document.getElementById("cropForm");
const submitBtn = document.getElementById("submitBtn");
const resultBox = document.getElementById("result");
const errorBox = document.getElementById("errorBox");
const resultCrop = document.getElementById("resultCrop");
const top3Box = document.getElementById("top3");
const errorText = document.getElementById("errorText");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  resultBox.hidden = true;
  errorBox.hidden = true;
  submitBtn.disabled = true;
  submitBtn.textContent = "Checking the soil...";

  const payload = {
    N: document.getElementById("N").value,
    P: document.getElementById("P").value,
    K: document.getElementById("K").value,
    temperature: document.getElementById("temperature").value,
    humidity: document.getElementById("humidity").value,
    ph: document.getElementById("ph").value,
    rainfall: document.getElementById("rainfall").value,
  };

  try {
    const res = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const data = await res.json();

    if (!data.success) {
      throw new Error(data.error || "Something went wrong.");
    }

    resultCrop.textContent = data.prediction;

    top3Box.innerHTML = "";
    data.top3.forEach((item) => {
      const row = document.createElement("div");
      row.className = "top3-row";
      row.innerHTML = `
        <span class="crop-name">${item.crop}</span>
        <span class="bar-track"><span class="bar-fill" style="width:${item.confidence}%"></span></span>
        <span class="pct">${item.confidence}%</span>
      `;
      top3Box.appendChild(row);
    });

    resultBox.hidden = false;
  } catch (err) {
    errorText.textContent = err.message;
    errorBox.hidden = false;
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Recommend a crop";
  }
});
