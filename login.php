<?php

session_start();

// Include database connection file
include_once "db_config.php";

// Get username and password from the form
$username = $_POST['username'];
$password = $_POST['password'];

// Query to check if user exists
$query = "SELECT * FROM users WHERE username='$username' AND password='$password'";
$result = mysqli_query($conn, $query);

// Check if query returns a row
if (mysqli_num_rows($result) == 1) {
    // User exists, set session variables and redirect to welcome page
    $_SESSION['username'] = $username;
    header("Location: welcome.php");
} else {
    // User doesn't exist, redirect back to login page with error message
    $_SESSION['error'] = "Invalid username or password";
    header("Location: index.php");
}

// Close database connection
mysqli_close($conn);
?>
