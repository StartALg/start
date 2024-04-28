<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the form data
    $meetingTitle = $_POST["meetingTitle"];
    $meetingDateTime = $_POST["meetingDateTime"];
    $personName = $_POST["personName"];
    $personEmail = $_POST["personEmail"];
    $comments = $_POST["comments"];

    // Compose the email message
    $to = "lokmanmih05@gmail.com"; // Replace with your email address
    $subject = "Meeting Reservation Details";
    $message = "Hello $personName,\n\n";
    $message .= "Thank you for reserving a meeting. Below are the details:\n\n";
    $message .= "Meeting Title: $meetingTitle\n";
    $message .= "Meeting Date and Time: $meetingDateTime\n";
    $message .= "Your Name: $personName\n";
    $message .= "Your Email: $personEmail\n";
    $message .= "Additional Comments: $comments\n\n";
    $message .= "You will be discussing with the tutor at the meeting.\n";
    $headers = "From: zakariabouidane@gmail.com"; // Replace with your email address

    // Send the email
    if (mail($to, $subject, $message, $headers)) {
        // Email sent successfully
        echo "Email sent successfully.";
    } else {
        // Email sending failed
        echo "Failed to send email. Please try again later.";
    }
} else {
    // If the form is not submitted, redirect back to the form page
    header("Location: index.html");
    exit;
}
?>
