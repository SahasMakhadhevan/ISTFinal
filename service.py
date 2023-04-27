def get_top_stats():
    movies = []
    customers = []

    return movies, customers


def get_transactions():
    transactions = []
    transactions.append(
        dict(ID='1', movieID='2', Customer='Smith', Movie='Superbad', Type='Payment', Pay_Method='Cash', Amount=6.95,
             Date='11/2/2017'))
    transactions.append(
        dict(ID='2', movieID='4', Customer='Jones', Movie='Fahr 9/11', Type='Deposit', Pay_Method='Credit card',
             Amount=3.60,
             Date='6/1/2017'))
    transactions.append(
        dict(ID='3', movieID='5', Customer='Ryder', Movie='Good Will', Type='Payment', Pay_Method='PayPal', Amount=5.78,
             Date='10/2/2017'))
    transactions.append(
        dict(ID='4', movieID='1', Customer='Walker', Movie='Spider-Man', Type='Payment', Pay_Method='Check',
             Amount=15.60, Date='5/10/2017'))
    transactions.append(
        dict(ID='5', movieID='1', Customer='Walker', Movie='Spider-Man', Type='Refund', Pay_Method='Check',
             Amount=10.00, Date='6/30/2017'))

    return transactions


def search(searchq):
    movieList = [dict(id='1', name='The Amazing  Spider-Man', year='2012'), dict(id='2', name='Superbad', year='2007'),
                 dict(id='3', name='Gone with the  Wind', year='1939'),
                 dict(id='4', name='Fahrenheit  9/11', year='2004'),
                 dict(id='5', name='Good Will  Hunting', year='1997')]
    if (searchq in movie['name'] for movie in movieList):
        return [movie for movie in movieList if searchq.lower() in movie['name'].lower()]

    return movieList


def get_movie(movie_id):
    movies = [dict(id=1, name='The Amazing Spider-Man', year=2012, number_in_stock=100, rental_or_sale_or_both='rental',
                   rental_price=1.99, sales_price=25.39, genre='Action & Adventure',
                   description='The story of Peter Parker, an outcast high schooler who  was abandoned by his parents as a boy, leaving him to be  raised by his Uncle Ben and Aunt May. Like most teenagers,  Peter is trying to figure out who he is and how he got to  be the person he is today. Peter is also finding his way  with his first high school crush, Gwen Stacy, and together,  they struggle with love, commitment, and secrets. As Peter  discovers a mysterious briefcase that belonged to his  father, he begins a quest to understand his parents  disappearance - leading him directly to Oscorp and the lab  of Dr. Curt Connors, his fathers former partner. As  Spider-Man is set on a collision course with Connors  alter-ego, The Lizard, Peter will make life-altering  choices to use his powers and shape his destiny to become a  hero.'),
              dict(id=2, name='Superbad', year=2007, number_in_stock=25, rental_or_sale_or_both='rental',
                   rental_price=0.99,
                   sales_price=10.99, genre='Comedy',
                   description='Two co-dependent high school seniors are forced to deal  with separation anxiety after their plan to stage a  booze-soaked party goes awry.'),
              dict(id=3, name='Gone with the Wind', year=1939, number_in_stock=4, rental_or_sale_or_both='both',
                   rental_price=0.99, sales_price=4.99, genre='Drama',
                   description='American classic in which a manipulative woman and a  roguish man carry on a turbulent love affair in the  American south during the Civil War and Reconstruction.'),
              dict(id=4, name='Fahrenheit 9/11', year=2004, number_in_stock=10, rental_or_sale_or_both='sale',
                   rental_price=0.99, sales_price=11.99, genre='Documentary',
                   description='Michael Moores view on what happened to the United States  after September 11; and how the Bush Administration  allegedly used the tragic event to push forward its agenda  for unjust wars in Afghanistan and Iraq.'),
              dict(id=5, name='Good Will Hunting', year=1997, number_in_stock=6, rental_or_sale_or_both='sale',
                   rental_price=0.59, sales_price=9.99, genre='Drama',
                   description='Will Hunting, a janitor at MIT, has a gift for mathematics  but needs help from a psychologist to find direction in his  life.')]

    return next((movie for movie in movies if str(movie['id']) == movie_id), None)
