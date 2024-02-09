-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 22, 2023 at 09:45 AM
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
(1, 'admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `dutyhourformulationdata`
--

CREATE TABLE `dutyhourformulationdata` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `timeIn` varchar(255) NOT NULL,
  `timeOut` varchar(255) NOT NULL,
  `totaldutyHours` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dutyhourformulationdata`
--

INSERT INTO `dutyhourformulationdata` (`id`, `email`, `timeIn`, `timeOut`, `totaldutyHours`) VALUES
(22, 'ream.mallorca.ui@phinmaed.com', '0:36', '1:13', '37'),
(23, 'karenmay@gmail.com', '1:15', '1:16', '1'),
(24, 'jimama@gmail.com', '', '', '0'),
(25, 'kylepama@gnail.cute', '1:17', '', '0');

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
  `id_totalHours` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hk_users`
--

INSERT INTO `hk_users` (`idnum`, `email`, `lname`, `fname`, `password`, `id_totalHours`) VALUES
('04-2122-035546', 'jimama@gmail.com', 'Jemima', 'Mariano', 'mariano09', 22),
('04-2122-035512', 'karenmay@gmail.com', 'Gaytano', 'Karen', 'Gaytano@13', 23),
('04-2122-031675', 'kylepama@gnail.cute', 'Kyle', 'Pama', 'pama@12', 24),
('04-2122-031572', 'ream.mallorca.ui@phinmaed.com', 'Mallorca', 'Reuben', 'reubencute', 25);

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `email` varchar(255) NOT NULL,
  `timeIn` varchar(255) NOT NULL,
  `timeOut` varchar(255) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `request`
--

INSERT INTO `request` (`email`, `timeIn`, `timeOut`, `id`) VALUES
('ream.mallorca.ui@phinmaed.com', '11:34', '11:34', 7),
('ream.mallorca.ui@phinmaed.com', '13:34', '13:34', 8),
('ream.mallorca.ui@phinmaed.com', '14:03', '14:03', 9);

-- --------------------------------------------------------

--
-- Table structure for table `timeintimeout`
--

CREATE TABLE `timeintimeout` (
  `TinToutgmail` varchar(255) NOT NULL,
  `TinToutdate` varchar(255) NOT NULL,
  `TimeOut` varchar(255) NOT NULL,
  `TimeIn` varchar(255) NOT NULL,
  `id_timInTimeOut` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `timeintimeout`
--

INSERT INTO `timeintimeout` (`TinToutgmail`, `TinToutdate`, `TimeOut`, `TimeIn`, `id_timInTimeOut`) VALUES
('ream.mallorca.ui@phinmaed.com', '2023-10-22', '1:13', '0:36', 20),
('karenmay@gmail.com', '2023-10-22', '1:16', '1:15', 21),
('kylepama@gnail.cute', '2023-10-22', '', '1:17', 22);

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
-- Indexes for table `hk_users`
--
ALTER TABLE `hk_users`
  ADD PRIMARY KEY (`email`),
  ADD UNIQUE KEY `idnum` (`idnum`),
  ADD KEY `id_totalHours` (`id_totalHours`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `timeintimeout`
--
ALTER TABLE `timeintimeout`
  ADD PRIMARY KEY (`id_timInTimeOut`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `dutyhourformulationdata`
--
ALTER TABLE `dutyhourformulationdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `timeintimeout`
--
ALTER TABLE `timeintimeout`
  MODIFY `id_timInTimeOut` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
