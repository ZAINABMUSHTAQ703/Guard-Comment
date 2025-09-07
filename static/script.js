async function submitComment() {
  const comment = document.getElementById("commentInput").value.trim();
  const messageDiv = document.getElementById("message");

  if (!comment) {
    messageDiv.innerHTML = "⚠️ Please type something!";
    messageDiv.className = "blocked";
    return;
  }

  const response = await fetch("/check_comment", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ comment: comment })
  });

  const result = await response.json();

  if (result.status === "blocked") {
    messageDiv.innerHTML = result.message;
    messageDiv.className = "blocked";
  } else {
    messageDiv.innerHTML = result.message;
    messageDiv.className = "allowed";

    // Add comment to approved list
    const commentList = document.getElementById("commentList");
    const li = document.createElement("li");
    li.textContent = comment;
    commentList.appendChild(li);

    // Clear input
    document.getElementById("commentInput").value = "";
  }
}
