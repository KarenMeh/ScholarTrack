<?php
include "conn.php";

if(isset($_POST['login'])){
$email=$_POST['email'];
$pass=$_POST['pass'];


    ///to pass data to flask
$response = file_get_contents("http://localhost:5000/adminDashboard?email='.urlencode($email) ");

 
    $check=mysqli_query($conn,"SELECT * FROM `admin` WHERE userName='$email' AND passWord='$pass'");
    $num=mysqli_num_rows($check);

    if ($num >=1){
        $_SESSION['email']=$email;

        ?>
        <script>

           alert("Account Accepted!");
           window.location.href="http://localhost/capstone/caps/dashboard%20admin/dashboardAdminFinal.php";
        </script>

        <?php
  
     }else{
        ?>
        <script>
           alert("Email or Password not Found!");
           window.location.href="admin.php";
        </script>
        <?php
     }
    }


    










?>