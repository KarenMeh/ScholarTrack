-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 17, 2024 at 04:13 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hkscholar`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `userName` varchar(255) NOT NULL,
  `adminIdNumber` varchar(255) NOT NULL,
  `passWord` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `userName`, `adminIdNumber`, `passWord`) VALUES
(1, 'Jester Paul Bacabac', '04-1234-1234', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `hk_assignd_teaecher`
--

CREATE TABLE `hk_assignd_teaecher` (
  `operatikon_ID` varchar(255) NOT NULL,
  `hk_ID` varchar(255) NOT NULL,
  `assigmentID` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hk_assignd_teaecher`
--

INSERT INTO `hk_assignd_teaecher` (`operatikon_ID`, `hk_ID`, `assigmentID`) VALUES
('Parel Kurt', '02-2387-700001', 45),
('Parel Kurt', '04-2200-90001', 46);

-- --------------------------------------------------------

--
-- Table structure for table `hk_users`
--

CREATE TABLE `hk_users` (
  `idnum` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `lname` varchar(255) NOT NULL,
  `fname` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `id_totalHours` varchar(255) NOT NULL,
  `program_course` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  `yrLvL` varchar(255) NOT NULL,
  `scholarship` varchar(255) NOT NULL,
  `dutyDesignation` varchar(255) NOT NULL,
  `dutySupervisor` varchar(255) NOT NULL,
  `reqiredDuty` varchar(255) NOT NULL,
  `remaningDuty` varchar(255) NOT NULL,
  `remDutyMins` varchar(255) NOT NULL,
  `statsForRenewal` varchar(255) NOT NULL,
  `SchoolYr` varchar(255) NOT NULL,
  `semister` varchar(255) NOT NULL,
  `Status_avail` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hk_users`
--

INSERT INTO `hk_users` (`idnum`, `email`, `lname`, `fname`, `password`, `id_totalHours`, `program_course`, `department`, `yrLvL`, `scholarship`, `dutyDesignation`, `dutySupervisor`, `reqiredDuty`, `remaningDuty`, `remDutyMins`, `statsForRenewal`, `SchoolYr`, `semister`, `Status_avail`) VALUES
('02-2387-700001', 'carmilo@gmail.com', 'Flame', 'Carmelo', '', '0', 'BSCE', 'COME', '4', 'HK100', 'AF', 'Parel Kurt', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'Na'),
('04-2200-90001', 'Dionar@gmail.com', 'Antioquia', 'Dionard', '', '0', 'BSHM', 'COA', '4', 'HK50', 'AF', 'Parel Kurt', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'Na'),
('04-2122-000002', 'donna@gmail.com', 'Mallorca', 'Donna', '', '0', 'BSBA', 'COM', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-000001', 'jasper@gmail.com', 'operio', 'jasper', '', '0', 'BSIT', 'CITE', '2', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-78627', 'Javelosa@gmail.com', 'Javelosa ', 'Wolf', '', '0', 'BSC', 'CCJE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-91734', 'jimama@gmail.com', 'Mariano', 'Jemima', '', '0', 'BSBA', 'CAS', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'av'),
('04-2002-90021', 'justin@gmail.com', 'Susal', 'Justiene', '', '0', 'BSCE', 'CHAS', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-035512', 'karenmay@gmail.com', 'Gaytano', 'Karen May', '', '0', 'BSIT', 'CITE', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'av'),
('04-2122-035546', 'kylepama@gnail.cute', 'Pama', 'Kayle', '', '0', 'BSBA', 'CAS', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'av'),
('09-2155-90828', 'malo@gmail.com', 'Amante', 'Malorena', '', '0', 'BSHM', 'CAHS', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-1234-87237', 'Pechera@gamil.com', 'Pechera', 'Alessandra', '', '0', 'BSBS', 'COE', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-031572', 'ream.mallorca.ui@phinmaed.com', 'Mallorca', 'Reuben', '', '40', 'BSIT', 'CITE', '3', 'HK75', '', '', '180', '179', '16.9999999999998', 'pending', '2023 - 2024', '2nd sem', 'av'),
('04-2122-000003', 'ryan@gmail.com', 'Mallorca', 'Ryan', '', '0', 'BSCE', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av');

-- --------------------------------------------------------

--
-- Table structure for table `operations_data`
--

CREATE TABLE `operations_data` (
  `Faculty_Lname` varchar(255) NOT NULL,
  `Faculty_Fname` varchar(255) NOT NULL,
  `Faculty_Password` varchar(255) NOT NULL,
  `Faculty_Id_Number` varchar(255) NOT NULL,
  `Operation_Dept` varchar(255) NOT NULL,
  `Operations_Mname` varchar(255) NOT NULL,
  `Operation_phone_Number` varchar(255) NOT NULL,
  `Operation_Designation-Position` varchar(255) NOT NULL,
  `Operations_Email` varchar(255) NOT NULL,
  `profilePics` varchar(255) NOT NULL,
  `operations_about` varchar(255) NOT NULL,
  `twitter` varchar(255) NOT NULL,
  `facebook` varchar(255) NOT NULL,
  `instagram` varchar(255) NOT NULL,
  `linkedin` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `status_ol` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `operations_data`
--

INSERT INTO `operations_data` (`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`, `profilePics`, `operations_about`, `twitter`, `facebook`, `instagram`, `linkedin`, `Address`, `status_ol`) VALUES
('Mondia', 'Zesty', 'zest123', '03-1234-123456', 'CHAS', 'G', '09876543219', 'Faculty', 'Zesty@gmail.com', '', '', '', '', '', '', '', 'offline'),
('Calasra', 'Robert', 'Robert123', '04-2119-123456', 'CITE', 'J', '09991234567', 'Faculty', 'robert@gmail.com', 'faculty_robert.jpg', '', '', '', '', '', '', 'offline'),
('Parel', 'Kurt', '@Kurt123456789', '04-2122-031289', 'CITE', 'H', '09996563067', 'Faculty', 'KURT2@GMAILK.COM', 'ser.jpg', 'Our mission is to explore the limitless possibilities of technology and harness its potential to drive positive change in the world. We are committed to staying at the forefront of technological advancements, empowering individuals with the knowledge and ', 'HTTPS://WWW.FACEBOOK.COM/KURT.PAREL', 'HTTPS://WWW.FACEBOOK.COM/KURT.PAREL', 'HTTPS://WWW.FACEBOOK.COM/KURT.PAREL', 'HTTPS://WWW.FACEBOOK.COM/KURT.PAREL', 'ILOILO CITY MANDURRIAO', 'Online'),
('Yacub', 'Bruce', 'bruce123', '05-3451-90896712', 'COME', 'F', '12345678901', 'Faculty', 'Bruce@gmail', '', '', '', '', '', '', '', 'offline');

-- --------------------------------------------------------

--
-- Table structure for table `operation_request`
--

CREATE TABLE `operation_request` (
  `Designation` varchar(255) NOT NULL,
  `Requirements` varchar(255) NOT NULL,
  `Report Day/s` varchar(255) NOT NULL,
  `Request` varchar(255) NOT NULL,
  `DEPT` varchar(255) NOT NULL,
  `SUPERVISOR` varchar(255) NOT NULL,
  `ID` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `reports/announcement`
--

CREATE TABLE `reports/announcement` (
  `content` varchar(500) NOT NULL,
  `date` varchar(255) NOT NULL,
  `time` varchar(255) NOT NULL,
  `adminName` varchar(255) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `reports/announcement`
--

INSERT INTO `reports/announcement` (`content`, `date`, `time`, `adminName`, `id`) VALUES
('        Duty Assignments the Upcoming for Week Announce', '2024-02-22', '8:43', 'admin', 5),
('        sir robert calasar ikaw gina pa tawag sa csdl kadto d mga 3 pm d ka ma late ha manda kalang', '2024-02-22', '10:28', 'admin', 6),
('        tryal acnnouncment lang dont pansin it hehe\r\n', '2024-02-22', '22:23', 'admin', 7),
('  DUTY HOURS EXTENDED      ', '2024-03-08', '15:3', 'Jester Paul Bacabac', 11);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `email` varchar(255) NOT NULL,
  `timeIn` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `timeOut` varchar(255) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `scholar_duty_records`
--

CREATE TABLE `scholar_duty_records` (
  `date` varchar(255) NOT NULL,
  `Hours_In_Out` int(255) NOT NULL,
  `Minutes_In_Out` int(255) NOT NULL,
  `Student_id_Number` varchar(255) NOT NULL,
  `id` int(11) NOT NULL,
  `Type_of_Process` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `scholar_duty_records`
--

INSERT INTO `scholar_duty_records` (`date`, `Hours_In_Out`, `Minutes_In_Out`, `Student_id_Number`, `id`, `Type_of_Process`) VALUES
('2024-03-17', 22, 9, '04-2122-031572', 292, 'IN'),
('2024-03-17', 22, 49, '04-2122-031572', 293, 'OUT');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `hk_assignd_teaecher`
--
ALTER TABLE `hk_assignd_teaecher`
  ADD PRIMARY KEY (`assigmentID`);

--
-- Indexes for table `hk_users`
--
ALTER TABLE `hk_users`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `idnum` (`idnum`),
  ADD KEY `id_totalHours` (`id_totalHours`);

--
-- Indexes for table `operations_data`
--
ALTER TABLE `operations_data`
  ADD PRIMARY KEY (`Faculty_Id_Number`);

--
-- Indexes for table `operation_request`
--
ALTER TABLE `operation_request`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `reports/announcement`
--
ALTER TABLE `reports/announcement`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `scholar_duty_records`
--
ALTER TABLE `scholar_duty_records`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hk_assignd_teaecher`
--
ALTER TABLE `hk_assignd_teaecher`
  MODIFY `assigmentID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `operation_request`
--
ALTER TABLE `operation_request`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `reports/announcement`
--
ALTER TABLE `reports/announcement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `scholar_duty_records`
--
ALTER TABLE `scholar_duty_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=294;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
