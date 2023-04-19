DROP DATABASE IF EXISTS syllabus_management_system;
CREATE DATABASE syllabus_management_system;
USE syllabus_management_system;

CREATE TABLE user_details
(
    account  varchar(30) not null,
    password varchar(20) not null
);

INSERT INTO user_details VALUES ("admin", "admin");

CREATE TABLE syllabus
(
    id                   int primary key auto_increment,
    major_id             varchar(20) not null,
    course_name          long varchar,
    credit_points_inECTs int,
    background_knowledge long varchar,
    textbook             long varchar,
    ref_literature       long varchar,
    course_content       long varchar,
    objectives           long varchar,
    lecture              int,
    tutorial             int,
    practical            int,
    attendance           int,
    exercise             int,
    assignment           int,
    report               int,
    midterm              int,
    final                int
);

INSERT INTO syllabus (id, major_id, course_name, credit_points_inECTs, background_knowledge, textbook, ref_literature,
                      course_content, objectives, lecture, tutorial, practical, attendance, exercise, assignment,
                      report, midterm, final)
VALUES (1, "CS", "PROBABILITIES & STATISTICS", 4, "Analysis, Integration and ODE", "[1].Spiegel R. M., Schiller J., Srinivasan R. A., Probability and Statistics, Third edition, McGraw Hill, 2009. [2].Montgomery C. D., Runger C. G., Applied Statistics and Probability for Engineers, Fifth edition, John Wileys& Sons, 2011.", "[1].Course notes, in-class exercises and homework problems.
[2].Spiegel R. M., Schiller J., Srinivasan R. A., Probability and Statistics, Third edition, McGraw
Hill, 2009.
[3].Montgomery C. D., Runger C. G., Applied Statistics and Probability for Engineers, Fifth
edition, John Wileys& Sons, 2011.
[4].Vidakovic B., Statistics for Bioengineering Sciences, Springer 2011.",
        "Basic Probability; Random Variables and Probability Distributions; Mathematical Expectation; Special Probability Distributions; Sampling Theory; Estimation Theory; Tests of Hypotheses and Significance; Curve Fitting, Regression, and Correlation; Analysis of Variance; Nonparametric Tests",
        "1. Ability to manipulate sets and events, use axioms of probability, computer probabilities of events & solve counting problems.
        2. Ability to generate random variables from experiments, use probability distribution and density
        functions, use common distributions and computer statistical quantities random variables and
        random vectors.
        3. Ability to determine the distributions and statistical quantities of random variables, to apply limit
        theorems.
        4. Ability to understand basic statistical concepts, random sampling, statistical inference, to
        regression and correlation.
        5. Ability to construct point estimation, confidence and prediction intervals.
        6. Ability to test hypotheses
        7. Ability to perform Analysis of Variance.", 25, 15, 0, 10, 10, 0, 0, 30, 50),

       (2, "CS", "ANALYSIS & ALGEBRAIC STRUCTURES", 3, "Math reasoning, expansions of the function into series",
        "[1] W. F. Trench, Introduction to real analysis (Available online). [2] Milner, Group theory, Lecture notes, 2003 (Available online for personal use)", "[1].G.Cain, J.Herod: Multivariable calculus, 1997.
[2].W. F. Trench, Introduction to real analysis (Available online)
[3].Milner, Group theory, Lecture notes, 2003 (Available online for personal use)
[4].Gedder et al., Algorithms for computer algebra, Kluwer Academic Publishers, 1992.",
        "Calculus of several variables: The limits, continuity of functions; The differentiability; The integration technics; Applications. Algebraic structures: Basic definitions; Semi groups as the flows; Groups acting on the sets; Computer algebra",
        "Basic understanding of how the multivariate calculus differs from 1D case: the double limits,
        continuity, partial derivatives, integration over the domain and curvilinear integrating technics.
        Students should be able to be familiar with some applications in the optimization problem and
        graphing visualization. Many new algebraic concepts will be introduced in the relations with ICT
        branch’ preparation: the learners should be known about the built-in structures in the networking
        basing on partitions, filters ordering of the most simple PC’ data processing.", 20, 16, 0, 5, 5, 0, 0, 20, 70),

       (3, "ICT ", "ALGORITHMS AND DATA STRUCTURES", 3, "Programming languages (C), Mathematics",
        "[1]Adam Drozdek, Data Structures and Algorithms in C++, 4th Edition, Cengage Learning, 2012",
        "[1] Adam Drozdek, Data Structures and Algorithms in C++, 4th Edition, Cengage Learning, 2012", "1. Basic Programming Concepts in C++
2. Elementary Data Structures
3. Abstract (Linear) Data Types I
4. Abstract (Linear) Data Types II
5. Recursive Algorithms
6. Trees
7. Sorting Algorithm I
8. Sorting Algorithm II
9. Searching Algorithm
10. Graphs",
        "- Understand the basic programming concepts
        - Understand analysis and design of computer algorithm and data structures
        - Analyze real-world problems and design appropriate data structures according to the problems using techniques from the course, Work individually or in a group",
        20, 0, 16, 10, 0, 30, 0, 0, 60),

       (4, "ICT", "OBJECT-ORIENTED PROGRAMMING", 3, "
- Understand fundamental concepts of programming
- Basic data types, array, string, pointer, etc,
- Basic algorithms such as sorting, searching, etc
- Have good programming style (e.g. comments, indentation, naming, etc)",
        "[1] Kathy Sierra, Bert Bates, Head First Java, 2nd Edition, O' Reilly, 2005. [2] Deitel & Deitel, Java How to Program, 9th Edition, Prentice Hall, 2011.", "[1].Kathy Sierra, Bert Bates, Head First Java, 2nd Edition, O' Reilly, 2005.
[2].Deitel&Deitel, Java How to Program, 9th Edition, Prentice Hall, 2011.
[3]. Java™ Platform, Standard Edition 7 API Specification,
http://docs.oracle.com/javase/7/docs/api/index.", "1. Course introduction - Introduce to Object-oriented programming
2. Introduction to Java programming language
3. Objects and classes - Instance variables and methods – Encapsulation
4. Objects and object references
5. Class members vs. Instance members - Java packages
6. Inheritance - Polymorphism
7. Assignment 1 presentation
8. Abstraction
9. Interfaces
10. Exceptions
11. Data structures
12. I/O Streams
13. Principles of object-oriented design
14. Assignment 2 presentation",
        "- Understand the basic principles and concepts of object-oriented programming
        - Practice how to use these concepts and principles with Java programming language
        - Apply object-oriented techniques to develop computer programs", 25, 0, 15, 10, 0, 20, 0, 0, 50),
	(5, "ICT", "OBJECT-ORIENTED PROGRAMMING", 3, "
- Understand fundamental concepts of programming 
- Basic data types, array, string, pointer, etc,
- Basic algorithms such as sorting, searching, etc 
- Have good programming style (e.g. comments, indentation, naming, etc)", "[1] Kathy Sierra, Bert Bates, Head First Java, 2nd Edition, O' Reilly, 2005. [2] Deitel & Deitel, Java How to Program, 9th Edition, Prentice Hall, 2011.", "[1].Kathy Sierra, Bert Bates, Head First Java, 2nd Edition, O' Reilly, 2005.
[2].Deitel&Deitel, Java How to Program, 9th Edition, Prentice Hall, 2011.
[3]. Java™ Platform, Standard Edition 7 API Specification, 
http://docs.oracle.com/javase/7/docs/api/index.", "1. Course introduction - Introduce to Object-oriented programming
2. Introduction to Java programming language
3. Objects and classes - Instance variables and methods – Encapsulation
4. Objects and object references
5. Class members vs. Instance members - Java packages
6. Inheritance - Polymorphism
7. Assignment 1 presentation
8. Abstraction
9. Interfaces
10. Exceptions
11. Data structures
12. I/O Streams
13. Principles of object-oriented design
14. Assignment 2 presentation", 
"- Understand the basic principles and concepts of object-oriented programming
- Practice how to use these concepts and principles with Java programming language 
- Apply object-oriented techniques to develop computer programs", 25, 0, 15, 40, 10, 20, 0, 0, 50),
	(6, "ICT", "SIGNALS AND SYSTEMS", 3, "N/A", "N/A", "[1] Signals and Systems [2nd Edition] by Alan V. Oppenheim and Alan S. Willsky. 
[2] Linear Systems and Signals [2nd Edition] by B. P. Lathi", "1. Signals, Systems, Operation/Transformations
2. Discrete time LTI system
3. Continuous LTI system
4. Properties of LTI system, Frequency Response
5. Fourier Series of Continuous-Time Periodic Signals
6. Fourier Series of Discrete-Time Periodic Signals
7. Continuous-time Fourier Transform
8. Fourier Transform: signals & systems
9. Discrete-time Fourier Transform
10. Sampling Theorem, Reconstruction/Interpolation
11. Review
12. Octave Introduction", 
"- Recognize the terminology that is used in the Signal Processing field. 
- Apply transform techniques and concepts in formulating and solving engineering problems.
- Think critically, ask", 20, 16, 0, 36, 20, 10, 0, 30, 50),
	(7, "ICT", "COMPUTER ARCHITECTURE", 3, "Digital Electronics", "[1]Computer Org and Design, 3rd Ed., Patterson &Hennessy, ©2007", "[1].Digital Design and Computer Architecture, David Money Harris.
[2].Computer Architecture: A Quantitative Approach, 3rd Edition, Hennessy & Patterson", "1. Simple Machine Implementation
2. MIPS Assembly Language
3. Memory Architecture
4. MIPS Pipeline behavior
5. Memory Architecture
6. Modern Computer Architecture
7. Memory Performance", 
"- Develop program that can use the computer architect to improve the performance", 24, 12, 0, 36, 10, 10, 0, 10, 70),
	(8, "CS", "ADVANCED COMPUTER ARCHITECTURE AND x86 ISA", 4, "N/A", "[1]. Computer Org and Design, 3rd Ed., Patterson &Hennessy, ©2007", "[1].Digital Design and Computer Architecture, David Money Harris
[2].Computer Architecture: A Quantitative Approach, 3rd Edition, Hennessy & Patterson", "1. Simple Machine Implementation
2. Memory Architecture
3. Modern Computer Architecture
4. Introduction to x86 Instruction Set",
"- Develop program that can use the computer architect to improve the performance.", 24, 16, 0, 40, 10, 10, 0, 30, 50),

	(9, "CS", "NETWORK PROGRAMMING", 4, "N/A", "[1]. Unix Network Programming, Volume 1: The Sockets Networking API, 3rd Edition (2003), by W. 
Richard Stevens et al.", "[1]. Unix Network Programming, Volume 1: The Sockets Networking API, 3rd Edition (2003), by W. Richard Stevens et al", "1. Introduction
2. OSI models
3. Routing and network services
4. Socket programming: Setup, Data Transfer, Message Framing, Disconnection
5. Blocking and Non-blocking sockets
6. Socket multiplexing",
"- Understand the OSI reference model and a variety of network protocols.
- Implement specific network programming constructs on Unix platforms to create robust realworld sockets-based applications.
- Design and implement client/server programs using a variety of protocols and platforms.
- Apply the concepts of the C programming language to the construction of moderately complex software implementation problems.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),

(10, "MATH", "ALGORITHMS AND DATA STRUCTURES", 3, "Programming languages (C), Mathematics", "[1]Adam Drozdek, Data Structures and Algorithms in C++, 4th Edition, Cengage Learning, 2012", "[1] Adam Drozdek, Data Structures and Algorithms in C++, 4th Edition, Cengage Learning, 2012", "1. Basic Programming Concepts in C++
2. Elementary Data Structures 
3. Abstract (Linear) Data Types I
4. Abstract (Linear) Data Types II
5. Recursive Algorithms
6. Trees
7. Sorting Algorithm I
8. Sorting Algorithm II
9. Searching Algorithm
10. Graphs", 
"- Understand the basic programming concepts
- Understand analysis and design of computer algorithm and data structures
- Analyze real-world problems and design appropriate data structures according to the problems using techniques from the course, Work individually or in a group",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(11, "MATH", "DISCRETE MATHEMATICS", 3, "N/A", "[1].Kenneth A. Rosen, Charles R. B. Wright: Discrete Mathematics and Its Applications, 6th Edition, Mc Graw Hill (2007).", "[1]. Kenneth A. Rosen, Charles R. B. Wright: Toán rời rạc ứng dụng trong tin học (bản dịch bởi Phạm 
Văn Thiều và Đặng Hữu Thịnh), NXB Nhà xuất bản Giáo dục, Hà Nội (2007). 
[2]. Susanna S. Epp: Discrete Mathematics with Applications, 4th Edition, Brooks/Cole Publishing 
Company (2010). 
[3]. Bender, E. A., Williamson, S. G.: A Short Course in Discrete Mathematics, ISBN 0-486-43946-
1, Dover (2005).", "1. Logic and Proofs, Sets
2. Introduction and Recursion
3. Counting
4. Advanced Counting Techniques
5. Relations
6. Boolean Algebra", 
"- Comprehend and use propositional and predicate logic. 
- Understand naive set theory, set operations. 
- Use concepts of relations; perform various operations with relations and functions (congruence, methods of proof, induction, recursion, etc..). 
- Solve problems in combinatorics (permutations, combinations, etc..). 
- Providing knowledge to learning other topics: Probabilities, Cryptography, Algorithm & Data Structures, Databases,..",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(12, "MATH", "NUMERICAL METHODS", 3, "N/A", "N/A", "[1]. Atkinson, Kelldan E.: An introduction to Numerical Analysis, 2rd Edition, Wiley, ISBN-10: 
0471624896; ISBN-13: 978-0471624899 (1989)
[2]. Hildebrand, F. B.: Introduction to Numerical Analysis, 2nd Edition McGraw-Hill, ISBN 0-070-28761-
9, (1974).
[3]. Leader, Jeffery J.: Numerical Analysis and Scientific Computation, Addison Wesley, ISBN 0-201-
73499-0 (2004). 
[4]. Robert J. Schilling, Sandra L. Harries: Applied Numerical Methods for Engineers using MATLAB 
and C, 3rd edition Thomson Brooks/Cole, ISBN-10: 0534370144; ISBN-13: 9780534370145 (2000).", "1. Sets Introduction, Errors in Computation
2. Interpolation and Approximation
3. Numerical solution of Non-linear Equations
4. Solution of system of linear algebraic equations
5. Numerical integration and differentiation
6. Solution of ordinary differential equations (ODE)
7. Numerical solution of Partial differential equations (PDE)", 
"- Understand the gap between theory and practice in computer science. 
- Know some algorithms in Numerical methods. 
- Have abilities to deploy or develop a Numerical method.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(13, "ICT", "BASIC DATABASES", 3, "N/A", "[1] Database Systems: The Complete Book (2nd Edition). Hector Garcia-Molina, Jeff Ullman, and 
Jennifer Widom. Prentice Hall, 2008
[2] Database Systems: A Practical Approach to Design, Implementation, and Management (6th Edition). Thomas Connolly and Carolyn Begg. Addison-Wesley, 2014.", "[1]. Database Systems: Design, Implementation, and Management (11st Edition). Carlos Coronel,Steven Morris. Cengage Learning, 2014
[2]. Database System Concepts (6th Edition). Avi Silberschatz, Henry F. Korth, S. Sudarshan.McGraw-Hill, 2010", "1. Introduction to databases
2. Relational Algebra
3. Basic SQL
4. More SQL
5. Constraints
6. Transactions, Views, Indexes
7. SQL Programming
8. Design Theory for Relational Databases
9. Entity-Relationship Model
10. 10. Other High Level Design Languages
11. SQL Authorization
12. Group Project
13. Group Project Presentation",
"- Understand basic database concepts and theories.
- Understand basic techniques of relational database programming.
- Apply relational modeling in database design",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(14, "ICT", "COMPUTER NETWORKS", 4, "N/A", "[1] Andrews S. Tannebaum, Computer Networks, 4th edition, Prentice Hall, 2002.
[2] CCNA : Cisco Networking Academy Program", "[1]. Larry L. Peterson, Computer Networks: A system approach, Morgan Kaufmann, 2011.
[2]. J. Kurose and K. Ross, Computer Networking: A Top-down approach, Addison-Wesley, 2009.", "1. Introduction to Networking & Internet 
2. Networking models 
3. Networking fundamentals 
4. Physical Layer 
5. Link Layers and Local Area Networks 
6. Network Layers and Routing 
7. Transport Layers 
8. Application Layers 
9. Project Presentation",
"- Understand the basic design, history and the evolution of the Internet and computer networks,
- Describe the key industry standards that define the Internet,
- Explain how digital messages are transported across physical network media through various wired/ wireless technologies and protocols,
- Understand the relationship between the Internet infrastructure, protocols and networked applications,
- Understand the fundamental characteristics of packet-switched data networks and the key protocols that make up the TCP/IP communications suite,
- Understand the key components and design principles associated with wide area networks as used by ISPs to deliver global network services,
- Configure the basic software and hardware required to operate/ support and troubleshoot network services,
- Get prepared for the advanced computer networks and network security courses.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(15, "ICT", "SOFTWARE ENGINEERING", 3, "The C/C++ programming language, UML", "[1]. Software Engineering, Ian Sommerville, 8th Edition, Addison Wesley Press, 2007", "[1].Software Engineering, Ian Sommerville, 8th Edition, Addison Wesley Press, 2007
[2].Software Engineering: A Practitioner's Approach, R.S. Pressman, McGraw-Hill, 2010
[3].G. Booch, J. Rumbaugh, and I. Jacobson, The Unified Modeling Language User Guide, 2nd edition, 
Addison-Wesley, 2005
[4].UML Tutorial: http://www.sparxsystems.com.au/uml-tutorial.html
[5].StarUML – A software modeling tool: http://staruml.sourceforge.net/en/", "1. Course introduction – Background information – Introduction to software engineering 
2. Socio-Technical Systems - Critical Systems 
3. Software Processes 
4. Software Requirements and Requirements Engineering Processes 
5. System Models 
6. Critical Systems Specification
7. Design Principles and Architectural Design 
8. User Interface Design 
9. Implementation 
10. Verification, Validation, and Testing 
11. Project Management
12. Final exam",
"- Describe the history of the term “software engineering” and explain its current meaning and importance
- Explain well-known software development process models 
- Select, with justification, a software development process which is most appropriate for the development and maintenance of a diverse range of software products
- Use a common, semi-formal method (for example, UML diagrams) to specify the requirements of a moderately sized software product 
- Conduct software design using an accepted program design methodology such as UML 
- Distinguish between different types and levels of testing (for instance, unit, integration, systems, and acceptance) for medium-size software products
- Discuss various testing techniques such as white box and black box testing 
- Discuss key principles and common methods for software project management such as scheduling, size estimation, cost estimation and risk analysis
- Get familiar with CASE tools and/or environments including UML drawing tools and IDEs",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(16, "ICT", "OPERATING SYSTEMS", 4, "C programming language", "[2].Andrew Tanenbaum, Modern Operating Systems, Prentice Hall
[3].William Stallings, Operating Systems, Prentice Hall
[4].Harvey M. Deitel, An introduction to operating systems. Addison-Wesley", "N/A", "1. Introduction to Operating Systems
2. Operating-System Structures
3. Processes
4. Threads
5. CPU Scheduling
6. Process Synchronization
7. Deadlocks
8. Memory Management
9. Virtual Memory
10. File-System Interface",
"- Know about the roles and the major components of Operating Systems.
- Understandwell the concurrency, the scheduling algorithm in Operating Systems.
- Understandmajor problems in Operating Systems such as deadlocks, synchronization,...andsolutions to these issues.
- Explain and implement virtual memory.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(17, "ICT", "DIGITAL SIGNAL PROCESSING", 4, "N/A", "N/A", "[1] Digital Signal Processing [4th Edition] by John G. Proakis and Dimitris G. Manolakis 
[2] Digital Signal Processing Using MATLAB [3rd Edition] by Vinay K. Ingle and John G. Proakis 
[3] Discrete-Time Signal Processing [3rd Edition] by Alan V. Oppenheim and Ronald W. Schafer 
[4] Signals and Systems [2nd Edition] by Alan V. Oppenheim and Alan S. Willsky", "1. Signals and Frequency
2. Difference Equation, Discrete-Time Fourier Transform, Sampling and Quantization
3. Z-transform
4. Inverse z-transform
5. Discrete Fourier Transform
6. Signal analysis and synthesis using DFT
7. Fast Fourier Transform
8. Digital Filters
9. FIR	and	IIR	filters
10. Interpolation and multi-rate systems, Digital Processors
11. Projects",
"- Recognize the terminology that is used in the Digital Signal Processing (DSP) field. 
- Apply transform techniques and concepts in formulating and solving engineering problems. 
- Analyze basic DSP building blocks: digital filters, spectrum analyzers, sample rate converters (upsampling and down-sampling), and the fast Fourier transform (FFT) algorithm. 
- Design and synthesize these building blocks and use them effectively in applications. 
- Think critically, ask questions, and apply problem solving techniques.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(18, "ICT", "MOBILE WIRELESS COMMUNICATION", 3, "N/A", "[1]. Mischa Schwartz: Mobile Wireless Communication, CAMBRIDGE UNIVERSITY PRESS, 1st Edition (2005). 
[2]. Wireless Communications: Principles and Practice (2nd Edition) by Theodore S. Rappaport", "N/A", "1. Introduction
2. Cellular concept and channel allocation
3. Multiple Access techniques
4. Second Generation Mobile Network System
5. 2.5/3G Mobile Network System
6. Wireless	LANs and personal-area networks",
"- Know the basic principles of wireless and mobile network.
- Understand basic wireless and mobile network protocol, mobile wireless management.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(19, "ICT", "SOFTWARE TESTING AND QUALITY ASSURANCE", 3, " Software Engineering", "[1] P. Ammann and J. Offutt. Introduction to Software Testing. Cambridge University Press, 2008. ISBN 978-0-521-88038-1", "[1] P. Ammann and J. Offutt. Introduction to Software Testing. Cambridge University Press, 2008. ISBN 978-0-521-88038-1", "1. Overview
2. Mathematical Background
3. Testing theory
4. Reviewing technique
5. Boundary testing
6. Equivalence testing
7. Decision table testing
8. Black box testing
9. Model-based testing
10. White box testing
11. Control flow testing
12. Data flow testing",
"- Provide an introduction to the software engineering testing process
- Describe the quality assurance process and its role in software development.
- The student will be instructed in a variety of testing techniques, methods, and tools.
- The student will be able to describe the state of the practice verification and validation techniques.
- The student will demonstrate proficiency in managing a software project to customer requirements.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(20, "ICT", "IMAGE PROCESSING", 3, "N/A", "[1] Solomon, Chris, and Toby Breckon. Fundamentals of Digital Image Processing: A practical approach with examples in Matlab. John Wiley & Sons, 2011. 
[2] Petrou, Maria, and Costas Petrou. Image processing: the fundamentals. John Wiley & Sons, 2010.", "N/A", "1. Course Introduction
2. Introduction to Matlab for Image Processing
3. Color Representation
4. Image transform
5. Assignment Presentation 1
6. Point Processing
7. Spatial filtering
8. Edge detection
9. Mathematical morphology
10. Assignment Presentation 2",
"- Understand the basic principles and concepts of image processing 
- Practice how to use these concepts and principles with Matlab",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(21, "ICT", "WEB APPLICATION DEVELOPMENT", 4, "N/A", "[1]. P. J. Deitel and H. M. Deitel; Internet & World Wide Web: How to Program 4th Edition, Prentice Hall, 2007, ISBN: 0131752421.
[2]. Sam Ruby, Agile Web Development with Rails 4, Pragmatic Bookshelf, 2013, ISBN: 978-1-93778-556-7", "[1].P. J. Deitel and H. M. Deitel; Internet & World Wide Web: How to Program 4th Edition, Prentice Hall, 2007, ISBN: 0131752421.
[2].Drupal Documentation, https://www.drupal.org/documentation
[3].Sam Ruby, Agile Web Development with Rails 4, Pragmatic Bookshelf, 2013, ISBN: 978-1-93778-556-7.
[4].Michal Zalewski, The Tangled Web: A Guide to Securing Modern Web Applications, No Starch Press, ISBN: 9781593273880", "1. Introduction to World Wide Web
2. Hypertext Markup Language (HTML)
3. Cascading Style Sheets (CSS)
4. Javascript
5. jQuery
6. Bootstrap
7. Assignment 1 Presentation
8. PHP & MySQL
9. CodeIgniter
10. XML
11. REST
12. Web security
13. Trend in Web technologies
14. Assignment 2 Presentation",
"- Understand background in Web technologies
- Understand principles in developing client and server sides of Web applications
- Have skills to develop Web applications with HTML, CSS, Javascript, and PHP
- Describe emerging trends in Web environments",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(22, "ICT", "DISTRIBUTED SYSTEMS", 3, "N/A", "[1]. Tanenbaum et al., Distributed systems: principles and paradigms, 2nd Edition, Pearson.", "[1]. Tanenbaum et al., Distributed systems: principles and paradigms, 2nd Edition, Pearson", "1. Introduction to Distributed Systems
2. Communication in Distributed Systems
3. Remote Procedure Call
4. Message Passing Interface
5. Map-Reduce Pattern
6. Distributed File Systems
7. Virtualization and Cloud Computing",
"- Understand the contrasting features between the distributed view of computing with the centralized one.
- Understand in detail how a few exemplar distributed applications work and what requirements they aim to satisfy. 
- Understand in detail how a few exemplar distributed applications work and what issues and challenges they must contend with. 
- Acquire practical skills in analyzing distributed applications. 
- Acquire practical skills in discovering, describing and classifying some of the fundamental concepts in distributed systems.",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(23, "ICT","COMPUTATIONAL THEORY", 4, "N/A", "[1] John Hopcroft, Rajeev Motowani, and Jeffrey Ullman, Automata Theory, Languages, and 
Computation. (Third Edition)", "[2] Thomas Sudkamp, Languages and Machines: An Introduction to the Theory of Computer Science. 
(Third Edition)", "1. Introduction
2. Mathematical background
3. Regular language and Finite Automata
4. Context-free languages
5. Computability and Turing machine
6. Complexity, P and NP",
"- Acquire a full understanding and mentality of Automata Theory as the basis of all computer science languages design.
- Have a clear understanding of the Automata theory concepts such as RE's, DFA's, NFA's, Stack's, Turing machines, and Grammars",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(24, "ICT", "BASICS PRINCIPLES OF PROJECT MANAGEMENT", 1, "N/A", "[1] Basics of Project Management
[2] Student Workbook: Fundamentals of Project Management, First edition1998
[3] James P. Lewis: Fundamentals of Project Management, Third edition, 2007
[4] Joseph Heagney: Fundamentals of Project Management, Fourth edition, 2011
[5] http://www.writeawriting.com/academic-writing/research-projectproposal", "N/A", "1. Project Introduction
2. Project management Basics
3. Scientific Research Project (3hours). Basic Scientific Research and Applied Research",
"- Identify basic steps of a project management
- Understand how to manage and organize a project
- Apply knowledge to a sample research project",
        20, 0, 16, 10, 0, 30, 0, 0, 60),
(25, "CS", "INTELLECTUAL PROPERTY MANAGEMENT", 2, "N/A", "[1] Erbisch FH. Basic workbook on intellectual property management. Published by Institute of International Agriculture, Michigan State University, USA, 2005
[2] Junghans C, Levy A. Intellectual property management : A guide for scientists, engineers, financiers, and managers. Weinheim: WileyVCH, 2006.", "N/A", "1. Introduction to intellectual property and its associated rights 
2. World intellectual property scene 
3. Protecting intellectual property
4. Protecting intellectual property
5. An intellectual property management office
6. Intellectual property agreements
7. How to search patents on selected databases
8. How to write and keep a laboratory notebook",
"- define terminology and concepts in IPRs and their management 
- identify different types of IP, the rights of ownership, scope of protection as well as the ways to create and to extract value from IP 
- recognize the important role of IP in organizations of different sectors for the purposes of product and technology development
- get an overview of the world IP scene; related IP conventions and treaties
- understand at a basic level about Vietnamese laws and regulations governing IPRs
- identify important components of an IP policy
- be familiar with the activities of an IP management office
- recognise several types of IP agreements and how to 
negotiate an IP agreement
- search scientific information and patent on online databases
- write and keep a laboratory notebook for IP protection",
        20, 0, 16, 10, 0, 30, 0, 0, 60);
SELECT *
FROM syllabus;

CREATE FUNCTION compareFuzzy(actual LONG VARCHAR, expected LONG VARCHAR) RETURNS BOOLEAN
    DETERMINISTIC
    RETURN IF(expected = '', TRUE, actual=expected OR actual REGEXP expected)