-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 06, 2020 at 10:51 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quizapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `historyquestions`
--

CREATE TABLE `historyquestions` (
  `question_no` int(11) NOT NULL,
  `question` text NOT NULL,
  `option1` text NOT NULL,
  `option2` text NOT NULL,
  `option3` text NOT NULL,
  `option4` text NOT NULL,
  `answer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `historyquestions`
--

INSERT INTO `historyquestions` (`question_no`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`) VALUES
(1, 'The Gupta Saka was founded by', 'Chandra Gupta the First', 'Samudra Gupta', 'Kumara Gupta', 'Chandra Gupta the Second', 1),
(2, 'By the Act of 1773 Parliament granted a loan of ______ to the East India Company.', 'Rs 480,000', 'Rs 400,000', 'Rs 500,000', 'Rs 300,000', 2),
(3, 'August Offer 1940 was made by the Viceroy', 'Lytton', 'Willingdon', 'Linlithgow', 'Minto', 3),
(4, 'Nastaliq was', 'a raga composed by Tansen', 'a manual of code of conduct for the Ulemas', 'a Persian script used in Medieval India', 'a cess levied by the Mughal rulers', 3),
(5, 'Who had paned the Vernacular Press Act into law?', 'Lord Lytton', 'Lord Hardinge', 'Lord Dalhousie', 'Lord Mayo', 1),
(6, 'The fourth and the last Buddhist Council was convened by', 'Ashoka', 'Kanishka', 'Huvishka', 'Menander', 2),
(7, 'The first Swarajist Conference was held at', 'Allahabad', 'Ahmedabad', 'Bardoli', 'Madras', 1),
(8, 'Which of the following was the main part of Aurobindos programme to achieve independence?', 'Constitutional agitation', 'Organisation of secret societies', 'Passive resistance', 'Terrorism', 3),
(9, 'Humayun died in the year', '1556', '1546', '1536', '1566', 1),
(10, 'The concept of Eight-Cold Path forms the theme of', 'Dharmachakrapravartana Sutta', 'Mahaparinibban Sutta', 'Dipavamsa', 'Divyavadana', 1),
(11, 'Name the religious personality who exercised a great influence over Shivaji', 'Guru Nanak Dev', 'Mirabai', 'Tukaram', 'Guru Ram Das', 4),
(12, 'The Government of India Act of 1935 consists of ______ sections and 10 schedules.', '321', '330', '331', '300', 1),
(13, 'The Buddhist monk who spread Buddhism in Tibet was', 'Nagarjuna', 'Padmasambhava', 'Asanga', 'Ananda', 2),
(14, 'Of the following European nations, only the ______ did not attempt to establish trading centres in India.', 'French', 'Italians', 'Dutch', 'Britishers', 2),
(15, 'The Mughal troops were largely drawn from', 'Tributary Chiefs', 'Central Contingents', 'The Rajput Chiefs', 'Mansabdars', 4),
(16, 'Who was the founder of the Boy Scouts and Civil Guides movement in India?', 'Baden Powell', 'Charles Andrew', 'Richard Temple', 'Robert Montgomery', 1),
(17, 'The later Vedic Age means the age of the compilation of', 'Samhitas', 'Aranyakas', 'All the above', 'Brahmanas', 3),
(18, 'Aurangzeb died in the year', '1707', '1700', '1760', '1764', 1),
(19, 'As per Wavells Plan the external affairs would be under the charge of ______.', 'An Indian Member of the Executive Council', 'Secretary of State', 'Viceroy', 'Parliament', 1),
(20, 'What was the capital of Shivajis Kingdom?', 'Karwar', 'Pune', 'Purandhar', 'Raigarh', 4),
(21, 'Babarnama was written by', 'Babar', 'Abul Fazl', 'Humayun', 'Akbar', 1),
(22, 'Madras was returned by the French to the British in 1748 by the Treaty of', 'London', 'Paris', 'Delhi', 'Aix-la-Chapelle', 4),
(23, 'Mahabandula was the great General of the', 'Nepalese', 'Marathas', 'Sikhs', 'Burmese', 4),
(24, 'Who had been the first to emphasise the instruction in Literature and science through the English Language was essential for building a modern India?', 'Ishwar Chandra Vidyasagar', 'GK Gokhale', 'MM Malaviya', 'Raj Ram Mohun Roy', 4),
(25, 'Tashkent Agreement was signed between India and Pakistan in the year', '1950', '1970', '1966', '1960', 3),
(26, 'A great astronomer and mathematician during the Gupta period was', 'Varahamihira', 'Vagabhatta', 'Bhanugupta', 'Aryabhatta', 4),
(27, 'The school of Indian art which is also known as the Greco-RomanBuddhist art is the _______ school', 'Mauryan', 'Gandhara', 'Shunga', 'Gupta', 2),
(28, 'Which Sultan of Delhi died while playing the chaugon (Polo)?', 'Qutub-ud-din Aibak', 'Ghiyasuddin Balban', 'Samsuddin Iltutmish', 'Nasiruddin Mahmood', 1),
(29, 'Who was the court poet of Harshavardhana?', 'Bhani', 'Bana', 'Ravi Kirti', 'Vishnu Sharma', 2),
(30, 'The Indus people were worshippers of', 'Indra', 'Mothers Goddess', 'Varuna', 'Rudra', 2),
(31, 'The members of the Board of Control must be paid from', 'Indian Revenues', 'The Consolidated Fund of England', 'Funds Voted by Parliament', 'The revenues of Princely States', 1),
(32, 'Among the numerous followers of Gandhis philosophy was, were', 'Bertrand Russell', 'Khan Abdul Gaffar Khan', 'All of the above', 'Marshal Tito', 2),
(33, 'The Indica was written by', 'Megasthanes', 'Kautilya', 'Patanjali', 'Panini', 1),
(34, 'Vivian Derozio had been associated with the ______ movement.', 'Young India', 'Young Bengal', 'Swadeshi', 'Back to the Vedas', 2),
(35, 'Who was not among the three revolutionaries who were hanged on March 23, 1931?', 'Sukhdev', 'Rajguru', 'Azad', 'Bhagat Singh', 3),
(36, 'The earliest evidence of silver in India is found in the', 'Silver punchmarked coins', 'Chalcolitchic cultures of western India', 'Vedic Texts', 'Harappan culture', 2),
(37, 'The subject-matter of Ajanta Paintings pertains to', 'Shaivism', 'Buddhism', 'Vaishnavism', 'Jainism', 2),
(38, 'Who was the ruler of Chittor, when Alauddin Khalji attacked and conquered it in 1303 aD?', 'Rana Kumbha', 'Rana Sanga', 'Rana Ratan Singh', 'Rana Hammir', 3),
(39, 'The Gupta king who assumed the title of Vikramaditya was', 'Kumaragupta', 'Chandragupta-II', 'Samudragupta', 'Skandagupta', 2),
(40, 'Shivajis Agra Adventure was planned by', 'Jai Singh', 'Shayista Khan', 'Afzal Khan', 'Mir Jumla', 1),
(41, 'Who composed the song Sare Jahan Se Achha Hindostan hamara?', 'Bhagat Singh', 'Josh Malihabadi', 'Chandra Shekhar Azad', 'Mohammed Iqbal', 4),
(42, 'The crop which was not known to Vedic people is', 'rice', 'barley', 'tobacco', 'wheat', 2),
(43, 'The caste system of India was created for :', 'occupational division of labour', 'economic uplift', 'recognition of the dignity of labour', 'immobility of labour', 1);

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `question_no` int(11) NOT NULL,
  `question` varchar(255) NOT NULL,
  `option1` varchar(255) NOT NULL,
  `option2` varchar(255) NOT NULL,
  `option3` varchar(255) NOT NULL,
  `option4` varchar(255) NOT NULL,
  `answer` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `questions`
--

INSERT INTO `questions` (`question_no`, `question`, `option1`, `option2`, `option3`, `option4`, `answer`) VALUES
(1, 'What is the smallest bone in the body ?', 'Patella', 'Stirrup', 'Thigh', 'Teeny', 2),
(2, 'What is the name of the biggest part of the human brain ?', 'Cerebrum', 'Cerebellum', 'Brainstem', 'None of these', 3),
(3, 'How many bones does an adult human have ?', '500', '110', '206', '55', 3),
(4, 'How many bones an adult human skeleton consists of ?', '204 bones', '206 bones', '208 bones', '214 bones', 2),
(5, 'In the human body,blood enters the aorta of the circulatory system from the', 'Left atrium', 'Left Ventricle', 'Right atrium', 'Right Ventricle', 2),
(6, 'How much of the volume of urine is produced in an adult human every 24 hours ?', '1 litre', '1.5 litres', '3 litres', '5 litres', 2),
(7, 'In which part of an eye a pigment is present which is responsible for brown,blue or black eyes ?', 'Cornea', 'Choroid', 'Iris', 'Vitreous Body', 3),
(8, 'Name the gland which controls blood pressure ?', 'Thalamus Gland', 'Adrenal Gland', 'Thyroid Gland', 'Pancreas Gland', 2),
(9, 'In which organ of the human body are the lymphosytes cells are formed ?', 'Liver', 'Bone Marrow', 'Pancreas', 'Spleen', 2),
(10, 'A human disorder cretinism is caused due to the under secretion of', 'Adrenalin hormone', 'Cortisone hormone', 'Glucagon hormone', 'Thyroxin hormone', 4),
(11, 'What percentage of the human body is water ?', '0.3', '0.8', '0.6', 'None of these', 3),
(12, 'How many lungs does the human body have ?', 'Four', 'Two', 'One', 'None of these', 2),
(13, 'What is the longest bone in the human body ?', 'Fibula', 'Tibia', 'Femur', 'None of these', 3),
(14, 'Cell or tissue death within a living body is called as', 'Neutrophilia', 'Nephrosis', 'Necrosis', 'Neoplasia', 3),
(15, 'When we eat something we like, our mouth waters.This is actually not water but fluid secreted from', 'Nasals Gland', 'Oval Epithelium', 'Salivery Gland', 'Tongue', 3),
(16, 'Which of the following is known as the voice box ?', 'Trachea', 'Pharynx', 'Epiglottis', 'Larynx', 4),
(17, 'What is the smallest bone in the human body ?', 'Stapes', 'Spine', 'Clavicle', 'None of these', 1),
(18, 'How many teeth does a normal adult human have ?', '20', '24', '32', '44', 2),
(19, 'What tissue connects to muscles to bone ?', 'Skin', 'Tendons', 'Joints', 'None of these', 2),
(20, 'Where in the body are new blood cells made ?', 'Heart', 'Bone Marrow', 'Liver', 'None of these', 2),
(21, 'What is the average heart beat in a human body per minute ?', '72', '75', '78', '80', 1),
(22, 'The contractile protiens in a muscles are ', 'Actin and Myosin', 'Actin and Tropomyosin', 'Myosin and Troponin', 'Troponin and Tropomyosin', 1),
(23, 'Which of the following is not a part of small intestine ?', 'Caecum', 'Duodenum', 'Jejunum', 'Ileum', 1),
(24, 'What is the human bodys largest external organ ?', 'Stomach', 'Skin', 'Liver', 'None of these', 2),
(25, 'Cartilage present in body is ', 'A Muscular Tissue', 'An Epithelial Tissue', 'A Connective Tissue', 'A Germinal Tissue', 3),
(26, 'Which one among the following glands is presents in pairs in human body ?', 'Adrenal', 'Liver', 'Pancreas', 'Pineal', 1),
(27, 'During the process of respiration in human beings ,the exchange of gases takes place in ', 'Bronchi', 'Alveoli', 'Bronchiole', 'Pleura', 2),
(28, 'How many parts is the hearts divided into ?', '8', '4', '2', 'None of these', 3),
(29, 'What is the shape of DNA called ?', 'Multiple helix', 'Single helix', 'Double helix', 'None of these', 3),
(30, 'What is the weakest muscle in the human body ?', 'Uretus', 'Gluteus Maximus', 'Stapedius', 'None of these', 3),
(31, 'In human beings,the opening of the stomach into the small intestine is called ', 'Caecum', 'Ileum', 'Oesophagus', 'Pylorus', 4),
(32, 'What is the body temperature of a normal man ?', '81.1 degree celsius', '36.9 degree celsius', '98.6 degree celsius', '21.7 degree celsius', 2),
(33, 'Which of the following helps in clotting the blood ?', 'Vitamin B1', 'Vitamin B2', 'Vitamin D', 'VitaminK', 4),
(34, 'What is the main component of bones and teeth ?', 'Calcium carbonate', 'Calcium phosphate', 'Calcium sulphate', 'Calcium nitrate', 2),
(35, 'The main constituent of hemoglobin is ', 'Chlorine', 'Iron', 'Calcium', 'None of these', 2),
(36, 'Which of the following have maximum calorific value ?', 'Carbohydrates', 'Fats', 'Protiens', 'Vitamins', 1);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `score` int(11) NOT NULL,
  `dp` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `name`, `email`, `password`, `score`, `dp`) VALUES
(1, 'Debashis Naskar', 'debanaskar13@gmail.com', 'deba86178001', 50, 'shahrukh.png'),
(2, 'Chandan Naskar', 'chandan@gmail.com', '123456', 50, 'govinda.png'),
(3, 'Anurupa Naskar', 'anurupa@gmail.com', '654987', 60, 'actress.png'),
(4, 'Debabrata Naskar', 'debosuvo@gmail.com', '258741', 0, 'ayushman.png'),
(5, 'Mrinmay Naskar', 'mri777@gmail.com', '986321455', 0, 'varun.png'),
(6, 'Suman Ghosh', 'suman@gmail.com', '147852', 20, 'background.png'),
(8, 'Soumik Pal', 'soumik@gmail.com', '123456', 0, 'akshay.png'),
(9, 'Santu  Senapati', 'santu@gmail.com', '123456789', 0, 'katrina.png'),
(10, 'Kushal Gowshami', 'kushal@gmail.com', '147852', 0, 'shraddha kapoor.png'),
(12, 'Nayan Pal', 'nayan@gmail.com', '5214', 0, 'newsbackground.png'),
(13, 'fsdaf', 'debashis@gmail.com', '159357', 0, 'varun.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `historyquestions`
--
ALTER TABLE `historyquestions`
  ADD PRIMARY KEY (`question_no`);

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`question_no`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `historyquestions`
--
ALTER TABLE `historyquestions`
  MODIFY `question_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=73;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `question_no` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
