<?php
  include('connection.php');
  $con = connection();

  $id = $_POST['id'];
  $title = $_POST['title'];
  $leader = $_POST['leader'];
  $description = $_POST['description'];

  $sql = "UPDATE teams SET `team_title`='$title', `leader`='$leader', `team_description`='$description'
  WHERE `team_id`='$id'";
  
  $query = mysqli_query($con, $sql);

  if($query){
    Header("Location: teams.php");
  };
?>