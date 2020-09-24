-- phpMyAdmin SQL Dump
-- version 4.0.10deb1ubuntu0.1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: 23/09/2020 às 21:18
-- Versão do servidor: 5.5.62-0ubuntu0.14.04.1
-- Versão do PHP: 5.5.9-1ubuntu4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Banco de dados: `data`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alembic_version`
--

CREATE TABLE IF NOT EXISTS `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

CREATE TABLE IF NOT EXISTS `alunos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) CHARACTER SET latin1 COLLATE latin1_general_ci NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `resultado` varchar(10) NOT NULL,
  `media` float NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=229 ;

--
-- Fazendo dump de dados para tabela `alunos`
--

INSERT INTO `alunos` (`id`, `nome`, `cpf`, `resultado`, `media`) VALUES
(1, 'AIURY AUDREY NASCIMENTO SANTOS', '2056296608', '0', 0),
(2, 'ALTIERRES WASHINGTON MAGALHAES FERREIRA', '2520096144', '0', 0),
(3, 'BRENDA SANTOS FARIAS', '14355729630', '74.45', 46.7117),
(4, 'CARLOS EDUARDO GONCALVES VIEIRA', '13979767647', '1.0', 67.3),
(5, 'CARLOS EDUARDO PEREIRA DE ARAUJO', '11437237673', '0', 0),
(6, 'CLAUDINEIA RIBEIRO PAIVA', '11154132609', '0', 0),
(7, 'DANIEL DURAES ALVES NETO', '13042178684', '0', 0),
(8, 'DEBORA CARLOS SOARES', '10932392636', '0', 0),
(9, 'DENILSON NERES SANTOS JUNIOR', '13212956690', '0', 0),
(10, 'DIEGO DA SILVA CARNEIRO', '12181975604', '0', 0),
(11, 'DIEGO NUNES BRITO', '13418431658', '0', 0),
(12, 'EDICARLOS FERREIRA DA SILVA JUNIOR', '14993206631', '0', 0),
(13, 'HEMERSON CHARLES MADUREIRA MACEDO', '9467437627', '0', 0),
(14, 'JACKSON WILLER MACEDO DUARTE', '13703613602', '0', 0),
(15, 'JOAO PEDRO JESUS SANTOS VIEIRA', '11492479675', '0', 0),
(16, 'JOSE GUILHERME MAGALHAES SILVA', '10727855603', '0', 0),
(17, 'LARISSE BATISTA DE MELO ROCHA', '13250541605', '0', 0),
(18, 'LUCAS ALMEIDA DE JESUS', '14139414600', '0', 0),
(19, 'LUCAS DE JESUS SUMIYA', '47740607800', '0', 0),
(20, 'LUCELIO CAMPOS SANTOS', '11377133648', '0', 0),
(21, 'LUIS HENRIQUE ALVES ABADIE', '13681854602', '0', 0),
(22, 'MATEUS FREIRE FERREIRA', '46553536864', '0', 0),
(23, 'MURILO CORREA BORGES', '13601623641', '0', 0),
(24, 'OTACILIO CESAR FERREIRA DA SILVA FILHO', '11555436617', '0', 0),
(25, 'PAULO CESAR SOARES FERREIRA', '12446972659', '0', 0),
(26, 'RUBENS ALMEIDA BRAGA JUNIOR', '13412991635', '0', 0),
(27, 'SAMUEL ROCHA AGUIAR', '12155917643', '0', 0),
(28, 'THAINNA GABRIELY DE FRANCA SILVA', '7058948607', '0', 0),
(29, 'VINICIUS RODRIGUES SILVA                                                                            ', '16215187798', '0', 0),
(30, 'VITOR PEREIRA DE OLIVEIRA', '14560586659', '0', 0),
(31, 'FARLEY VINICIUS DA SILVA LIMA', '11168148626', '0', 0),
(32, 'IARA FARIA VITORIA', '9211658624', '0', 0),
(33, 'MAIKE JORDAN RODRIGUES DA SILVA', '12061177611', '0', 0),
(34, 'WELLISON TIAGO GONCALVES MOURA', '9631090655', '0', 0),
(35, 'WESLEY SEBASTHIAN DIAS MAGALHAES', '12251421645', '0', 0),
(36, 'ARLEY OLIVEIRA DA MOTA', '13109943662', '0', 0),
(37, 'DANIEL MAGALHAES HOED', '12507303689', '0', 0),
(38, 'DOUGLAS DE CASTRO MARTINS', '10917430611', '0', 0),
(39, 'EVANDRA ALMEIDA SANTOS', '12824085690', '0', 0),
(40, 'FERNANDO BARBOSA MELO', '12390342612', '0', 0),
(41, 'JOAO PEDRO VIANA GUIMARAES', '11566978670', '0', 0),
(42, 'KELVIM MELO DUARTE', '13237347671', '0', 0),
(43, 'LIDIANE DE SOUZA MIRANDA', '11218526610', '0', 0),
(44, 'MARCELO DE CARVALHO PEREIRA DA SILVA', '11282654608', '0', 0),
(45, 'RAYSSA RAMOS FERREIRA', '12215321628', '0', 0),
(46, 'THIAGO SANTOS LIMA', '11394213603', '0', 0),
(47, 'WALISSON FARIAS FRANCA', '10710139632', '0', 0),
(48, 'ALEXANDRE SANTOS RODRIGUES', '12814395688', '0', 0),
(49, 'ALEX MARQUES FERREIRA', '14382623618', '0', 0),
(50, 'ALEX RODRIGUES BARBOSA', '13705496603', '0', 0),
(51, 'ANA LUIZA DE SOUZA PIMENTA', '9962524601', '0', 0),
(52, 'CAMILLA MAGALHAES GALVAO', '12445311624', '0', 0),
(53, 'CHRISTIAN SALES ARAUJO SILVA', '13312555620', '0', 0),
(54, 'DAVID HIAGO SILVA OLIVEIRA', '13934251609', '0', 0),
(55, 'EMANUEL ARRUDAS DE MACEDO', '11145866689', '0', 0),
(56, 'GEOVANA ABREU DOS SANTOS', '9952172621', '0', 0),
(57, 'JOAO PAULO SANTOS PEREIRA', '4474028627', '0', 0),
(58, 'LARISSA CRISTINE CARNEIRO ARAUJO', '12502890683', '0', 0),
(59, 'LARISSA FAGUNDES LOPES', '13700648618', '0', 0),
(60, 'LINCONN ALVES LIMA', '13471630694', '0', 0),
(61, 'LUCIMARIO DA SILVA MATOS', '13401152637', '0', 0),
(62, 'MATHEUS HENRIQUE SANTOS DOS REIS', '2111538698', '0', 0),
(63, 'NATHALIA FELIX DA SILVA', '14355045692', '0', 0),
(64, 'NEIVALDO LOPES DE OLIVEIRA', '2008506606', '0', 0),
(65, 'NEVITON CARLOS DE JESUS JUNIOR', '13932402677', '0', 0),
(66, 'RAYANE SOUZA BARBOSA', '11605317659', '0', 0),
(67, 'RONEIDE DE OLIVEIRA FERREIRA', '14142480677', '0', 0),
(68, 'SUELI DE SOUZA CAMPOS', '8150143688', '0', 0),
(69, 'ANTONIO MESQUITA DA COSTA                                                                           ', '32314351886', '0', 0),
(70, 'AQUILLA ODLANIER FARIA NASCIMENTO', '9551920643', '0', 0),
(71, 'CAIO VINICIUS DE SOUZA NUNES', '12137752646', '0', 0),
(72, 'JANIELLY ARAUJO LOPES', '10011456663', '0', 0),
(73, 'JARDEL LOPES FERREIRA', '11368501630', '0', 0),
(74, 'JEAN CARLOS DIAS DA SILVA', '10836697618', '0', 0),
(75, 'JOSIMAR PEREIRA SANTANA', '7748362610', '0', 0),
(76, 'LIDIANE RIBEIRO NUNES', '8166256622', '0', 0),
(77, 'MARIANA FIGUEIREDO DA MOTA', '11816913626', '0', 0),
(78, 'WANDER KENNEDY BATISTA CORDEIRO', '11936537621', '0', 0),
(79, 'WELLINGTON GONCALVES FERREIRA BRITO', '11498588697', '0', 0),
(80, 'BRENO DE ALMEIDA RODRIGUES', '13686524686', '0', 0),
(81, 'CLEITON RODRIGUES DE OLIVEIRA', '12053525622', '0', 0),
(82, 'DOUGLAS SANTANA DE SOUZA', '8245333646', '0', 0),
(83, 'FABIO PEREIRA MAGALHAES', '11019342633', '0', 0),
(84, 'IGOR PEREIRA DE ALMEIDA', '12581460610', '0', 0),
(85, 'JEANNE ROCHA DE ALMEIDA', '12413652612', '0', 0),
(86, 'JEFFERSON FERREIRA DE ALMEIDA', '12677588641', '0', 0),
(87, 'JOAO MAIK FERREIRA', '10182019632', '0', 0),
(88, 'JOSUE DE SOUZA ORMUNDO JUNIOR', '11756574685', '0', 0),
(89, 'LUCAS EUGENIO DIAS COSTA', '10026104601', '0', 0),
(90, 'MARCOS DANIEL VIEIRA DE SOUZA', '12130262619', '0', 0),
(91, 'THAIS BARBOSA', '12799833616', '0', 0),
(92, 'THALLYS LISBOA SIMOES', '12590743661', '0', 0),
(93, 'VICTOR FELIPE DOS REIS OLIVEIRA', '12686566663', '0', 0),
(94, 'ANANDA PEREIRA SA', '13015021621', '0', 0),
(95, 'ANTONIO RODRIGO BATISTA MOURA', '12445307600', '0', 0),
(96, 'DARLAN FERREIRA DE JESUS', '10411786628', '0', 0),
(97, 'DAYVISON MARLEY NUNES SILVA', '10702597643', '51.88', 60.9383),
(98, 'EVANIO GABRIEL DE SOUZA FRANCISCO', '12247793630', '0', 0),
(99, 'EWERTON CARDOSO SILVA', '8007085637', '0', 0),
(100, 'FABIO HENRIQUE MESQUITA DE ALMEIDA', '12048522602', '0', 0),
(101, 'FELIPE DOS SANTOS OLIVEIRA', '12487334606', '0', 0),
(102, 'GABRIEL MENDES DE MELO', '33359076800', '0', 0),
(103, 'JAQUELINE PEREIRA SILVA', '11917145608', '0', 0),
(104, 'JOICE FERREIRA PASSOS', '7998205636', '0', 0),
(105, 'JOVAI BIZERRA DA SILVA', '13233724667', '0', 0),
(106, 'KELY PEREIRA CORREA', '12454768666', '0', 0),
(107, 'MAURICIO PEREIRA DE JESUS', '12173367617', '0', 0),
(108, 'MICHELE SOUZA RODRIGUES', '12530671630', '0', 0),
(109, 'NILCILAINE LOPES DA MOTA', '13516318619', '0', 0),
(110, 'RAFAEL RAMOS ALVES', '12647198683', '0', 0),
(111, 'RODRIGO MARQUES CAMPOS', '13374077633', '0', 0),
(112, 'VICTOR TOME ABREU', '12582953695', '0', 0),
(113, 'WESLEY DA SILVA RODRIGUES', '13093113660', '0', 0),
(114, 'ALEX BRUNO RODRIGUES COSTA', '7097869640', '0', 0),
(115, 'ANDREWS DAVIDSON MARTINS RIBAS', '11503760669', '0', 0),
(116, 'EMERSON SANTOS FARIAS', '13497237620', '0', 0),
(117, 'FAGNER VIEIRA DE ALMEIDA', '12691268659', '0', 0),
(118, 'FARLEY PEREIRA DA SILVA', '9511197614', '0', 0),
(119, 'JANE GONCALVES VIEIRA', '10956781675', '0', 0),
(120, 'JARDEL MOTA SILVA', '11356856659', '0', 0),
(121, 'JOICE OLIVEIRA ANDRADE', '10919648665', '0', 0),
(122, 'JOSEMAR GONCALVES BEZERRA FILHO', '11975381602', '0', 0),
(123, 'MANOEL ALEXANDRE TAVARES SILVA', '12085599664', '0', 0),
(124, 'MAURICIO SANTOS', '12162407604', '0', 0),
(125, 'ALANA KESSIA MATOS DE OLIVEIRA', '11358862613', '0', 0),
(126, 'CAIO BELINO LOPES', '10213644606', '0', 0),
(127, 'CAIO CESAR FERREIRA RAMOS', '10546757677', '0', 0),
(128, 'CAIO GABRIEL DE OLIVEIRA FARIAS', '10919669662', '0', 0),
(129, 'DAVID EDSON GONCALVES NEVES', '10742386643', '0', 0),
(130, 'DIOGO SOARES RODRIGUES', '10705423697', '0', 0),
(131, 'DOUGLAS LACERDA XAVIER', '13409147608', '0', 0),
(132, 'EDENILSON FERNANDES DA SILVA', '10836701666', '0', 0),
(133, 'EMERSON PEREIRA OLIVEIRA', '12568061618', '0', 0),
(134, 'GUILHERME MARTINS LEITE', '12465105612', '0', 0),
(135, 'IARA SIMOES DA SILVA', '11379446686', '0', 0),
(136, 'JOAO PAULO GOMES DE ARAUJO MAGALHAES', '12931022616', '0', 0),
(137, 'JOHN KEVIN SILVA VIEIRA', '9956356689', '0', 0),
(138, 'LUANA NATIELLE COSTA LEAL', '12935597680', '0', 0),
(139, 'LUIZ PHILIP DIAS FERREIRA', '13226317601', '0', 0),
(140, 'ORLANDO DE SOUZA CARNEIRO NETO', '12580897690', '0', 0),
(141, 'RAIANE GOMES DOS SANTOS', '5278977108', '0', 0),
(142, 'SILLAS LACERDA XAVIER', '13994467624', '0', 0),
(143, 'WANDERSON RANGEL PEREIRA DE SOUZA', '13233753683', '0', 0),
(144, 'WIEDER SANTOS CASTRO', '11673756611', '0', 0),
(145, 'ALINE FERREIRA DA CONCEICAO', '11597804630', '0', 0),
(146, 'AMAURI PEREIRA DE JESUS', '11684086604', '0', 0),
(147, 'DIEGO ALVES DA COSTA', '6204238620', '0', 0),
(148, 'ERIKA MARIA DOS SANTOS', '11455817651', '0', 0),
(149, 'IGOR GUEDES RIBEIRO', '10707185645', '0', 0),
(150, 'KESIA CORREIA SILVA', '11794996621', '0', 0),
(151, 'MICILENE BISPO SANTOS', '11474212697', '0', 0),
(152, 'VINICIUS DIAS DE SOUZA', '9494093674', '0', 0),
(153, 'AMANDA DA SILVA COIMBRA', '13675190633', '0', 0),
(154, 'ANA LUIZA LACERDA LOPES', '10406130639', '0', 0),
(155, 'CAIO XAVIER MAIA', '12085129609', '0', 0),
(156, 'CHIRLEY NUNES PEREIRA DOS SANTOS', '12790790612', '0', 0),
(157, 'CLAUDIO HENRIQUE SOUZA SANTOS', '12579531688', '0', 0),
(158, 'DAYPSON LUCAS ALVES LIMA', '13597961690', '0', 0),
(159, 'DIEGO ASSIS LOPES DOS SANTOS', '11752434692', '0', 0),
(160, 'FABIO JUNIOR SANTOS FERREIRA', '9641283650', '0', 0),
(161, 'GERALDO DE OLIVEIRA E SILVA NETO', '10929840623', '0', 0),
(162, 'GUILHERME LUIS VIANA ALVES                                                                          ', '46687585827', '0', 0),
(163, 'JOAO VICTOR MELO LIMA', '13709724660', '0', 0),
(164, 'JOELI DE OLIVEIRA MOTA', '5039346662', '0', 0),
(165, 'LUCAS DE MOURA MACEDO', '13937779612', '0', 0),
(166, 'MARCELO HENRIQUE GUIMARAES DA SILVA JUNIOR', '12692985699', '0', 0),
(167, 'MARCO ALVES DE ALMEIDA', '13815192617', '0', 0),
(168, 'MAURILIO NUNES MAGALHAES', '11327148692', '0', 0),
(169, 'MICHELLE NAYARA SILVA', '12601107618', '0', 0),
(170, 'RAPHAELLA CANGANE DA SILVA FERRAZ', '10926571699', '0', 0),
(171, 'SANDY APARECIDA DE OLIVEIRA DE ARAUJO', '13921544645', '0', 0),
(172, 'TAINA RODRIGUES DA ROCHA', '13855651604', '0', 0),
(226, 'PROFESSOR TADS', '12358963222', '0', 0),
(228, 'VALDIRENE NUNES DA SILVA ', '10702597645', '0', 0);

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplina`
--

CREATE TABLE IF NOT EXISTS `disciplina` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) NOT NULL,
  `periodo` int(2) NOT NULL,
  `nomeData` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `periodo` (`periodo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=38 ;

--
-- Fazendo dump de dados para tabela `disciplina`
--

INSERT INTO `disciplina` (`id`, `nome`, `periodo`, `nomeData`) VALUES
(1, 'Algoritmo', 1, 'Algoritmo'),
(2, 'Fundamentos da Computação', 1, 'Fundamentos_Computacao'),
(3, 'Inglês Técnico', 1, 'Ingles'),
(4, 'Logica Matemática', 1, 'Logica_Matematica'),
(5, 'Matemática Computacional', 1, 'Matematica_Computacional'),
(6, 'Língua Portuguesa', 1, 'Lingua_Portuguesa'),
(7, 'Teoria Geral da Administração', 1, 'TGA'),
(8, 'Arquitetura e Organização', 2, 'Arquitetura_Organizacao'),
(9, 'Banco de Dados I', 2, 'Banco_Dados_I'),
(10, 'Modelos e Paradigmas de Programação', 2, 'Modelos_Paradigmas_Programacao'),
(11, 'Programação Estruturada', 2, 'Programacao_Estruturada'),
(12, 'Sistemas Operacionais', 2, 'Sistemas_Operacionais'),
(13, 'Banco de Dados II', 3, 'Banco_Dados_II'),
(14, 'Estatísticas', 3, 'Estatisticas'),
(15, 'Programação Orientada a Objeto', 3, 'Programacao_Orientada_Objeto'),
(16, 'Programação Web I', 3, 'Programacao_Web_I'),
(17, 'Redes de Computadores I', 3, 'Redes_Computadores_I'),
(18, 'Analise e Projeto de Sistema', 4, 'Analise_Projeto_Sistema'),
(19, 'Engenharia de Software', 4, 'Engenharia_Software'),
(20, 'Programação Web II', 4, 'Programacao_Web_II'),
(21, 'Programação de Sistemas Corporativos', 4, 'Programacao_Sistemas_Corporativos'),
(22, 'Redes de Computadores II', 4, 'Redes_Computadores_II'),
(23, 'Arquitetura de Software', 5, 'Arquitetura_Software'),
(24, 'Auditoria e Segurança', 5, 'Auditoria_Seguranca'),
(25, 'Empreendedorismo', 5, 'Empreendedorismo'),
(26, 'Gerencia de Projetos ', 5, 'Gerencia_projetos'),
(27, 'Interface Homem Maquina', 5, 'Interface_Homem_Maquina'),
(28, 'Introdução a Contabilidade', 5, 'Contabilidade'),
(29, 'Processo Unificado De Sistemas', 5, 'Processo_Unificado'),
(30, 'Gerência de Recursos Informacional', 6, 'Gerencia_Recursos_Informacional'),
(31, 'Legislação Aplicada', 6, 'Legislacao_Aplicada'),
(32, 'Metodologias Ágeis', 6, 'Metodologias_Ageis'),
(33, 'Metodologia Cientifica', 6, 'Metodologia_Cientifica'),
(34, 'Qualidade de Software', 6, 'Qualidade_de_Software'),
(35, 'Seminários', 6, 'Seminarios'),
(36, 'Tópicos Especiais', 6, 'Topicos_Especiais'),
(37, 'Fundamentos de Sistemas de\r\nInformação', 2, 'Fundamentos_Sistemas_Informacao');

-- --------------------------------------------------------

--
-- Estrutura para tabela `disciplinas_alunos`
--

CREATE TABLE IF NOT EXISTS `disciplinas_alunos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_disciplinas` int(11) NOT NULL,
  `nomeDisciplina` varchar(50) NOT NULL,
  `resultado` varchar(11) NOT NULL,
  `id_alunos` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_aluno_disciplina` (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=45 ;

--
-- Fazendo dump de dados para tabela `disciplinas_alunos`
--

INSERT INTO `disciplinas_alunos` (`id`, `id_disciplinas`, `nomeDisciplina`, `resultado`, `id_alunos`) VALUES
(1, 18, '18  Analise e Projeto de Sistema', '67.54', 97),
(2, 1, '1  Algoritmo', '30.56', 97),
(3, 19, '19  Engenharia de Software', '67.3', 97),
(4, 17, '17  Redes de Computadores I', '46.63', 97),
(5, 19, '19  Engenharia de Software', '22.27', 97),
(6, 35, '35  Seminários', '74.45', 97),
(7, 20, '20  Programação Web II', '76.83', 3),
(8, 27, '27  Interface Homem Maquina', '23.72', 3),
(9, 27, '27  Interface Homem Maquina', '23.72', 3),
(10, 18, '18  Analise e Projeto de Sistema', '24.12', 97),
(11, 16, '16  Programação Web I', '57.48', 97),
(12, 16, '16  Programação Web I', '57.48', 97),
(13, 16, '16  Programação Web I', '57.48', 97),
(14, 26, '26  Gerencia de Projetos ', '69.6', 97),
(15, 26, '26  Gerencia de Projetos ', '69.6', 97),
(16, 26, '26  Gerencia de Projetos ', '69.6', 97),
(17, 32, '32  Metodologias Ágeis', '84.91', 97),
(18, 32, '32  Metodologias Ágeis', '84.91', 97),
(19, 19, '19  Engenharia de Software', '67.3', 97),
(20, 19, '19  Engenharia de Software', '67.3', 97),
(21, 19, '19  Engenharia de Software', '67.3', 97),
(22, 19, '19  Engenharia de Software', '67.3', 97),
(23, 35, '35  Seminários', '74.45', 97),
(24, 35, '35  Seminários', '74.45', 97),
(25, 35, '35  Seminários', '74.45', 97),
(26, 35, '35  Seminários', '74.45', 97),
(27, 19, '19  Engenharia de Software', '67.3', 97),
(28, 19, '19  Engenharia de Software', '67.3', 97),
(29, 1, '1  Algoritmo', '63.85', 97),
(30, 17, '17  Redes de Computadores I', '46.63', 97),
(31, 19, '19  Engenharia de Software', '67.3', 97),
(32, 19, '19  Engenharia de Software', '67.3', 97),
(33, 19, '19  Engenharia de Software', '67.3', 4),
(34, 18, '18  Analise e Projeto de Sistema', '67.54', 97),
(35, 18, '18  Analise e Projeto de Sistema', '67.54', 97),
(36, 18, '18  Analise e Projeto de Sistema', '67.54', 97),
(37, 32, '32  Metodologias Ágeis', '4.72', 3),
(38, 20, '20  Programação Web II', '76.83', 3),
(39, 18, '18  Analise e Projeto de Sistema', '4.39', 97),
(40, 17, '17  Redes de Computadores I', '46.63', 97),
(41, 35, '35  Seminários', '74.45', 3),
(42, 16, '16  Programação Web I', '1.0', 4),
(43, 21, '21  Programação de Sistemas Corporativos', '57.65', 97),
(44, 33, '33  Metodologia Cientifica', '51.88', 97);

-- --------------------------------------------------------

--
-- Estrutura para tabela `periodo`
--

CREATE TABLE IF NOT EXISTS `periodo` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `nome` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Fazendo dump de dados para tabela `periodo`
--

INSERT INTO `periodo` (`id`, `nome`) VALUES
(1, '1º Periodo'),
(2, '2º Periodo'),
(3, '3º Periodo'),
(4, '4º Periodo'),
(5, '5º Periodo'),
(6, '6º Periodo');

-- --------------------------------------------------------

--
-- Estrutura para tabela `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(250) NOT NULL,
  `celular` varchar(11) NOT NULL,
  `cpf` varchar(11) NOT NULL,
  `email` varchar(250) NOT NULL,
  `nomeUsuario` varchar(50) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `celular` (`celular`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nomeUsuario` (`nomeUsuario`),
  UNIQUE KEY `cpf` (`cpf`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `celular`, `cpf`, `email`, `nomeUsuario`, `tipo`, `senha`) VALUES
(1, 'DAYVISON MARLEY NUNES SILVA', '38992047149', '10702597643', 'dayvison99@hotmail.com', 'DAYVISON99', 'admin', 'secretamarley99'),
(3, 'PETRÔNIO SILVA', '99999999999', '11111111111', 'petronio@gmail.com', 'petronio', 'admin', '123');

--
-- Restrições para dumps de tabelas
--

--
-- Restrições para tabelas `disciplina`
--
ALTER TABLE `disciplina`
  ADD CONSTRAINT `disciplina_periodo` FOREIGN KEY (`periodo`) REFERENCES `periodo` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
