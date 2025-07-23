document.addEventListener("DOMContentLoaded", function () {
    const timeSlots = document.querySelectorAll(".time-slot");
    const hiddenInput = document.getElementById("selected-time");

    timeSlots.forEach(slot => {
        slot.addEventListener("click", () => {
            timeSlots.forEach(s => s.classList.remove("selected"));
            slot.classList.add("selected");
            hiddenInput.value = slot.innerText;
        });
    });
});

