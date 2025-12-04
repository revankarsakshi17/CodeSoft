document.getElementById("uploadForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const fileInput = document.getElementById("imageInput");
    const result = document.getElementById("result");

    if (!fileInput.files.length) {
        alert("Please upload an image.");
        return;
    }

    // Show result box
    result.style.display = "block";
    result.innerHTML = "Analyzing... Please wait ⏳";

    const formData = new FormData();
    formData.append("image", fileInput.files[0]);

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (data.error) {
            result.innerHTML = `❌ Error: ${data.error}`;
            return;
        }

        // Show result with emoji
        result.innerHTML = `
            <span style="font-size:40px;">${getEmoji(data.mood)}</span>
            <h3>Mood: ${data.mood.toUpperCase()}</h3>
            <p>${data.caption}</p>
        `;
    } catch (error) {
        result.innerHTML = "❌ Server Error";
    }
});

function getEmoji(mood) {
    const emojis = {
        happy: "😊",
        sad: "😢",
        angry: "😠",
        surprise: "😲",
        fear: "😨",
        neutral: "😐"
    };
    return emojis[mood] || "🙂";
}
