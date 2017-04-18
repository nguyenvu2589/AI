## Connect Four
Connect Four is a two-player connection game in which the players first choose a color and then take turns dropping colored discs from 
the top into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the next available space within 
the column. The objective of the game is to connect four of one's own discs of the same color next to each other vertically, horizontally,
or diagonally before your opponent. Connect Four is a strongly solved game. The first player can always win by playing the right moves.

## Specifics
You will write a program to play Connect Four. Your program will read, from standard input, a description of the current game state in 
JSON format and write, to standard output, its move in JSON format. Your will be provided a driver program and a naïve player program 
(that makes random, valid moves) that will be used to test your player program. You can also test your player program against itself 
and other student’s player programs.
An acceptable player program must:
1. Read the game state in JSON format from standard input and write the move in JSON format to standard output. 
Any desired trace or debugging information – as well as error messages – may be printed to standard error, which will be written 
to a text file.
2. Play a valid game of Connect Four. In particular, it must make valid moves in response to the current game state.
3. Consistently beat the naïve Connect Four player program provided. [The naïve player program may be the first player and – by chance 
– make optimal moves and win a game. But, this would be exceedingly rare.]

In addition, every student must play their player program against at least one other student player model. Students are encouraged to
form tournaments pitting several student player models against each other and ranking them.
You may program your player model in any programming language you like. The JSON web site has links to JSON parsers for many languages – 
there are often several available for any particular language. Your player program must be callable from the command line.
Driver Program
The driver program is written in Racket and runs under Windows, Apple OS X, and (various) Linux operating systems. You will need to 
download and install Racket for your system. It is available from the Racket web site http://racket-lang.org/. [I generally use the 64-bit
version. But, the 32-bit version is fine for this project.]
The driver program and naïve player program are available from the class Canvas page:
 connect-four-driver.rkt Driver program that plays to player programs
 connect-four-naive.rkt Naïve player program – makes random, valid moves Configuring the driver program
The driver program – connect-four-driver.rkt – can be directly edited and run from the DrRacket IDE. You don’t need to compile it.
There are several global variables at the top of the connect-four-driver.rkt file.
;;; Define grid dimensions.
(define HEIGHT 6) (define WIDTH 7)
;;; These will eventually be command line arguments.
(define exe-1 "connect-four-naive.exe")
(define args-1 "")
(define exe-2 "C:\\Program Files\\Racket\\Racket.exe") (define args-2 "connect-four-naive.rkt")
The first two, HEIGHT and WIDTH, define the size of the grid. The standard connect four grid, 6 × 7, is the default. 
The smallest size that makes sense is 4 × 4. Your program must be able to accommodate any grid size up to 16 × 16. [The maximum size 
here is totally arbitrary and you may choose to handle even larger ones.] For a tournament, you may consider a 6 × 8 grid. This may 
reduce the benefit to the first player.
The next group of four (4) define the two (2) player program command lines. Each is defined by the name of the executable program and 
any command line arguments. There are two cases: (1) If a player program is compiled as an executable – as is the first case here – you 
just give the path to that executable. In this case, there are no arguments. (2) If a player model is interpreted – such as Python or, 
as shown here, Racket – or runs in a virtual machine environment – such as Java, you give the path to the executable for the 
interpreter or VM and the arguments specific to your player model – typically the source code file (for an interpreter) or object code 
file (for a VM).
Note that this example is for a Windows environment. For an Apple OS X or Linux environment, there will not be a .exe extension for 
executable files.
It is important that the executable name be either a complete relative path from the current working directory or a complete absolute
path. Particularly, the command isn’t executed inside a command shell and it won’t search the PATH environment variable for the 
executable name. [Your mileage may vary depending on operating system, etc.]
## Compiling the naïve player program
The naïve player program can be either compiled – as in the first case above – or interpreted – as in the second case above. Generally,
I would recommend compiling a player model. This is the only possibility for compiled languages like C++. It is optional for some 
interpreted languages, like Racket, that provide both compiled and interpreted options. Java is (generally) a combination of the two. 
You compile your source code to byte code using the javac command and execute the resulting byte code using the JVM using the java 
command.
The easiest way to compile the naïve player program is to open the Rack source code file connect- four-naive.rkt in DrRacket. Then 
select “Racket > Create Execuable ...” from the menu bar. This brings up the following dialog box.
 Make sure the “Stand-alone (for this machine only, run compiled copy)” and “Racket” options are selected. Then click the “Create” 
 button to create the executable. It will take several seconds to complete. You should then have a connect-four-naive.exe file in the 
 same directory as the source code file. [Note that for Apple OS X and Linux, there will not be a .exe extension on the executable.]


## Running the driver program
At this point, you should be able to load the driver program and play to naïve player programs against each other. First, open the 
connect-four-driver.rkt file in DrRacket
Then, click on the Run button. This will start the two player programs and alternate between them sending them the current game state 
and receiving their move. This continues until either one player wins or there are no move moves, in which case the game is a draw. 
Note that the driver randomly selects one of the players to move first.
