<?php
// Database configuration
$dbHost = "localhost";
$dbUsername = "root";
$dbPassword = "Admin";
$dbName = "login_system";

// Create database connection
$conn = mysqli_connect($dbHost, $dbUsername, $dbPassword, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?>
