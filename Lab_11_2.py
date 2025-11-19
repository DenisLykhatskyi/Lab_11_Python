import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def load_data(filename):
    try:
        df = pd.read_csv(filename, parse_dates=['Date'], dayfirst=True, index_col='Date')
        df = df.dropna(axis=1, how='all')
        return df
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return None

def show_plot(df):
    numeric_df = df.select_dtypes(include=['number'])
    
    if numeric_df.empty:
        print("Немає даних для побудови графіка.")
        return

    print("Побудова загального графіка для всіх велодоріжок...")
    
    numeric_df.plot(figsize=(15, 10))
    
    plt.title("Використання велодоріжок за рік")
    plt.xlabel("Дата")
    plt.ylabel("Кількість велосипедистів")
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.show()

def main():
    filename = 'comptage_velo_2017.csv'
    df = load_data(filename)

    if df is None:
        return

    while True:
        print("\nМЕНЮ АНАЛІЗУ ВЕЛОДОРІЖОК (2017)")
        print("1. Вивести перші 5 рядків")
        print("2. Вивести інформацію про типи даних")
        print("3. Описова статистика")
        print("4. Загальна кількість велосипедистів за рік")
        print("5. Кількість велосипедистів по кожній доріжці")
        print("6. Визначити найпопулярніший місяць (для перших 3-х доріжок)")
        print("7. ПОКАЗАТИ ГРАФІК")
        print("0. Вихід")

        choice = input("\nВаш вибір: ")

        if choice == '1':
            print("\nПерші 5 рядків:")
            print(df.head())

        elif choice == '2':
            print("\nInfo:")
            print(df.info())

        elif choice == '3':
            print("\nDescribe:")
            print(df.describe())

        elif choice == '4':
            total = df.sum(numeric_only=True).sum()
            print(f"\nЗагальна кількість велосипедистів: {total:.0f}")

        elif choice == '5':
            print("\nСума по кожній доріжці:")
            print(df.sum(numeric_only=True))

        elif choice == '6':
            print("\nНайпопулярніші місяці:")
            numeric_df = df.select_dtypes(include=['number'])
            monthly_data = numeric_df.resample('ME').sum()
            
            check_cols = numeric_df.columns[:3]
            
            for path in check_cols:
                max_date = monthly_data[path].idxmax()
                max_val = monthly_data.loc[max_date, path]
                print(f"Доріжка '{path}': {max_date.strftime('%B')} ({max_val:.0f})")

        elif choice == '7':
            show_plot(df)

        elif choice == '0':
            print("Роботу завершено.")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()