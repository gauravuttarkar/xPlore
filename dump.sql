-- MySQL dump 10.13  Distrib 5.7.24, for Linux (x86_64)
--
-- Host: localhost    Database: xplore
-- ------------------------------------------------------
-- Server version	5.7.24-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `xplore`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `xplore` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `xplore`;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add planet',7,'add_planet'),(26,'Can change planet',7,'change_planet'),(27,'Can delete planet',7,'delete_planet'),(28,'Can view planet',7,'view_planet'),(29,'Can add galaxy',8,'add_galaxy'),(30,'Can change galaxy',8,'change_galaxy'),(31,'Can delete galaxy',8,'delete_galaxy'),(32,'Can view galaxy',8,'view_galaxy'),(33,'Can add constellation',9,'add_constellation'),(34,'Can change constellation',9,'change_constellation'),(35,'Can delete constellation',9,'delete_constellation'),(36,'Can view constellation',9,'view_constellation');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `constellations_constellation`
--

DROP TABLE IF EXISTS `constellations_constellation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `constellations_constellation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `constellationName` varchar(100) NOT NULL,
  `origin` varchar(200) DEFAULT NULL,
  `meaning` varchar(200) DEFAULT NULL,
  `brightestStar` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `constellations_constellation`
--

LOCK TABLES `constellations_constellation` WRITE;
/*!40000 ALTER TABLE `constellations_constellation` DISABLE KEYS */;
INSERT INTO `constellations_constellation` VALUES (1,'Andromeda','ancient (Ptolemy)','Andromeda (The chained maiden or princess)','Alpheratz'),(2,'Antlia','1763, Lacaille','air pump','α Antliae'),(3,'Apus','1603, Uranometria, created by Keyser and de Houtman','Bird-of-paradise','α Apodis'),(4,'Aquarius','ancient (Ptolemy)','water-bearer','Sadalsuud'),(5,'Aquila','ancient (Ptolemy)','eagle','Altair'),(6,'Ara','ancient (Ptolemy)','altar','β Arae'),(7,'Aries','ancient (Ptolemy)','ram','Hamal'),(8,'Auriga','ancient (Ptolemy)','charioteer','Capella'),(9,'Boötes','ancient (Ptolemy)','herdsman','Arcturus'),(10,'Caelum','1763, Lacaille','chisel or graving tool','α Caeli'),(11,'Camelopardalis','1613, Plancius[7]','giraffe','β Camelopardalis'),(12,'Cancer','ancient (Ptolemy)','crab','Tarf[8]'),(13,'Canes Venatici','1690, Firmamentum Sobiescianum, Hevelius','hunting dogs','Cor Caroli'),(14,'Canis Major','ancient (Ptolemy)','greater dog','Sirius'),(15,'Canis Minor','ancient (Ptolemy)','lesser dog','Procyon'),(16,'Capricornus','ancient (Ptolemy)','sea goat','Deneb Algedi'),(17,'Carina','1763, Lacaille, split from Argo Navis','keel','Canopus'),(18,'Cassiopeia','ancient (Ptolemy)','Cassiopeia (mythological character)','Schedar[8]'),(19,'Centaurus','ancient (Ptolemy)','centaur','Rigil Kentaurus[8]'),(20,'Cepheus','ancient (Ptolemy)','Cepheus (mythological character)','Alderamin'),(21,'Cetus','ancient (Ptolemy)','sea monster (later interpreted as a whale)','Diphda[8]'),(22,'Chamaeleon','1603, Uranometria, created by Keyser and de Houtman','chameleon','α Chamaeleontis'),(23,'Circinus','1763, Lacaille','compasses','α Circini'),(24,'Columba','1592, Plancius, split from Canis Major','dove','Phact'),(25,'Coma Berenices','1603, Uranometria, split from Leo','Berenice\'s hair','β Comae Berenices'),(26,'Corona Australis[9]','ancient (Ptolemy)','southern crown','Meridiana[8]'),(27,'Corona Borealis','ancient (Ptolemy)','northern crown','Alphecca'),(28,'Corvus','ancient (Ptolemy)','crow','Gienah'),(29,'Crater','ancient (Ptolemy)','cup','δ Crateris'),(30,'Crux','1603, Uranometria, split from Centaurus','southern cross','Acrux'),(31,'Cygnus','ancient (Ptolemy)','swan or Northern Cross','Deneb'),(32,'Delphinus','ancient (Ptolemy)','dolphin','Rotanev'),(33,'Dorado','1603, Uranometria, created by Keyser and de Houtman','dolphinfish','α Doradus'),(34,'Draco','ancient (Ptolemy)','dragon','Eltanin[8]'),(35,'Equuleus','ancient (Ptolemy)','pony','Kitalpha'),(36,'Eridanus','ancient (Ptolemy)','river Eridanus (mythology)','Achernar'),(37,'Fornax','1763, Lacaille','chemical furnace','Dalim[8]'),(38,'Gemini','ancient (Ptolemy)','twins','Pollux'),(39,'Grus','1603, Uranometria, created by Keyser and de Houtman','Crane','Alnair'),(40,'Hercules','ancient (Ptolemy)','Hercules (mythological character)','Kornephoros'),(41,'Horologium','1763, Lacaille','pendulum clock','α Horologii'),(42,'Hydra','ancient (Ptolemy)','Hydra (mythological creature)','Alphard'),(43,'Hydrus','1603, Uranometria, created by Keyser and de Houtman','lesser water snake','β Hydri'),(44,'Indus','1603, Uranometria, created by Keyser and de Houtman','Indian (of unspecified type)','α Indi'),(45,'Lacerta','1690, Firmamentum Sobiescianum, Hevelius','lizard','α Lacertae'),(46,'Leo','ancient (Ptolemy)','lion','Regulus'),(47,'Leo Minor','1690, Firmamentum Sobiescianum, Hevelius','lesser lion','Praecipua'),(48,'Lepus','ancient (Ptolemy)','hare','Arneb'),(49,'Libra','ancient (Ptolemy)','balance','Zubeneschamali[8]'),(50,'Lupus','ancient (Ptolemy)','wolf','α Lupi'),(51,'Lynx','1690, Firmamentum Sobiescianum, Hevelius','lynx','α Lyncis'),(52,'Lyra','ancient (Ptolemy)','lyre','Vega'),(53,'Mensa','1763, Lacaille','Table Mountain (South Africa)','α Mensae'),(54,'Microscopium','1763, Lacaille','microscope','γ Microscopii'),(55,'Monoceros','1613, Plancius','unicorn','β Monocerotis'),(56,'Musca','1603, Uranometria, created by Keyser and de Houtman','fly','α Muscae'),(57,'Norma','1763, Lacaille','carpenter\'s level','γ2 Normae'),(58,'Octans','1763, Lacaille','octant (instrument)','ν Octantis'),(59,'Ophiuchus','ancient (Ptolemy)','serpent-bearer','Rasalhague'),(60,'Orion','ancient (Ptolemy)','Orion (mythological character)','Rigel'),(61,'Pavo','1603, Uranometria, created by Keyser and de Houtman','peacock','Peacock'),(62,'Pegasus','ancient (Ptolemy)','Pegasus (mythological winged horse)','Enif'),(63,'Perseus','ancient (Ptolemy)','Perseus (mythological character)','Mirfak'),(64,'Phoenix','1603, Uranometria, created by Keyser and de Houtman','phoenix','Ankaa'),(65,'Pictor','1763, Lacaille','easel','α Pictoris'),(66,'Pisces','ancient (Ptolemy)','fishes','Alpherg'),(67,'Piscis Austrinus','ancient (Ptolemy)','southern fish','Fomalhaut'),(68,'Puppis','1763, Lacaille, split from Argo Navis','poop deck','Naos'),(69,'Pyxis','1763, Lacaille','mariner\'s compass','α Pyxidis'),(70,'Reticulum','1763, Lacaille','eyepiece graticule','α Reticuli'),(71,'Sagitta','ancient (Ptolemy)','arrow','γ Sagittae'),(72,'Sagittarius','ancient (Ptolemy)','archer','Kaus Australis'),(73,'Scorpius','ancient (Ptolemy)','scorpion','Antares'),(74,'Sculptor','1763, Lacaille','sculptor','α Sculptoris'),(75,'Scutum','1690, Firmamentum Sobiescianum, Hevelius','shield (of Sobieski)','α Scuti'),(76,'Serpens[11]','ancient (Ptolemy)','snake','Unukalhai'),(77,'Sextans','1690, Firmamentum Sobiescianum, Hevelius','sextant','α Sextantis'),(78,'Taurus','ancient (Ptolemy)','bull','Aldebaran'),(79,'Telescopium','1763, Lacaille','telescope','α Telescopii'),(80,'Triangulum','ancient (Ptolemy)','triangle','β Trianguli'),(81,'Triangulum Australe','1603 Uranometria, created by Keyser and de Houtman','southern triangle','Atria'),(82,'Tucana','1603 Uranometria, created by Keyser and de Houtman','toucan','α Tucanae'),(83,'Ursa Major','ancient (Ptolemy)','great bear','Alioth');
/*!40000 ALTER TABLE `constellations_constellation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(9,'constellations','constellation'),(5,'contenttypes','contenttype'),(8,'galaxy','galaxy'),(7,'planets','planet'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-10-29 18:15:41.637763'),(2,'auth','0001_initial','2018-10-29 18:15:55.783499'),(3,'admin','0001_initial','2018-10-29 18:15:58.939277'),(4,'admin','0002_logentry_remove_auto_add','2018-10-29 18:15:59.038602'),(5,'admin','0003_logentry_add_action_flag_choices','2018-10-29 18:15:59.119914'),(6,'contenttypes','0002_remove_content_type_name','2018-10-29 18:16:00.870695'),(7,'auth','0002_alter_permission_name_max_length','2018-10-29 18:16:01.183282'),(8,'auth','0003_alter_user_email_max_length','2018-10-29 18:16:01.394774'),(9,'auth','0004_alter_user_username_opts','2018-10-29 18:16:01.474725'),(10,'auth','0005_alter_user_last_login_null','2018-10-29 18:16:02.620542'),(11,'auth','0006_require_contenttypes_0002','2018-10-29 18:16:02.675852'),(12,'auth','0007_alter_validators_add_error_messages','2018-10-29 18:16:02.741080'),(13,'auth','0008_alter_user_username_max_length','2018-10-29 18:16:02.920902'),(14,'auth','0009_alter_user_last_name_max_length','2018-10-29 18:16:03.099976'),(15,'sessions','0001_initial','2018-10-29 18:16:03.957390'),(16,'planets','0001_initial','2018-10-30 12:47:54.282557'),(17,'galaxy','0001_initial','2018-11-02 09:08:56.464153'),(18,'galaxy','0002_auto_20181102_1921','2018-11-02 19:21:59.476074'),(19,'galaxy','0003_galaxy_distance','2018-11-02 19:37:48.426912'),(20,'constellations','0001_initial','2018-11-05 16:15:06.951866'),(21,'constellations','0002_auto_20181105_1737','2018-11-05 17:37:12.651615');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `galaxy_galaxy`
--

DROP TABLE IF EXISTS `galaxy_galaxy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `galaxy_galaxy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `galaxyName` varchar(100) NOT NULL,
  `image` varchar(500) NOT NULL,
  `constellation` varchar(100) NOT NULL,
  `origin` varchar(3000) NOT NULL,
  `notes` varchar(3000) DEFAULT NULL,
  `distance` decimal(10,5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `galaxy_galaxy`
--

LOCK TABLES `galaxy_galaxy` WRITE;
/*!40000 ALTER TABLE `galaxy_galaxy` DISABLE KEYS */;
INSERT INTO `galaxy_galaxy` VALUES (1,'Andromeda','https://en.wikipedia.org/wiki/File:Andromeda_Galaxy_(with_h-alpha).jpg','Andromeda','Andromeda, which is shortened from \"Andromeda Galaxy\", gets its name from the area of the sky in which it appears, the constellation of Andromeda.','Andromeda is the closest big galaxy to the Milky Way and is expected to collide with the Milky Way around 4 billion years from now. The two will eventually merge into a single new galaxy called Milkomeda.',2.53700),(2,'Black Eye Galaxy','https://en.wikipedia.org/wiki/File:Blackeyegalaxy.jpg','Coma Berenices','It has a spectacular dark band of absorbing dust in front of the galaxys bright nucleus, giving rise to its nicknames of the \"Black Eye\" or \"Evil Eye\" galaxy.',NULL,24.01000),(3,'Bodes Galaxy','https://en.wikipedia.org/wiki/File:Messier_81_HST.jpg','Ursa Major','Named for Johann Elert Bode who discovered this galaxy in 1774.',NULL,11.80000),(4,'Cartwheel Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Cartwheel_Galaxy.jpg/250px-Cartwheel_Galaxy.jpg','Sculptor','Its visual appearance is similar to that of a spoked cartwheel.',NULL,500.00000),(5,'Cigar Galaxy','https://en.wikipedia.org/wiki/File:M82_HST_ACS_2006-14-a-large_web.jpg','Ursa Major','Appears similar in shape to a cigar.',NULL,12.40000),(6,'Comet Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/CometGalaxy.jpg/70px-CometGalaxy.jpg','Sculptor','This galaxy is named after its unusual appearance, looking like a comet.','The comet effect is caused by tidal stripping by its galaxy cluster, Abell 2667.',3200.00000),(7,'Cosmos Redshift 7','https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Eso1524aArtist%E2%80%99s_impression_of_CR7_the_brightest_galaxy_in_the_early_Universe.jpg/70px-Eso1524aArtist%E2%80%99s_impression_of_CR7_the_brightest_galaxy_in_the_early_Universe.jpg','Sextans','The name of this galaxy is based on a redshift (z) measurement of nearly 7 (actually, z = 6.604)','Galaxy Cosmos Redshift 7 is reported to be the brightest of distant galaxies (z > 6) and to contain some of the earliest first stars (first generation; Population III) that produced the chemical elements needed for the later formation of planets and life as we know it',12900.00000),(8,'Hoags Object','https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/Hoag%27s_object.jpg/70px-Hoag%27s_object.jpg','Serpens Caput','This is named after Art Hoag, who discovered this ring galaxy.','It is of the subtype Hoag-type galaxy, and may in fact be a polar-ring galaxy with the ring in the plane of rotation of the central object.',612.80000),(9,'Large Magellanic Cloud','https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Large.mc.arp.750pix.jpg/70px-Large.mc.arp.750pix.jpg','Mensa','Named after Ferdinand Magellan','This is the fourth largest galaxy in the Local Group, and forms a pair with the SMC, and from recent research, may not be part of the Milky Way system of satellites at all',0.16300),(10,'Small Magellanic Cloud','https://upload.wikimedia.org/wikipedia/commons/thumb/7/7a/Small_Magellanic_Cloud_%28Digitized_Sky_Survey_2%29.jpg/70px-Small_Magellanic_Cloud_%28Digitized_Sky_Survey_2%29.jpg','Tucana','Named after Ferdinand Magellan','This forms a pair with the LMC, and from recent research, may not be part of the Milky Way system of satellites at all.',0.20000),(11,'Mayalls Object','https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Hubble_Interacting_Galaxy_Arp_148_%282008-04-24%29.jpg/70px-Hubble_Interacting_Galaxy_Arp_148_%282008-04-24%29.jpg','Ursa Major','This is named after Nicholas Mayall, of the Lick Observatory, who discovered it','Also called VV 32 and Arp 148, this is a very peculiar looking object, and is likely to be not one galaxy, but two galaxies undergoing a collision. Event in images is a spindle shape and a ring shape.',450.00000),(12,'Milky Way','https://upload.wikimedia.org/wikipedia/commons/thumb/4/43/ESO-VLT-Laser-phot-33a-07.jpg/70px-ESO-VLT-Laser-phot-33a-07.jpg','Sagittarius','The appearance from Earth of the galaxy – a band of light.','The galaxy containing the Sun and its Solar System, and therefore Earth.',0.00000),(13,'Pinwheel Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/M101_hires_STScI-PRC2006-10a.jpg/70px-M101_hires_STScI-PRC2006-10a.jpg','Ursa Major','Similar in appearance to a pinwheel (toy).',NULL,21.00000),(14,'Sombrero Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/M104_ngc4594_sombrero_galaxy_hi-res.jpg/70px-M104_ngc4594_sombrero_galaxy_hi-res.jpg','Virgo','Similar in appearance to a sombrero.',NULL,31.10000),(15,'Sunflower Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Messier_63_GALEX_WikiSky.jpg/70px-Messier_63_GALEX_WikiSky.jpg','Canes Venatici','Similar in appearance to a sunflower.',NULL,27.00000),(16,'Tadpole Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/UGC_10214HST.jpg/70px-UGC_10214HST.jpg','Draco','The name comes from the resemblance of the galaxy to a tadpole.','This shape resulted from tidal interaction that drew out a long tidal tail.',420.00000),(17,'Whirlpool Galaxy','https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Messier51_sRGB.jpg/70px-Messier51_sRGB.jpg','Canes Venatici','From the whirlpool appearance this gravitationally disturbed galaxy exhibits.',NULL,23.00000);
/*!40000 ALTER TABLE `galaxy_galaxy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `planets_planet`
--

DROP TABLE IF EXISTS `planets_planet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `planets_planet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `planetName` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `planets_planet`
--

LOCK TABLES `planets_planet` WRITE;
/*!40000 ALTER TABLE `planets_planet` DISABLE KEYS */;
INSERT INTO `planets_planet` VALUES (1,'Earth');
/*!40000 ALTER TABLE `planets_planet` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-05 23:31:42
