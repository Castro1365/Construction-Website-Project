// Simple JS just for the contact form confirmation
function handleContactSubmit(event) {
    event.preventDefault();
    alert("Thank you! Your request has been recorded. We will contact you soon.");
    event.target.reset();
}
