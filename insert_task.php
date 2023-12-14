<?php
  include('connection.php');
  $con = connection();

  $title = $_POST['title'];
  $project = $_POST['project'];
  $assignedTo = $_POST['assignedTo'];
  $dueDate = $_POST['dueDate'];
  $status = $_POST['status'];

  $sql = "INSERT INTO `tasks` (`task_title`, `project`, `assigned_to`, `task_due_date`, `status`) 
  VALUES ('$title', '$project', '$assignedTo', '$dueDate', '$status')";
  
  $query = mysqli_query($con, $sql);

  if($query){
    Header("Location: tasks.php");
  };
?>