<?php
  include('connection.php');
  $con = connection();

  $title = $_POST['title'];
  $leader = $_POST['leader'];
  $description = $_POST['description'];

  $sql = "INSERT INTO `teams` (`team_title`, `leader`, `team_description`) 
  VALUES ('$title', '$leader', '$description')";
  
  $query = mysqli_query($con, $sql);

  if($query){
    Header("Location: teams.php");
  };
?>