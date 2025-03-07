<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta content="width=device-width, initial-scale=1.0" name="viewport">

  <title> ScholarTrack</title>
  <meta content="" name="description">
  <meta content="" name="keywords">

  <!-- Favicons -->
  <link href="static/assetsLanding/img/" rel="icon">
  <link href="static/assetsLanding/img/apple-touch-icon.png" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Montserrat:300,300i,400,400i,500,500i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">

  <!-- Vendor CSS Files -->
  <link href="static/assetsLanding/vendor/aos/aos.css" rel="stylesheet">
  <link href="static/assetsLanding/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
  <link href="static/assetsLanding/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
  <link href="static/assetsLanding/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
  <link href="static/assetsLanding/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
  <link href="static/assetsLanding/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

  <!-- Template Main CSS File -->
  <link href="static/assetsLanding/css/styleUsere.css" rel="stylesheet">
  
</head>
<style>
  
body {
  font-family: "Open Sans", sans-serif;
 
  color: #555555;
}

a {
  text-decoration: none;
  color: #7cc576;
}

a:hover {
  color: #9ed49a;
  text-decoration: none;
}
.text{

}
h1
h2
h3,
h4,
h5,
h6 {
  /* font-family: "Source Sans Pro",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"; */
}

/*--------------------------------------------------------------
# Back to top button
--------------------------------------------------------------*/
.back-to-top {
  position: fixed;
  visibility: hidden;
  opacity: 0;
  right: 15px;
  bottom: 15px;
  z-index: 996;
  background: #7cc576;
  width: 40px;
  height: 40px;
  border-radius: 4px;
  transition: all 0.4s;
}

.back-to-top i {
  font-size: 28px;
  color: #fff;
  line-height: 0;
}

.back-to-top:hover {
  background: #97d193;
  color: #fff;
}

.back-to-top.active {
  visibility: visible;
  opacity: 1;
}
.row .text{
  line-height: 30px;
  padding-top: 20px;
  text-indent: 50px;
  word-spacing: 5px;
  text-align: justify;
}
/*--------------------------------------------------------------
# Disable AOS delay on mobile
--------------------------------------------------------------*/
@media screen and (max-width: 768px) {
  [data-aos-delay] {
    transition-delay: 0 !important;
  }
}

/*--------------------------------------------------------------
# Header
--------------------------------------------------------------*/
#header {
  height: 90px;
  transition: all 0.5s;
  z-index: 997;
  transition: all 0.5s;
  background: #fff;
  box-shadow: 0 4px 10px -3px hsla(0, 0%, 75%, 0.5);
}

#header .logo h1 {
  font-size: 28px;
  margin: 0;
  line-height: 1;
  font-weight: 400;
  letter-spacing: 3px;
  text-transform: uppercase;
}

#header .logo h1 a,
#header .logo h1 a:hover {
  color: #fff;
  text-decoration: none;
}

#header .logo img {
  padding: 0;
  margin: 0;
  max-height: 70px;
}

@media (max-width: 992px) {
  #header {
    height: 70px;
  }
}

.scrolled-offset {
  margin-top: 90px;
}

@media (max-width: 992px) {
  .scrolled-offset {
    margin-top: 90px;
  }
}


/*--------------------------------------------------------------
# Hero Section
--------------------------------------------------------------*/
#hero {
  width: 100%;
  height: 115vh;
  background: fixed;
  background-image: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 20%, rgba(61,153,112,1) 100%);
  position: relative;

}

#hero .hero-container {
  background-color: #fff;
  max-width: 590px;
  border: 5px solid #3b6085;
  padding-top: 20px;
  height: 620px;
  padding: 300px;
  border-radius: 30px;
  margin-left: 450px;
  margin-top: 15px;
  justify-content: center;
  align-items: center;
  text-align: center;
  padding: 0 0px;
  padding-bottom: 400px;
}


.hero-logo img{
  margin-left: 23.2%;
  margin-top: 25px;
  margin-bottom: 22px;
}


#hero h1 {
  margin: 0 0 10px 0;
  padding-bottom: 10px;
  font-size: 35px;
  font:bolder;
  font-family:'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
  margin-top: 13px;
  letter-spacing: 1px;
  font-weight: 500;
  line-height: 56px;
  color-scheme: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 50%, rgba(61,153,112,1) 100%);
}

#hero h2 {
 color: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 50%, rgba(61,153,112,1) 100%);
  margin-bottom: 40px;
  font-size: 18px;
  margin-top: 30px;
  text-transform: uppercase;
  letter-spacing: 0.8px;
}

#hero .btn-get-started {
  font-weight: 700;
  font-family: "Montserrat", sans-serif;
  text-transform: uppercase;
  font-weight: 400;
  font-size: 16px;
  letter-spacing: 1px;
  display:inline-block;
  padding: 12px 37px;
  background: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 50%, rgba(61,153,112,1) 100%);
  color:  white;
  
}
#hero .btn-get-starteds {
  font-family: "Montserrat", sans-serif;
  text-transform: uppercase;
  font-weight: 400;
  font-size: 16px;
  letter-spacing: 1px;
  display:inline-block;
  padding: 12px 37px;
  background: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 50%, rgba(61,153,112,1) 100%);
  color:  white;
 
}
#hero .btn-get-started1 {
  font-family: "Montserrat", sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  font-weight: 600;
  border-radius: 15px;
  font-size: 16px;
  letter-spacing: 1px;
  display:inline-block;
  padding: 12px 37px;
  margin-top: 40px;
  background: linear-gradient(180deg, rgba(0,31,63,1) 0%, rgba(4,75,148,1) 10%, rgba(61,153,112,1) 100%);
  color:  white;
}
#hero .btn-get-started1:hover {
  transition: 0.5s;
  background: gray;
  color: white;
  border: 2px rgba(56, 56, 56, 0.927);

 

}

#hero .btn-get-starteds:hover {
  transition: 0.5s;
  background: white;
  color:  #585656;;

}
#hero .user-details {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
 
}
#hero .nice{
position:relative;
margin-left: 100px;
margin-top: 0px;
margin-top: 10px;
  
}

.user-details .input-box .details{
  display: block;
  border-radius: 50px;
  font-weight: bold;
  text-align: left;
  margin-left: 150px;
  padding-bottom: 20px;


}

.user-details .input-box{
  width: calc(100%);
}

.user-details .input-box input{
  border-radius: 10px;
  padding-left: 10px;
  width: 50%;
  height: 40px;
  padding-bottom: 10px;
  padding-top: 10px;

}

section {
  padding: 60px 0;
  overflow: hidden;
}
.unod .input-box input{
height: 40px;
align-items: center;
width: 200px;
outline: none;
border: 2px rgba(56, 56, 56, 0.927);
padding-left: 19px;
padding-right: 1px;
font-size: 16px;
border-bottom-width: 2px;
transition: all 0.3s ease;
}

.section-bg {
  background-color: whitesmoke;
}

.section-title {
  text-align: center;
  padding-bottom: 40px;
}

.section-title h2 {
  font-size: 32px;
  font-weight: bold;
  text-transform: uppercase;
  margin-bottom: 15px;
  padding-bottom: 0;
  color: #151515;
}

.section-title p {
  margin-bottom: 0;
  color: #aeaeae;
}

@media (max-width: 768px) {

#hero .hero-container {
  max-width: 500px;
  width: fit-content;
  margin: 20px;
}

.user-details .input-box .details{
  max-height: 300px;
  font-weight: bold;
  text-align: left;
  padding-bottom: 20px;
  margin-left: 0;
  margin-left: 100px;
}
#hero .btn-get-started {
margin-left: 150px;
margin-top: 100px;
margin: 0;

}
#hero .btn-get-started:hover {
  transition: 0.5s;
  background: white;
  color: gray;


}

#hero h2 {
  margin-bottom: px;
  font-size: 18px;
  margin-top: 5px;
  font-weight: 400;
  text-transform: uppercase;
  padding: 10px;
}
#hero h1{
  margin-top: 20px;
  margin-bottom: 40px;
  
}



}
</style>


<body>

  <!-- ======= Hero Section ======= -->
  <section id="hero">
    <div class="hero-container">
  
      <a href="" class="hero-logo"><img src="static/assetsLanding\img\2.png" width="340px"></a>
      <h2 data-aos="fade-up">Automated Phinma UI Scholar's System for <br> Monitoring</p></h2>
      <h1 data-aos="zoom-in">SCHOLAR TRACK</h1>
      <a data-aos="fade-up" data-aos-delay00 ="100" href="{{url_for('sts_Page')}}" class="btn-get-started1 scrollto">GET STARTED</a>
     
    </div>
  </section><!-- End Hero -->


  <!-- Vendor JS Files -->
  <script src="static/assetsLanding/vendor/aos/aos.js"></script>
  <script src="static/assetsLanding/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="static/assetsLanding/vendor/glightbox/js/glightbox.min.js"></script>
  <script src="static/assetsLanding/vendor/isotope-layout/isotope.pkgd.min.js"></script>
  <script src="static/assetsLanding/vendor/swiper/swiper-bundle.min.js"></script>
  <script src="static/assetsLanding/vendor/php-email-form/validate.js"></script>

  
  <!-- Template Main JS File -->
  <script src="static/assetsLanding/js/main.js"></script>


    </div>
  </div>
</div>

</body>

</html>