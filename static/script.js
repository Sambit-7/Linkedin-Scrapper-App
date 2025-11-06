function checkProgress() {
  fetch("/progress_status")
    .then((response) => response.json())
    .then((data) => {
      if (data.status === "done") {
        window.location.href = "/result";
      } else if (data.status === "running") {
        const percent = Math.round((data.current / data.total) * 100);
        document.getElementById("progressFill").style.width = percent + "%";
        document.getElementById("progressText").innerText =
          `Scraped ${data.current} of ${data.total} profiles (${percent}%)`;
      }
      setTimeout(checkProgress, 1000);
    });
}
window.onload = checkProgress;
