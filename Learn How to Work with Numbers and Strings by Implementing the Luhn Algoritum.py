def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1] #[::-1] reversed the all data
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit) #数値や文字列を整数型に変換する

    sum_of_even_digits = 0　#パラメーター
    even_digits = card_number_reversed[1::2] #偶数位を記録
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10) #商　と　剰余　の数値を足す
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    #print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1241'
    card_translation = str.maketrans({'-': '', ' ': ''})　　#読み取るデータにある’-’と" "を置き換え　　文字列の変換テーブルするため
    translated_card_number = card_number.translate(card_translation)#一緒に使う　str.maketrans({'-': '', ' ': ''})
  
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
