from scraper import extract_politics_section, extract_economy_section, extract_society_section, extract_tech_section

politics_result = extract_politics_section("20211015", "20211016")
economy_result = extract_economy_section("20211015", "20211016")
society_result = extract_society_section("20211015", "20211016")
tech_result = extract_tech_section("20211015", "20211016")
all_result = politics_result + economy_result + society_result + tech_result


cg = "정치"
newpaper = "중앙일보"
word = "이재명"

# 단일 선택일 때의 조건 처리
# print_result = [result for result in all_result if result["category"] == cg and result["newspaper"] == newpaper and word in result["title"]]

# 복수 조건일 때의 조건 처리
def apply_temrs(cgs, newspapers, word):    

    showing_result = []
    for cg, newspaper in zip(cgs, newspapers):
        for result in all_result:
            if result["category"] == cg:
                showing_result.append(result)
    
    for newspaper in newspapers:
        for result in reversed(showing_result):
            if result["newspaper"] != newspaper:
                showing_result.remove(result)
    
    if word is not None:
        for result in reversed(showing_result):
            if not(word in result["title"]):
                showing_result.remove(result)
    return showing_result

gs = ["정치", "경제"]
news = ["중앙일보", "경향신문"]
word = "이재명"

for result in apply_temrs(gs, news, word):
    print(result)
    print("=======================================")