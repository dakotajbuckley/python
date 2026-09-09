# 5.1 
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

car2 = 'toyota'
print("\nIs car2 == 'toyota' and car == 'subaru'? I predict True")
print(car2 == 'toyota' and car == 'subaru')

print("\nIs car2 == 'subaru' and car == 'subaru'? I predict False")
print(car2 == 'subaru' and car == 'subaru')

print("\nIs car2 != 'toyota'? I predict False")
print(car2 != 'toyota')

print("\nIs car != 'subaru' and car2 == 'toyota'? I predict False")
print(car != 'subaru' and car2 == 'toyota')

favorite_games = ["Hollow Knight", "Dark Souls", "Cuphead", "Silksong"]
print("\nIs 'Hollow Knight' in favorite_games? I predict True")
print('Hollow Knight' in favorite_games)

print("\nIs 'Dakota' or 'Silksong' in favorite_games? I predict True")
print('Dakota' in favorite_games or 'Silksong' in favorite_games)

print("\nIs 'Dakota' not in favorite_games? I predict True")
print('Dakota' not in favorite_games)

print("\nIs car in favorite_games? I predict False")
print(car in favorite_games)
