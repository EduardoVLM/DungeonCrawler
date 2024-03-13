<?php
session_start();
include "db_config.php";
 
 
 
if(isset($_POST['username']) && isset($_POST['password'])) {
function validate($data) {
        $data = trim($data);
        $data = stripslashes($data);
        $data = htmlspecialchars($data);
        return $data;
    }
 
//her definer jeg variablene//
 
$brukernavn = validate($_POST['username']);
$passord = validate($_POST['password']);
 
//Hvis brukernavn eller passord mangler sender dette en feilmelding til url
if(empty($brukernavn)) {
    header ("Location: createUser.php?error=Username is required!");
    exit();
}
else if(empty($passord)) {
    header ("Location: createUser.php?error=Password is required!");
    exit();
}
 
echo $_POST['username'];
 
//her legges brukeren inn i databasen
$sql = "INSERT INTO users (username, password) VALUES ('".$brukernavn."', '".$passord."')";
 
// if statement for å sende brukeren tilbake til startsiden
if ($result = mysqli_query($conn, $sql)){
    header("location: index.php");
 
                }      
 
           
 
        }
     
?>
 
<!DOCTYPE html>
<html>
<head>
 
</head>
<body>
    <form method="post">
        <h2>Opprett bruker:</h2>
        <label>Bruker: </label>
    <input type="text" name="username" placeholder="username"><br/>
        <label>password: </label>
    <input type="password" name="password" placeholder="password"><br/>
    <input type="submit">
    </form>
   
</body>
</html>
 
 
 
<?php
 
?>