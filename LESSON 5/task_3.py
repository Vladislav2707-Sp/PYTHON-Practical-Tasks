def analyze_scores(scores_list):
    min_mark = min(scores_list)
    max_mark = max(scores_list)
    middle = round(sum(scores_list) / len(scores_list), 1)

    return min_mark , max_mark , middle


min_m, max_m, middle_m = analyze_scores(scores_list = [2, 4, 99, -1, 45, 31, 757, 100])
    


print(f"Найменша оцінка: {min_m}", f"Найбільша оцінка: {max_m}", f"Середнє арефметичне: {middle_m}", sep = " | ")