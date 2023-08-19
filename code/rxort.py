def binary_to_decimal(binary_str):
    decimal_value = int(binary_str, 2)
    return decimal_value

# 입력값을 공백으로 분리하여 리스트
input_str = "01000011 01000000 01110001 01110000 01101100 00111101 00111101 01000010 01110000 01110000 01101100 01000000 00111100 00111101 01110000 01000111 00111100 00111110 01000000 01101100 00111110 01000000 01000010 01101100 01110011 01110000 00111100 01000000 01101100 01000000 01000001 01000001 01110010 01110001 01101101 01000111 01110010 00111101 01000010 01000000 01000001 00111110 01110001 01000000 01000000 01000010 00111101 01000111 01000101 01110011 01101101 01000011 01000000 01000001 01110010 01000010 01101101 01000001 01000111 01101100 01000001 00111101 01000000 01110001"

# 공백으로 분리된 이진수를 10진수로 변환하여 결과 리스트를 생성
result = [binary_to_decimal(bin_str) for bin_str in input_str.split()]

# 결과 리스트를 출력
print(result)

# 리스트 안의 숫자 개수를 출력
print("리스트 안의 숫자 개수:", len(result))