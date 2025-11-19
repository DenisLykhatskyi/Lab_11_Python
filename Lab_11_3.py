import nltk
from nltk.corpus import gutenberg
from nltk.probability import FreqDist
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import string

def plot_histogram(most_common, title):
    words = [word for word, count in most_common]
    counts = [count for word, count in most_common]

    plt.figure(figsize=(10, 6))
    plt.bar(words, counts, color='skyblue')
    plt.title(title)
    plt.xlabel('Слова')
    plt.ylabel('Кількість входжень')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def main():
    file_id = 'shakespeare-caesar.txt'
    try:
        words = gutenberg.words(file_id)
    except LookupError:
        print(f"Помилка: Текст '{file_id}' не знайдено. Переконайтеся, що пакет 'gutenberg' завантажено.")
        return

    cleaned_words = None
    
    while True:
        print(f"\nАНАЛІЗ ТЕКСТУ: {file_id}")
        print("1. Визначити загальну кількість слів у тексті")
        print("2. Топ-10 слів (з урахуванням стоп-слів) + Графік")
        print("3. Видалити стоп-слова та пунктуацію (процесинг)")
        print("4. Топ-10 слів (БЕЗ стоп-слів та пунктуації) + Графік")
        print("0. Вихід")

        choice = input("\nВаш вибір: ")

        if choice == '1':
            print(f"\nЗагальна кількість слів (токенів): {len(words)}")

        elif choice == '2':
            fdist = FreqDist(words)
            top_10 = fdist.most_common(10)
            print("\nТоп-10 слів (сирі дані)")
            for word, count in top_10:
                print(f"{word}: {count}")
            plot_histogram(top_10, "Топ-10 слів (разом зі стоп-словами)")

        elif choice == '3':
            print("\nВиконується очистка тексту...")
            try:
                stop_words = set(stopwords.words('english'))
            except LookupError:
                print("Помилка: Не знайдено словник 'stopwords'.")
                continue

            punct = set(string.punctuation)
            
            cleaned_words = [
                w.lower() for w in words 
                if w.lower() not in stop_words 
                and w not in punct 
                and w.isalpha()
            ]
            print(f"Очистку завершено. Кількість слів після фільтрації: {len(cleaned_words)}")

        elif choice == '4':
            if cleaned_words is None:
                print("\nПомилка: Спочатку виконайте пункт 3 (очистка тексту).")
            else:
                fdist_clean = FreqDist(cleaned_words)
                top_10_clean = fdist_clean.most_common(10)
                print("\nТоп-10 слів (очищені дані)")
                for word, count in top_10_clean:
                    print(f"{word}: {count}")
                plot_histogram(top_10_clean, "Топ-10 слів (без сміття)")

        elif choice == '0':
            print("Роботу завершено.")
            break
        
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()