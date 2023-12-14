<?php
    include('connection.php');
    $con = connection();
    $id = $_GET['proj_id'];

    $sql = "DELETE FROM projects WHERE `proj_id` = '$id'";
    $query = mysqli_query($con, $sql);
    
    if($query){
        Header("Location: projects.php");
    };
?>