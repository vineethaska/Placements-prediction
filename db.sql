/*
SQLyog Community v11.52 (32 bit)
MySQL - 5.5.30 : Database - placement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`placement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `placement`;

/*Table structure for table `dataset` */

DROP TABLE IF EXISTS `dataset`;

CREATE TABLE `dataset` (
  `CodingSkills` varchar(100) DEFAULT NULL,
  `AptitudeSkills` varchar(100) DEFAULT NULL,
  `TechnicalSkills` varchar(100) DEFAULT NULL,
  `CommunicationSkills` varchar(100) DEFAULT NULL,
  `PresentationSkills` varchar(100) DEFAULT NULL,
  `AcademicPerformance` varchar(100) DEFAULT NULL,
  `EnglishProficiency` varchar(100) DEFAULT NULL,
  `ProgrammingSkills` varchar(100) DEFAULT NULL,
  `ManagementSkills` varchar(100) DEFAULT NULL,
  `Projects` varchar(100) DEFAULT NULL,
  `Internships` varchar(100) DEFAULT NULL,
  `Placed` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `name` varchar(100) DEFAULT NULL,
  `stdid` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `mno` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
