import time

print(
    "------------------------------ Welcome in Kaun Banega Crore Pati ------------------------------\n"
)
KBC = [
    "1.Who is the first Prime_Minister of India ?",
    "2.Current Railway Minister of India is ?",
    "3.Which god is known as 'Gauri Nandan' ?",
    "4.What does not grow on tree according to a popular Hindi saying ?",
    "5.Which city is known as Pink City in India ?",
    "6.Who wrote India's National Anthem ?",
    "7.How many religions are there in India ?",
    "8.When is the National Hindi Diwas celebrated ?",
    "9.How many states are there in India?" "10.Where in India Gate located?",
]
KBC_ANS = [
    "\ta.Jawahar Lal Nehru\n\tb.Narendra Modi\n\tc.Manmohan Singh\n\td.Indira Gandhi",
    "\ta.Mamta Banarjee\n\tb.Ram Vilash\n\tc.Ashivini Vaishnaw\n\td.Piyush Goyal",
    "\ta.Agni\n\tb.Indra\n\tc.Hanuman\n\td.Ganesh",
    "\ta.Money\n\tb.Flowers\n\tc.Leaves\n\td.Fruits",
    "\ta.Bangalore\n\tb.Maysore\n\tc.Jaipur\n\td.Kochi",
    "\ta.Rabindranath Tagore\n\tb.Lal Bahadur Shastri\n\tc.Chetan Bhagat\n\td.RK Narayan",
    "\ta. 6\n\tb. 7\n\tc. 8\n\td. 9\n",
    "\t a. 13 September\n\tb. 14 September\n\tc. 14 July\n\td. 15 August",
    "\ta. 28\n\tb. 29\n\tc. 31\n\td. 30\n",
    "\ta.Agra\n\tb.Punjab\n\tc.Mumbai\n\td.New Delhi",
]
KBC_ANS1 = ["a", "c", "d", "a", "c", "a", "a", "b", "a", "d"]
KBC_Prize_Money = [
    1000,
    10000,
    50000,
    100000,
    1000000,
    5000000,
    10000000,
    50000000,
    100000000,
    500000000,
]
Sum = 0

for Question in range(len(KBC)):

    print(KBC[Question])
    print(KBC_ANS[Question])
    ANSWER = input("enter your choice:\t")
    if ANSWER.lower() == (KBC_ANS1[Question]):
        print('"it is correct."')
        print(f"You won {KBC_Prize_Money[Question]}rs.")
        print(f"Next, Question on your screen of {KBC_Prize_Money[Question + 1]}rs.")
        time.sleep(2)
        Sum = Sum + KBC_Prize_Money[Question]
    else:
        print("Wrong Answer")
        break
print(f"Total prize you win {Sum}rs.")
