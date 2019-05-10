# ImageToASCII

Convert images to ASCII text.

## About

A simple Python script to convert images to ASCII text using PIL.

Requirements: **Pillow (PIL)**.

## Usage

See ```py img2ascii.py -h```.

```
usage: img2ascii.py [-h] [--dest [DEST]] [--width WIDTH] [--invert]
                    [--font_ratio FONT_RATIO] [--contrast CONTRAST]
                    image

positional arguments:
  image                 Image file path.

optional arguments:
  -h, --help            show this help message and exit
  --dest [DEST]         Output text file path. Leave empty to output to
                        stdout.
  --width WIDTH         Output text width.
  --invert              Invert black and white text.
  --font_ratio FONT_RATIO
                        Specify your font's width/height ratio, if the
                        resulting image's aspect ratio is wrong.
  --contrast CONTRAST   Input higher values for more contrast (e.g. 7).
```

**Note**: Images that contain transparency might not get converted correctly!

```
py .\img2ascii.py .\demo.jpg --width 100 --contrast 21 --font_ratio 0.37 --dest demo.txt

&&&&&&&&&&&&88&&&&&&&&&&&&&&&&&&WWWW&WWWWWWWWW#MMM#*****ooaahkbqZ!<>Jmqpdhhaao***MM#WWWWWWW&&&&&&&&&
&&&&&&&&&&8&&&&&&&&&&&&&&&&&&WWWMMWWWWWWW#MMM#*****o*oaaaakbdpw0Jjl<"{/).Lqdkhoao***#M##WWWMWW&&&&&&
&&&&&&&&&&&&&&&&&&&W&&&&&WWWMWWWWWWW#MMMM#*****ooaaoaakkbdpqw0Jzx|+;..'!)cLwqpbhaaao***#M#WWWMW&&&&&
&&&&&8&&&&&&&&&&&&&&&WWMMWWWWWWM##MM*****oooaaaaakkbddqqqw0QJctI....$$.'^.tYQ0qqdbbaaaao**M##WWMWW&&
&&&&&&&&&&&&WW&&&&&WMWWWWWM##MM*****oooaoahhahkbddqpmmQLJYzur|?;  $$$$$I.^?/uYL0Zwqqdbkhao**##WWMMW&
&&&&&&&&&&W&&&&WWMMWWWMM#MM****oooaaaahaakkbddqpqZCc)[].i??+!;,'..$$$$$..':ii~|fxvv|`Xmdkaoo*##MWWMW
&&&&&&&&W&&&WWMWWWWMMMMM***ooaaaaaabkdbddpwqqqZ0LXu(^'......h&.$$$$$$$$$$$$.$.',`..'.^{Qqkhao*##MWWM
&&&&&&&&&WWWWWWW#MM***oooaahkbkdqqppppqqwZZZQQJzur1+I'.8$$$$$$$$$$$$$$$$$$$$$$$$$$$`.+xLmqhaao**##WW
&&&&&&&&WWWWWM#M#***oaaaakbdq0zvzJCJJJJYXXzccvj\}:. ' $$$$$$$$$$$$$$$$$$$$$$$$$$$$.."]tzQqdkhao*MM#W
&&&&&WMMWWWMMM****oaohkkdppZLz1.^~?[}-I.>]}{{}?~;...$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.'.'jZpbhao**##W
&&&&WWWWMM#***oaaaakkdpqqZ0JXx(<^.  ... .. .`""`..@$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$b.;1z0qbkoo***MW
&&WMWW##**oahhkkkddqpqZ0CXvf\[!`...'$$$$$$$$$....$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.{X0pbkaao**MM
&WWWMM**ahkbpqwmZ0QCCYXvf[^.^'.  $$$$$$$$$$$$$$``$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.1cLwqbkaao**M#
&MWW#*oap0CXcu}"[()+??+i.`...$$Z$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.>\cJZqpbkaao**M#
&MWW#*oap0LYcu1'}()_]?+i.^.. W$.$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.>\cJZqdbkaao**M#
&WWWMM**ahhbpqwmm0QCCYXvj}'.^`'. @$$$$$$$$$$$$$).$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$].(cLwqbkaao**M#
&&WMWW##**oahhkkkbdqqqZZCXvj\}!`....$$$$$$$$${...$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$%.(XZqbkaao**M#
&&&&WWWWMM#***oaaaakkbpqq00Czx(<`.  ...... .^""^..I$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$@.:)X0qbkoo**#MW
&&&&&WMMWWWM##***ooaahkkddpZQz1.^+?}}?l.<[11{}]~;...$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$....jZpbhao**##W
&&&&&&&&WWWWWM#M#***oaaaakbdq0ccXJCJJJJYYXzccvj/{: .,.$$$$$$$$$$$$$$$$$$$$$$$$$$$$..,]tc0qdkha**MM#W
&&&&&&&&&WWWWWWW#MM****ooaahkbkdpqppppqqwmZZQQJzur)~I'.$%$$$$$$$$$$$$$$$$$$$$$$$8$$.._xLmqhaao**##WW
&&&&&&&&W&&&WWMMWWWMMMMM***ooaaaaaabkdbdddwqwqZ0LXu(,k .....$o'$$$$$$$$$$$B.$ ',^.''.,]Qqkhao*##MWWM
&&&&&&&&&&W&&&&WWMMWWWWM#MM****oooaaaahaakkbddqpqZCv|}].+]?~!I,`..$$$$$..`:i<+|juvv\`Ymdkhao*##MWWMW
&&&&&&&&&&&&WW&&&&&WMWWWWWM##MM*****oooaoaahahkbddqpq0QQJYcur|?;. $$$$$r.^]tuJCZZqqqdbkhao**##WWMMW&
&&&&&8&&&&&&&&&&&&&&&WWWMWWWWWWW##MM#*****oooaaaahhkbdpqpwZ0Jcj>`...@$.`,'fY0mppdkkhoao**#MMWWWMWW&&
&&&&&&&&8&&&&&&&&&&W&&&&&WWWMWWWWWWW###MM#*****ooaaohakkbdppw0Jzx|+;..'!)cLwqdbhaaao***#M#WWWMW&&&&&
&&&&&&&&&&8&&&&&&&&&&&&&&&&&&WWWMMWWWWWWW#MMM#*****o*oaaaakbdpwZJj>@,1/|.Lpdkhoao***#M#MWWWMWW&&W&&&
&&&&&&&&&&&&88&&&&&&&&&&&&&&&&&&WWWWWWWWWWWWWW#MMM#*****ooaahkbpZl~+LZqpdhhaao***MM#WWWWWWW&&&&&&&&&
```

![Demo JPG](./demo.jpg)