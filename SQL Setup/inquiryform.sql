-- MySQL dump 10.13  Distrib 8.0.41, for Win64 (x86_64)
--
-- Host: localhost    Database: spacepotatoesdb
-- ------------------------------------------------------
-- Server version	8.0.41

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
-- Table structure for table `inquiryform`
--

DROP TABLE IF EXISTS `inquiryform`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inquiryform` (
  `Topic` varchar(150) NOT NULL,
  `Inquiry` varchar(100) NOT NULL,
  `CreateDate` varchar(45) NOT NULL,
  `Status` bit(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inquiryform`
--

LOCK TABLES `inquiryform` WRITE;
/*!40000 ALTER TABLE `inquiryform` DISABLE KEYS */;
INSERT INTO `inquiryform` VALUES ('feedback, general','','2025-05-13 03:50:12',_binary '\0'),('feedback, transaction','','2025-05-13 03:50:15',_binary '\0'),('inquiry, other','','2025-05-13 03:52:12',_binary '\0'),('transaction, general','yes','2025-05-13 03:56:12',_binary '\0'),('feedback, general','test','2025-05-13 04:05:40',_binary '\0'),('feedback, general','this is a test ','2025-05-13 12:03:15',_binary '\0'),('feedback, transaction','YAYYYYY','2025-05-13 12:33:03',_binary '\0'),('transaction','I got extra money. can i keep it?','2025-05-13 12:36:17',_binary '\0'),('inquiry','yesyes','2025-05-13 12:58:30',_binary '\0'),('inquiry, general','test','2025-05-14 17:25:11',_binary '\0');
/*!40000 ALTER TABLE `inquiryform` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-05-16 17:44:17
