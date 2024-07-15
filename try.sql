-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: ELECTION
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

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
-- Table structure for table `Candidate`
--

DROP TABLE IF EXISTS `Candidate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Candidate` (
  `Candidate_ID` int NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Aadhar_No` bigint DEFAULT NULL,
  `Source_of_Funding` varchar(255) DEFAULT NULL,
  `Total_Donations` decimal(10,2) DEFAULT NULL,
  `Total_Funding_Received` decimal(10,2) DEFAULT NULL,
  `Total_Expenditure` decimal(10,2) DEFAULT NULL,
  `Party_ID` int DEFAULT NULL,
  `Constituency_ID` int DEFAULT NULL,
  PRIMARY KEY (`Candidate_ID`),
  KEY `Party_ID` (`Party_ID`),
  KEY `Aadhar_No` (`Aadhar_No`),
  KEY `Constituency_ID` (`Constituency_ID`),
  CONSTRAINT `candidate_ibfk_1` FOREIGN KEY (`Party_ID`) REFERENCES `Political_Party` (`Party_ID`),
  CONSTRAINT `candidate_ibfk_2` FOREIGN KEY (`Aadhar_No`) REFERENCES `citizen` (`Aadhar_No`),
  CONSTRAINT `candidate_ibfk_3` FOREIGN KEY (`Constituency_ID`) REFERENCES `Constituency` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Candidate`
--

LOCK TABLES `Candidate` WRITE;
/*!40000 ALTER TABLE `Candidate` DISABLE KEYS */;
INSERT INTO `Candidate` VALUES (1,'John Doe',1234567890,'Self-Funded',5000.00,5000.00,3000.00,1,1),(2,'Jane Smith',2345678901,'Donations',8000.00,10000.00,6000.00,2,2),(3,'Amit Patel',3456789012,'Party Funding',10000.00,12000.00,8000.00,1,3),(4,'Priya Sharma',4567890123,'Self-Funded',6000.00,6000.00,4000.00,2,4),(5,'Raj Kumar',5678901234,'Donations',7000.00,9000.00,5000.00,3,5);
/*!40000 ALTER TABLE `Candidate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Constituency`
--

DROP TABLE IF EXISTS `Constituency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Constituency` (
  `C_ID` int NOT NULL,
  `C_Name` varchar(255) DEFAULT NULL,
  `State_Name` varchar(255) DEFAULT NULL,
  `Total_Residing_Citizens` int DEFAULT NULL,
  `Polling_Booths` int DEFAULT NULL,
  `EVM_Machines` int DEFAULT NULL,
  PRIMARY KEY (`C_ID`),
  KEY `State_Name` (`State_Name`),
  CONSTRAINT `constituency_ibfk_1` FOREIGN KEY (`State_Name`) REFERENCES `STATE` (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Constituency`
--

LOCK TABLES `Constituency` WRITE;
/*!40000 ALTER TABLE `Constituency` DISABLE KEYS */;
INSERT INTO `Constituency` VALUES (1,'Mumbai South','Maharashtra',500000,50,100),(2,'Bangalore Central','Karnataka',700000,70,120),(3,'Ahmedabad South','Gujarat',600000,60,110),(4,'Lucknow Central','Uttar Pradesh',800000,80,130),(5,'Chennai West','Tamil Nadu',900000,90,140);
/*!40000 ALTER TABLE `Constituency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Department`
--

DROP TABLE IF EXISTS `Department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Department` (
  `ID` int NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Number_of_Employees` int DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Department`
--

LOCK TABLES `Department` WRITE;
/*!40000 ALTER TABLE `Department` DISABLE KEYS */;
INSERT INTO `Department` VALUES (1,'Election Administration',50),(2,'Voter Registration',30),(3,'Polling Management',40),(4,'Legal Affairs',20),(5,'Information Technology',25);
/*!40000 ALTER TABLE `Department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `EVM_Machine`
--

DROP TABLE IF EXISTS `EVM_Machine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `EVM_Machine` (
  `Machine_ID` int NOT NULL,
  `No_of_Votes` int DEFAULT NULL,
  `Const_ID` int DEFAULT NULL,
  PRIMARY KEY (`Machine_ID`),
  KEY `Const_ID` (`Const_ID`),
  CONSTRAINT `evm_machine_ibfk_1` FOREIGN KEY (`Const_ID`) REFERENCES `Constituency` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `EVM_Machine`
--

LOCK TABLES `EVM_Machine` WRITE;
/*!40000 ALTER TABLE `EVM_Machine` DISABLE KEYS */;
INSERT INTO `EVM_Machine` VALUES (1,500,1),(2,600,2),(3,700,3),(4,800,4),(5,900,5);
/*!40000 ALTER TABLE `EVM_Machine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Educational_Qualification`
--

DROP TABLE IF EXISTS `Educational_Qualification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Educational_Qualification` (
  `C_ID` int NOT NULL,
  `Qualification` varchar(255) NOT NULL,
  PRIMARY KEY (`C_ID`,`Qualification`),
  CONSTRAINT `educational_qualification_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `Candidate` (`Candidate_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;



--
-- Dumping data for table `Educational_Qualification`
--

LOCK TABLES `Educational_Qualification` WRITE;
/*!40000 ALTER TABLE `Educational_Qualification` DISABLE KEYS */;
INSERT INTO `Educational_Qualification` VALUES (1,'Bachelor of Arts'),(1,'Master of Arts'),(2,'Bachelor of Science'),(2,'Master of Science'),(3,'Bachelor of Commerce'),(3,'Master of Commerce'),(4,'Bachelor of Engineering'),(4,'Master of Business Administration'),(5,'Bachelor of Law'),(5,'Master of Law');
/*!40000 ALTER TABLE `Educational_Qualification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Employee`
--

DROP TABLE IF EXISTS `Employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Employee` (
  `ID` int NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Position` varchar(255) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `PinCode` varchar(10) DEFAULT NULL,
  `Residence` varchar(255) DEFAULT NULL,
  `Email` varchar(255) DEFAULT NULL,
  `Contact_Number` varchar(15) DEFAULT NULL,
  `Working_Department` varchar(255) DEFAULT NULL,
  `Super_ID` int DEFAULT NULL,
  `Street_Address` varchar(255) DEFAULT NULL,
  `City` varchar(255) DEFAULT NULL,
  `State` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Super_ID` (`Super_ID`),
  CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`Super_ID`) REFERENCES `Employee` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Employee`
--

LOCK TABLES `Employee` WRITE;
/*!40000 ALTER TABLE `Employee` DISABLE KEYS */;
INSERT INTO `Employee` VALUES (1,'John Doe','Manager','1985-05-15','12345','123 Main St','john.doe@email.com','123-456-7890','Management',NULL,'Cityville','Metropolis','Stateville'),(2,'Jane Smith','Supervisor','1990-08-22','56789','456 Oak St','jane.smith@email.com','987-654-3210','Operations',1,'Townsville','Metropolis','Stateville'),(3,'Amit Patel','Analyst','1988-02-10','98765','789 Pine St','amit.patel@email.com','765-432-1098','Finance',1,'Citytown','Metroville','Stateville'),(4,'Priya Sharma','Developer','1992-11-05','54321','101 Cedar St','priya.sharma@email.com','654-321-0987','IT',2,'Villagetown','Metroville','Stateville'),(5,'Raj Kumar','Intern','1995-07-18','23456','202 Maple St','raj.kumar@email.com','876-543-2109','IT',4,'Hometown','Smallville','Stateville');
/*!40000 ALTER TABLE `Employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `FIR_Candidates`
--

DROP TABLE IF EXISTS `FIR_Candidates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `FIR_Candidates` (
  `Candidate_ID` int NOT NULL,
  `FIR_Number` int NOT NULL,
  PRIMARY KEY (`Candidate_ID`,`FIR_Number`),
  KEY `FIR_Number` (`FIR_Number`),
  CONSTRAINT `fir_candidates_ibfk_1` FOREIGN KEY (`Candidate_ID`) REFERENCES `Candidate` (`Candidate_ID`),
  CONSTRAINT `fir_candidates_ibfk_2` FOREIGN KEY (`FIR_Number`) REFERENCES `criminal_record` (`FIR_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `FIR_Candidates`
--

LOCK TABLES `FIR_Candidates` WRITE;
/*!40000 ALTER TABLE `FIR_Candidates` DISABLE KEYS */;
INSERT INTO `FIR_Candidates` VALUES (1,1001),(2,1002),(3,1003),(4,1004),(5,1005);
/*!40000 ALTER TABLE `FIR_Candidates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Member_of_Parliament`
--

DROP TABLE IF EXISTS `Member_of_Parliament`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Member_of_Parliament` (
  `Cnd_ID` int NOT NULL,
  `PP_ID` int NOT NULL,
  `CT_Id` int NOT NULL,
  PRIMARY KEY (`Cnd_ID`,`PP_ID`,`CT_Id`),
  KEY `PP_ID` (`PP_ID`),
  KEY `CT_Id` (`CT_Id`),
  CONSTRAINT `member_of_parliament_ibfk_1` FOREIGN KEY (`Cnd_ID`) REFERENCES `Candidate` (`Candidate_ID`),
  CONSTRAINT `member_of_parliament_ibfk_2` FOREIGN KEY (`PP_ID`) REFERENCES `Political_Party` (`Party_ID`),
  CONSTRAINT `member_of_parliament_ibfk_3` FOREIGN KEY (`CT_Id`) REFERENCES `Constituency` (`C_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Member_of_Parliament`
--

LOCK TABLES `Member_of_Parliament` WRITE;
/*!40000 ALTER TABLE `Member_of_Parliament` DISABLE KEYS */;
INSERT INTO `Member_of_Parliament` VALUES (1,1,1),(3,1,3),(2,2,2),(4,2,4),(5,3,5);
/*!40000 ALTER TABLE `Member_of_Parliament` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Political_Party`
--

DROP TABLE IF EXISTS `Political_Party`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Political_Party` (
  `Party_ID` int NOT NULL,
  `Party_Name` char(60) DEFAULT NULL,
  `Party_President` char(30) DEFAULT NULL,
  `Party_Headquarters` char(30) DEFAULT NULL,
  `Symbol` char(30) DEFAULT NULL,
  `Total_Members` int DEFAULT NULL,
  `Seats_Contested` int DEFAULT NULL,
  PRIMARY KEY (`Party_ID`),
  UNIQUE KEY `Party_ID` (`Party_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Political_Party`
--

LOCK TABLES `Political_Party` WRITE;
/*!40000 ALTER TABLE `Political_Party` DISABLE KEYS */;
INSERT INTO `Political_Party` VALUES (1,'Indian National Congress','Sonia Gandhi','New Delhi','Hand',500000,200),(2,'Bharatiya Janata Party','J.P. Nadda','New Delhi','Lotus',550000,220),(3,'Aam Aadmi Party','Arvind Kejriwal','New Delhi','Broom',300000,150),(4,'Communist Party of India (Marxist)','Sitaram Yechury','New Delhi','Hammer and Sickle',100000,50),(5,'Shiv Sena','Uddhav Thackeray','Mumbai','Bow and Arrow',200000,100);
/*!40000 ALTER TABLE `Political_Party` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `STATE`
--

DROP TABLE IF EXISTS `STATE`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `STATE` (
  `NAME` varchar(255) NOT NULL,
  `NUMBER_OF_CITIZENS` int DEFAULT NULL,
  `NUMBER_OF_CONSTITUENCIES` int DEFAULT NULL,
  `NUMBER_OF_REGIONAL_PARTIES` int DEFAULT NULL,
  `RESIDING_CITIZENS` int DEFAULT NULL,
  PRIMARY KEY (`NAME`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `STATE`
--

LOCK TABLES `STATE` WRITE;
/*!40000 ALTER TABLE `STATE` DISABLE KEYS */;
INSERT INTO `STATE` VALUES ('Andhra Pradesh',50000000,25,3,48000000),('Gujarat',60000000,26,4,58000000),('Karnataka',70000000,30,3,68000000),('Kerala',35000000,20,2,33000000),('Maharashtra',80000000,48,5,75000000),('Tamil Nadu',90000000,40,4,86000000),('Uttar Pradesh',220000000,80,8,210000000);
/*!40000 ALTER TABLE `STATE` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Tenure`
--

DROP TABLE IF EXISTS `Tenure`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Tenure` (
  `CandidateID` int NOT NULL,
  `Term_Start_Date` date DEFAULT NULL,
  PRIMARY KEY (`CandidateID`),
  CONSTRAINT `tenure_ibfk_1` FOREIGN KEY (`CandidateID`) REFERENCES `Candidate` (`Candidate_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Tenure`
--

LOCK TABLES `Tenure` WRITE;
/*!40000 ALTER TABLE `Tenure` DISABLE KEYS */;
INSERT INTO `Tenure` VALUES (1,'2023-05-01'),(2,'2023-05-01'),(3,'2023-05-01'),(4,'2023-05-01'),(5,'2023-05-01');
/*!40000 ALTER TABLE `Tenure` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Vote_Count_Machine_Party`
--

DROP TABLE IF EXISTS `Vote_Count_Machine_Party`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Vote_Count_Machine_Party` (
  `Political_Party_ID` int NOT NULL,
  `Machine_ID` int NOT NULL,
  `Vote_Count` int DEFAULT NULL,
  PRIMARY KEY (`Political_Party_ID`,`Machine_ID`),
  KEY `Machine_ID` (`Machine_ID`),
  CONSTRAINT `vote_count_machine_party_ibfk_1` FOREIGN KEY (`Political_Party_ID`) REFERENCES `Political_Party` (`Party_ID`),
  CONSTRAINT `vote_count_machine_party_ibfk_2` FOREIGN KEY (`Machine_ID`) REFERENCES `EVM_Machine` (`Machine_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Vote_Count_Machine_Party`
--

LOCK TABLES `Vote_Count_Machine_Party` WRITE;
/*!40000 ALTER TABLE `Vote_Count_Machine_Party` DISABLE KEYS */;
INSERT INTO `Vote_Count_Machine_Party` VALUES (1,1,500),(2,2,600),(3,3,700),(4,4,800),(5,5,900);
/*!40000 ALTER TABLE `Vote_Count_Machine_Party` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `WORKS_FOR`
--

DROP TABLE IF EXISTS `WORKS_FOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `WORKS_FOR` (
  `C_ID` int NOT NULL,
  `D_ID` int NOT NULL,
  `E_ID` int NOT NULL,
  PRIMARY KEY (`C_ID`,`D_ID`,`E_ID`),
  KEY `D_ID` (`D_ID`),
  KEY `E_ID` (`E_ID`),
  CONSTRAINT `works_for_ibfk_1` FOREIGN KEY (`C_ID`) REFERENCES `Constituency` (`C_ID`),
  CONSTRAINT `works_for_ibfk_2` FOREIGN KEY (`D_ID`) REFERENCES `Department` (`ID`),
  CONSTRAINT `works_for_ibfk_3` FOREIGN KEY (`E_ID`) REFERENCES `Employee` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `WORKS_FOR`
--

LOCK TABLES `WORKS_FOR` WRITE;
/*!40000 ALTER TABLE `WORKS_FOR` DISABLE KEYS */;
INSERT INTO `WORKS_FOR` VALUES (1,1,1),(2,2,2),(3,3,3),(4,4,4),(5,5,5);
/*!40000 ALTER TABLE `WORKS_FOR` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `citizen`
--

DROP TABLE IF EXISTS `citizen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `citizen` (
  `Citizen_ID` int NOT NULL,
  `Aadhar_No` bigint DEFAULT NULL,
  `Name` char(30) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Street_Address` char(100) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Nationality` char(20) DEFAULT NULL,
  `Annual_Income` int DEFAULT NULL,
  `Educational_Background` char(20) DEFAULT NULL,
  `State` char(20) DEFAULT NULL,
  `City` char(20) DEFAULT NULL,
  `PinCode` int DEFAULT NULL,
  `Contact_Number` bigint DEFAULT NULL,
  `Email_Address` char(30) DEFAULT NULL,
  PRIMARY KEY (`Citizen_ID`),
  UNIQUE KEY `Aadhar_No` (`Aadhar_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `citizen`
--

LOCK TABLES `citizen` WRITE;
/*!40000 ALTER TABLE `citizen` DISABLE KEYS */;
INSERT INTO `citizen` VALUES (1,1234567890,'John Doe','1990-05-15','123 Main St','M','Indian',500000,'Graduate','Maharashtra','Mumbai',400001,9876543210,'john.doe@email.com'),(2,2345678901,'Jane Smith','1985-08-22','456 Oak St','F','Indian',600000,'Postgraduate','Karnataka','Bangalore',560001,8765432109,'jane.smith@email.com'),(3,3456789012,'Amit Patel','1992-02-10','789 Pine St','M','Indian',400000,'Undergraduate','Gujarat','Ahmedabad',380001,7654321098,'amit.patel@email.com'),(4,4567890123,'Priya Sharma','1988-11-05','101 Cedar St','F','Indian',700000,'Postgraduate','Uttar Pradesh','Lucknow',226001,6543210987,'priya.sharma@email.com'),(5,5678901234,'Raj Kumar','1980-07-18','202 Maple St','M','Indian',800000,'Graduate','Tamil Nadu','Chennai',600001,5432109876,'raj.kumar@email.com');
/*!40000 ALTER TABLE `citizen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `criminal_record`
--

DROP TABLE IF EXISTS `criminal_record`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `criminal_record` (
  `FIR_Number` int NOT NULL,
  `Nature_of_Offence` varchar(255) DEFAULT NULL,
  `Jurisdiction` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`FIR_Number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `criminal_record`
--

LOCK TABLES `criminal_record` WRITE;
/*!40000 ALTER TABLE `criminal_record` DISABLE KEYS */;
INSERT INTO `criminal_record` VALUES (1001,'Bribery','City Police Department'),(1002,'Fraud','County Sheriff Office'),(1003,'Assault','State Police'),(1004,'Drug Trafficking','Drug Enforcement Agency'),(1005,'Cybercrime','Federal Bureau of Investigation');
/*!40000 ALTER TABLE `criminal_record` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department_responsibility`
--

DROP TABLE IF EXISTS `department_responsibility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department_responsibility` (
  `D_ID` int NOT NULL,
  `Responsibility` varchar(255) NOT NULL,
  PRIMARY KEY (`D_ID`,`Responsibility`),
  CONSTRAINT `department_responsibility_ibfk_1` FOREIGN KEY (`D_ID`) REFERENCES `Department` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department_responsibility`
--

LOCK TABLES `department_responsibility` WRITE;
/*!40000 ALTER TABLE `department_responsibility` DISABLE KEYS */;
INSERT INTO `department_responsibility` VALUES (1,'Election Administration'),(1,'Polling Management'),(1,'Voter Registration'),(2,'IT Infrastructure'),(2,'Software Development'),(3,'Financial Planning'),(4,'Legal Compliance'),(5,'Operational Efficiency');
/*!40000 ALTER TABLE `department_responsibility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manifesto`
--

DROP TABLE IF EXISTS `manifesto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manifesto` (
  `Party_ID` int NOT NULL,
  `Party_Name` varchar(255) DEFAULT NULL,
  `Publication_Date` date DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Content` text,
  `Face_of_Election` varchar(255) DEFAULT NULL,
  `Tagline` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Party_ID`),
  CONSTRAINT `manifesto_ibfk_1` FOREIGN KEY (`Party_ID`) REFERENCES `Political_Party` (`Party_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manifesto`
--

LOCK TABLES `manifesto` WRITE;
/*!40000 ALTER TABLE `manifesto` DISABLE KEYS */;
INSERT INTO `manifesto` VALUES (1,'Party A','2023-04-01','Election Manifesto 2023','Our vision is to...','John Candidate','Vote for Change'),(2,'Party B','2023-04-02','Manifesto for Better Future','We promise to...','Jane Candidate','Building Tomorrow'),(3,'Party C','2023-04-03','Peoples Agenda','In our manifesto...','Amit Candidate','Empowering Citizens'),(4,'Party D','2023-04-04','Vision 2023','Our commitment is to...','Priya Candidate','Progress with Integrity'),(5,'Party E','2023-04-05','New Horizons','Explore our plans for...','Raj Candidate','Innovation for All');
/*!40000 ALTER TABLE `manifesto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `voter`
--

DROP TABLE IF EXISTS `voter`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `voter` (
  `Aadhar_No` bigint DEFAULT NULL,
  `Voter_ID` int NOT NULL,
  `DOB` date DEFAULT NULL,
  `Street_Address` char(100) DEFAULT NULL,
  `Gender` char(1) DEFAULT NULL,
  `Nationality` char(20) DEFAULT NULL,
  `Annual_Income` int DEFAULT NULL,
  `Educational_Background` char(30) DEFAULT NULL,
  `State` char(20) DEFAULT NULL,
  `City` char(20) DEFAULT NULL,
  `PinCode` int DEFAULT NULL,
  `Name` char(30) DEFAULT NULL,
  `Voting_constituency` char(30) DEFAULT NULL,
  PRIMARY KEY (`Voter_ID`),
  UNIQUE KEY `Voter_ID` (`Voter_ID`),
  UNIQUE KEY `Aadhar_No` (`Aadhar_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `voter`
--

LOCK TABLES `voter` WRITE;
/*!40000 ALTER TABLE `voter` DISABLE KEYS */;
INSERT INTO `voter` VALUES (1234567890,1001,'1990-05-15','123 Main St','M','Indian',500000,'Graduate','Maharashtra','Mumbai',400001,'John Doe','Mumbai South'),(2345678901,1002,'1985-08-22','456 Oak St','F','Indian',600000,'Postgraduate','Karnataka','Bangalore',560001,'Jane Smith','Bangalore Central'),(3456789012,1003,'1992-02-10','789 Pine St','M','Indian',400000,'Undergraduate','Gujarat','Ahmedabad',380001,'Amit Patel','Ahmedabad South'),(4567890123,1004,'1988-11-05','101 Cedar St','F','Indian',700000,'Postgraduate','Uttar Pradesh','Lucknow',226001,'Priya Sharma','Lucknow Central'),(5678901234,1005,'1980-07-18','202 Maple St','M','Indian',800000,'Graduate','Tamil Nadu','Chennai',600001,'Raj Kumar','Chennai West');
/*!40000 ALTER TABLE `voter` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-02  4:24:11
