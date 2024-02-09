-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 09, 2024 at 04:52 AM
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
  `passWord` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `userName`, `passWord`) VALUES
(1, 'admin', 'admin123'),
(2, 'robert', 'robert123');

-- --------------------------------------------------------

--
-- Table structure for table `dutyhourformulationdata`
--

CREATE TABLE `dutyhourformulationdata` (
  `id` int(11) NOT NULL,
  `idNumber_stdnt` varchar(255) NOT NULL,
  `totaldutyHours` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dutyhourformulationdata`
--

INSERT INTO `dutyhourformulationdata` (`id`, `idNumber_stdnt`, `totaldutyHours`) VALUES
(27, '04-2122-031572', '0'),
(28, '04-2122-91734', '0'),
(29, '04-2122-000001', '0'),
(30, '04-2122-000002', '0'),
(31, '04-2122-035512', '0'),
(32, '04-2122-000003', '0');

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
('Parel', '04-2122-035512', 5),
('Parel', '04-2122-031572', 6),
('Parel', '04-2122-000001', 7);

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
('02-2387-700001', 'carmilo@gmail.com', 'Flame', 'Carmelo', '123', '0', 'BSCE', 'COME', '4', 'HK100', 'Student Facilitator', 'Nicole Lampa', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-000002', 'donna@gmail.com', 'Mallorca', 'Donna', '123', '0', 'BSBA', 'CMA', '1', 'HK25', 'Assistant Facilitator', 'Dean Seth Nono', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av'),
('04-2122-000001', 'jasper@gmail.com', 'operio', 'jasper', '123', '0', 'BSIT', 'CITE', '2', 'HK100', 'Student Facilitator', 'Zesty Mondia', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'Na'),
('04-2122-91734', 'jimama@gmail.com', 'Mariano', 'Jemima', 'jem', '0', 'BSBA', 'CAS', '1', 'HK100', 'Student Facilitator', 'Robert Calasara', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'av'),
('04-2122-035512', 'karenmay@gmail.com', 'Gaytano', 'Karen May', '1313', '0', 'BSIT', 'CITE', '4', 'HK75', 'Student Facilitator', 'Robert Calasara', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'Na'),
('04-2122-035546', 'kylepama@gnail.cute', 'Pama', 'Kayle', 'kyle', '0', 'BSBA', 'CAS', '2', 'HK25', 'Assistant Facilitator', 'Robert Calasara', '180', '180', '0', 'pending', '2023 - 2024', '2nd sem', 'av'),
('04-2122-031572', 'ream.mallorca.ui@phinmaed.com', 'Mallorca', 'Reuben', '123', '10', 'BSIT', 'CITE', '3', 'HK50', 'Assistant Facilitator', 'Robert Calasara', '180', '179', '50.000000000000405', 'pending', '2023 - 2024', '2nd sem', 'Na'),
('04-2122-000003', 'ryan@gmail.com', 'Mallorca', 'Ryan', '123', '0', 'BSCE', 'COE', '4', 'HK75', 'Assistant Facilitator', 'Kurt Parel', '180', '180', '0', 'pending', '2023-2024', '2nd sem', 'av');

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
  `Operations_Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `operations_data`
--

INSERT INTO `operations_data` (`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`) VALUES
('Mondia', 'Zesty', 'zest123', '03-1234-123456', 'CHAS', 'G', '09876543219', 'Faculty', 'Zesty@gmail.com'),
('Calasra', 'Robert', 'Robert123', '04-2119-123456', 'CITE', 'J', '09991234567', 'Faculty', 'robert@gmail.com'),
('Parel', 'Kurt', 'kurt123', '04-2122-031289', 'CITE', 'H', '09921345678', 'Faculty', 'Kurt@gmail.com'),
('Yacub', 'Bruce', 'bruce123', '05-3451-90896712', 'COME', 'F', '12345678901', 'Faculty', 'Bruce@gmail');

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

--
-- Dumping data for table `operation_request`
--

INSERT INTO `operation_request` (`Designation`, `Requirements`, `Report Day/s`, `Request`, `DEPT`, `SUPERVISOR`, `ID`) VALUES
('af', '2nd', 'F', '2', 'CITE', 'Calasra', 2),
('sf', '2nd', 'F-TH', '1', 'CITE', 'Calasra', 3),
('af', '3rd', 'F/Sat', '5', 'CITE', 'Parel', 4),
('af', '4th', 'M-Wed', '1', 'CITE', 'Parel', 5),
('sf', '3rd', 'f-th', '4', 'CITE', 'Parel', 6),
('Gosto  migo', 'gwapo', 'forever', '1', 'CITE', 'Calasra', 7),
('AF', '3rd yr', 'T', '3', 'CHAS', 'Mondia', 8);

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
('2024-02-09', 10, 33, '04-2122-031572', 243, 'IN'),
('2024-02-09', 10, 34, '04-2122-031572', 244, 'OUT'),
('2024-02-09', 10, 34, '04-2122-031572', 245, 'IN'),
('2024-02-09', 10, 35, '04-2122-031572', 246, 'OUT'),
('2024-02-09', 10, 35, '04-2122-031572', 247, 'IN'),
('2024-02-09', 10, 36, '04-2122-031572', 248, 'OUT'),
('2024-02-09', 10, 36, '04-2122-031572', 249, 'IN'),
('2024-02-09', 10, 40, '04-2122-031572', 250, 'OUT'),
('2024-02-09', 10, 40, '04-2122-031572', 251, 'IN'),
('2024-02-09', 10, 40, '04-2122-031572', 252, 'OUT'),
('2024-02-09', 10, 45, '04-2122-031572', 253, 'IN'),
('2024-02-09', 10, 52, '04-2122-031572', 254, 'IN'),
('2024-02-09', 10, 53, '04-2122-031572', 255, 'OUT'),
('2024-02-09', 10, 54, '04-2122-031572', 256, 'IN'),
('2024-02-09', 10, 55, '04-2122-031572', 257, 'OUT'),
('2024-02-09', 10, 57, '04-2122-031572', 258, 'IN'),
('2024-02-09', 10, 58, '04-2122-031572', 259, 'OUT');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `dutyhourformulationdata`
--
ALTER TABLE `dutyhourformulationdata`
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
-- AUTO_INCREMENT for table `dutyhourformulationdata`
--
ALTER TABLE `dutyhourformulationdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `hk_assignd_teaecher`
--
ALTER TABLE `hk_assignd_teaecher`
  MODIFY `assigmentID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `operation_request`
--
ALTER TABLE `operation_request`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `scholar_duty_records`
--
ALTER TABLE `scholar_duty_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=260;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
