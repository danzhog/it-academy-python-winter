# Создайте словарь с помощью генератора словарей,
# так чтобы его ключами были числа от 1 до 20,
# а значениями кубы этих чисел.

dictionary = {number: number**3 for number in range(1, 21)}
print(dictionary)
