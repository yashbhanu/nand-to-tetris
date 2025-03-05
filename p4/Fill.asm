// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/4/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

//// Replace this comment with your code.
(MLOOP)

@KBD
D=M
@FALSE
D;JEQ
@R1
M=-1
@CEND
0;JMP
(FALSE)
@R1
M=0
(CEND)


@SCREEN
D=A
@R0
M=D

(LOOP)
@R1
D=M
@R0
A=M
M=D
@R0
M=M+1
@KBD
D=A
@R0
D=D-M
@LOOP
D;JGT


@MLOOP
0;JMP