import pandas as pd

def main():
    countries_data = {
        'Україна': {'population_millions': 41.2, 'area_thousand_km2': 603.5, 'capital': 'Київ', 'continent': 'Європа', 'gdp_billion': 160},
        'Польща': {'population_millions': 37.9, 'area_thousand_km2': 312.7, 'capital': 'Варшава', 'continent': 'Європа', 'gdp_billion': 679},
        'Німеччина': {'population_millions': 83.2, 'area_thousand_km2': 357.6, 'capital': 'Берлін', 'continent': 'Європа', 'gdp_billion': 4260},
        'Франція': {'population_millions': 65.5, 'area_thousand_km2': 551.7, 'capital': 'Париж', 'continent': 'Європа', 'gdp_billion': 2958},
        'США': {'population_millions': 331.9, 'area_thousand_km2': 9833.5, 'capital': 'Вашингтон', 'continent': 'Пн. Америка', 'gdp_billion': 23320},
        'Канада': {'population_millions': 38.2, 'area_thousand_km2': 9984.7, 'capital': 'Оттава', 'continent': 'Пн. Америка', 'gdp_billion': 1988},
        'Японія': {'population_millions': 125.7, 'area_thousand_km2': 377.9, 'capital': 'Токіо', 'continent': 'Азія', 'gdp_billion': 4941},
        'Індія': {'population_millions': 1408.0, 'area_thousand_km2': 3287.3, 'capital': 'Нью-Делі', 'continent': 'Азія', 'gdp_billion': 3176},
        'Китай': {'population_millions': 1444.2, 'area_thousand_km2': 9597.0, 'capital': 'Пекін', 'continent': 'Азія', 'gdp_billion': 17730},
        'Бразилія': {'population_millions': 214.3, 'area_thousand_km2': 8515.8, 'capital': 'Бразиліа', 'continent': 'Пд. Америка', 'gdp_billion': 1609}
    }

    df = pd.DataFrame.from_dict(countries_data, orient='index')
    df.index.name = 'Country'
    df.reset_index(inplace=True)

    while True:
        print("\nМЕНЮ АНАЛІЗУ ДАНИХ (DATAFRAME)")
        print("1. Вивести перші 3 рядки (head)")
        print("2. Перевірити типи даних та розмірність")
        print("3. Отримати описову статистику")
        print("4. Розрахувати та додати стовпець 'ВВП на душу населення'")
        print("5. Фільтрація (ВВП > 10 000)")
        print("6. Сортування (за ВВП)")
        print("7. Групування та середнє значення (по континентах)")
        print("8. Додаткова агрегація (макс. ВВП та унікальні континенти)")
        print("9. Вивести весь DataFrame")
        print("0. Вихід")

        choice = input("\nОберіть опцію: ")

        if choice == '1':
            print("\nПерші 3 рядки:")
            print(df.head(3))

        elif choice == '2':
            print("\nТипи даних:")
            print(df.dtypes)
            print(f"\nРозмірність: {df.shape}")

        elif choice == '3':
            print("\nСтатистика:")
            print(df.describe())

        elif choice == '4':
            df['gdp_per_capita'] = (df['gdp_billion'] * 1000) / df['population_millions']
            print("\nСтовпець додано успішно")
            print(df[['Country', 'gdp_per_capita']].head())

        elif choice == '5':
            if 'gdp_per_capita' in df.columns:
                filtered = df[df['gdp_per_capita'] > 10000]
                print("\nРезультат фільтрації (> 10k на душу)")
                print(filtered[['Country', 'gdp_per_capita']])
            else:
                print("\nПомилка: Спочатку виконайте пункт 4 (розрахунок стовпця).")

        elif choice == '6':
            sorted_df = df.sort_values(by='gdp_billion', ascending=False)
            print("\nТоп країн за ВВП:")
            print(sorted_df[['Country', 'gdp_billion']])

        elif choice == '7':
            print("\nСередні показники по регіонах:")
            try:
                print(df.groupby('continent')[['population_millions', 'gdp_billion']].mean())
            except Exception as e:
                print(f"Помилка групування: {e}")

        elif choice == '8':
            print(f"\nМаксимальний ВВП: {df['gdp_billion'].max()} млрд")
            print(f"Кількість континентів: {df['continent'].nunique()}")

        elif choice == '9':
            print("\nПовна таблиця:")
            print(df)

        elif choice == '0':
            print("Роботу завершено.")
            break

        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()