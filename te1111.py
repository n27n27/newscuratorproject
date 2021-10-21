showing_result = []
title = "홍준표가 못생겼다."
showing_result.append({"title" : title})


word = "문재인"


if word is not None:
    for result in showing_result:
        
        if not(word in result["title"]):
            print("준표있다.")


# if word is not None:
#         for result in showing_result:
#             if not(word in showing_result["title"]):
#                 showing_result.remove(result)








