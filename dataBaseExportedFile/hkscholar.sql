-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 29, 2024 at 10:30 AM
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
(95, '2024-03-29 08:06:05', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(96, '2024-03-29 08:07:14', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(97, '2024-03-29 08:12:49', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(98, '2024-03-29 08:12:55', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(99, '2024-03-29 08:27:21', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(100, '2024-03-29 08:27:57', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(101, '2024-03-29 08:37:55', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(102, '2024-03-29 08:40:01', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(103, '2024-03-29 08:40:35', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(104, '2024-03-29 08:43:14', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(105, '2024-03-29 08:43:23', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(106, '2024-03-29 08:44:55', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(107, '2024-03-29 08:46:11', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(108, '2024-03-29 08:47:10', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(109, '2024-03-29 08:47:29', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(110, '2024-03-29 08:48:16', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(111, '2024-03-29 08:49:36', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(112, '2024-03-29 08:49:49', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(113, '2024-03-29 08:49:56', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(114, '2024-03-29 09:00:50', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(115, '2024-03-29 09:02:21', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log out to the system'),
(116, '2024-03-29 09:10:21', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(117, '2024-03-29 09:39:00', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Requested an HK scholar'),
(118, '2024-03-29 09:47:38', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(119, '2024-03-29 09:48:29', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(120, '2024-03-29 09:49:37', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(121, '2024-03-29 09:50:19', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(122, '2024-03-29 09:57:16', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(123, '2024-03-29 11:06:03', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Just log in to the system'),
(124, '2024-03-29 11:33:20', 'UI-22-167-F', 'Parel Kurt', 'CITE', 'Update profile'),
(125, '2024-03-29 11:33:29', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Update profile'),
(126, '2024-03-29 11:34:04', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(127, '2024-03-29 13:08:12', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(128, '2024-03-29 14:04:38', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log out to the system'),
(129, '2024-03-29 16:40:32', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(130, '2024-03-29 16:40:48', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log out to the system'),
(131, '2024-03-29 16:41:49', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(132, '2024-03-29 16:42:05', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar'),
(133, '2024-03-29 16:42:20', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar'),
(134, '2024-03-29 16:42:36', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log out to the system'),
(135, '2024-03-29 16:44:07', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(136, '2024-03-29 17:08:09', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar'),
(137, '2024-03-29 17:14:31', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar'),
(138, '2024-03-29 17:17:02', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar'),
(139, '2024-03-29 17:21:41', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log out to the system'),
(140, '2024-03-29 17:21:45', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Just log in to the system'),
(141, '2024-03-29 17:23:32', 'UI-22-167-F', 'Parel Kurt Ellie', 'CITE', 'Requested an HK scholar');

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
(1, 'Bacabac Jester Paul', '04-1234-1234', '@Jester1234', 'serjester.jpg', 'im good', '09876543219', 'Iloilo city', 'Bruce@gmail', 'https://www.facebook.com/jemayyyy', 'https://www.facebook.com/karenmaygaytano', 'https://www.facebook.com/jemayyyy', 'https://www.facebook.com/reuben.mallorca');

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
('Parel Kurt', '04-2122-031572', 58),
('Parel Kurt Ellie', '04-1920-02837', 59),
('Parel Kurt Ellie', '04-1920-02836', 60),
('Parel Kurt Ellie', '04-2122-14569', 61),
('Parel Kurt Ellie', '04-2122-000001', 62),
('Parel Kurt Ellie', '04-2122-59333', 63),
('Parel Kurt Ellie', '04-2122-59433', 64),
('Parel Kurt Ellie', '04-1920-04122', 65),
('Parel Kurt Ellie', '04-2122-78627', 66);

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
('04-2122-045729', 'abegail@gmail.com', 'Pang-al', 'Abegail', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02832', 'addie@gmail.com', 'Gaytano', '\r\nAddie', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2120-02883', 'adrian@gmail.com', 'Quia', 'Adrian', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59333', 'albina@gmail.com', 'Sacapno', 'Albina', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-54863', 'alden@gmail.com', 'Alde', 'Rochielle', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-85249', 'aldric@gmail.com', 'Richard', 'Alden', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2120-02863', 'alex@gmail.com', 'Gonzaga', 'Alex', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02436', 'aljur@gmail.com', 'Abrenica', 'Aljur', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04593', 'almarzora@gmail.com', 'Almazora', 'Ridjez Jhann ', '@jhohn', '0', 'Bachelor of Science in Tourism Management', 'COM', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14479', 'alonzo@gmail.com', 'Muhlach', 'Alonzo', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14659', 'alyssa@gmail.com', 'Valdez', 'Alyssa', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-032809', 'amaquin@gmail.com', 'Amaquin', 'Argie', '@Amaquin', '0', 'Bachelor of Science in Business Administration', 'COM', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034305	', 'anam@gmail.com', 'Anam', 'Arvie Ann', '@Anamamm', '0', 'Bachelor of Science in Business Administration', 'COM', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031370	', 'anaud@gmail.com', 'Anaud', 'Jolyn', '@Anaudd', '0', 'Bachelor of Science in Business Administration', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59343', 'andrew@gmail.com', 'Sacapano', 'Andrew', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1617-05234	', 'antioquia@gmail.com', 'Antioquia', 'Dionard', '@Dionard123', '0', 'Bachelor of Science in Business Administration', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2021-02572	', 'aragorata@gmail.com', 'Aragorat', 'Kim Raxamm', '@Raxamm123', '0', 'Bachelor of Science in Business Administration', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02837', 'arthur@gmail.com', 'Nery', '\r\nArthur', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-52863', 'belen@gmail.com', 'Gregorio', 'Belen', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-030617', 'bernaalfonso@gmail.com', 'Alfonso', 'Bernadeth', '@berna', '0', 'Bachelor of Science in Hospitality Management', 'COM', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-032061', 'biboso@gmmail.com', 'Biboso', 'Rona Mae', '@Ronamae', '0', 'Bachelor of Science in Tourism Management', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2120-02963', 'bonnie@gmail.com', 'Onnie', 'Bonnie', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59433', 'buday@gmail.com', 'Mariano', 'Gem', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-031410', 'bunagan@gmmail.com', 'Bunagan', 'Sean Carlo', '@Seancarlo', '0', 'Bachelor of Science in Tourism Management', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1617-01658', 'buslon@gmmail.com', 'Buslon', 'Ai Xylnn', '@Buslon123', '0', 'Bachelor of Science in Tourism Management', 'COM', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034824', 'calatana@gmmail.com', 'Calatana', 'Allyna Treyes', '@Calatana123', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1516-01987', 'capanang@gmmail.com', 'Capanang', 'Joepeth', '@Capanang123', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02635', 'carladrias@gmail.com', 'Adrias', 'Carl Justin', '@Carladrias', '0', 'Bachelor of Science in Hospitality Management', 'COM', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034271', 'carlon@gmmail.com', 'Capanang', 'Carl Anthony', '@Anthony123', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('02-2387-700001', 'carmelo@gmail.com', 'Flame', 'Carmelo', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1819-04346', 'castor@gmail.com', 'Castor', 'Eden Kervie', '', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-88349', 'charles@gmail.com', 'Coning', 'Charles ', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14459', 'cj@gmail.com', 'Delos Dez', 'Cj', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2220-01831', 'clarie@gmail.com', 'Sivana', 'Clarie', '', '0', '\r\nBachelor of Science in Nursing', 'CAHS\r\n', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02833', 'collin@gmail.com', 'Carson', '\r\nKollin', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1819-05025', 'cornel@gmail.com', 'Cornel', 'Eddie', '', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02843', 'cristine@gmail.com', 'Gabinete', '\r\nCristine', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04232', 'dacalos@gmail.com', 'Dacalos', 'Eljohn Ray', '', '0', 'Bachelor of Science in Tourism Management', 'COM', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2231-01836', 'daisy@gmail.com', 'Lamboya', 'Daisy', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02636', 'daniel@gmail.com', 'Padilla', 'Daniel', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14739', 'daren@gmail.com', 'Gado', 'Daren', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14569', 'dave@gmail.com', 'Ildefonso', 'Dave', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-035939', 'david@gmail.com', 'Patricio', 'David', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-000002', 'donna@gmail.com', 'Mallorca', 'Donna', '', '0', 'Bachelor of Science in Tourism Management', 'COM', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04122', 'edwin@gmail.com', 'Jaytano', 'Edwin', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '1', 'HK50', 'Student Facilitator', 'Parel Kurt Ellie', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-033129', 'eleferia@gmail.com', 'Eleferia', 'John Carl', '', '0', 'Bachelor of Science in Business Administration', 'COM', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-24839', 'elmo@gmail.com', 'Luces', 'Elmo', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-001010', 'embon@gmail.com', 'Embon', 'Farah', '', '0', 'Bachelor of Science in Business Administration', 'COM', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2210-01831', 'emie@gmail.com', 'Gidote', 'Emie', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-01222', 'enrico@gmail.com', 'Soriano', 'Enrico', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02446', 'enrique@gmail.com', 'Gil', 'Enrique', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02632', 'faith@gmail.com', 'Nazareno', 'Faith', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '3', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('	\r\n04-1920-02832', 'flor@gmail.com', 'Bacusa', 'Flor', '', '0', 'Bachelor of Science in Nursing', '\r\nCAHS', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-25939', 'glendale@gmail.com', 'Pandinio', 'Glendale', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-24939', 'jake@gmail.com', 'Sastre', 'Jake', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02222', 'james@gmail.com', 'Bond', 'James', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '2', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02422', 'jamesong@gmail.com', 'Reid', 'James', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '2', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2231-51836', 'janela@gmail.com', 'Huam', 'Janela', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-000001', 'jasper@gmail.com', 'Operio', 'Jasper', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK100', '', '', '180', '180', '0.0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-78627', 'Javelosa@gmail.com', 'Javelosa ', 'Wolf', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '1', 'HK100', 'Student Facilitator', 'Parel Kurt Ellie', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-2122-045839', 'jayar@gmail.com', 'Pagsagan', 'Jayar', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-13479', 'jc@gmail.com', 'Delos Santos', 'Jc', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14759', 'jema@gmail.com', 'Galanza', 'Jema', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034719', 'jennifer@gmail.com', 'Perez', 'Jennifer', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2211-01831', 'jernie@gmail.com', 'Ortega', 'Jernie', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14839', 'jhonrei@gmail.com', 'Sacapano', 'Jhonrei', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-91734', 'jimama@gmail.com', 'Mariano', 'Jemima', '', '0', 'Bachelor of Science in Pharmacy', 'CAHS', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035338', 'jimanga@gmail.com', 'Jimanga', 'Jose', '', '0', 'Bachelor of Secondary Education', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04312', 'jimenez@gmail.com', 'Jimenez', 'Missy', '', '0', 'Bachelor of Secondary Education', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-54643', 'jocel@gmail.com', 'Overio', 'Jocel', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2231-01832', 'jocelan@gmail.com', 'Espena', 'Jocel', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2121-02968', 'jolina@gmail.com', 'Magdangal', 'Jolina', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-23939', 'jomel@gmail.com', 'Flores', 'Jomel', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2002-90021', 'justin@gmail.com', 'Susal', 'Justiene', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035512', 'karenmay@gmail.com', 'Gaytano', 'Karen May', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-145859', 'kenneth@gmail.com', 'Tio', 'Kenneth', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-88249', 'kiana@gmail.com', 'Coning', '\r\nKiana', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02836', 'kiddie@gmail.com', 'Santos', 'Kiddie', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'Na', 'warning'),
('04-1920-04442', 'kim@gmail.com', 'Gonzaga', 'Kim', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-145829', 'kimmy@gmail.com', 'Dionasa', 'Kimmy', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04342', 'kingston@gmail.com', 'Gobaga', 'Kingston', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02432', 'kurts@gmail.com', 'Panganiban', 'Kurts', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '2', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035546', 'kylepama@gnail.cute', 'Pama', 'Kyle Francis', '', '0', 'Bachelor of Arts in Psychology', 'CAHS', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023 - 2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031565', 'legario@gmail.com', 'Legario', 'Karen Joy', '', '0', 'Bachelor of Science in Business Administration', 'COM', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035839', 'leoandro@gmail.com', 'Bondo', 'Leoandro', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-032560', 'luna@gmail.com', 'Luna', 'Hazel', '', '0', 'Bachelor of Science in Business Administration', 'COM', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('09-2155-90828', 'malo@gmail.com', 'Amante', 'Malorena', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '1', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-04222', 'mark@gmail.com', 'Gaytano', 'Mark', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '1', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-35249', 'marko@gmail.com', 'Huston', 'Marko', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2121-02963', 'marvin@gmail.com', 'Agustin', 'Marvin', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59533', 'maxine@gmail.com', 'Medina', 'Maxine', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02883', 'meg@gmail.com', 'Solanoy', 'Meg', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59534', 'mic@gmail.com', 'Villacorte', 'Mic', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-145729', 'miccayl@gmail.com', 'Pang-al', 'Miccay', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031653', 'nakpil@gmail.com', 'Nakpil', 'Marc Dave', '', '0', 'Bachelor of Science in Business Administration', 'COM', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-02963', 'nick@gmail.com', 'Villanueva', 'Nick', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02532', 'nicole@gmail.com', 'Parel', 'Nicole', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '3', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035729', 'novie@gmail.com', 'Galliano', 'Novie', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-030723', 'nulada@gmail.com', 'Nulada', 'Richen', '', '0', 'Bachelor of Science in Accountancy', 'COA', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-88649', 'omar@gmail.com', 'Coning', 'Omar', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-032086', 'palaez@gmail.com', 'Palaez', 'Benz', '', '0', 'Bachelor of Science in Accountancy', 'COA', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-030506', 'pareja@gmail.com', 'Parejas', 'Doji', '', '0', 'Bachelor of Science in Accountancy', 'COA', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-033804', 'paulino@gmail.com', 'Paulino', 'Eunice', '', '0', 'Bachelor of Science in Accountancy', 'COA', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1234-87237', 'Pechera@gamil.com', 'Pechera', 'Alessandra', '', '0', 'Bachelor of Science in Marine Engineering\r\n', 'COME', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-54943', 'pia@gmail.com', 'Casidsid', 'Pia', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-15479', 'Queenie@gmail.com', 'Delos Reyes', 'Queenie', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-25949', 'ralph@gmail.com', 'Susang', 'Ralph', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-02863', 'randy@gmail.com', 'Santiago', 'Randy', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031572', 'ream.mallorca.ui@phinmaed.com', 'Mallorca', 'Reuben', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '1', 'HK75', '', '', '180', '0', '0', 'Complete', '2023 - 2024', 'FIRST SEMESTER', 'Na', 'success'),
('04-1920-03635', 'regine@gmail.com', 'Onatyag', 'Regine', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '3', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02839', 'rico@gmail.com', 'Blangko', 'Rico', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '1', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-59323', 'rjames@gmail.com', 'Meren', 'Rjames', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2121-32963', 'robert@gmail.com', 'Guillano', 'Robert', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031574', 'rodriguez@gmail.com', 'Rodriguez', 'Mark Angelo', '', '0', 'Bachelor of Science in Accountancy', 'COA', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2220-02832', 'romely@gmail.com', 'Manuel', 'Romely', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2220-02831', 'ronalyn@gmail.com', 'Haylo', 'Ronalyn', '', '0', '\r\n\r\nBachelor of Science in Nursing', 'CAHS', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-000003', 'ryan@gmail.com', 'Mallorca', 'Ryan', '', '0', 'Bachelor of Secondary Education', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-031327', 'salaya@gmail.com', 'Salaya', 'Eric', '', '0', 'Bachelor of Science in Accountancy', 'COA', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-01024', 'salvacion@gmail.com', 'Salacion', 'Daniel', '', '0', 'Bachelor of Science in Accountancy', 'COA', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035251', 'santillana@gmail.com', 'Santillana', 'Dj Mae', '', '0', 'Bachelor of Science in Accountancy', 'COA', '3', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-032649', 'sarona@gmail.com', 'Sarona', 'Jhon Rey', '', '0', 'Bachelor of Science in Accountancy', 'COA', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034238', 'seblante@gmail.com', 'Seblante', 'Stephanie', '', '0', 'Bachelor of Science in Accountancy', 'COA', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-001443', 'segovia@gmail.com', 'Segovia', 'Angela', '', '0', 'Bachelor of Elementary Education', 'COED', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-54963', 'shane@gmail.com', 'Hamasa', 'Shane', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-14469', 'shaun@gmail.com', 'Ildefonso', 'Shaun', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034729', 'Shiela@gmail.com', 'Flores', 'Shiela', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '2', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034222', 'sibidong@gmail.com', 'Sibidong', 'Jyseth', '', '0', 'Bachelor of Science in Accountancy', 'COA', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-035230', 'sicatin@gmail.com', 'Sicatin', 'Justine Carl', '', '0', 'Bachelor of Elementary Education', 'COED', '1', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034150', 'siva@gmail.com', 'Siva', 'Davien', '', '0', 'Bachelor of Secondary Education', 'COED', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-01489', 'sumbe@gmail.com', 'Sumbe', 'Jhon Rey', '', '0', 'Bachelor of Secondary Education', 'COED', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-00805', 'tabarnero@gmail.com', 'Tabarnero', 'Mary Grace', '', '0', 'Bachelor of Secondary Education', 'COED', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-001114', 'tahum@gmail.com', 'Tahum', 'Romea', '', '0', 'Bachelor of Secondary Education', 'COED', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-045739', 'tim@gmail.com', 'Marquez', 'Tim', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '4', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-01843', 'tin@gmail.com', 'Labindao\r\n', 'Tin', '', '0', 'Bachelor of Science in Civil Engineering', 'COE', '2', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-1920-02736', 'tony@gmail.com', 'Labrosca\r\n', '\r\nTony', '', '0', 'Bachelor of Science in Criminology', 'CCJE', '4', 'HK100', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-145869', 'tyler@gmail.com', 'Chou', 'Tyler', '', '0', 'Bachelor of Science in Information Technology', 'CITE', '3', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-034379', 'velasco@gmail.com', 'Velasco', 'Mylene', '', '0', 'Bachelor of Secondary Education', 'COED', '3', 'HK25', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-030973', 'villanueve@gmail.com', 'Villanueva', 'James Mathew', '', '0', 'Bachelor of Secondary Education', 'COED', '4', 'HK50', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-58343', 'zach@gmail.com', 'Fernandez', 'Zach', '', '0', 'Bachelor of Science in Nursing', 'CAHS', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning'),
('04-2122-25249', 'zember@gmail.com', 'Pantia', 'Zember', '', '0', 'Bachelor of Science in Marine Engineering', 'COME', '2', 'HK75', '', '', '180', '180', '0', 'pending', '2023-2024', 'FIRST SEMESTER', 'av', 'warning');

-- --------------------------------------------------------

--
-- Table structure for table `hk_user_activelogs`
--

CREATE TABLE `hk_user_activelogs` (
  `id` int(11) NOT NULL,
  `date_time` varchar(255) NOT NULL,
  `hk_id` varchar(255) NOT NULL,
  `hk_name` varchar(255) NOT NULL,
  `dept` varchar(255) NOT NULL,
  `act_perm` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
  `operations_about` varchar(2555) NOT NULL,
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
('Parel', 'Kurt Ellie', '$2b$12$jpQ2KAxM9YkGXNdJ4LTXbO68.u5gex5TJUtX41hAXgUXSaM0QHDXO', 'UI-22-167-F', 'CITE', 'E', '09876543219', 'Faculty', 'kurt.parel.ui@phinmaed.com', 'ser.jpg', ' IT instructor passionate about empowering individuals with the knowledge and skills needed to thrive in the dynamic world of technology.', 'https://www.facebook.com/kurt.parel', 'https://www.facebook.com/kurt.parel', 'https://www.facebook.com/kurt.parel', 'https://www.facebook.com/kurt.parel', 'ILOILO CITY MANDORIAO', 'ACTIVE', 'success');

-- --------------------------------------------------------

--
-- Table structure for table `operation_feedback`
--

CREATE TABLE `operation_feedback` (
  `id_feed` int(11) NOT NULL,
  `feedMess` varchar(255) NOT NULL,
  `feed_name` varchar(255) NOT NULL,
  `feed_date` varchar(255) NOT NULL,
  `feed_pic` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `operation_feedback`
--

INSERT INTO `operation_feedback` (`id_feed`, `feedMess`, `feed_name`, `feed_date`, `feed_pic`) VALUES
(3, 'I like the system interface its very easy to use and understand', 'KURT PAREL', '2024-03-29 09:11', 'ser.jpg');

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

--
-- Dumping data for table `opertaion_req_acc`
--

INSERT INTO `opertaion_req_acc` (`Faculty_Lname`, `Faculty_Fname`, `Faculty_Password`, `Faculty_Id_Number`, `Operation_Dept`, `Operations_Mname`, `Operation_phone_Number`, `Operation_Designation-Position`, `Operations_Email`) VALUES
('Mondia', 'Zesty', '$2b$12$ljb6UYc9A7ijJ.VKZRt/oeqbCCimrDCoAoymZ0oeKqZkceOxxAO46', 'UI-19-117-F', 'CITE', 'G', '09476959407', 'Faculty', 'zesty.mondia.ui@phinmaed.com'),
('Calasara', 'Robert', '$2b$12$LqeyiTb3zlV61jP7iEsx4.WiUuJC6jGSFJWLswZMo.aWmjRT2fFtS', 'UI-19-120-F', 'CITE', 'J', '09876543219', 'Faculty', 'robert.calasara.ui@phinmaed.com');

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
('Exciting news for all aspiring Python programmers! ????\r\n\r\nWe are thrilled to announce the launch of our brand new Python Programming Course, designed to kickstart your journey into the world of coding.', '2024-03-29', '10:0', 'Bacabac Jester Paul', 15);

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
-- Indexes for table `hk_user_activelogs`
--
ALTER TABLE `hk_user_activelogs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `operations_data`
--
ALTER TABLE `operations_data`
  ADD PRIMARY KEY (`Faculty_Id_Number`);

--
-- Indexes for table `operation_feedback`
--
ALTER TABLE `operation_feedback`
  ADD PRIMARY KEY (`id_feed`);

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
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=142;

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `hk_assignd_teaecher`
--
ALTER TABLE `hk_assignd_teaecher`
  MODIFY `assigmentID` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=67;

--
-- AUTO_INCREMENT for table `hk_user_activelogs`
--
ALTER TABLE `hk_user_activelogs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `operation_feedback`
--
ALTER TABLE `operation_feedback`
  MODIFY `id_feed` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `operation_request`
--
ALTER TABLE `operation_request`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `reports/announcement`
--
ALTER TABLE `reports/announcement`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `scholar_duty_records`
--
ALTER TABLE `scholar_duty_records`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=309;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
