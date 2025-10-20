-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: syngenta_connect
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin_account`
--

DROP TABLE IF EXISTS `admin_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin_account` (
  `admin_id` int NOT NULL AUTO_INCREMENT,
  `admin_email` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `admin_username` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `admin_password` varchar(512) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`admin_id`),
  KEY `admin_email` (`admin_email`)
) ENGINE=InnoDB AUTO_INCREMENT=23413 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin_account`
--

LOCK TABLES `admin_account` WRITE;
/*!40000 ALTER TABLE `admin_account` DISABLE KEYS */;
INSERT INTO `admin_account` VALUES (12312,'haitamhsat899@gmail.com','haitam','scrypt:32768:8:1$Pu7RofDknhdjZMRT$b93c3a12ab11d05502698c03d1d51a5b40b70da87e6745ed6fbea4d4905e23eeed9e229c2bd3a62bb114c40e5eba972cd3a91a3d54c58f6d471b9fa677a46a50',1);
/*!40000 ALTER TABLE `admin_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('453590eff1e2');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `asset_existence`
--

DROP TABLE IF EXISTS `asset_existence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `asset_existence` (
  `employee_id` int NOT NULL,
  `asset_serial` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `existence` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `first_scan_date` date DEFAULT NULL,
  `last_scan_date` date DEFAULT NULL,
  `scan_counter` int DEFAULT NULL,
  PRIMARY KEY (`employee_id`,`asset_serial`),
  KEY `asset_serial` (`asset_serial`),
  CONSTRAINT `asset_existence_ibfk_1` FOREIGN KEY (`asset_serial`) REFERENCES `employee_assets` (`asset_serial`),
  CONSTRAINT `asset_existence_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `asset_existence`
--

LOCK TABLES `asset_existence` WRITE;
/*!40000 ALTER TABLE `asset_existence` DISABLE KEYS */;
INSERT INTO `asset_existence` VALUES (9999,'75QPVV3','Exist','2025-08-25','2025-08-25',1),(12320,'5CG024BK30','Exist','2025-09-13','2025-10-06',12),(13371,'H2QPVV3','Exist','2025-08-28','2025-08-28',1),(20202,'12H12HKLMNI','Exist','2025-07-10','2025-07-10',1),(22134,'12HQ30BM1','Exist','2025-07-08','2025-07-09',23),(22222,'D52S9K3','Exist','2025-07-10','2025-07-10',5),(32421,'3B123331H','Exist','2025-07-01','2025-08-25',64),(33123,'2MLSN32QPR','Exist','2025-07-10','2025-07-10',1),(89123,'5CG024BK50','Exist','2025-07-09','2025-07-09',1),(606012,'3B122121H','Exist','2025-10-11','2025-10-11',15);
/*!40000 ALTER TABLE `asset_existence` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_assets`
--

DROP TABLE IF EXISTS `employee_assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_assets` (
  `asset_serial` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_id` int DEFAULT NULL,
  `asset_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_using_date` date DEFAULT NULL,
  `last_using_date` date DEFAULT NULL,
  PRIMARY KEY (`asset_serial`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `employee_assets_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_assets`
--

LOCK TABLES `employee_assets` WRITE;
/*!40000 ALTER TABLE `employee_assets` DISABLE KEYS */;
INSERT INTO `employee_assets` VALUES ('12H12HKLMNI',20202,'HP_EliteBook_840_G7','2024-01-03',NULL),('12HQ30BM1',22134,'Laptop','2022-03-17',NULL),('2MLSN32QPR',33123,'Tablet','2022-02-01',NULL),('3B122121H',606012,'HP EliteBook 840 G7','2024-10-14',NULL),('3B123331H',32421,'Monitor','2020-12-01',NULL),('5CG024BK30',12320,'Dell Laltitude 5330','2025-09-13',NULL),('5CG024BK50',89123,'HP_EliteBook_840_G6','2024-02-03',NULL),('75QPVV3',9999,'Dell Latitude 5420','2025-07-10',NULL),('D52S9K3',22222,'Dell Latitude 5420','2025-07-11',NULL),('H2QPVV3',13371,'Dell Latitude 5430','2020-02-19',NULL);
/*!40000 ALTER TABLE `employee_assets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `employee_id` int NOT NULL AUTO_INCREMENT,
  `employee_fullname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `employee_email` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `employee_email` (`employee_email`)
) ENGINE=InnoDB AUTO_INCREMENT=606013 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1111,'John Snow','johnsnow32@gmail.com'),(9999,'Barak obama','barakobama121@gmail.com'),(12320,'abdellah laaroui','abdellahlaroui90@gmail.com'),(12345,'Ayoub amhaouch','ayoubamhaouch123@gmail.com'),(13371,'Mohamed Hassan Chadili','mohammedhassan99@gamil.com'),(20202,'mehdi ayoub','mehdiayoub123@gmail.com'),(22134,'mohammed ayoub','mohammedayoub322@gmail.com'),(22222,'Brahim Essafi','brahimessafi323@gmail.com'),(32421,'AYOUB HSA','ayoubhsa213@gmail.com'),(33123,'adam filali','adamfilali32@gmail.com'),(89123,'Zainab Kheir','ZainabKheir123@gmail.com'),(606012,'Othman Oussaid','othmanoussaid79@gmail.com');
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_user_account`
--

DROP TABLE IF EXISTS `temp_user_account`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_user_account` (
  `temp_user_id` int NOT NULL,
  `temp_user_password` varchar(512) COLLATE utf8mb4_unicode_ci NOT NULL,
  `is_user` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`temp_user_id`),
  CONSTRAINT `temp_user_account_ibfk_1` FOREIGN KEY (`temp_user_id`) REFERENCES `temp_user_informations` (`temp_user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_user_account`
--

LOCK TABLES `temp_user_account` WRITE;
/*!40000 ALTER TABLE `temp_user_account` DISABLE KEYS */;
INSERT INTO `temp_user_account` VALUES (121314,'scrypt:32768:8:1$WEMPpk1u4tyLTd6c$5f91e8ac0334b1b31aa7f54b20eb303c24577e7158e282cd3a01d593f234f56d38d7fe86f2d66b86d54f49e84ba27644de5bebddeb3eaaa7676c1e0bd6d39b4e',1),(212612,'scrypt:32768:8:1$ZVziRNLwOHk3NkE2$0d6b8c1cf8607c17c705fb0dd83f5a13c721da0d6f2c979ee600af391afab4c7d83dc0ba93ba33745e84706dab331f15ebe5c96ef952f65406f131c8d4c6566a',1),(321221,'scrypt:32768:8:1$xF1j1JVoIwHaEnpS$cd66f3c387b893466ca1a7d5106005ebc1c4b4037101764437b56316269bb35a320b5f362040b2ff48eab95f1f0046778a5740597fd09a1921d0fa611e7b31ff',NULL);
/*!40000 ALTER TABLE `temp_user_account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_user_feedback`
--

DROP TABLE IF EXISTS `temp_user_feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_user_feedback` (
  `feedback_id` int NOT NULL AUTO_INCREMENT,
  `asset_serial` varchar(30) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `employee_id` int DEFAULT NULL,
  `asset_temperature` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `asset_noise` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `asset_state` varchar(512) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `asset_serial` (`asset_serial`),
  KEY `employee_id` (`employee_id`),
  CONSTRAINT `temp_user_feedback_ibfk_1` FOREIGN KEY (`asset_serial`) REFERENCES `asset_existence` (`asset_serial`),
  CONSTRAINT `temp_user_feedback_ibfk_2` FOREIGN KEY (`employee_id`) REFERENCES `employees` (`employee_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_user_feedback`
--

LOCK TABLES `temp_user_feedback` WRITE;
/*!40000 ALTER TABLE `temp_user_feedback` DISABLE KEYS */;
INSERT INTO `temp_user_feedback` VALUES (1,'12HQ30BM1',22134,'Normal','Moderate','something\n'),(2,'2MLSN32QPR',33123,NULL,NULL,NULL),(3,'5CG024BK50',89123,NULL,NULL,NULL),(4,'12H12HKLMNI',20202,'Very Hot','Low','uhe'),(5,'3B122121H',606012,'Hot','High','something');
/*!40000 ALTER TABLE `temp_user_feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `temp_user_informations`
--

DROP TABLE IF EXISTS `temp_user_informations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `temp_user_informations` (
  `temp_user_id` int NOT NULL AUTO_INCREMENT,
  `temp_user_email` varchar(60) COLLATE utf8mb4_unicode_ci NOT NULL,
  `temp_user_fullname` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `temp_user_get_access_date` datetime NOT NULL,
  `temp_user_rem_access_date` date DEFAULT NULL,
  `temp_user_Company` varchar(30) COLLATE utf8mb4_unicode_ci NOT NULL,
  `temp_user_role` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`temp_user_id`),
  UNIQUE KEY `temp_user_email` (`temp_user_email`)
) ENGINE=InnoDB AUTO_INCREMENT=321222 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `temp_user_informations`
--

LOCK TABLES `temp_user_informations` WRITE;
/*!40000 ALTER TABLE `temp_user_informations` DISABLE KEYS */;
INSERT INTO `temp_user_informations` VALUES (121314,'mohammedali123@gamil.com','mohammed ali','2025-07-01 10:54:11',NULL,'dell','Technician'),(212612,'mohammedkamal32@gmail.com','Mohammed Kamal','2025-10-11 13:17:26',NULL,'Dell','Technicien'),(321221,'haitamhsa799@gmail.com','Haitam Amhaouch','2025-06-26 07:09:28',NULL,'HP','technician');
/*!40000 ALTER TABLE `temp_user_informations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-10-20  9:32:31
