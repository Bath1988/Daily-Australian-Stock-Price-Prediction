fetch("http://localhost:8000/predict")
  .then(res => res.json())
  .then(data => {
    document.getElementById("prediction").innerText = 
      `Next day: $${data.yhat[0].toFixed(2)}`;
  });