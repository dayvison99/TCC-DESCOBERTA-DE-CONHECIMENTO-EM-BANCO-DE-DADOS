-- phpMyAdmin SQL Dump
-- version 4.0.10deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tempo de Geração: 21/01/2019 às 23:59
-- Versão do servidor: 5.5.60-0ubuntu0.14.04.1
-- Versão do PHP: 5.5.9-1ubuntu4.25

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
-- Estrutura para tabela `disciplina`
--

CREATE TABLE IF NOT EXISTS `disciplina` (
  `id` int(2) NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `periodo` int(2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `periodo` (`periodo`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=37 ;

--
-- Fazendo dump de dados para tabela `disciplina`
--

INSERT INTO `disciplina` (`id`, `nome`, `periodo`) VALUES
(1, 'Algoritmo', 1),
(2, 'Fundamentos da Computação', 1),
(3, 'Inglês Técnico', 1),
(4, 'Lógica Matemática', 1),
(5, 'Matemática Computacional', 1),
(6, 'Língua Portuguesa', 1),
(7, 'Teoria Geral da Administração', 1),
(8, 'Arquitetura e Organização', 2),
(9, 'Banco de Dados I', 2),
(10, 'Modelos e Paradigmas de Programação', 2),
(11, 'Programação Estruturada', 2),
(12, 'Sistemas Operacionais', 2),
(13, 'Banco de Dados II', 3),
(14, 'Estatísticas', 3),
(15, 'Programação Orientada a Objeto', 3),
(16, 'Programação Web I', 3),
(17, 'Redes de Computadores I', 3),
(18, 'Analise e Projeto de Sistema', 4),
(19, 'Engenharia de Software', 4),
(20, 'Programação Web II', 4),
(21, 'Programação de Sistemas Corporativos', 4),
(22, 'Redes de Computadores II', 4),
(23, 'Arquitetura de Software', 5),
(24, 'Auditoria e Segurança', 5),
(25, 'Empreendedorismo', 5),
(26, 'Gerencia de Projetos ', 5),
(27, 'Interface Homem Maquina', 5),
(28, 'Introdução a Contabilidade', 5),
(29, 'Processo Unificado De Sistemas', 5),
(30, 'Gerência de Recursos Informacional', 6),
(31, 'Legislação Aplicada', 6),
(32, 'Metodologias Ágeis', 6),
(33, 'Metodologia Cientifica', 6),
(34, 'Qualidade de Software', 6),
(35, 'Seminários', 6),
(36, 'Tópicos Especiais', 6);

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
  `cpf` varchar(14) NOT NULL,
  `email` varchar(250) NOT NULL,
  `nomeUsuario` varchar(50) NOT NULL,
  `tipo` varchar(10) NOT NULL,
  `senha` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`),
  UNIQUE KEY `celular` (`celular`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `nomeUsuario` (`nomeUsuario`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Fazendo dump de dados para tabela `usuario`
--

INSERT INTO `usuario` (`id`, `nome`, `celular`, `cpf`, `email`, `nomeUsuario`, `tipo`, `senha`) VALUES
(1, 'Dayvison Nunes', '38992047149', '107.025.976-43', 'dayvison99@hotmail.com', 'DAYVISON99', 'admin', 'secreta123'),
(2, 'Clarice Santos Pereira', '38999363231', '122.125.369-73', 'claricesantos031@gmail.com', 'clarice', 'padrao', 'secreta123'),
(3, 'Petrônio Silva', '99999999999', '111.111.111-11', 'petronio@gmail.com', 'petronio', 'admin', '123');

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
