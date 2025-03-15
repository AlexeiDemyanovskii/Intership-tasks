def find_path(n, m):
    array = list(range(1, n + 1))
    path = [https://github.com/AlexeiDemyanovskii/Intership-tasks/new/main]
    index = 0

    

    while True:
        path.append(array[index])
        index = (index + m - 1) % n  # Вычисляем следующий индекс для начала нового интервала
        if array[index] in path:
            break

    return path

def main():
    if len(sys.argv) != 3:
        print("Некорректное количество аргументов. Ожидается 2 аргумента.")
        return

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    path = find_path(n, m)
    print(''.join(map(str, path)))

if __name__ == "__main__":
    main()
