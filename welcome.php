<?php
// Start session to persist user login status
session_start();

// Check if user is logged in, if not redirect to login page
if (!isset($_SESSION['username'])) {
    header("Location: index.php");
    exit;
}

// Display welcome message
echo "Welcome, " . $_SESSION['username'] . "! You are logged in.";

// Link to logout
echo "<br><a href='logout.php'>Logout</a>";
?>
