# pyHocusPocus

### how it works

* Also known as the 21 card trick, this trick uses simple mathematical deduction
* using a (7x3) grid matrix, after each turn the row that is chosen, that row is now placed in the middle (like a sandwich), between either of the other rows not chosen. Then redealt to rows 1, 2, and 3. After the first round then 2 subsequent rounds, the card will be narrowed down to 33.33% of being 1 of 3 cards; the player tells your there card, you never know it until they tell you.
* Here is a Great Video from Numberpile over this trick: [21 Card Trick - Numberphile](https://youtu.be/d7dg7gVDWyg) 

## usage 
```
Windows 10
py .\Pocus.py
```
## Demo
* Screen Shots
* During Demo Recommended Card was used, but is not required. However the ending will look slightly different since you arent using the card it recommends.
![image info](./media/demo1.png)
![image info](./media/demo2.png)
![image info](./media/demo3.png)
![image info](./media/demo4.png)
#### Testing
```
comment out line 260 in Pocus.py, person_Pocus()
and uncomment line 261 test_Pocus()
Then run test-pocus.ps1
This will run 1000 tests and verify that all answers are correct.
```
* usage
```
Powershell
.\test-pocus.ps1
CMD
Powershell -ExecutionPolicy Bypass -file .\test-pocus.ps1
```
