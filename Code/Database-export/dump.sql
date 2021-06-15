-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: easy_cat_set
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bak`
--

DROP TABLE IF EXISTS `bak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bak` (
  `BakID` int NOT NULL,
  `BakTypeID` int NOT NULL,
  `Gewicht` float DEFAULT NULL,
  `Temperatuur` float DEFAULT NULL,
  `Datum` date DEFAULT NULL,
  `Tijd` time DEFAULT NULL,
  PRIMARY KEY (`BakID`),
  KEY `fk_baktypes_idx` (`BakTypeID`),
  CONSTRAINT `fk_baktypes` FOREIGN KEY (`BakTypeID`) REFERENCES `baktype` (`BakTypeID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bak`
--

LOCK TABLES `bak` WRITE;
/*!40000 ALTER TABLE `bak` DISABLE KEYS */;
INSERT INTO `bak` VALUES (1,2,NULL,16.21,'2021-12-24','01:57:40'),(2,1,2.99,27.24,NULL,NULL),(3,1,NULL,28.09,'2021-01-25','02:48:52'),(4,2,NULL,22.7,'2021-12-03','10:03:52'),(5,2,3.75,19.29,NULL,NULL),(6,2,NULL,15.95,'2021-08-06','06:09:51'),(7,1,3.08,17.64,NULL,NULL),(8,2,NULL,16.45,'2021-04-20','20:13:01'),(9,2,NULL,16.13,'2021-03-12','16:14:50'),(10,2,3.58,28.24,NULL,NULL),(11,1,NULL,29.97,'2021-04-26','08:01:31'),(12,1,NULL,26.9,'2021-10-03','08:38:20'),(13,1,2.46,29.92,NULL,NULL),(14,2,3.64,20.64,NULL,NULL),(15,1,NULL,18.26,'2021-10-25','03:08:37'),(16,2,NULL,19.13,'2021-06-27','19:48:27'),(17,2,1.38,17.32,NULL,NULL),(18,1,NULL,15.66,'2021-07-23','23:59:44'),(19,2,NULL,28.54,'2021-10-30','05:51:02'),(20,1,NULL,23.43,'2021-04-20','20:47:58'),(21,2,4.22,18.08,NULL,NULL),(22,1,NULL,19.62,'2021-04-29','12:39:56'),(23,1,NULL,21.57,'2021-02-15','18:54:33'),(24,1,NULL,23.73,'2021-01-05','13:47:25'),(25,2,1.34,22.78,NULL,NULL),(26,2,NULL,15.58,'2021-09-11','22:29:52'),(27,2,NULL,25.55,'2021-05-30','01:32:01'),(28,1,NULL,16.48,'2021-02-17','02:11:53'),(29,1,NULL,29.99,'2021-09-14','14:25:31'),(30,2,NULL,18.44,'2021-12-06','02:48:30'),(31,1,NULL,19.39,'2021-04-19','21:03:00'),(32,2,3.37,17.71,NULL,NULL),(33,2,NULL,25.63,'2021-03-24','09:57:50'),(34,2,2.37,21.98,NULL,NULL),(35,2,NULL,29.42,'2021-02-08','15:29:07'),(36,2,NULL,29.21,'2021-04-19','22:23:03'),(37,1,NULL,18.45,'2021-04-26','10:15:48'),(38,1,0.47,17.44,NULL,NULL),(39,1,NULL,25.64,'2021-07-30','04:29:58'),(40,1,NULL,26.26,'2021-04-28','03:49:31'),(41,1,4.36,15.92,NULL,NULL),(42,2,NULL,26.35,'2021-04-12','05:34:44'),(43,2,NULL,20.62,'2021-06-02','14:47:03'),(44,2,1.64,29.11,NULL,NULL),(45,1,NULL,17.6,'2021-08-31','14:53:09'),(46,2,NULL,19.69,'2021-10-26','18:22:45'),(47,1,0.19,27.02,NULL,NULL),(48,1,NULL,22,'2021-09-07','05:22:43'),(49,1,NULL,25.96,'2021-12-10','16:46:32');
/*!40000 ALTER TABLE `bak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baktype`
--

DROP TABLE IF EXISTS `baktype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baktype` (
  `BakTypeID` int NOT NULL AUTO_INCREMENT,
  `Type` varchar(45) NOT NULL,
  PRIMARY KEY (`BakTypeID`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baktype`
--

LOCK TABLES `baktype` WRITE;
/*!40000 ALTER TABLE `baktype` DISABLE KEYS */;
INSERT INTO `baktype` VALUES (1,'Drinkbak'),(2,'Voerbak');
/*!40000 ALTER TABLE `baktype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gewicht_bakken`
--

DROP TABLE IF EXISTS `gewicht_bakken`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gewicht_bakken` (
  `Gewicht_bakkenID` int NOT NULL AUTO_INCREMENT,
  `Gewicht_drinkbak` float DEFAULT NULL,
  `Gewicht_voerbak` float DEFAULT NULL,
  PRIMARY KEY (`Gewicht_bakkenID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gewicht_bakken`
--

LOCK TABLES `gewicht_bakken` WRITE;
/*!40000 ALTER TABLE `gewicht_bakken` DISABLE KEYS */;
/*!40000 ALTER TABLE `gewicht_bakken` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kattenluik`
--

DROP TABLE IF EXISTS `kattenluik`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kattenluik` (
  `KattenluikID` int NOT NULL AUTO_INCREMENT,
  `KattenluikOptieID` int NOT NULL,
  `Datum` date DEFAULT NULL,
  `Tijd` time DEFAULT NULL,
  PRIMARY KEY (`KattenluikID`),
  KEY `fk_kattenluikoptie_idx` (`KattenluikOptieID`),
  CONSTRAINT `fk_kattenluikoptie` FOREIGN KEY (`KattenluikOptieID`) REFERENCES `kattenluikoptie` (`KattenluikOptieID`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kattenluik`
--

LOCK TABLES `kattenluik` WRITE;
/*!40000 ALTER TABLE `kattenluik` DISABLE KEYS */;
INSERT INTO `kattenluik` VALUES (1,1,'2021-12-18','08:26:18'),(2,3,'2021-01-26','01:00:10'),(3,3,'2021-05-08','09:51:17'),(4,1,'2021-09-07','23:46:20'),(5,1,'2021-07-13','20:14:39'),(6,3,'2021-09-02','22:16:18'),(7,1,'2021-03-23','08:15:22'),(8,2,'2021-05-02','05:25:52'),(9,1,'2021-01-01','06:51:30'),(10,1,'2021-03-01','22:00:26'),(11,2,'2021-10-09','08:58:38'),(12,3,'2021-09-30','03:23:03'),(13,2,'2021-07-26','02:16:33'),(14,1,'2021-06-18','11:07:53'),(15,3,'2021-03-17','18:32:33'),(16,1,'2021-06-08','04:54:22'),(17,1,'2021-09-21','04:16:26'),(18,3,'2021-04-20','17:28:33'),(19,1,'2021-05-26','19:48:16'),(20,2,'2021-07-06','01:51:36'),(21,3,'2021-05-29','12:37:01'),(22,1,'2021-02-04','14:35:09'),(23,2,'2021-06-27','05:04:01'),(24,2,'2021-04-25','10:00:06'),(25,2,'2021-01-09','03:17:08'),(26,2,'2021-11-21','06:16:53'),(27,3,'2021-04-13','07:21:15'),(28,2,'2021-04-24','01:05:14'),(29,2,'2021-07-29','17:42:09'),(30,3,'2021-02-20','05:25:08'),(31,2,'2021-07-16','18:07:45'),(32,3,'2021-02-21','01:13:19'),(33,1,'2021-03-11','04:29:28'),(34,3,'2021-11-25','08:19:27'),(35,3,'2021-11-03','04:00:35'),(36,1,'2021-01-12','04:56:06'),(37,1,'2021-09-08','20:37:14'),(38,3,'2021-02-15','11:52:56'),(39,1,'2021-06-20','22:31:43'),(40,3,'2021-11-09','19:43:23'),(41,2,'2021-08-29','00:13:20'),(42,1,'2021-11-25','12:09:31'),(43,3,'2021-10-28','18:06:26'),(44,3,'2021-07-24','10:03:24'),(45,3,'2021-08-29','21:45:46'),(46,2,'2021-10-30','18:18:09'),(47,3,'2021-03-06','17:22:05'),(48,3,'2021-06-29','11:04:01'),(49,2,'2021-11-01','04:18:26'),(50,3,'2021-03-15','08:47:52');
/*!40000 ALTER TABLE `kattenluik` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kattenluikoptie`
--

DROP TABLE IF EXISTS `kattenluikoptie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kattenluikoptie` (
  `KattenluikOptieID` int NOT NULL,
  ` Optie` varchar(45) NOT NULL,
  PRIMARY KEY (`KattenluikOptieID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kattenluikoptie`
--

LOCK TABLES `kattenluikoptie` WRITE;
/*!40000 ALTER TABLE `kattenluikoptie` DISABLE KEYS */;
INSERT INTO `kattenluikoptie` VALUES (1,'open/open'),(2,'open/gesloten'),(3,'gesloten/gesloten');
/*!40000 ALTER TABLE `kattenluikoptie` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-15  0:24:13
