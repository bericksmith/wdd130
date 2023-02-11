total_score = 0

def main():
    print('This program is an implementation of the Rosenberg Self-Esteem Scale. This program will show you ten statements that you could possibly apply to yourself. Please rate how much you agree with each of the statements by responding with one of these four letters:')
    print('D means you strongly disagree with the statement.')
    print('d means you disagree with the statement.')
    print('a means you agree with the statement.')
    print('A means you strongly agree with the statement.')
    print()
    question1 = input('1. I feel that I am a person of worth, at least on an\nequal plane with others.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_positive(question1,0)
    question2 = input('2. I feel that I have a number of good qualities.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_positive(question2,total_score)
    question3 = input('3. All in all, I am inclined to feel that I am a failure.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_negative(question3,total_score)  
    question4 = input('4. I am able to do things as well as most other people.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_positive(question4,total_score)
    question5 = input('5. I feel I do not have much to be proud of.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_negative(question5,total_score) 
    question6 = input('6. I take a positive attitude toward myself.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_positive(question6,total_score)
    question7 = input('7. On the whole, I am satisfied with myself.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_positive(question7,total_score)
    question8 = input('8. I wish I could have more respect for myself.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_negative(question8,total_score) 
    question9 = input('9. I certainly feel useless at times.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_negative(question9,total_score) 
    question10 = input('10. At times I think I am no good at all.\n   Enter D, d, a, or A: ')
    total_score=rosenburg_negative(question10,total_score) 



    print(f'Your score is: {total_score}')
    print()
    print('A score below 15 may indicate problematic low self-esteem.')


def rosenburg_positive(letter,total_score):
    if letter == 'D':
        score = 0
    elif letter == 'd':
        score = 1
    elif letter == 'a':
        score = 2
    elif letter == 'A':
        score = 3
    total_score += score

    return total_score

def rosenburg_negative(letter,total_score):
    if letter == 'D':
        score = 3
    elif letter == 'd':
        score = 2
    elif letter == 'a':
        score = 1
    elif letter == 'A':
        score = 0

    total_score += score

    return total_score


main()


