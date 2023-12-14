<?php
  include('connection.php');
  $con = connection();

  $name = $_POST['name'];
  $description = $_POST['description'];
  $dueDate = $_POST['dueDate'];

  $sql = "INSERT INTO `projects` (`proj_name`, `proj_description`, `proj_due_date`) 
  VALUES ('$name', '$description', '$dueDate')";
  
  $query = mysqli_query($con, $sql);

  if($query){
    Header("Location: projects.php");
  };
?>