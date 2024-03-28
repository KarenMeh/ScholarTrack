-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 28, 2024 at 01:04 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `active_logs`
--

CREATE TABLE `active_logs` (
  `id` int(255) NOT NULL,
  `date_time` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `uname` varchar(255) NOT NULL,
  `dept` varchar(255) NOT NULL,
  `act_perm` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `active_logs`
--

INSERT INTO `active_logs` (`id`, `date_time`, `user_id`, `uname`, `dept`, `act_perm`) VALUES
(2, '2024-03-19 22:48:31', '03-1234-123456', 'Mondia Zesty', 'CAHS', 'Just log in to the system'),
(3, '2024-03-19 23:15:59', '03-1234-123456', 'Mondia Zesty', 'CAHS', 'Just log out to the system'),
(4, '2024-03-19 23:17:33', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(5, '2024-03-19 23:20:57', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(6, '2024-03-19 23:30:55', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(7, '2024-03-19 23:31:12', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Update profile'),
(8, '2024-03-19 23:34:44', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Change credentials'),
(9, '2024-03-19 23:39:47', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(10, '2024-03-19 23:40:35', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(11, '2024-03-19 23:40:39', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(12, '2024-03-19 23:41:24', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log in to the system'),
(13, '2024-03-19 23:41:46', '04-2122-022772', 'Mariano Jemima', 'COA', 'Update profile'),
(14, '2024-03-19 23:43:12', '04-2122-022772', 'Mariano Jemima', 'COA', 'Update profile'),
(15, '2024-03-26 18:33:06', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(16, '2024-03-27 14:38:01', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(17, '2024-03-27 15:27:18', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(18, '2024-03-27 16:15:19', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(19, '2024-03-27 21:41:43', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(20, '2024-03-27 21:41:48', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(21, '2024-03-27 21:44:30', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(22, '2024-03-27 21:44:33', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(23, '2024-03-27 21:55:39', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(24, '2024-03-27 21:58:15', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(25, '2024-03-27 22:00:30', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(26, '2024-03-27 22:00:57', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(27, '2024-03-27 22:01:19', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(28, '2024-03-27 22:02:32', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(29, '2024-03-27 22:02:51', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(30, '2024-03-27 22:03:00', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(31, '2024-03-27 22:03:26', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(32, '2024-03-27 22:05:30', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(33, '2024-03-27 22:09:29', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(34, '2024-03-27 22:12:08', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(35, '2024-03-27 22:12:48', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(36, '2024-03-27 22:27:33', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(37, '2024-03-27 22:28:19', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(38, '2024-03-27 22:28:41', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(39, '2024-03-27 22:29:52', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(40, '2024-03-27 22:35:46', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(41, '2024-03-27 22:35:48', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(42, '2024-03-27 23:35:18', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(43, '2024-03-27 23:51:33', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(44, '2024-03-27 23:55:19', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Requested an HK scholar'),
(45, '2024-03-28 14:18:22', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(46, '2024-03-28 18:54:37', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(47, '2024-03-28 18:55:19', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Update profile'),
(48, '2024-03-28 19:00:28', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(49, '2024-03-28 19:01:03', '04-2122-022772', 'Mariano Jemima', 'COM', 'Just log in to the system'),
(50, '2024-03-28 19:01:20', '04-2122-022772', 'Mariano Jemima', 'COM', 'Update profile'),
(51, '2024-03-28 19:08:05', '04-2122-022772', 'Mariano Jemima', 'COM', 'Just log out to the system'),
(52, '2024-03-28 19:08:30', '04-2122-022772', 'Mariano Jemima', 'COM', 'Just log in to the system'),
(53, '2024-03-28 19:09:36', '04-2122-022772', 'Mariano Jemima', 'COM', 'Just log out to the system'),
(54, '2024-03-28 19:11:25', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(55, '2024-03-28 19:11:29', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(56, '2024-03-28 19:13:33', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log in to the system'),
(57, '2024-03-28 19:18:02', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log out to the system'),
(58, '2024-03-28 19:18:13', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log in to the system'),
(59, '2024-03-28 19:20:34', '04-2122-022772', 'Mariano Jemima', 'COA', 'Change credentials'),
(60, '2024-03-28 19:20:45', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log out to the system'),
(61, '2024-03-28 19:20:53', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log in to the system'),
(62, '2024-03-28 19:21:12', '04-2122-022772', 'Mariano Jemima', 'COA', 'Update profile'),
(63, '2024-03-28 19:21:20', '04-2122-022772', 'Mariano Jemima', 'COA', 'Just log out to the system'),
(64, '2024-03-28 19:21:33', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log in to the system'),
(65, '2024-03-28 19:21:36', '04-2122-000777', 'Gaytano Karen May', 'CITE', 'Just log out to the system'),
(66, '2024-03-28 19:36:12', '04-2122-031572', 'Mallorca Reuben', 'CITE', 'Just log in to the system'),
(67, '2024-03-28 19:40:49', '04-2122-031572', 'Mallorca Reuben', 'COA', 'Just log in to the system'),
(68, '2024-03-28 19:51:27', '11-1111-111111', 'Pama Kyle Frances', 'CAHS', 'Just log in to the system');

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `id` int(11) NOT NULL,
  `userName` varchar(255) NOT NULL,
  `adminIdNumber` varchar(255) NOT NULL,
  `passWord` varchar(255) NOT NULL,
  `profilePics` varchar(255) NOT NULL,
  `About` varchar(255) NOT NULL,
  `Phone` varchar(255) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Twitter` varchar(255) NOT NULL,
  `Facebook` varchar(255) NOT NULL,
  `Instagram` varchar(255) NOT NULL,
  `Linkedin` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`id`, `userName`, `adminIdNumber`, `passWord`, `profilePics`, `About`, `Phone`, `Address`, `Email`, `Twitter`, `Facebook`, `Instagram`, `Linkedin`) VALUES
(1, 'Bacabac Jester Paul', '04-1234-1234', '@Jester123', 'serjester.jpg', 'im good', '09876543219', 'Iloilo city', 'Bruce@gmail', 'https://www.facebook.com/jemayyyy', 'https://www.facebook.com/karenmaygaytano', 'https://www.facebook.com/jemayyyy', 'https://www.facebook.com/reuben.mallorca');

-- --------------------------------------------------------

--
-- Table structure for table `hk_assignd_teaecher`
--

CREATE TABLE `hk_assignd_teaecher` (
  `operatikon_ID` varchar(255) NOT NULL,
  `hk_ID` varchar(255) NOT NULL,
  `assigmentID` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hk_assignd_teaecher`
--

INSERT INTO `hk_assignd_teaecher` (`operatikon_ID`, `hk_ID`, `assigmentID`) VALUES
('Gaytano Karen May', '04-2122-031572', 54),
('Gaytano Karen May', '04-2122-000001', 55),
('Gaytano Karen May', '02-2387-700001', 56);

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
  `Status_avail` varchar(255) NOT NULL,
  `status_color` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hk_users`
--

INSERT INTO `hk_users` (`idnum`, `email`, `lname`, `fname`, `password`, `id_totalHours`, `program_course`, `department`, `yrLvL`, `scholarship`, `dutyDesignation`, `dutySupervisor`, `reqiredDuty`, `remaningDuty`, `remDutyMins`, `statsForRenewal`, `SchoolYr`, `semister`, `Status_avail`, `status_color`) VALUES
('02-2387-700001', 'carmilo@gmail.com', 'Flame', 'Carmelo', '', '0', 'BSCE', 'COME', '4', 'HK100', 'SF', 'Gaytano Karen May', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2200-90001', 'Dionar@gmail.com', 'Antioquia', 'Dionard', '', '0', 'BSHM', 'COA', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-000002', 'donna@gmail.com', 'Mallorca', 'Donna', '', '0', 'BSBA', 'COM', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-000001', 'jasper@gmail.com', 'operio', 'jasper', '', '0', 'BSIT', 'CITE', '3', 'HK100', 'SF', 'Gaytano Karen May', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-78627', 'Javelosa@gmail.com', 'Javelosa ', 'Wolf', '', '0', 'BSC', 'CCJE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-91734', 'jimama@gmail.com', 'Mariano', 'Jemima', '', '0', 'BSBA', 'CAS', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2002-90021', 'justin@gmail.com', 'Susal', 'Justiene', '', '0', 'BSCE', 'CHAS', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035512', 'karenmay@gmail.com', 'Gaytano', 'Karen May', '', '0', 'BSIT', 'CITE', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035546', 'kylepama@gnail.cute', 'Pama', 'Kayle', '', '0', 'BSBA', 'CAS', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('09-2155-90828', 'malo@gmail.com', 'Amante', 'Malorena', '', '0', 'BSHM', 'CAHS', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1234-87237', 'Pechera@gamil.com', 'Pechera', 'Alessandra', '', '0', 'BSBS', 'COE', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031572', 'ream.mallorca.ui@phinmaed.com', 'Mallorca', 'Reuben', '', '1', 'BSIT', 'CITE', '1', 'HK75', 'AF', 'Gaytano Karen May', '180', '0', '0.0', 'Complete', '2023 - 2024', 'FIRST SEMESTER', 'Na', 'success'),
('04-2122-000003', 'ryan@gmail.com', 'Mallorca', 'Ryan', '', '0', 'BSCE', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning');

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
  `status_ol` varchar(255) NOT NULL,
  `color_status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `operations_data`
--

INSERT INTO `operations_data` (`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`, `profilePics`, `operations_about`, `twitter`, `facebook`, `instagram`, `linkedin`, `Address`, `status_ol`, `color_status`) VALUES
('Gaytano', 'Karen May', '$2b$12$2Y0s48Qxz1qKEYrMULbmFuMN9mnhO64AIJRw/93C2SEunafhGMaEq', '04-2122-000777', 'CITE', 'G', '09948486859', 'Super Cute', 'karenmaygaytano@gmail.com', 'KARENS.jpg', '', '', '', '', '', '', 'INACTIVE', 'danger'),
('Mariano', 'Jemima', '$2b$12$TKL1UrSENeGpc71Fwu9PzuBugGEKB/LMUzz/xlesk.Ap9jxqT9Ol.', '04-2122-022772', 'COA', 'G', '09476959407', 'Chairman', 'Jemima@gmail.com', 'jemProfile.jpg', '', '', '', '', '', '', 'INACTIVE', 'danger'),
('Mallorca', 'Reuben', '$2b$12$xUvJ73XI5Vfz1DwKT5rSt.9ohLSlKuHSXg/PWZW0Rzo4qzcFjLoxO', '04-2122-031572', 'COA', 'A', '09948486859', 'COO', 'ream.mallorca.ui@phinmaed.com', '', '', '', '', '', '', '', 'ACTIVE', 'success'),
('Pama', 'Kyle Frances', '$2b$12$N0yUdmSnFzTFStKvLDYu1.vf0Bw781c.hrDPPuR5w8m5/bnY7fCSK', '11-1111-111111', 'CAHS', 'P', '09476959407', 'Chairman', 'kylepama@gnail.cute', '', '', '', '', '', '', '', 'ACTIVE', 'success');

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `operation_request`
--

INSERT INTO `operation_request` (`Designation`, `Requirements`, `Report Day/s`, `Request`, `DEPT`, `SUPERVISOR`, `ID`) VALUES
('SF', '1', 'Mon-Tues', '1', 'CITE', 'Gaytano Karen May', 25);

-- --------------------------------------------------------

--
-- Table structure for table `opertaion_req_acc`
--

CREATE TABLE `opertaion_req_acc` (
  `Faculty_Lname` varchar(255) NOT NULL,
  `Faculty_Fname` varchar(255) NOT NULL,
  `Faculty_Password` varchar(255) NOT NULL,
  `Faculty_Id_Number` varchar(255) NOT NULL,
  `Operation_Dept` varchar(255) NOT NULL,
  `Operations_Mname` varchar(255) NOT NULL,
  `Operation_phone_Number` varchar(255) NOT NULL,
  `Operation_Designation-Position` varchar(255) NOT NULL,
  `Operations_Email` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `reports/announcement`
--

INSERT INTO `reports/announcement` (`content`, `date`, `time`, `adminName`, `id`) VALUES
('        Duty Assignments the Upcoming for Week Announce', '2024-02-22', '8:43', 'admin', 5),
('        sir robert calasar ikaw gina pa tawag sa csdl kadto d mga 3 pm d ka ma late ha manda kalang', '2024-02-22', '10:28', 'admin', 6),
('  DUTY HOURS EXTENDED      ', '2024-03-08', '15:3', 'Jester Paul Bacabac', 11);

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scholar_duty_records`
--

INSERT INTO `scholar_duty_records` (`date`, `Hours_In_Out`, `Minutes_In_Out`, `Student_id_Number`, `id`, `Type_of_Process`) VALUES
('2024-03-28', 11, 52, '04-2122-031572', 296, 'IN'),
('2024-03-28', 11, 53, '04-2122-031572', 297, 'OUT');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `active_logs`
--
ALTER TABLE `active_logs`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `opertaion_req_acc`
--
ALTER TABLE `opertaion_req_acc`
  ADD PRIMARY KEY (`Faculty_Id_Number`);

--
-- Indexes for table `reports/announcement`
--
ALTER TABLE `reports/announcement`
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
-- AUTO_INCREMENT for table `active_logs`
--
ALTER TABLE `active_logs`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hk_assignd_teaecher`
--
ALTER TABLE `hk_assignd_teaecher`
  MODIFY `assigmentID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `operation_request`
--
ALTER TABLE `operation_request`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `reports/announcement`
--
ALTER TABLE `reports/announcement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `scholar_duty_records`
--
ALTER TABLE `scholar_duty_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=298;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
