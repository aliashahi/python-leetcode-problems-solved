


def calc():
    MAZAYA = 1710000
    BASE = 6510000
    HOUR_COUNT = 167
    ATTENDED_HOUR = 118.5

    print("Paye :","{:,.0f} Tuman". format(BASE))
    print("Mazaya :","{:,.0f} Tuman". format(MAZAYA))
    print("Aspected Hour:","{} Hour". format(HOUR_COUNT))
    print("Attended Hour:","{} Hour". format(ATTENDED_HOUR))
    print("Subtraction :","{} Hour". format(HOUR_COUNT - ATTENDED_HOUR))
    print("-"*50)

    ALL_INCOME = MAZAYA + BASE

    LOST_ON_LESS_HOUR = BASE * ((HOUR_COUNT - ATTENDED_HOUR)/HOUR_COUNT)
    LOST_ON_LESS_HOUR += (BASE * 0.27) * ((HOUR_COUNT - ATTENDED_HOUR)/HOUR_COUNT)

    ALL_INCOME -= BASE * 0.03
    ALL_INCOME -= LOST_ON_LESS_HOUR
    print("what is left : {:,.0f} Tuman". format(ALL_INCOME - ALL_INCOME%1000))
    
if __name__ == '__main__':
    calc()
    